from urllib.request import urlretrieve
import csv
import os
import subprocess
import shutil

from pandas import read_csv

counter = 0

os.system("rm -rf classes")
os.system("rm -rf test_set")
os.system("rm -rf cifar-10-batches-bin")

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
			#if(counter == 5):
			#	break
			#meta_file.write(str(X[i][0]) + '\n')
			#print(image_num)
			sixty_per = int(image_num*0.6)
			for m in range(sixty_per+1, image_num):
				impath = path + '/' + str(m) + '.jpg'
				destpath = testpath + '/' + str(test_im_no) + '.jpg'
				shutil.move(impath, destpath)
				test_im_no += 1
			if(counter == 100):
				break
			meta_file.write(str(X[i][0]) + '\n')
			testpath = 'test_set/' + str(counter)
			os.makedirs(testpath)
			path = 'classes/' + str(counter)
			os.makedirs(path)
			print("class and test_set " + str(counter) + " is completed")
			image_num = 0
			test_im_no = 0
			filepath = path + '/' + str(image_num) + '.jpg'
			image_num += 1
			urlretrieve(str(X[i][1]), filepath)
			#counter+=1
			#if (counter == 5):
			#	break
			counter+=1
			string = str(X[i][0])
		else:
			filepath = path + '/' + str(image_num) + '.jpg'
			image_num += 1
			urlretrieve(str(X[i][1]), filepath)
meta_file.close()
print("Classes names written in batches.meta.txt file")
print("Images downloaded in separate folders under classes")
print("Converting images to 32*32 format")
#os.system("chmod +x resize-script.sh")
#os.system("chmod +x resize_test_images.sh")
subprocess.call(['./resize-script.sh'])
#subprocess.call(['./resize_test_images.sh'])
print("Image conversion to 32*32 done")

print("Calling python code to convert image to .bin format")
os.system("python convert.py")
os.makedirs('cifar-10-batches-bin')
shutil.move('data_batch_1.bin', 'cifar-10-batches-bin')
shutil.move('test_batch.bin', 'cifar-10-batches-bin')
shutil.move('batches.meta.txt', 'cifar-10-batches-bin')
os.system("tar -cvzf cifar-10-binary.tar.gz cifar-10-batches-bin")
os.makedirs("/tmp/cifar10_data")
shutil.move("cifar-10-binary.tar.gz", "/tmp/cifar10_data/")
#os.system("rm -rf classes")
#os.system("rm -rf test_set")
#os.system("rm -rf cifar-10-batches-bin")
os.system("python cifar10_train.py")
