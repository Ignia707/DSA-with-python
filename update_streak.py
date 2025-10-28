import os, datetime, subprocess

today = datetime.date.today()
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# --- Count today's commits ---
commits_today = subprocess.getoutput(f'git log --since="{today}" --pretty=oneline')
commit_lines = commits_today.strip().split("\n") if commits_today.strip() else []
commit_count_today = len(commit_lines)

# --- Log activity ---
if commit_count_today > 0:
    log_file = os.path.join(log_dir, f"{today}.md")
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write(f"## {today}\n- {commit_count_today} commit(s) made today.\n")

# --- Calculate streak ---
dates = sorted([f[:-3] for f in os.listdir(log_dir) if f.endswith(".md")])
streak = len(dates)

# --- Last 7 days bar chart ---
def get_past_commits(days=7):
    data = []
    for i in range(days):
        day = today - datetime.timedelta(days=(days - 1 - i))
        log_file = os.path.join(log_dir, f"{day}.md")
        if os.path.exists(log_file):
            with open(log_file) as f:
                lines = f.readlines()
            count = sum("commit" in l for l in lines)
        else:
            count = 0
        data.append(count)
    return data

bars = get_past_commits()
chart = "".join(["▮" if c > 0 else "▯" for c in bars])

# --- Total commits (in repo) ---
total_commits = int(subprocess.getoutput("git rev-list --count HEAD"))

# --- Update README ---
readme = f"""# 🔥 Work Streak Tracker

**Current Streak:** {streak} days  
**Total Commits:** {total_commits}  
**Last Updated:** {today}

## 📊 7-Day Activity
{chart}  
▮ = commit made | ▯ = no commit

---

_Updated automatically every day via GitHub Actions._
"""
with open("README.md", "w") as f:
    f.write(readme)
