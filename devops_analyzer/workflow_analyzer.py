import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("commits.csv")
df['date'] = pd.to_datetime(df['date'])
df['day'] = df['date'].dt.date

daily_commits = df.groupby('day').count()['message']
daily_commits.plot(title="Daily Commits", figsize=(10,5))
plt.ylabel("Commits")
plt.show()