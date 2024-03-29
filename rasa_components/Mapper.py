from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata

import nltk
import os
import sys

class Mapper(Component):
    name = "Mapper"
    provides = ["intent"]
    requires = ["intent_number","confident"]
    defaults = {}
    language_list = ["en"]

    def __init__(self, component_config=None):
        super(Mapper, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        pass

    def map(self, intent):
        mapper = {
            "1": "open a new bank account",
            "2": "savings account",
            "3": "fixed account",
            "4": "account type",
            "5": "selection",
            "6": "try again",
            "7": "don't try again",
            "8": "correct detailas",
            "9": "incorrect details",
            "10": "confirmation",
            "11": "not confirmation",
            "12": "number of months",
            "13": "after completion",
            "14": "monthly"
        }

        return mapper[str(intent)]

    def setIntent(self,intent, confident):
        final_intent = {
            "name": intent,
            "confidence": confident
        }
        return final_intent

    def process(self, message, **kwargs):
        intent_num = message.get("intent_number")
        conf = message.get("confident")
        message.set("intent", self.setIntent(self.map(intent_num), conf), add_to_output=True)


    def persist(path, project_name, fixed_model_name):
        pass
