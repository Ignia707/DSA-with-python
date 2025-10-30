import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

# --- Example Data (30 days) ---
np.random.seed(42)
dates = pd.date_range("2025-10-01", "2025-10-30")
activity_count = np.random.randint(0, 10, size=len(dates))

df = pd.DataFrame({"date": dates, "activity_count": activity_count})

# --- Color gradient (green → yellow → orange → red) ---
colors = plt.cm.YlOrRd(np.linspace(0.2, 1, len(df)))

# --- Plot setup ---
plt.figure(figsize=(10, 4))
points = plt.scatter(df["date"], df["activity_count"], c=df["activity_count"], 
                     cmap="YlOrRd", s=70, edgecolor="#222", linewidth=0.6)
plt.plot(df["date"], df["activity_count"], color="#555", linewidth=1.2, alpha=0.7)

# --- Value labels for top 7 points ---
top_idx = df["activity_count"].nlargest(7).index
for i in top_idx:
    plt.text(df["date"][i], df["activity_count"][i] + 0.3, str(df["activity_count"][i]),
             ha="center", va="bottom", fontsize=7, color="#333")

# --- Format axes ---
plt.title("🗓️ October Activity Overview", fontsize=13, fontweight="bold", pad=10)
plt.xlabel("")
plt.ylabel("Commits", fontsize=9)
plt.xticks(rotation=45, fontsize=8)
plt.grid(axis="y", linestyle="--", alpha=0.3)

# Calendar-style date ticks
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))

plt.tight_layout()
plt.colorbar(points, label="Commit intensity", pad=0.02)
plt.savefig("streak_chart.png", dpi=300, transparent=True)
plt.show()

# --- Mini table for last 7 days ---
last7 = df.tail(7).copy()
print("📅 Recent Activity (Last 7 Days):")
print(last7[["date", "activity_count"]].to_string(index=False))
