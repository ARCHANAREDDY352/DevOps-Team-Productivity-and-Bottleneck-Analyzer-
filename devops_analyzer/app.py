import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 DevOps Bottleneck Analyzer")

df = pd.read_csv("commits.csv")
df['date'] = pd.to_datetime(df['date'])
df['day'] = df['date'].dt.date

st.subheader("Raw Commit Data")
st.dataframe(df.head())

# Commit frequency
daily = df.groupby('day').count()['message'].reset_index()
st.subheader("Daily Commit Chart")
st.line_chart(daily.set_index('day'))

st.subheader("Suggestions")
avg = daily['message'].mean()
low_days = daily[daily['message'] < avg * 0.5]
if not low_days.empty:
    st.warning("Low productivity on days:")
    st.write(low_days)
    st.info("✅ Suggestion: Improve review/test cycles, rebalance tasks.")
else:
    st.success("Team workflow looks good!")