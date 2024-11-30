import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import pandas as pd
import numpy as np
import os
import datetime as dt

# Global path settings
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
repo_name = "tul_fitnessapp"
path_script = os.path.dirname(os.path.realpath(__file__))
path_dir = os.path.dirname(os.path.realpath(path_script))
index = path_script.find(repo_name)
path_models = os.path.join(path_dir, "models")
path_data = os.path.join(path_dir, "data")

# Define the RNN model
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers=1):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        self.rnn = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        
    def forward(self, x, h):
        out, h = self.rnn(x, h)
        out = self.fc(out[:, -1, :])  # We are only interested in the output of the last time step
        return out, h
    

class CustomDataset(Dataset):
    def __init__(self, csv_file):
        data = pd.read_csv(csv_file)
        self.features = data.iloc[:, 1:-1].values
        self.targets = data.iloc[:, 3].values
        print(self.targets)

        self.features = torch.tensor(self.features, dtype=torch.float32)
        self.targets = torch.tensor(self.targets, dtype=torch.float32)

    def __len__(self):
        return len(self.features)

    def __getitem__(self, idx):
        return {'data': self.features[idx], 'target': self.targets[idx]}
    
def save_model(model, name):
    try:
        torch.save(model, os.path.join(path_models, f'{name}.pth'))
        print(f"Saved model: {name} at: {dt.datetime.now()}")
    except Exception as e:
        print(f"Failed to save a model: {name}! Error code: {e} {dt.datetime.now()}")

def load_model(name):
    try:
        model = torch.load(os.path.join(path_models, f'{name}.pth'))
        print(f"Loaded model: {name} at: {dt.datetime.now()}")
        return model
    except Exception as e:
        print(f"Failed to load a model: {name}! Error code: {e} {dt.datetime.now()}")



def main():
    dataset = CustomDataset(os.path.join(path_data, "model_data.csv"))
    input_size = dataset.features.shape[1]
    hidden_size = 128
    output_size = input_size
    num_layers = 1
    num_epochs = 5
    learning_rate = 0.001
    train = True
    continue_train = False

    print(f"PATH DATA: {path_data}")
    data_loader = DataLoader(dataset, batch_size=1, shuffle=True)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    criterion = nn.MSELoss()

    if train:
        if continue_train:
            RNN_Model = load_model(name="RNN_model")
            RNN_Model.to(device)
        else:
            RNN_Model = RNN(input_size=input_size, hidden_size=hidden_size, output_size=output_size, num_layers=num_layers)
            RNN_Model.to(device)
        optimizer = optim.Adam(RNN_Model.parameters(), lr=learning_rate)

        for epoch in range(num_epochs):
            for batch in data_loader:
                features = batch['data'].to(device).view(1, -1, input_size)
                targets = batch['target'].to(device)

                h = (torch.zeros(num_layers, features.size(0), hidden_size).to(device),
                    torch.zeros(num_layers, features.size(0), hidden_size).to(device))
                
                outputs, h = RNN_Model(features, h)
                loss = criterion(outputs, targets)
                
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                
            print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.7f}')
    else:
        h = (torch.zeros(num_layers, features.size(0), hidden_size).to(device),
            torch.zeros(num_layers, features.size(0), hidden_size).to(device))
        RNN_Model.eval()
        outputs = RNN_Model(dataset.features, h)

if __name__ == '__main__':
    main()
