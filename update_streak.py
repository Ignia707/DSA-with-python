#!/usr/bin/env python3
"""
update_streak.py (debugged & improved)
- Detect primary human author (skips common bots)
- Builds per-day commit counts for that author (last DAYS)
- Computes current consecutive-day streak (UTC)
- Generates a labeled Matplotlib chart streak_chart.png
- Injects streak section into README.md between markers
- Prints debug info to stdout
"""

import subprocess
from collections import Counter
from datetime import datetime, timedelta, timezone
import os
import re
import sys

# Matplotlib in non-GUI mode
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# ---------- Config ----------
README = "README.md"
CHART_FILE = "streak_chart.png"
MARKER_START = "<!-- STREAK:START -->"
MARKER_END = "<!-- STREAK:END -->"
DAYS = 7
BOT_NAMES = {
    "github-actions[bot]", "dependabot[bot]", "dependabot", "web-flow", "GitHub",
    "dependabot-preview[bot]"
}
# ----------------------------

def run_git(args):
    p = subprocess.run(["git"] + args, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {p.stderr.strip()}")
    return p.stdout.strip()

def detect_primary_author(n_commits=500):
    """Pick most frequent non-bot author from recent commits; fallback to config name/email."""
    try:
        out = run_git(["log", f"-n{n_commits}", "--pretty=format:%an <%ae>"])
    except RuntimeError:
        return None
    authors = [line.strip() for line in out.splitlines() if line.strip()]
    # Filter bots
    filtered = [a for a in authors if not any(bot.lower() in a.lower() for bot in BOT_NAMES)]
    if filtered:
        counts = Counter(filtered)
        return counts.most_common(1)[0][0]  # returns "Name <email>"
    # fallback to config
    name = run_git(["config", "user.name"]).strip() or None
    email = run_git(["config", "user.email"]).strip() or None
    if name and email:
        return f"{name} <{email}>"
    if name:
        return name
    if email:
        return email
    return None

def commit_counts_by_date(author):
    """
    Return Counter mapping 'YYYY-MM-DD' -> commit_count for the given author.
    If author is None, counts all commits.
    """
    if author:
        arg = f"--author={author}"
        out = run_git(["log", arg, "--pretty=format:%ad", "--date=short"])
    else:
        out = run_git(["log", "--pretty=format:%ad", "--date=short"])
    lines = [l.strip() for l in out.splitlines() if l.strip()]
    return Counter(lines)

def calc_streak_from_counts(counts_counter):
    """Count consecutive days including today with commits (>0) using UTC."""
    today = datetime.now(timezone.utc).date()
    streak = 0
    d = today
    while True:
        if counts_counter.get(str(d), 0) > 0:
            streak += 1
            d -= timedelta(days=1)
        else:
            break
    return streak

def last_n_day_counts(counter, days=DAYS):
    """Return list oldest->newest commit counts (integers) for last `days` days (UTC)."""
    today = datetime.now(timezone.utc).date()
    counts = []
    for i in range(days-1, -1, -1):
        day = today - timedelta(days=i)
        counts.append(counter.get(str(day), 0))
    return counts

def total_commits_count(counter, author=None):
    """Total commits by author (sum of counts) or fallback to repo total."""
    if counter is not None:
        return sum(counter.values())
    try:
        out = run_git(["rev-list", "--count", "HEAD"])
        return int(out.strip())
    except Exception:
        return 0
def build_streak_section_markdown(streak, total_commits, counts_counter):
    """
    Enhanced README section with heatmap chart + 7-day commit table.
    """
    today = datetime.now(timezone.utc).date()
    today_str = today.isoformat()

    # Build last 7 days table
    last7_dates = [today - timedelta(days=i) for i in range(6, -1, -1)]
    last7_data = [(d.strftime("%b %d"), counts_counter.get(str(d), 0)) for d in last7_dates]

    # Basic metrics
    total_week = sum(c for _, c in last7_data)
    avg = total_week / 7 if total_week else 0
    best_day = max(last7_data, key=lambda x: x[1])
    active_days = sum(1 for _, c in last7_data if c > 0)

    md = []
    md.append("# 🔥 Work Streak Tracker\n")
    md.append("> 30-day activity heatmap + 7-day detail view\n")
    md.append(f"**Current Streak:** {streak} days  ")
    md.append(f"**Total Commits:** {total_commits}  ")
    md.append(f"**Last Updated:** {today_str}\n")
    md.append("## 📆 30-Day Heatmap\n")
    md.append(f"![30-Day Heatmap]({CHART_FILE})\n")
    md.append(f"**Active days:** {active_days}/7 • **Best day:** {best_day[0]} ({best_day[1]}) • **Avg/day:** {avg:.2f}\n")

    md.append("\n### 🗓️ Last 7 Days Summary\n")
    md.append("| Date | Commits |")
    md.append("|------|----------|")
    for date, c in last7_data:
        md.append(f"| {date} | {c} |")

    md.append("\n_Heatmap and summary auto-updated daily via GitHub Actions._\n")
    md.append("---\n")
    return "\n".join(md)


def update_readme_section(new_section_md):
    if os.path.exists(README):
        with open(README, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = ""
    if MARKER_START in content and MARKER_END in content:
        pattern = re.compile(re.escape(MARKER_START) + ".*?" + re.escape(MARKER_END), re.DOTALL)
        replacement = f"{MARKER_START}\n{new_section_md}\n{MARKER_END}"
        new_content = re.sub(pattern, replacement, content)
    else:
        if not content.endswith("\n"):
            content += "\n"
        new_content = content + f"\n{MARKER_START}\n{new_section_md}\n{MARKER_END}\n"
    with open(README, "w", encoding="utf-8") as f:
        f.write(new_content)

def make_chart(counts_counter, out_file=CHART_FILE, transparent=True):
    """
    Creates a visually rich 30-day activity chart with dark theme and white labels.
    """
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import pandas as pd
    import numpy as np
    from datetime import datetime, timedelta, timezone

    plt.style.use("dark_background")

    days = 30
    today = datetime.now(timezone.utc).date()
    dates = [today - timedelta(days=i) for i in range(days - 1, -1, -1)]
    commits = [counts_counter.get(str(d), 0) for d in dates]
    df = pd.DataFrame({"date": dates, "activity_count": commits})

    # --- Color scheme ---
    cmap = plt.cm.YlOrRd
    norm = plt.Normalize(vmin=min(commits), vmax=max(commits) if max(commits) > 0 else 1)

    plt.figure(figsize=(10, 4))
    points = plt.scatter(
        df["date"], df["activity_count"],
        c=df["activity_count"], cmap=cmap, s=70,
        edgecolor="#111", linewidth=0.6
    )
    plt.plot(df["date"], df["activity_count"], color="#999", linewidth=1.2, alpha=0.7)

    # --- Value labels for top points ---
    top_idx = df["activity_count"].nlargest(7).index
    for i in top_idx:
        plt.text(
            df["date"][i], df["activity_count"][i] + 0.3,
            str(df["activity_count"][i]),
            ha="center", va="bottom", fontsize=8,
            color="white", fontweight="bold"
        )

    # --- Axes & labels ---
    plt.title(f"🗓️ {today.strftime('%B')} Activity Overview", fontsize=13, fontweight="bold", pad=10)
    plt.ylabel("Commits", fontsize=9, color="white")
    plt.xticks(rotation=45, fontsize=8, color="white")
    plt.yticks(color="white")
    plt.grid(axis="y", linestyle="--", alpha=0.3)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))

    plt.tight_layout()
    cbar = plt.colorbar(points, label="Commit Intensity", pad=0.02)
    cbar.ax.yaxis.label.set_color("white")
    plt.savefig(out_file, dpi=300, transparent=transparent)
    plt.close()


def main():
    try:
        author = detect_primary_author()
    except Exception as e:
        print("ERROR detecting author:", e)
        author = None

    print("Detected author:", repr(author))

    counts_counter = None
    try:
        counts_counter = commit_counts_by_date(author)
    except Exception as e:
        print("ERROR gathering commit dates:", e)
        counts_counter = Counter()

    # debug print: show sample of commit dates/counters
    sample_lines = list(counts_counter.items())[:10]
    print("Sample date counts (up to 10):", sample_lines)

    streak = calc_streak_from_counts(counts_counter)
    counts = last_n_day_counts(counts_counter, DAYS)
    total = total_commits_count(counts_counter, author)

    print(f"Computed streak: {streak}")
    print(f"7-day counts (oldest->newest): {counts}")
    print(f"Total commits (author fallback): {total}")

    make_chart(counts_counter)
    section_md = build_streak_section_markdown(streak, total, counts_counter)
    update_readme_section(section_md)

    print("Updated README and chart.")

if __name__ == "__main__":
    main()
