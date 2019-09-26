import os
from PIL import Image, ImageOps
import glob

'''
pathIn = path to video
pathOut = where output images will be saved
name = name of file
newsize = desired size
int_desiredLength = integer point for output image file name, eg int_desiredLength=3 ---> image1_000, image2_001,..
'''

if not os.path.exists(pathOut):
    os.makedirs(pathOut)

for i, file in enumerate(glob.glob(pathIn + '/*')):

    fname = name + '_{str_0:0>{str_1}}.jpg'.format(str_0=i+1, str_1=int_desiredLength)
    im = Image.open(file)
    im.thumbnail((newsize), Image.ANTIALIAS)
    apparent_size = im.size
    apparent_h, apparent_w = im.size
    desired_h, desired_w = newsize
    delt_h, delt_w = abs(apparent_h - desired_h), abs(apparent_w - desired_w)

    padding = (delt_h // 2, delt_w // 2, delt_h - (delt_h // 2), delt_w - (delt_w // 2))
    im = ImageOps.expand(im, padding)
    desired_size = im.size
    print('{0}: {1}====>{2}'.format(fname, apparent_size, desired_size))
    im.save(os.path.join(pathOut, fname))
