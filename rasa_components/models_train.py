import logging
from rasa_core import config as config_core
from rasa_nlu import config as config_nlu
from rasa_core import utils
from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
import pprint
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu.test import run_evaluation


logfile = 'train_model.log'


def train_core(domain_file, model_path, training_data_file, policy_config):
    # logging.basicConfig(filename=logfile, level=logging.DEBUG)
    agent = Agent(domain_file, policies=config_core.load(policy_config))
    training_data = agent.load_data(training_data_file)
    agent.train(training_data)
    agent.persist(model_path)
    return agent

def train_nlu(data_path, configs, model_path):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    training_data = load_data(data_path)
    trainer = Trainer(config_nlu.load(configs))
    trainer.train(training_data)
    model_directory = trainer.persist(path = model_path, project_name='current', fixed_model_name='nlu')
    # run_evaluation(data_path, model_directory)


if __name__ == '__main__':
    train_nlu('./data/nlu.md', 'nlu_config.yml', '../rasa_models')
    # train_core('domain.yml', '../rasa_models/dialogue', './data/stories.md', 'policy.yml')
