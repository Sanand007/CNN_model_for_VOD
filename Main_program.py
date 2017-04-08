from urllib.request import urlretrieve
import csv
import os
import subprocess

from pandas import read_csv

counter = 0

os.makedirs('classes')
filepath = 'english.csv'
names = ['ANP', 'image_url']
dataframe = read_csv(filepath, names=names)
array = dataframe.values
X = array[1:,:]
print(len(X))
image_num = 0
path = ""
filepath = ""
with open('batches.meta.txt', 'w') as meta_file:
	string = ""
	for i in range(0, len(X)):
		if (i == 0):
			meta_file.write(X[0][0] + '\n')
			path = 'classes/' + str(counter)
			os.makedirs(path)
			filepath = path + '/' + str(image_num) + '.jpg'
			image_num += 1
			urlretrieve(str(X[0][1]), filepath)
			counter += 1
			string = str(X[0][0])
		elif (string != str(X[i][0])):
			meta_file.write(str(X[i][0]) + '\n')
			path = 'classes/' + str(counter)
			os.makedirs(path)
			image_num = 0
			filepath = path + '/' + str(image_num) + '.jpg'
			image_num += 1
			urlretrieve(str(X[i][1]), filepath)
			counter+=1
			string = str(X[i][0])
		elif (image_num < 6):
			filepath = path + '/' + str(image_num) + '.jpg'
			image_num += 1
			urlretrieve(str(X[i][1]), filepath)
		if (counter == 3):
			print(i)
			break
meta_file.close()
print("Classes names written in batches.meta.txt file")
print("Images downloaded in separate folders under classes")
print("Converting images to 32*32 format")
subprocess.call(['./resize-script.sh'])
print("Image conversion to 32*32 done")
print("Calling python code to convert image to .bin format")
os.system("python convert-images-to-cifar-format.py")
