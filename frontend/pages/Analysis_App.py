import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Plotting Demo")

st.markdown("<h1 style='text-align: center;'>Analytics</h1>", unsafe_allow_html=True)

# new_df = pd.read_csv(r'E:/Mumbai Flat Real Estate Intelligence/datasets/data viz.csv')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # frontend/pages
CSV_PATH = os.path.join(BASE_DIR, "..", "..", "datasets", "data viz.csv")

CSV_PATH = os.path.normpath(CSV_PATH)  # Windows/Linux safe path

new_df = pd.read_csv(CSV_PATH)


st.header('location Price per Sqft Geomap')
group_df = new_df.groupby('major_location').agg({
    'price': lambda x: pd.to_numeric(x, errors='coerce').mean(),
    'price_per_sqft': lambda x: pd.to_numeric(x, errors='coerce').mean(),
    'built_up_area': lambda x: pd.to_numeric(x, errors='coerce').mean(),
    'latitude': lambda x: pd.to_numeric(x, errors='coerce').mean(),
    'longitude': lambda x: pd.to_numeric(x, errors='coerce').mean()
}).reset_index()

# If dots are still not visible, try this version:
fig = go.Figure()

# Add scattermapbox trace
fig.add_trace(go.Scattermapbox(
    lat=group_df['latitude'],
    lon=group_df['longitude'],
    mode='markers+text',
    marker=dict(
        size=group_df['built_up_area'] / group_df['built_up_area'].max() * 50 + 10,
        color=group_df['price_per_sqft'],
        colorscale='Plasma',
        showscale=True,
        colorbar=dict(title="Price per Sq Ft (₹)", thickness=20),
        opacity=0.8
    ),
    text=group_df['major_location'],
    hovertext=group_df.apply(
        lambda row: f"<b>{row['major_location']}</b><br>"
                   f"Price/sqft: ₹{row['price_per_sqft']:,.0f}<br>"
                   f"Avg Area: {row['built_up_area']:,.0f} sq.ft<br>"
                   f"Avg Price in cr: ₹{row['price']:,.0f}",
        axis=1
    ),
    hoverinfo='text'
))

# Update layout
fig.update_layout(
    mapbox_style="open-street-map",
    mapbox=dict(
        center=dict(lat=19.0760, lon=72.8777),
        zoom=10
    ),
    title="Mumbai Real Estate: Price per Square Foot",
    height=600,
    margin={"r":0,"t":50,"l":0,"b":0}
)

st.plotly_chart(fig,use_container_width=True)



st.header('Area Vs Price')
AvP = px.scatter(new_df, x="built_up_area", y="price", color="bedrooms", title="Area Vs Price")
st.plotly_chart(AvP, use_container_width=True)



st.header('BHK Pie Chart')

location_options = sorted(new_df['major_location'].unique().tolist())

location_options.insert(0,'overall')

selected_location = st.selectbox('Select location', location_options)

if selected_location == 'overall':

    fig2 = px.pie(new_df, names='bedrooms')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(new_df[new_df['major_location'] == selected_location], names='bedrooms')

    st.plotly_chart(fig2, use_container_width=True)



st.header('Side by Side BHK price comparison')

fig3 = px.box(new_df[new_df['bedrooms'] <= 4], x='bedrooms', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)