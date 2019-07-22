import io
import pyqrcode
from base64 import b64encode
import eel
import cv2
import os
from PIL import Image
import os, sys

eel.init('web')


@eel.expose
def dummy(dummy_param):
    print("I got a parameter: ", dummy_param)
    #print("Ajinkya", os.getcwd())
    path0=os.getcwd()
    path = path0+'/images/'
    print('path0',path0)
    print('path', path)
    dirs = os.listdir(path)
    print(path)
    print(dirs)


    for item in dirs:
    	if os.path.isfile(path+item):
    		im = Image.open(path+item)
    		f, e = os.path.splitext(path+item)
    		imResize = im.resize((129,129), Image.ANTIALIAS)
    		imResize.save(f + ' resized.jpg', 'JPEG', quality=90)


    #image = cv2.imread(current+'/pan.png')
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #print(current)
    #print(dirs)
    #cv2.imwrite('image.jpg', gray)
    #return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}
    

"""
@eel.expose
def generate_qr(data):
    img = pyqrcode.create(data)
    buffers = io.BytesIO()
    img.png(buffers, scale=8)
    encoded = b64encode(buffers.getvalue()).decode("ascii")
    print("QR code generation successful.")

    return "data:image/png;base64, " + encoded

"""
eel.start('index.html', size=(1000, 600))
