import torch
import os
from torch.utils.data import Dataset
import datetime as dt
from torchvision import datasets, transforms
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
import seaborn as sb
import numpy as np
torch.autograd.set_detect_anomaly(True)

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers=1):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        self.rnn = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        
    def forward(self, x, h):
        out, h = self.rnn(x, h)
        out = self.fc(out)
        return out, h

class CustomDataset(Dataset):
    def __init__(self, data, targets, device):
        self.data = torch.tensor(data, dtype=torch.float32, device=device) / 255.0
        self.targets = torch.tensor(targets, dtype=torch.long, device=device)
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        sample = {'data': self.data[idx], 'target': self.targets[idx]}
        return sample

# Dodanie szumu do obrazu
class AddNoise(object):
    def __init__(self, noise_factor, threshold):
        self.noise_factor = noise_factor
        self.threshold = threshold

    def __call__(self, img):
        mask = np.random.rand(28,28)
        return img * ((mask < self.threshold) * mask)

# Przycięcie połowy obrazu
class RandomCropHalf(object):
    def __call__(self, img):
        h, w = img.size()
        return img[:h//2, :]

def mnist(device, train, augment=False):
    mnist = datasets.MNIST(root='data', train=train, download=True, transform=None)
    data = mnist.data.float() / 255.0
    targets = mnist.targets
    
    # Filter out "0" class samples
    data_zero = data[targets == 0]
    targets_zero = targets[targets == 0]
    
    # Apply data augmentation if requested
    if augment:
        augmented_data = []
        augmentation_transform = transforms.Compose([
            AddNoise(noise_factor=0, threshold=0.5), 
            #RandomCropHalf()
        ])
        
        for img in data_zero:
            # Convert tensor to PIL Image
            augmented_img = augmentation_transform(img)
            #plt.imshow(augmented_img)
            #plt.show()
            augmented_data.append(augmented_img)
        
        # Concatenate augmented data with original data
        data_zero = torch.cat((data_zero, torch.stack(augmented_data)), dim=0)
        targets_zero = torch.cat((targets_zero, targets_zero), dim=0)  # Assuming labels stay the same
    
    return CustomDataset(data_zero, targets_zero, device), 28*28

# Global path settings
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
repo_name = "tul_fitnessapp"
path_script = os.path.dirname(os.path.realpath(__file__))
path_dir = os.path.dirname(os.path.realpath(path_script))
index = path_script.find(repo_name)
path_models = os.path.join(path_dir, "models")
path_data = os.path.join(path_dir, "data")


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


def generate_image(model, start_pixel, hidden_size, num_layers):
    model.eval()
    generated_image = [start_pixel]
    h = (torch.zeros(num_layers, 1, hidden_size).to(device),
         torch.zeros(num_layers, 1, hidden_size).to(device))
    
    input_pixel = start_pixel.view(1, 1, 1)
    for _ in range(28 * 28 - 1):
        output, h = model(input_pixel, h)
        next_pixel = output.view(-1)
        generated_image.append(next_pixel)
        input_pixel = next_pixel.view(1, 1, 1)
    
    generated_image = torch.stack(generated_image).view(28,28).detach().cpu().numpy()
    #print(f'GENd img: {generated_image}')
    return generated_image


def main():
    """
    sequence_length represents the number of time steps in each sequence. For the MNIST dataset, where each image is 28x28 pixels, 
    the sequence length is 28*28 = 784. This means each image is treated as a sequence of 784 time steps, 
    where each pixel value is an input at a time step.
    """
    data, sequence_length = mnist(device=device, train=True, augment=True)
    train = True
    continue_train = False

    """
    h in RNN Model
    The h variable in the RNN model represents the hidden state of the RNN. For an LSTM (Long Short-Term Memory) network, it typically includes two components: the hidden state (h) and the cell state (c). These states are used to carry information across time steps in sequence data, allowing the network to maintain memory of previous inputs.

    Hidden State (h): Captures the output of the LSTM at each time step.
    Cell State (c): Carries long-term information.
    In the context of the code, h is initialized with zeros at the beginning of training for each batch:
    """

    data_loader = DataLoader(data, batch_size=64, shuffle=True)

    if train:
        if continue_train:
            RNN_Model = load_model(name="RNN_model")
            RNN_Model.to(device)
        else:
            RNN_Model = RNN(input_size=1, hidden_size=128, output_size=1, num_layers=1)
            RNN_Model.to(device)

        num_epochs = 10
        criterion = nn.MSELoss()
        optimizer = optim.Adam(RNN_Model.parameters(), lr=0.001)
        print(f'DEVICE RUNNING: {device}')

        for epoch in range(num_epochs):
            for batch in data_loader:
                images = batch['data'].to(device)
                images = images.view(-1, sequence_length, 1)
                print(f'IMAGES SIZE: {len(images)}')
                
#================================================================================================================================                
                h = (torch.zeros(1, images.size(0), 128).to(device), torch.zeros(1, images.size(0), 128).to(device))
                #Trenowanie piksel po pikselu dla każego zdjęcia
                for pixel in range(images.size(1)):
                    pix_val = images[:,pixel,:].unsqueeze(-1)
                    outputs, h = RNN_Model(pix_val, h)
                
                    loss = criterion(outputs.squeeze(), pix_val.squeeze())
                
                    optimizer.zero_grad()
                    loss.backward(retain_graph=True)
                    optimizer.step()
                    print(f'Epoch [{epoch + 1}/{num_epochs}], Pixel [{pixel}/784] Loss: {loss.item():.7f}')
            
            print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.7f}')
#================================================================================================================================                

        save_model(RNN_Model, "RNN_model")
    else:
        RNN_Model = load_model(name="RNN_model")
        RNN_Model.to(device)


    _, ax = plt.subplots(5,2, figsize=(10,8))
    for index in range(10):
        generated_image = generate_image(RNN_Model, torch.randn(1).to(device), 128, 1)
        ax[index // 2, index % 2].imshow(generated_image, cmap='gray')

    plt.show()

if __name__ == "__main__":
    main()