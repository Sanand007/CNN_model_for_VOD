This model is capable to use visual ontology dataset to extract and write all the possible ANP's and then extract and download all the images of each class in separate folders and then convert the images to 32*32 bits and then divide the trainig dataset to 60 for training and 40 for testing and then convert it separately to .bin format.


Go to VOD website and request to download the csv file containing all the ANP arranged with image url.

Download and extract the english.csv file to the same folder as this model and run Main_program.py


first make a virtualenv with python3.5.  This is important to run Main_program.py

if you want to run it with python 2.7 then you need to adjust request.urlretrieve as per python2.7
