from chatbot.data_engine import DataEngine
from chatbot.llm_engine import LLMEngine


class QueryRouter:

    def __init__(self):

        self.data_engine = DataEngine()
        self.data_engine.load_data()

        self.llm_engine = LLMEngine()

    def route(self, question):

        question = question.lower()

        # =========================
        # Investment Localities
        # =========================

        if "best locality" in question \
        or "investment locality" in question:

            result = (
                self.data_engine
                .get_top_investment_localities()
            )

            return result.to_string()

        # =========================
        # Luxury Localities
        # =========================

        elif "luxury" in question:

            result = (
                self.data_engine
                .get_top_luxury_localities()
            )

            return result.to_string()

        # =========================
        # Average Price
        # =========================

        elif (
        "average price" in question
        or
        "average property price" in question
        ):

            price = (
                self.data_engine
                .get_average_property_price()
            )

            return f"Average Property Price: ₹{price:,.0f}"
        
        elif (
        "expensive locality" in question
        or "most expensive" in question
        ):
    
            result = (
                self.data_engine
                .get_top_expensive_localities()
            )

            return result.to_string()

        # =========================
        # Top Regions
        # =========================

        elif "top region" in question \
        or "best region" in question:

            result = (
                self.data_engine
                .get_top_regions()
            )

            return result.to_string()

        # =========================
        # Everything Else → LLM
        # =========================

        else:

            return self.llm_engine.answer_question(
                question
            )