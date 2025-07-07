import pandas as pd

def suggest(df):
    df['date'] = pd.to_datetime(df['date'])
    df['day'] = df['date'].dt.date
    daily = df.groupby('day').count()['message'].reset_index()
    avg = daily['message'].mean()

    low_days = daily[daily['message'] < avg * 0.5]
    if not low_days.empty:
        print("⚠️ Low productivity on these days:")
        print(low_days['day'].tolist())
        print("Suggestion: Balance workload, improve code review cycle.")
    else:
        print("✅ Workflow looks healthy!")

df = pd.read_csv("commits.csv")
suggest(df)