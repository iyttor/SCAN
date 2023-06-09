import os
import torch
import torchvision.datasets as datasets
from PIL import Image
from utils.mypath import MyPath
from torchvision import transforms as tf
from glob import glob


class Imagene(datasets.ImageFolder):
	def __init__(self, root=MyPath.db_root_dir('imagene'), split='train', transform=None):
		super(Imagene, self).__init__(root=os.path.join(root, split), transform=None)

		self.transform = transform
		self.split = split
		self.resize = tf.Resize(256)

	def __len__(self):
		return len(self.imgs)

	def __getitem__(self, index):
		path, target = self.imgs[index]
		with open(path, 'rb') as f:
			img = Image.open(f).convert('RGB')
		im_size = img.size
		img = self.resize(img)

		if self.transform is not None:
			img = self.transform(img)

		out = {'image': img, 'target': target, 'meta': {'im_size': im_size, 'index': index}}

		return out

	def get_image(self, index):
		path, target = self.imgs[index]
		with open(path, 'rb') as f:
			img = Image.open(f).convert('RGB')
		img = self.resize(img)
		return img
