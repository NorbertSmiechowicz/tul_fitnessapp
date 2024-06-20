from model import RNN
import torch
import os
from logging_elastic_config import logger
import datetime as dt
from rabbitmq import send_message_rabbit, receive_message_rabbit


#Global path settings
repo_name   = "tul_fitnessapp"
path_script = os.path.dirname(os.path.realpath(__file__))
path_dir    = os.path.dirname(os.path.realpath(path_script))
index       = path_script.find(repo_name)
path_models = path_dir + "\\models\\"
path_data   = path_dir + "\\data\\"



def save_model(model, name):
    try:
        torch.save(model, path_models + f'{name}.pth')
        logger.info(f"Saved model: {name} at: {dt.datetime.now()}")
    except Exception as e:
        logger.error(f"Failed to save a model: {name}! Error code: {e} {dt.datetime.now()}")

def load_model(name):
    try:
        model = torch.load(path_models + f'{name}.pth')
        logger.info(f"Loaded model: {name} at: {dt.datetime.now()}")
        return model
    except Exception as e:
        logger.error(f"Failed to load a model: {name}! Error code: {e} {dt.datetime.now()}")


def main():
    print(f"Path to models: {path_models}")
    print(f"Path to script: {path_script}")
    print(f"Path to data: {path_data}")
    print(f"Path to AI_MODELS directory: {path_dir}")
    print(f"Torch version: {torch.__version__}")

    try:
        model = load_model(name='CNN_cifar')
        print("Model downloaded succesfully!!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()