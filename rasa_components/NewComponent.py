from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata

import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
from custom_intent_predictor.predict import predictIntent


class new_component(Component):
    """A pre-trained sentiment component"""

    name = "new_component"
    provides = ["intents"]
    requires = []
    defaults = {}
    language_list = ["en"]

    def __init__(self, component_config=None):
        super(new_component, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        """Not needed, because the the model is pretrained"""
        pass

    def convert_to_rasa(self,predicted_intent, conf, message):
        """Convert model output into the Rasa NLU compatible output format."""

        intent = {
                     'name': predicted_intent,
                     'confidence': conf
                 }

        # entity = {"value": value,
        #           "confidence": confidence,
        #           "entity": "sentiment",
        #           "extractor": "sentiment_extractor"}

        return intent

    def process(self, message, **kwargs):
        """Retrieve the text message, pass it to the classifier
            and append the prediction results to the message class."""

        # sid = SentimentIntensityAnalyzer()
        # res = sid.polarity_scores(message.text)
        # key, value = max(res.items(), key=lambda x: x[1])
        # print ("message is -",message)
        predicted_intent, conf = predictIntent(message.text)
        intent = self.convert_to_rasa(predicted_intent,conf, message.text)

        message.set("intent", intent, add_to_output=True)

    def persist(path, project_name, fixed_model_name):
        """Pass because a pre-trained model is already persisted"""

        pass
