import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np
import os
import datetime as dt


cifar10_classes = [    'airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
num_epochs = 30
train = False
#name_data = 'CIFAR10'
name_data = 'MNIST'
if name_data is 'CIFAR10':
    # Ustawienia
    batch_size = 64
    latent_dim = 100
    num_classes = 10
    image_size = 32
    channels = 3

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,), (0.5,))
    ])

    # Ładowanie danych MNIST
    train_dataset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
    train_loader  = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
elif name_data is 'MNIST':
    # Ustawienia
    batch_size = 64
    latent_dim = 100
    num_classes = 10
    image_size = 28
    channels = 1

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    # Ładowanie danych MNIST
    train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    train_loader  = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# Global path settings
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
repo_name = "tul_fitnessapp"
path_script = os.path.dirname(os.path.realpath(__file__))
path_dir = os.path.dirname(os.path.realpath(path_script))
index = path_script.find(repo_name)
path_models = os.path.join(path_dir, "models")
path_data = os.path.join(path_dir, "data")

def save_model(model):
    try:
        torch.save(model, os.path.join(path_models, f'{name_data}'))
        print(f"Saved model: {name_data} at: {dt.datetime.now()}")
    except Exception as e:
        print(f"Failed to save a model: {name_data}! Error code: {e} {dt.datetime.now()}")

def load_model():
    try:
        model = torch.load(os.path.join(path_models, f'{name_data}'))
        print(f"Loaded model: {name_data} at: {dt.datetime.now()}")
        return model
    except Exception as e:
        print(f"Failed to load a model: {name_data}! Error code: {e} {dt.datetime.now()}")


class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.label_emb = nn.Embedding(num_classes, num_classes)
        
        self.init_size = image_size // 4
        self.l1 = nn.Sequential(nn.Linear(latent_dim + num_classes, 128 * self.init_size ** 2))
        
        self.conv_blocks = nn.Sequential(
            nn.BatchNorm2d(128),
            nn.Upsample(scale_factor=2),
            nn.Conv2d(128, 128, 3, stride=1, padding=1),
            nn.BatchNorm2d(128, 0.8),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Upsample(scale_factor=2),
            nn.Conv2d(128, 64, 3, stride=1, padding=1),
            nn.BatchNorm2d(64, 0.8),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(64, channels, 3, stride=1, padding=1),
            nn.Tanh(),
        )

    def forward(self, noise, labels):
        gen_input = torch.cat((self.label_emb(labels), noise), -1)
        out = self.l1(gen_input)
        out = out.view(out.shape[0], 128, self.init_size, self.init_size)
        img = self.conv_blocks(out)
        return img


class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.label_embedding = nn.Embedding(num_classes, num_classes)

        self.model = nn.Sequential(
            nn.Linear(num_classes + int(np.prod((channels, image_size, image_size))), 512),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(512, 512),
            nn.Dropout(0.4),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(512, 512),
            nn.Dropout(0.4),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(512, 1),
            nn.Sigmoid()
        )

    def forward(self, img, labels):
        d_in = torch.cat((img.view(img.size(0), -1), self.label_embedding(labels)), -1)
        validity = self.model(d_in)
        return validity


def generate_image(generator, class_label, ax):
    z = torch.randn(1, latent_dim).to(device)
    label = torch.tensor([class_label], device=device)
    generated_img = generator(z, label).cpu().detach().numpy()
    if name_data is 'CIFAR10':
        generated_img = np.transpose(generated_img, (0, 2, 3, 1)).astype(np.float32)
        ax.set_title(f"GEN for {cifar10_classes[class_label]}")
        ax.tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)
    else:
        ax.tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)
        ax.set_title(f"GEN for {class_label}")

    ax.imshow(generated_img.squeeze())


if __name__ == "__main__":

    generator = Generator()
    discriminator = Discriminator()

    optimizer_G = optim.Adam(generator.parameters(), lr=0.0002, betas=(0.5, 0.999))
    optimizer_D = optim.Adam(discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))

    adversarial_loss = nn.BCELoss()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    generator.to(device)
    discriminator.to(device)
    adversarial_loss.to(device)

    if train is True:
        for epoch in range(num_epochs):
            for i, (imgs, labels) in enumerate(train_loader):
                
                batch_size = imgs.size(0)
                
                # Prawdziwe obrazki i etykiety
                real_imgs = imgs.to(device)
                labels = labels.to(device)
                valid = torch.ones((batch_size, 1), device=device, dtype=torch.float32)
                fake = torch.zeros((batch_size, 1), device=device, dtype=torch.float32)
                
                # Trening Dyskryminatora
                optimizer_D.zero_grad()
                
                # Prawdziwe obrazki
                real_loss = adversarial_loss(discriminator(real_imgs, labels), valid)
                
                # Fałszywe obrazki
                z = torch.randn(batch_size, latent_dim, device=device)
                gen_labels = torch.randint(0, num_classes, (batch_size,), device=device)
                fake_imgs = generator(z, gen_labels)
                fake_loss = adversarial_loss(discriminator(fake_imgs.detach(), gen_labels), fake)
                
                d_loss = (real_loss + fake_loss) / 2
                d_loss.backward()
                optimizer_D.step()
                
                # Trening Generatora
                optimizer_G.zero_grad()
                
                g_loss = adversarial_loss(discriminator(fake_imgs, gen_labels), valid)
                
                g_loss.backward()
                optimizer_G.step()
                
                if i % 100 == 0:
                    print(f"[Epoch {epoch}/{num_epochs}] [Batch {i}/{len(train_loader)}] [D loss: {d_loss.item():.4f}] [G loss: {g_loss.item():.4f}]")
        save_model(generator)
    else:
        generator = load_model()
        _, ax = plt.subplots(5,2, figsize=(10,7))
        for index in range(10):
            generate_image(generator, index, ax[index // 2][index % 2])
        plt.show()


