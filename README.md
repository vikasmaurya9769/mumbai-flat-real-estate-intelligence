🏙️ Mumbai Flat Real Estate Intelligence

A complete data-driven application for analyzing real estate trends, predicting flat prices, and recommending apartments in the Mumbai Metropolitan Region (MMR).

🚀 Features
🔍 1. Analysis Module

MMR Price per Sqft Geomap

Area vs Price Scatter

BHK Distribution Pie Charts

Side-by-side BHK Price Comparison

Location-based insights

💰 2. Price Predictor

Built using:

Random Forest Regressor

GridSearchCV Hyperparameter Tuning

Ordinal + OneHot + Target Encoding

Final R² Score → 0.92

Users can predict flat prices based on:

Location

Area

BHK

Bathrooms

Balconies

Property Age

Furnishing Type

🧭 3. Recommendation System

Two types of recommendations:

Radius-Based Apartment Finder

Similarity-Based Apartment Recommender

📌 Note: Demo dataset used for recommendation may contain sample society data.

📦 mumbai-flat-real-estate-intelligence
│
├── analytics_module/
├── data_cleaning/
├── datasets/
├── feature selection and base model/
├── frontend/
│   ├── home.py
│   ├── pages/
│   ├── models/
│
└── requirements.txt
|
└──gitattributes
└── README.md

🛠️ Technologies Used

Python

Streamlit

Scikit-learn

Pandas, NumPy

Plotly

BeautifulSoup & Geopy

Machine Learning & EDA

📌 Author
Vikas Maurya – Computer Engineering Student
Building real-world ML applications in analytics & AI.
