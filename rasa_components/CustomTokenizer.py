from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata

import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
import sys

class Tokenizer(Component):
    """A pre-trained sentiment component"""

    name = "Tokenizer"
    provides = ["tokens"]
    requires = []
    defaults = {}
    language_list = ["en"]

    def __init__(self, component_config=None):
        super(Tokenizer, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        """Not needed, because the the model is pretrained"""
        pass

    def tokenizer(self,sentence):
        return sentence.split()

    def process(self, message, **kwargs):
        """Retrieve the text message, pass it to the classifier
            and append the prediction results to the message class."""
        message.set("tokens", self.tokenizer(message.text), add_to_output=True)

    def persist(path, project_name, fixed_model_name):
        """Pass because a pre-trained model is already persisted"""

        pass
