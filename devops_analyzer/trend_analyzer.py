import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("commits.csv")
df['date'] = pd.to_datetime(df['date'])
df['weekday'] = df['date'].dt.day_name()

sns.countplot(data=df, x='weekday', order=[
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])
plt.title("Commits by Day of Week")
plt.show()