from model import RNN
import torch
import os

#Global path settings
repo_name = "tul_fitnessapp"
path_script = os.path.dirname(os.path.realpath(__file__))
path_dir = os.path.dirname(os.path.realpath(path_script))
index = path_script.find(repo_name)
path_models = path_dir + "\\models\\"



def save_model(model, name):
    torch.save(model, path_models + f'{name}.pth')

def load_model(name):
    return torch.load(path_models + f'{name}.pth')


def main():
    print(path_models)
    print(path_script)
    print(path_dir)

    try:
        model = load_model(name='CNN_cifar')
        print("Model downloaded succesfully!!")
    except Exception as e:
        print(f"An error occurred: {e}")

    


if __name__ == "__main__":
    main()