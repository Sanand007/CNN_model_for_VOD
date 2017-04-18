from PIL import Image
from scipy.misc import imread
import imghdr
import os
from array import *

data = array('B')

for dirname, dirnames, filenames in os.walk('./classes'):
	for filename in filenames:
		if(filename.endswith('.png')):
			try:
				im = Image.open(os.path.join(dirname, filename)).convert('RGB')
			except ValueError:
				continue
			pix = im.load()
			image = imread(os.path.join(dirname, filename))
			if(len(image.shape) == 3):
				print('RGB' + str(dirname) + '/' + str(filename))
				class_name = int(os.path.join(dirname).split('/')[-1])
				data.append(class_name)
				for color in range(0,3):
					for x in range(0,32):
						for y in range(0,32):
							data.append(pix[x,y][color])
			else:
				print('other' + str(dirname) + '/' + str(filename))
				continue
output_file = open('data_batch_1.bin', 'wb')
data.tofile(output_file)
output_file.close()


for dirname, dirnames, filenames in os.walk('./test_set'):
	for filename in filenames:
		if(filename.endswith('.png')):
			try:
				im = Image.open(os.path.join(dirname, filename)).convert('RGB')
			except ValueError:
				continue
			pix = im.load()
			image = imread(os.path.join(dirname, filename))
			if(len(image.shape) == 3):
				print('RGB' + str(dirname) + '/' + str(filename))
				class_name = int(os.path.join(dirname).split('/')[-1])
				data.append(class_name)
				for color in range(0,3):
					for x in range(0,32):
						for y in range(0,32):
							data.append(pix[x,y][color])
			else:
				print('other' + str(dirname) + '/' + str(filename))
				continue
output_file = open('test_batch.bin', 'wb')
data.tofile(output_file)
output_file.close()