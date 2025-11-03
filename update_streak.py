#!/usr/bin/env python3
"""
update_streak.py (Fixed & Improved)
- Detects primary human author (skips bots)
- Builds per-day commit counts for last 30 days
- Computes current consecutive-day streak (counts up to yesterday to avoid penalizing incomplete days)
- Generates a clear, readable day-by-day bar chart
- Updates README.md with streak info and chart
"""

import subprocess
from collections import Counter
from datetime import datetime, timedelta, timezone
import os
import re

# Matplotlib in non-GUI mode
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# ---------- Config ----------
README = "README.md"
CHART_FILE = "streak_chart.png"
MARKER_START = "<!-- STREAK:START -->"
MARKER_END = "<!-- STREAK:END -->"
DAYS = 30  # Show 30 days in chart
BOT_NAMES = {
    "github-actions[bot]", "dependabot[bot]", "dependabot", "web-flow", "GitHub",
    "dependabot-preview[bot]"
}
# ----------------------------

def run_git(args):
    """Execute git command and return output."""
    p = subprocess.run(["git"] + args, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {p.stderr.strip()}")
    return p.stdout.strip()

def detect_primary_author(n_commits=500):
    """Pick most frequent non-bot author from recent commits."""
    try:
        out = run_git(["log", f"-n{n_commits}", "--pretty=format:%an <%ae>"])
    except RuntimeError:
        return None
    
    authors = [line.strip() for line in out.splitlines() if line.strip()]
    # Filter out bots
    filtered = [a for a in authors if not any(bot.lower() in a.lower() for bot in BOT_NAMES)]
    
    if filtered:
        counts = Counter(filtered)
        return counts.most_common(1)[0][0]
    
    # Fallback to git config
    try:
        name = run_git(["config", "user.name"]).strip()
        email = run_git(["config", "user.email"]).strip()
        if name and email:
            return f"{name} <{email}>"
    except:
        pass
    
    return None

def commit_counts_by_date(author, days=DAYS):
    """
    Return Counter mapping 'YYYY-MM-DD' -> commit_count for the given author.
    Only counts commits from the last `days` days.
    """
    # Get commits from last N days
    since_date = (datetime.now(timezone.utc).date() - timedelta(days=days)).isoformat()
    
    if author:
        out = run_git([
            "log", 
            f"--author={author}", 
            f"--since={since_date}",
            "--pretty=format:%ad", 
            "--date=short"
        ])
    else:
        out = run_git([
            "log",
            f"--since={since_date}",
            "--pretty=format:%ad", 
            "--date=short"
        ])
    
    lines = [l.strip() for l in out.splitlines() if l.strip()]
    return Counter(lines)

def calc_streak_from_counts(counts_counter):
    """
    Count consecutive days with commits, starting from yesterday.
    We check yesterday first to avoid penalizing an incomplete today.
    """
    yesterday = (datetime.now(timezone.utc).date() - timedelta(days=1))
    streak = 0
    d = yesterday
    
    # Count backwards from yesterday
    while True:
        if counts_counter.get(str(d), 0) > 0:
            streak += 1
            d -= timedelta(days=1)
        else:
            break
    
    return streak

def total_commits_from_counter(counter):
    """Total commits from counter."""
    return sum(counter.values())

def build_streak_section_markdown(streak, total_commits, counts_counter):
    """
    Build the README streak section with enhanced metrics.
    """
    today = datetime.now(timezone.utc).date()
    today_str = today.strftime("%Y-%m-%d")
    
    # Calculate metrics from last 30 days
    active_days = sum(1 for count in counts_counter.values() if count > 0)
    
    if counts_counter:
        best_date = max(counts_counter.items(), key=lambda x: x[1])
        best_date_str = datetime.strptime(best_date[0], "%Y-%m-%d").strftime("%b %d")
        best_count = best_date[1]
        avg_per_day = total_commits / DAYS
    else:
        best_date_str = "N/A"
        best_count = 0
        avg_per_day = 0
    
    md = []
    md.append("# 🔥 Work Streak Tracker\n")
    md.append("> Track your DSA learning consistency\n")
    md.append(f"**Current Streak:** {streak} days  ")
    md.append(f"**Total Commits (30d):** {total_commits}  ")
    md.append(f"**Last Updated:** {today_str}\n")
    md.append("## 📊 30-Day Activity Chart\n")
    md.append(f"![30-Day Activity]({CHART_FILE})\n")
    md.append(f"**Active days:** {active_days}/{DAYS} • ")
    md.append(f"**Best day:** {best_date_str} ({best_count} commits) • ")
    md.append(f"**Avg/day:** {avg_per_day:.1f}\n")
    md.append("---\n")
    
    return "\n".join(md)

def update_readme_section(new_section_md):
    """Insert or update the streak section in README."""
    if os.path.exists(README):
        with open(README, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = ""
    
    if MARKER_START in content and MARKER_END in content:
        pattern = re.compile(
            re.escape(MARKER_START) + ".*?" + re.escape(MARKER_END), 
            re.DOTALL
        )
        replacement = f"{MARKER_START}\n{new_section_md}\n{MARKER_END}"
        new_content = re.sub(pattern, replacement, content)
    else:
        if not content.endswith("\n"):
            content += "\n"
        new_content = content + f"\n{MARKER_START}\n{new_section_md}\n{MARKER_END}\n"
    
    with open(README, "w", encoding="utf-8") as f:
        f.write(new_content)

def make_chart(counts_counter, out_file=CHART_FILE):
    """
    Creates a clean, readable bar chart showing day-by-day commits for 30 days.
    """
    plt.style.use("dark_background")
    
    # Prepare 30 days of data
    today = datetime.now(timezone.utc).date()
    dates = [today - timedelta(days=i) for i in range(DAYS - 1, -1, -1)]
    commits = [counts_counter.get(str(d), 0) for d in dates]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(14, 5))
    
    # Color mapping: 0 commits = gray, 1-2 = yellow, 3-5 = orange, 6+ = red
    colors = []
    for c in commits:
        if c == 0:
            colors.append('#2d2d2d')  # Dark gray for no activity
        elif c <= 2:
            colors.append('#FDD835')  # Yellow
        elif c <= 5:
            colors.append('#FB8C00')  # Orange
        else:
            colors.append('#E53935')  # Red
    
    # Create bar chart
    bars = ax.bar(range(len(dates)), commits, color=colors, edgecolor='#444', linewidth=0.5)
    
    # Add value labels on bars
    for i, (bar, count) in enumerate(zip(bars, commits)):
        if count > 0:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.1,
                str(count),
                ha='center', va='bottom',
                fontsize=8, color='white', fontweight='bold'
            )
    
    # Format x-axis with dates
    date_labels = [d.strftime('%m/%d') for d in dates]
    ax.set_xticks(range(len(dates)))
    ax.set_xticklabels(date_labels, rotation=45, ha='right', fontsize=8, color='white')
    
    # Add vertical lines to separate weeks
    for i in range(0, len(dates), 7):
        ax.axvline(x=i - 0.5, color='#555', linestyle='--', linewidth=0.8, alpha=0.5)
    
    # Labels and title
    month_name = today.strftime('%B %Y')
    ax.set_title(f'📅 Commit Activity - Last 30 Days ({month_name})', 
                 fontsize=14, fontweight='bold', color='white', pad=15)
    ax.set_ylabel('Commits', fontsize=11, color='white')
    ax.set_xlabel('Date', fontsize=11, color='white')
    
    # Grid
    ax.grid(axis='y', linestyle='--', alpha=0.3, color='#666')
    ax.set_axisbelow(True)
    
    # Set y-axis to start at 0
    ax.set_ylim(bottom=0)
    
    # Style
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#666')
    ax.spines['bottom'].set_color('#666')
    ax.tick_params(colors='white')
    
    plt.tight_layout()
    plt.savefig(out_file, dpi=300, facecolor='#0d1117', edgecolor='none')
    plt.close()

