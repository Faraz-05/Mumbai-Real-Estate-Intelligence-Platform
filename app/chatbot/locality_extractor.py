from chatbot.data_engine import DataEngine


class LocalityExtractor:

    def __init__(self):

        self.data_engine = DataEngine()

        self.data_engine.load_data()

        self.localities = (
            self.data_engine.investment_df[
                "locality"
            ]
            .unique()
            .tolist()
        )

    def extract_locality(self, question):

        question = question.lower()

        for locality in self.localities:

            if locality.lower() in question:

                return locality

        return None