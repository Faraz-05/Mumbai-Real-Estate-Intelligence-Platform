<div align="center">

# 🏠 Mumbai Real Estate Intelligence Platform

### AI Powered Property Valuation, Investment Analytics, Explainable AI and Locality Intelligence

<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/LightGBM-ML_Model-green?style=for-the-badge" />
<img src="https://img.shields.io/badge/SHAP-Explainable_AI-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge" />
<img src="https://img.shields.io/badge/PowerBI-Business_Intelligence-yellow?style=for-the-badge" />

### Predict • Explain • Analyze • Invest

</div>

# 🎯 Problem Statement

Mumbai is one of the most expensive and dynamic real estate markets in India.

Property buyers and investors often face challenges such as:

- Lack of transparent pricing
- Difficulty comparing localities
- No explainability behind property valuation
- Limited investment intelligence
- Fragmented market insights

This project solves these challenges using Machine Learning,
Explainable AI and Business Intelligence dashboards.

# 🎯 Problem Statement

Mumbai is one of the most expensive and dynamic real estate markets in India.

Property buyers and investors often face challenges such as:

- Lack of transparent pricing
- Difficulty comparing localities
- No explainability behind property valuation
- Limited investment intelligence
- Fragmented market insights

This project solves these challenges using Machine Learning,
Explainable AI and Business Intelligence dashboards.

# 🏗️ Architecture

Raw Data
    ↓
Data Cleaning
    ↓
Feature Engineering
    ↓
LightGBM Model Training
    ↓
SHAP Explainability
    ↓
Prediction Engine
    ↓
Recommendation Engine
    ↓
AI Assistant
    ↓
Streamlit Dashboard
    ↓
Power BI Dashboard

# 📸 Streamlit Dashboard

![Home](visuals/property_price_prediction1.png)
![Prediction](visuals/property_price_prediction2.png)
![](visuals/property_price_prediction3.png)
![Investment Analysis](visuals/Investment_Analysis.png)
![](visuals/Investment_analysis2.png)
![AI assistant](visuals/ai_chatbot.png)
![Market KPIs](visuals/market_kpi.png)

# 📊 Power BI Analytics Dashboard

![Exceutive Overview](visuals/Executive_overview.png)
![Location & Geo Analysis ](visuals/Location_Geo_Analysis.png)
![Investment & Market Analysis Dashboard](visuals/Investment_Market_Analysis.png)
![Property & Pricing Analysis Dashboard](visuals/Propert_Pricing_Analysis.png)
![ML Prediction & AI Intelligence Dashboard](visuals/ML_Prediction_AI.png)

# 🤖 Machine Learning Pipeline

Model Used:

- LightGBM Regressor

Target:

- Property Price (INR)

Features:

- Region
- Property Type
- Bedrooms
- Carpet Area
- Built-up Area
- Floor
- Furnishing
- Builder Tier
- Metro Distance
- Connectivity Score
- Luxury Score

Model predicts the expected market value of a property in Mumbai.

# 🧠 Explainable AI (SHAP)

One major challenge in real estate valuation is understanding:

"Why did the model predict this price?"

To solve this problem, SHAP (SHapley Additive Explanations) was integrated.

SHAP helps identify:

- Which features increase property value
- Which features decrease property value
- Relative contribution of each feature
- Model transparency for users

## SHAP Feature Importance

![SHAP Bar](visuals/shap_bar.png)

## SHAP Summary Plot

![SHAP Summary](visuals/shap_summary.png)

Key Insights:

- Carpet Area has the strongest impact on price.
- Luxury Score significantly influences valuation.
- Connectivity improves property attractiveness.
- Metro accessibility positively affects pricing.
- Property age reduces estimated value.

This provides transparency and trust in predictions.

# 🎯 Investment Recommendation Engine

A recommendation engine was developed to suggest suitable investment localities.

Inputs:

- User Budget
- Predicted Property Value
- Locality Investment Score

Output:

- Top Investment Localities
- Average Price
- Luxury Score
- Investment Score

This allows users to discover areas offering strong investment potential.

# 🤖 AI Real Estate Assistant

The project includes a local AI Assistant capable of answering:

- Should I invest in Powai?
- Is Bandra West expensive?
- Tell me about Worli.
- Which locality has better investment potential?

The assistant retrieves locality intelligence from the analytics dataset.

# 🚧 Challenges Faced

### 1. Data Quality Issues

Real estate data contained:

- Missing values
- Duplicate records
- Inconsistent locality names

Solution:

- Data cleaning pipeline
- Standardization techniques

---

### 2. Feature Engineering

Creating meaningful features from raw property data was challenging.

Solution:

- Distance metrics
- Luxury scoring
- Connectivity scoring

---

### 3. Model Explainability

Users needed transparency behind predictions.

Solution:

- SHAP Explainability Integration

---

### 4. Dashboard Integration

Combining:

- Machine Learning
- Streamlit
- Power BI
- AI Assistant

into one platform required modular architecture.

---

### 5. Recommendation Logic

Balancing:

- Investment Score
- Budget Constraints
- Locality Ranking

required multiple iterations.

# 💻 Technology Stack

## Machine Learning

- Python
- Pandas
- NumPy
- Scikit-Learn
- LightGBM
- SHAP

## Dashboard

- Streamlit
- Plotly

## Business Intelligence

- Power BI

## AI Components

- Ollama
- FAISS
- Sentence Transformers

## Visualization

- Matplotlib
- Seaborn

# 📂 Project Structure

app/
│
├── chatbot/
├── data/
├── models/
├── visuals/
├── dashboard/
├── reports/
├── notebooks/
│
├── main.py
└── requirements.txt

# 🔮 Future Scope

- RAG-based AI Assistant
- Real-Time Property Listings
- Rental Price Prediction
- Interactive Map Visualization
- Property Comparison Engine
- Personalized Investment Portfolios
- Cloud Deployment on AWS

# 👨‍💻 Author

Faraz Kazi

Artificial Intelligence & Data Science Engineer

Skills:

- Data Science
- Machine Learning
- Explainable AI
- Power BI
- Python Development

GitHub:
https://github.com/Faraz-05

LinkedIn:
(www.linkedin.com/in/farazkazi)