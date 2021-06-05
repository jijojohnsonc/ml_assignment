import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
import seaborn as sns 

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("World Happiness Report (2019)")
df = pd.read_csv('2019.csv')
no_of_countries = df.shape[0]
middle = no_of_countries // 2
dt = df.head().append(df[middle - 2:middle + 3]).append(df.tail())
st.table(dt)
st.text("The above table shows the data of best 5, average 5, and worst 5 countries by ranking")

score_array = np.array(df['Score'])
avg_score = round(np.mean(score_array), 4)
df = df.apply(lambda x : x['Score'] >= avg_score, axis=1)
top_countries = len(df[df == True].index)
st.text("(Source: https://www.kaggle.com/unsdsn/world-happiness?select=2019.csv)")
st.text("Average Score = {}".format(avg_score))
st.text("No. of countries having Score >= {} is {}".format(avg_score, top_countries))
st.text("No. of countries having Score < {} is {}".format(avg_score, no_of_countries - top_countries))

st.subheader("Bar Plot")
dt.plot(kind='bar', x='Country or region', y='Score')
st.pyplot()

st.subheader("Heat map")
sns.heatmap(dt.corr(), annot=True)
st.pyplot()

st.subheader("Jointplot")
sns.jointplot(data=dt, x='GDP per capita', y='Healthy life expectancy')
st.pyplot()