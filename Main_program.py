import urllib
import csv

from pandas import read_csv

filepath = 'english.csv'
names = ['ANP', 'image_url']
dataframe = read_csv(filepath, names=names)
array = dataframe.values
X = array[1:,:]
print(len(X))

#urllib.urlretrieve("http://farm1.staticflickr.com/215/517510757_9ced246a66.jpg", "local-filename.jpg")
