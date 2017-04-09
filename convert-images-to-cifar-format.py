#python script for converting 32x32 pngs to format

from PIL import Image
import os
from array import *

data = array('B')

for dirname, dirnames, filenames in os.walk('./classes'):
    for filename in filenames:
        if (filename.endswith('.jpg')):
            im = Image.open(os.path.join(dirname, filename))
            pix = im.load()

            class_name = int(os.path.join(dirname).split('/')[-1])

            data.append(class_name)

            for color in range(0,3):
                for x in range(0,32):
                    for y in range(0,32):
                        data.append(pix[x,y][color])

output_file = open('cnn-ready.bin', 'wb')
data.tofile(output_file)
output_file.close()



'''for dirname, dirnames, filenames in os.walk('./test_set'):
    for filename in filenames:
        if (filename.endswith('.jpg')):
            im = Image.open(os.path.join(dirname, filename))
            pix = im.load()

            class_name = int(os.path.join(dirname).split('/')[-1])

            data.append(class_name)

            for color in range(0,3):
                for x in range(0,32):
                    for y in range(0,32):
                        data.append(pix[x,y][color])

output_file = open('test.bin', 'wb')
data.tofile(output_file)
output_file.close()'''
