import cv2
import numpy as np
import glob
import re
import os
from natsort import natsorted,ns
import json

numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

mylistcrop = os.listdir("Cropped Images")
mylistcrop = natsorted(mylistcrop, alg=ns.IGNORECASE)
mylistimage = os.listdir("Real Images")
mylistimage = natsorted(mylistimage, alg=ns.IGNORECASE)

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)


count = 0
imagedict = {}
list2 = []
list3 = []
list4 = []
for j in sorted(glob.iglob("Real Images\*"), key= numericalSort):
    value = -1
    print(mylistimage[count])
    imagedict[mylistimage[count]] = []
    list3.clear()
    list4.clear()
    for f in sorted(glob.iglob("Cropped Images\*"), key= numericalSort):
        img = cv2.imread(j)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        
        template = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
        w, h = 0, 0
        w, h = template.shape[::-1]
        img_shape = list(gray_img.shape)
        crop_shape = list(template.shape)
        value = value+1
        list2.clear()
        list1 = [item1 for item1, item2 in zip(img_shape, crop_shape) if item1 > item2]
        if ((len(list1))==2):
            pass
        else:
            continue
        result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= 0.9)
        pt = 0
        for pt in zip(*loc[::-1]):
            list2 = [pt[0], pt[1], (pt[0] + w), (pt[1] + h)]
        if not list2:
            continue
        tup1 = (mylistcrop[value], [pt[0], pt[1], (pt[0] + w), (pt[1] + h)])
        imagedict[mylistimage[count]].append(tup1)
    print(imagedict[mylistimage[count]])
    count = count +1


with open('jsondocument.json', 'w') as outfile:
    json.dump(imagedict, outfile, indent=2, cls=MyEncoder)  
