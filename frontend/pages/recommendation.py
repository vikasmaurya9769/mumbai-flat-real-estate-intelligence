import streamlit as st
import pickle
import pandas as pd
import os

st.set_page_config(page_title="Apartment Recommender", layout="wide")

# --------------------- Load Pickle Files ------------------------
@st.cache_data
def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

# Safe pickle loader
@st.cache_resource
def load_pickle(path):
    with open(path, "rb") as f:
        return pickle.load(f)

# Base directory of THIS script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build paths to all model files
MODELS_DIR = os.path.normpath(os.path.join(BASE_DIR, "..", "models"))

LOCATION_DF_PATH = os.path.join(MODELS_DIR, "location_distance.pkl")
COS1_PATH = os.path.join(MODELS_DIR, "cosine_sim1.pkl")
COS2_PATH = os.path.join(MODELS_DIR, "cosine_sim2.pkl")
COS3_PATH = os.path.join(MODELS_DIR, "cosine_sim3.pkl")

# Load all files
location_df = load_pickle(LOCATION_DF_PATH)
cosine_sim1 = load_pickle(COS1_PATH)
cosine_sim2 = load_pickle(COS2_PATH)
cosine_sim3 = load_pickle(COS3_PATH)

# -------------------- Recommendation Logic ----------------------
def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3

    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    top_properties = location_df.index[top_indices].tolist()

    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df


# --------------------- UI ------------------------------

st.markdown("##  Search Apartments By Location Radius")

col1, col2 = st.columns([2, 1])

with col1:
    selected_location = st.selectbox(
        'Select a Location',
        sorted(location_df.columns.to_list())
    )

with col2:
    radius = st.number_input('Radius (in Kms)', min_value=1, max_value=50, step=1)

if st.button('Search Nearby'):
    st.subheader(f" Results within {radius} km of **{selected_location}**")

    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()

    if result_ser.empty:
        st.warning("No properties found within this radius.")
    else:
        for key, value in result_ser.items():
            st.markdown(
                f"""
                <div style="
                    padding:12px;
                    background:#1E1E1E;
                    color:#EAEAEA;
                    border-radius:8px;
                    margin-bottom:10px;
                    border:1px solid #333;
                ">
                    <b>{key}</b><br>
                    <span style="color:#B0B0B0;">{round(value/1000, 2)} km away</span>
                </div>
                """,
                unsafe_allow_html=True
            )

# ------------------------------------------------------------
st.markdown("---")
st.markdown("## Recommend Similar Apartments")

selected_appartment = st.selectbox(
    'Select an Apartment',
    sorted(location_df.index.to_list())
)

if st.button('Recommend'):
    recommendation_df = recommend_properties_with_scores(selected_appartment)

    st.markdown(f"###  Similar to **{selected_appartment}**")

    for _, row in recommendation_df.iterrows():
        st.markdown(
            f"""
            <div style="
                padding:12px;
                background:#1E1E1E;
                color:#EAEAEA;
                border-radius:8px;
                margin-bottom:10px;
                border:1px solid #333;
            ">
                <b>{row['PropertyName']}</b><br>
                <span style="color:#B0B0B0;">Similarity Score: {round(row['SimilarityScore'], 3)}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
