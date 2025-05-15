# !pip install streamlit
# !python -m streamlit run main.py

import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
# Generate data
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]
# y = x^2
# Create the plot
fig, ax = plt.subplots()
ax.plot(x, y)
# Display the plot in Streamlit
st.pyplot(fig)

import plotly.express as px
# Create a simple dataset
df = px.data.iris()
# Create a scatter plot
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
# Display the Plotly figure
st.plotly_chart(fig)

import altair as alt
# Create a simple dataset
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [1, 4, 9, 16, 25]
})
# Create an Altair line chart
chart = alt.Chart(df).mark_line().encode(
    x='x',
    y='y'
)
# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=False)

import seaborn as sns
# Load the built-in Seaborn dataset
tips = sns.load_dataset('tips')
# Create a Seaborn scatter plot
sns_plot = sns.scatterplot(x='total_bill', y='tip', data=tips)
# Display the plot
st.pyplot(sns_plot.figure)

import plotly.express as px
# Create a simple dataset
df = px.data.gapminder()
# Create a slider for year selection
year = st.slider("Select Year", min_value=1952, max_value=2007, step=5, value=2002)
# Filter the data based on selected year
filtered_df = df[df['year'] == year]
# Create an interactive scatter plot
fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', color='continent')
# Display the Plotly figure
st.plotly_chart(fig)

import pydeck as pdk
# Create a Pydeck map
deck = pdk.Deck(
    layers=[pdk.Layer(
        'ScatterplotLayer',
        data=[{'latitude': 27.7749, 'longitude': 77.4194}],
        get_position='[longitude, latitude]',
        get_radius=500,
        get_fill_color=[255, 0, 0],
        pickable=True
    )],
    initial_view_state=pdk.ViewState(
        latitude=27.7749,
        longitude=77.4194,
        zoom=10
    )
)
# Display the map
st.pydeck_chart(deck)

