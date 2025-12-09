# 🏙️ Mumbai Flat Real Estate Intelligence

A comprehensive machine learning-powered analytics platform for Mumbai's real estate market, featuring price prediction, interactive visualizations, and intelligent property recommendations.

## 📊 Live Demo
*(coming Soon )*

## ✨ Features

### 🔍 **Analytics Dashboard**
- **Geospatial Price Visualization**: Interactive map showing price per sqft across Mumbai
- **Comparative Analysis**: Side-by-side BHK price distributions with box plots
- **Market Trends**: Area vs price scatter plots and BHK distribution pie charts
- **Insightful Metrics**: Location-based statistics and property pattern analysis

### 🎯 **Price Prediction Engine**
- **High-Accuracy Model**: Random Forest Regressor with 92% R² score
- **Comprehensive Features**:
  - Location, area, bedrooms, bathrooms
  - Property age, furnishing type, balcony count
  - Price range estimation for better interpretability
- **Optimized Performance**: GridSearchCV for hyperparameter tuning
- **Smart Encoding**: Combination of ordinal, one-hot, and target encoding

### 🤝 **Intelligent Recommendations**
- **Radius-Based Search**: Find apartments within specific kilometers of a location
- **Similarity Matching**: Cosine similarity-based society recommendations
- **Feature-Based Filtering**: Multiple criteria for personalized suggestions

---

## 📂 Project Structure

```text
mumbai-flat-real-estate-intelligence/
│
├── analytics_module/
│   ├── analysis.ipynb            # Visualizations & Insights
│   └── recommender-system.ipynb  # Recommendation logic
│
├── data_cleaning/                # Data Preprocessing Pipeline
│   ├── data_processing.ipynb
│   ├── eda-multivariate-analysis.ipynb
│   ├── feature-eng.ipynb
│   └── ... (imputation, outlier treatment)
│
├── datasets/
│   ├── Mumbai_flat_list_raw.csv           # Original Kaggle Data
│   ├── mumbai_flat_2.csv                  # Processed Data
│   └── MMR_Housing_Residential_Projects.csv
│
├── feature_selection_and_base_model/
│   ├── model_selection.ipynb
│   └── feature_selection.ipynb
│
├── frontend/                     # Streamlit Application
│   ├── home.py                   # Entry point
│   ├── pages/
│   │   ├── Analysis_App.py
│   │   ├── Price_predictor.py
│   │   └── recommendation.py
│   └── models/                   # Serialized models (Exclude large files)
│
├── requirements.txt
├── .gitattributes
└── README.md
```
## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/mumbai-flat-real-estate-intelligence.git
cd mumbai-flat-real-estate-intelligence
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the application
```bash
streamlit run frontend/home.py
```
4. Access the dashboard
Open your browser and navigate to http://localhost:8501

## 📊 Data Sources

| Dataset | Description | Records | Purpose |
|---------|-------------|---------|---------|
| **Mumbai Flat Listings** | Primary dataset from Kaggle | 2,500 | Price prediction & analytics |
| **mumbai_flat_2** | Supplementary dataset | 7,500 | Price prediction & analytics |
| **MMR Housing Projects** | Generated sample data | 150 | Recommendation system demo |

> **Note**: The recommendation system uses demo society data for educational purposes. Real-world deployment should use verified property listings.

## 🛠️ Technologies

| Category | Tools |
|:--------:|:-----:|
| **Core Framework** | Python, Streamlit |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn, GridSearchCV |
| **Visualization** | Plotly, Matplotlib |
| **Geospatial** | Geopy, Folium |
| **Similarity Search** | Cosine Similarity, Vectorization |

## 📈 Model Performance

| Metric | Score |
|:------:|:-----:|
| **R² Score** | 0.92 |
| **MAE** | 0.24 |


## 📄 License
This project is for educational purposes. Please ensure compliance with data usage terms when using external datasets.

## 👥 Acknowledgments
Kaggle for providing the base datasets
Streamlit community for excellent documentation
Mumbai real estate portals for market insights
