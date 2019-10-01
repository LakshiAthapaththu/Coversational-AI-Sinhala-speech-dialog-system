from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata
import nltk
import os
import sys

class Tokenizer(Component):

    name = "Tokenizer"
    provides = ["tokens"]
    requires = []
    defaults = {}
    language_list = ["en"]

    def __init__(self, component_config=None):
        super(Tokenizer, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        pass

    def tokenizer(self,sentence):
        return sentence.split()

    def process(self, message, **kwargs):
        message.set("tokens", self.tokenizer(message.text), add_to_output=True)

    def persist(path, project_name, fixed_model_name):
        pass
