import torch
from torch import nn as nn

class Net(nn.Module):
	def __init__(self):
		super (Net, self).__init__()

		self.cnn1 = nn.Conv2d(in_channels = 1, out_channels = 32, kernel_size = 5, stride = 1, padding = 2)
		self.relu1 = nn.ReLU()
		self.norm1 = nn.BatchNorm2d(32)
		nn.init.xavier_uniform(self.cnn1.weight)
		self.maxpool1 = nn.MaxPool2d(kernel_size=2)
		self.cnn2 = nn.Conv2d(in_channels = 32, out_channels = 64, kernel_size = 3, stride = 1, padding = 2)
		self.relu2 = nn.ReLU()
		self.norm2 = nn.BatchNorm2d(64)
		nn.init.xavier_uniform(self.cnn2.weight)

		self.maxpool2 = nn.MaxPool2d(kernel_size=2)

		self.fc1 = nn.Linear(4096, 4096)
		self.fcrelu = nn.ReLU()

		self.fc2 = nn.Linear(4096, 10)
        
	def forward(self, x):
		out = self.cnn1(x)
		out = self.relu1(out)
		out = self.norm1(out)
        # 1,32,28,28
		out = self.maxpool1(out) #(1,32,14,14)

		out = self.cnn2(out) #(1,64,16,16)
		out = self.relu2(out)
		out = self.norm2(out)

		out = self.maxpool2(out) #(1,64,8,8) (4096)

		out = out.view(out.size(0),-1)

		out = self.fc1(out)
		out = self.fcrelu(out)

		out = self.fc2(out)
		return out
