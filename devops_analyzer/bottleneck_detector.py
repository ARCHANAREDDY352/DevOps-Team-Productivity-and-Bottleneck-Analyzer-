from sklearn.ensemble import IsolationForest
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("commits.csv")
df['date'] = pd.to_datetime(df['date'])
df['day'] = df['date'].dt.date
daily = df.groupby('day').count()['message'].reset_index()
daily.columns = ['day', 'commits']

model = IsolationForest(contamination=0.1)
daily['anomaly'] = model.fit_predict(daily[['commits']])

plt.plot(daily['day'], daily['commits'], label='Commits')
plt.scatter(daily[daily['anomaly'] == -1]['day'],
            daily[daily['anomaly'] == -1]['commits'],
            color='red', label='Anomaly')
plt.legend()
plt.title("Bottleneck Detection")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()