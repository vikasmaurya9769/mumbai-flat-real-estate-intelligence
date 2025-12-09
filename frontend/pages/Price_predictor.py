import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

st.set_page_config(page_title="viz Demo")

#['bedrooms', 'bathrooms', 'balcony', 'property_age', 'major_location','built_up_area', 'furnishing_type']

st.title('Mumbai Flat Price Predictor')


# Path to the current file (Price_predictor.py or recommendation.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # frontend/pages

# Build correct relative paths
MODEL_DF_PATH = os.path.join(BASE_DIR, "..", "models", "df.pkl")
MODEL_PIPELINE_PATH = os.path.join(BASE_DIR, "..", "models", "pipeline.pkl")

# Normalize the path for Linux/Render (VERY IMPORTANT)
MODEL_DF_PATH = os.path.normpath(MODEL_DF_PATH)
MODEL_PIPELINE_PATH = os.path.normpath(MODEL_PIPELINE_PATH)


# Load the pickles
with open(MODEL_DF_PATH, "rb") as file:
    df = pickle.load(file)

with open(MODEL_PIPELINE_PATH, "rb") as file:
    pipeline = pickle.load(file)
st.header('Enter your inputs')

major_location = st.selectbox('Location',sorted(df['major_location'].unique().tolist()))

bedrooms = float(st.selectbox('Number of Bedroom',sorted(df['bedrooms'].unique().tolist())))

built_up_area = float(st.number_input('Built Up Area'))

bathroom = float(st.selectbox('Number of Bathroom',sorted(df['bathrooms'].unique().tolist())))

balcony = st.selectbox('Balconies',sorted(df['balcony'].unique().tolist()))

furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))

property_age = st.selectbox('Property Age',sorted(df['property_age'].unique().tolist()))


if st.button('Predict'):

    # form a dataframe
    data = [[ bedrooms, bathroom, balcony, property_age, major_location, built_up_area,  furnishing_type, ]]
    columns = ['bedrooms', 'bathrooms', 'balcony', 'property_age',
               'major_location', 'built_up_area', 'furnishing_type']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    # predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.12
    high = base_price + 0.12

    # display
    st.text("The price of the flat is between {} Cr and {} Cr".format(round(low,2),round(high,2)))