import os, datetime, subprocess

today = datetime.date.today()
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Fetch latest commits
commits_today = subprocess.getoutput(f'git log --since="{today}" --pretty=oneline')

# Log only if committed today
if commits_today:
    log_file = os.path.join(log_dir, f"{today}.md")
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write(f"## {today}\n- Commit(s) made today.\n")

# Count streak days
streak = len([f for f in os.listdir(log_dir) if f.endswith(".md")])

# Update README
readme = f"# 🔥 Work Streak Tracker\n\n**Current Streak:** {streak} days\n\nLast updated: {today}\n"
with open("README.md", "w") as f:
    f.write(readme)
