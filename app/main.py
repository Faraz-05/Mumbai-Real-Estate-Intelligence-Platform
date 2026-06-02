import streamlit as st
import plotly.express as px

from chatbot.prediction_engine import PredictionEngine
from chatbot.data_engine import DataEngine
from chatbot.query_router import QueryRouter
from chatbot.explainability_engine import (
    ExplainabilityEngine
)
from chatbot.recommendation_engine import (
    RecommendationEngine
)


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Mumbai Real Estate Intelligence",
    layout="wide"
)

st.title(
    "🏠 Mumbai Real Estate Intelligence Platform"
)

st.markdown(
    """
    AI Powered Property Analytics,
    Price Prediction,
    Investment Insights,
    and Local AI Assistant
    """
)

st.divider()


# =====================================================
# LOAD ENGINES ONLY ONCE
# =====================================================

@st.cache_resource
def load_prediction_engine():

    engine = PredictionEngine()

    engine.load_model()

    return engine


@st.cache_resource
def load_data_engine():

    engine = DataEngine()

    engine.load_data()

    return engine


@st.cache_resource
def load_query_router():

    return QueryRouter()


prediction_engine = load_prediction_engine()

@st.cache_resource
def load_explainer():

    return ExplainabilityEngine(
        prediction_engine
    )

explainer = load_explainer()

data_engine = load_data_engine()

query_router = load_query_router()

@st.cache_resource
def load_recommendation_engine():

    return RecommendationEngine()


recommendation_engine = (
    load_recommendation_engine()
)


# =====================================================
# CREATE TABS
# =====================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "🏠 Price Prediction",
        "📈 Investment Analytics",
        "🤖 AI Assistant",
        "📊 Market KPIs"
    ]
)


# =====================================================
# TAB 1 - PRICE PREDICTION
# =====================================================

with tab1:

    st.header(
        "Property Price Prediction"
    )

    region = st.selectbox(
        "Region",
        [
            "Central",
            "Far Western",
            "Navi Mumbai",
            "South Mumbai",
            "Thane",
            "Western"
        ]
    )

    tier = st.selectbox(
        "Tier",
        [
            "affordable",
            "mid",
            "premium",
            "luxury"
        ]
    )

    property_type = st.selectbox(
        "Property Type",
        [
            "1BHK",
            "2BHK",
            "3BHK",
            "4BHK",
            "5BHK_penthouse"
        ]
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=10,
        value=2
    )

    carpet_area = st.number_input(
        "Carpet Area (sqft)",
        value=900
    )

    built_up_area = st.number_input(
        "Built Up Area (sqft)",
        value=1100
    )

    floor = st.number_input(
        "Floor",
        value=10
    )

    total_floors = st.number_input(
        "Total Floors",
        value=30
    )

    property_age = st.number_input(
        "Property Age",
        value=5
    )

    furnishing = st.selectbox(
        "Furnishing",
        [
            "fully_furnished",
            "semi_furnished",
            "unfurnished"
        ]
    )

    parking = st.selectbox(
        "Parking",
        [
            "1_covered",
            "2_covered",
            "none",
            "open"
        ]
    )

    balconies = st.number_input(
        "Balconies",
        value=2
    )

    builder_tier = st.selectbox(
        "Builder Tier",
        [
            "local",
            "tier1",
            "tier2"
        ]
    )

    metro_distance = st.number_input(
        "Metro Distance (minutes)",
        value=5
    )

    to_bkc = st.number_input(
        "Distance to BKC (km)",
        value=7
    )

    to_nariman = st.number_input(
        "Distance to Nariman Point (km)",
        value=18
    )

    luxury_score = st.slider(
        "Luxury Score",
        1,
        5,
        3
    )

    connectivity_score = st.slider(
        "Connectivity Score",
        1,
        100,
        80
    )

    if st.button("Predict Price"):

        property_data = {

            "region": region,
            "tier": tier,
            "property_type": property_type,
            "bedrooms": bedrooms,
            "carpet_area_sqft": carpet_area,
            "built_up_area_sqft": built_up_area,
            "floor": floor,
            "total_floors": total_floors,
            "property_age": property_age,
            "furnishing": furnishing,
            "parking": parking,
            "balconies": balconies,
            "builder_tier": builder_tier,
            "metro_distance_min": metro_distance,
            "to_bkc_km": to_bkc,
            "to_nariman_point_km": to_nariman,
            "luxury_score": luxury_score,
            "connectivity_score": connectivity_score
        }

        prediction = prediction_engine.predict_price(
            property_data
        )

        explanations = (
            explainer.get_top_explanations(
            property_data
            )
        )

        st.success(
            f"Predicted Price: ₹{prediction:,.0f}"
        )

        st.subheader(
            "Top Positive Factors"
        )

        st.dataframe(
            explanations["positive"]
        )

        st.subheader(
            "Top Negative Factors"
        )

        st.dataframe(
            explanations["negative"]
        )

        fig = explainer.create_waterfall_plot(
            property_data
        )

        st.pyplot(fig)

        ## recommended Investment locations:
        st.subheader(
            "Recommended Investment Localities"
        )

        recommendations = (
            recommendation_engine
            .recommend_localities(
                region=region,
                budget=prediction
            )
        )

        st.dataframe(
            recommendations
        )


