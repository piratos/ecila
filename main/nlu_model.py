from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

import sys

# train function
# data: data,json
# config: spacy config file
# model: save trained model
def train_nlu(data, config, model_dir):
	training_data = load_data(data)
	trainer = Trainer(RasaNLUConfig(config))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'proto1')


# run the trained model
# query: message we want the model to respond to it
def run_nlu(query, config='spacy'):
	interpreter = Interpreter.load('models/nlu/default/proto1', RasaNLUConfig('config_%s.json' % config))
	return interpreter.parse(query)


def main():
	config = 'spacy'
	if len(sys.argv) == 3:
		if sys.argv[2] == 'spacy':
			config = 'spacy'
		elif sys.argv[2] == 'mitie':
			config = 'mitie'
	if len(sys.argv) < 2:
		print('run with options "run" or "train" ')
	elif sys.argv[1] == 'train':
		train_nlu('data/data.json', 'config_%s.json' % config, 'models/nlu')
	elif sys.argv[1] == 'run':
		print(run_nlu('I wonder how is it in barcelona tomorrow', config=config))
	else:
		print('run with options "run" or "train" ')

if __name__ == '__main__':
	main()
