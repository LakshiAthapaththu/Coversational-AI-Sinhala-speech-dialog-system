# coding=utf-8
import logging
import pprint
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter
from rasa_nlu.test import run_evaluation


logfile = 'run_nlu_model.log'

def run_nlu(nlu_path):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    interpreter = Interpreter.load(nlu_path)
    # file_read = open('test_sentences','r')
    # for line in file_read:
    #     sentence = line.strip()
    pprint.pprint(interpreter.parse('මාස හය'))



if __name__ == '__main__':
    # train_nlu('./data/nlu.md', 'nlu_config.yml', './models')
    run_nlu('../rasa_models/current/nlu')
