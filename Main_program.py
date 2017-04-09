from urllib.request import urlretrieve
import csv
import os
import subprocess
import shutil

from pandas import read_csv

counter = 0

os.makedirs('classes')
os.makedirs('test_set')
test_im_no = 0
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
			testpath = 'test_set/' + str(counter)
			os.makedirs(testpath)
			filepath = path + '/' + str(image_num) + '.jpg'
			image_num += 1
			urlretrieve(str(X[0][1]), filepath)
			counter += 1
			string = str(X[0][0])
		elif (string != str(X[i][0])):
			meta_file.write(str(X[i][0]) + '\n')
			print(image_num)
			sixty_per = int(image_num*0.6)
			for m in range(sixty_per+1, image_num):
				impath = path + '/' + str(m) + '.jpg'
				destpath = testpath + '/' + str(test_im_no) + '.jpg'
				shutil.move(impath, destpath)
				test_im_no += 1
			if (counter == 5):
				break
			testpath = 'test_set/' + str(counter)
			os.makedirs(testpath)
			path = 'classes/' + str(counter)
			os.makedirs(path)
			image_num = 0
			test_im_no = 0
			filepath = path + '/' + str(image_num) + '.jpg'
			image_num += 1
			urlretrieve(str(X[i][1]), filepath)
			counter+=1
			string = str(X[i][0])
		elif (image_num <= 10):
			filepath = path + '/' + str(image_num) + '.jpg'
			image_num += 1
			urlretrieve(str(X[i][1]), filepath)
meta_file.close()
print("Classes names written in batches.meta.txt file")
print("Images downloaded in separate folders under classes")
print("Converting images to 32*32 format")
subprocess.call(['./resize-script.sh'])
print("Image conversion to 32*32 done")

print("Calling python code to convert image to .bin format")
os.system("python convert-images-to-cifar-format.py")
