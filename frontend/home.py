import streamlit as st

st.set_page_config(page_title="Mumbai Real Estate Intelligence", layout="wide")

# ----------- TITLE -----------
st.markdown(
    """
    <h1 style='text-align:center; font-size:48px;'>
        Mumbai Real Estate Intelligence
    </h1>
    <p style='text-align:center; font-size:20px; color:#bbbbbb;'>
        A Smart Analytics, Price Prediction & Recommendation Platform for Mumbai and nearby urban regions Properties
    </p>
    <hr style='margin-top:20px;'>
    """,
    unsafe_allow_html=True
)

# ----------- OVERVIEW SECTION -----------
st.markdown(
    """
    <h2> Project Overview</h2>
    <p style='font-size:18px; color:#dddddd;'>
        This platform helps users explore the Mumbai and nearby urban regions real estate market 
        using advanced data analytics, machine learning models, and intelligent recommendation systems.
        It consists of three main modules:
    </p>
    """,
    unsafe_allow_html=True
)

# MODULE 1
st.markdown(
    """
    <h3>1️ Analysis App</h3>
    <p style='font-size:17px; color:#cccccc;'>
        • Interactive visualizations such as price per sqft geomaps, BHK distribution,  
        area vs price trends, and location-wise insights.<br>
        • Helps users understand real estate trends across Mumbai, Navi Mumbai, and Thane.
    </p>
    """,
    unsafe_allow_html=True
)

# MODULE 2
st.markdown(
    """
    <h3>2️ Price Predictor</h3>
    <p style='font-size:17px; color:#cccccc;'>
        • A machine learning model trained on real property data (9,600+ rows).<br>
        • Predicts flat prices based on location, area, BHK, balconies, age & furnishing.<br>
        • Outputs an estimated price range for better decision-making.
    </p>
    """,
    unsafe_allow_html=True
)

# MODULE 3
st.markdown(
    """
    <h3>3️ Apartment Recommendation System</h3>
    <p style='font-size:17px; color:#cccccc;'>
        • Suggests similar apartments based on features like price, location & configuration.<br>
        • Also includes a radius-based search to find nearby societies within a chosen distance.<br>
    </p>

    <p style='font-size:15px; color:#999999; margin-top:-10px;'>
         <b>Note:</b> The Recommendation System uses a 
        <i>sample demonstration dataset</i> for societies.  
        It showcases how recommendation logic works, but the society details 
        may not reflect real-world listings.
    </p>
    """,
    unsafe_allow_html=True
)

# ----------- HOW TO USE -----------
st.markdown(
    """
    <h2> How to Use This Application</h2>
    <p style='font-size:17px; color:#cccccc;'>
        ✔ Navigate to <b>Analysis App</b> to explore real estate insights.<br>
        ✔ Go to <b>Price Predictor</b> to estimate the price of any flat.<br>
        ✔ Use the <b>Recommendation</b> module to discover similar or nearby apartments.<br>
    </p>
    """,
    unsafe_allow_html=True
)

# ----------- FOOTER -----------
st.markdown(
    """
    <hr>
    <p style='text-align:center; font-size:15px; color:#777777;'>
        Built by Vikas Maurya • 2025 • Mumbai Flat Real Estate Intelligence
    </p>
    """,
    unsafe_allow_html=True
)