def main():
    print("="*60)
    print("Starting Streak Tracker Update")
    print("="*60)
    
    # Detect author
    try:
        author = detect_primary_author()
        print(f"✓ Detected author: {author}")
    except Exception as e:
        print(f"✗ ERROR detecting author: {e}")
        author = None
    
    # Get commit counts
    try:
        counts_counter = commit_counts_by_date(author, DAYS)
        print(f"✓ Collected commit data for last {DAYS} days")
        
        # Debug: show recent dates
        if counts_counter:
            recent = sorted(counts_counter.items(), reverse=True)[:5]
            print(f"  Recent dates: {recent}")
    except Exception as e:
        print(f"✗ ERROR gathering commits: {e}")
        counts_counter = Counter()
    
    # Calculate metrics
    streak = calc_streak_from_counts(counts_counter)
    total = total_commits_from_counter(counts_counter)
    
    print(f"✓ Current streak: {streak} days")
    print(f"✓ Total commits (30d): {total}")
    
    # Generate chart
    try:
        make_chart(counts_counter)
        print(f"✓ Generated chart: {CHART_FILE}")
    except Exception as e:
        print(f"✗ ERROR creating chart: {e}")
    
    # Update README
    try:
        section_md = build_streak_section_markdown(streak, total, counts_counter)
        update_readme_section(section_md)
        print(f"✓ Updated {README}")
    except Exception as e:
        print(f"✗ ERROR updating README: {e}")
    
    print("="*60)
    print("Update Complete!")
    print("="*60)

if __name__ == "__main__":
    main()
