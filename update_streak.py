import os, datetime, subprocess, re

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

# --- 7-day bar chart ---
def get_past_commits(days=7):
    data = []
    for i in range(days):
        day = today - datetime.timedelta(days=(days - 1 - i))
        log_file = os.path.join(log_dir, f"{day}.md")
        count = 1 if os.path.exists(log_file) else 0
        data.append(count)
    return data

bars = get_past_commits()
chart = "".join(["▮" if c > 0 else "▯" for c in bars])
total_commits = int(subprocess.getoutput("git rev-list --count HEAD"))

# --- Build streak section ---
streak_section = f"""
# 🔥 Work Streak Tracker

**Current Streak:** {streak} days  
**Total Commits:** {total_commits}  
**Last Updated:** {today}

## 📊 7-Day Activity
{chart}  
▮ = commit made | ▯ = no commit

---

_Updated automatically every day via GitHub Actions._
"""

# --- Update only between markers in README ---
readme_path = "README.md"
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
else:
    content = ""

pattern = re.compile(r"<!-- STREAK:START -->(.*?)<!-- STREAK:END -->", re.DOTALL)
replacement = f"<!-- STREAK:START -->{streak_section}<!-- STREAK:END -->"

if re.search(pattern, content):
    new_content = re.sub(pattern, replacement, content)
else:
    new_content = content.strip() + "\n\n" + replacement

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(new_content)