# =====================================================
# TAB 2 - INVESTMENT ANALYTICS
# =====================================================

with tab2:

    st.header(
        "Investment Analytics"
    )

    # ==========================================
    # TABLES
    # ==========================================

    st.subheader(
        "Top Investment Localities"
    )

    investment_df = (
        data_engine
        .get_top_investment_localities()
    )

    st.dataframe(
        investment_df
    )

    st.subheader(
        "Top Luxury Localities"
    )

    luxury_df = (
        data_engine
        .get_top_luxury_localities()
    )

    st.dataframe(
        luxury_df
    )

    st.subheader(
        "Top Expensive Localities"
    )

    expensive_df = (
        data_engine
        .get_top_expensive_localities()
    )

    st.dataframe(
        expensive_df
    )

    st.divider()

    # ==========================================
    # CHART 1
    # INVESTMENT SCORE COMPARISON
    # ==========================================

    st.subheader(
        "Investment Score Comparison"
    )

    fig1 = px.bar(
        investment_df,
        x="locality",
        y="investment_score",
        title="Top Investment Localities",
        text_auto=".2f"
    )

    st.plotly_chart(
        fig1,
        width="stretch"
    )

    # ==========================================
    # CHART 2
    # PRICE VS INVESTMENT SCORE
    # ==========================================

    st.subheader(
        "Price vs Investment Score"
    )

    fig2 = px.scatter(
        investment_df,
        x="price_inr",
        y="investment_score",
        size="luxury_score",
        color="locality",
        hover_name="locality",
        title="Investment Score vs Property Price"
    )

    st.plotly_chart(
        fig2,
        width="stretch"
    )

    # ==========================================
    # CHART 3
    # LUXURY SCORE
    # ==========================================

    st.subheader(
        "Luxury Score Comparison"
    )

    fig3 = px.bar(
        luxury_df,
        x="locality",
        y="luxury_score",
        title="Top Luxury Localities",
        text_auto=".2f"
    )

    st.plotly_chart(
        fig3,
        width="stretch"
    )

    # ==========================================
    # CHART 4
    # MOST EXPENSIVE LOCALITIES
    # ==========================================

    st.subheader(
        "Most Expensive Localities"
    )

    fig4 = px.bar(
        expensive_df,
        x="Locality",
        y="Avg_Price",
        title="Most Expensive Localities"
    )

    st.plotly_chart(
        fig4,
        width="stretch"
    )


# =====================================================
# TAB 3 - AI ASSISTANT
# =====================================================

with tab3:

    st.header(
        "AI Real Estate Assistant"
    )

    st.write(
        "Ask questions like:"
    )

    st.write(
        "- Should I invest in Powai?"
    )

    st.write(
        "- Is Bandra West expensive?"
    )

    st.write(
        "- Tell me about Worli"
    )

    user_question = st.text_input(
        "Ask your question"
    )

    if st.button(
        "Ask AI"
    ):

        with st.spinner(
            "Thinking..."
        ):

            answer = query_router.route(
                user_question
            )

            st.write(answer)


# =====================================================
# TAB 4 - MARKET KPIs
# =====================================================

with tab4:

    st.header(
        "Mumbai Market KPIs"
    )

    avg_price = (
        data_engine.get_average_property_price()
    )

    summary = (
        data_engine.get_summary()
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Average Property Price",
            f"₹{avg_price:,.0f}"
        )

    with col2:

        st.metric(
            "Total Localities",
            summary["localities"]
        )

    with col3:

        st.metric(
            "Investment Records",
            summary["investment_records"]
        )

    st.subheader(
        "Top Regions"
    )

    st.dataframe(
        data_engine.get_top_regions()
    )