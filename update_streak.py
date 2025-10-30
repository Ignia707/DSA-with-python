import subprocess
from datetime import datetime, timedelta

def get_author_name():
    result = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True)
    return result.stdout.strip()

def get_commit_dates(author):
    result = subprocess.run(
        ["git", "log", f"--author={author}", "--pretty=format:%ad", "--date=short"],
        capture_output=True, text=True
    )
    return set(result.stdout.splitlines())

def calculate_streak(dates):
    today = datetime.utcnow().date()
    streak = 0
    day = today
    while str(day) in dates:
        streak += 1
        day -= timedelta(days=1)
    return streak, len(dates)

def build_streak_section(streak, total):
    return f"""
# 🔥 Work Streak Tracker

**Current Streak:** {streak} days  
**Total Commits:** {total}  
**Last Updated:** {datetime.utcnow().date()}

## 📊 7-Day Activity
▮▮▮▯▮▮▮  
▮ = commit made | ▯ = no commit

---

_Updated automatically every day via GitHub Actions._
"""

def update_readme(streak, total):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    if "# 🔥 Work Streak Tracker" in content:
        content = content.split("# 🔥 Work Streak Tracker")[0].strip()

    new_readme = content + build_streak_section(streak, total)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme)

if __name__ == "__main__":
    author = get_author_name()
    commit_dates = get_commit_dates(author)
    streak, total = calculate_streak(commit_dates)
    update_readme(streak, total)
