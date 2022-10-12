import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import imutils
import os



#Loads the image at path and returns the cropped version in color and in gray scale
def load_board_image_cropped(path):
    if(not os.path.exists(path)):
        return (None,None)
    cropXBegin = 139
    cropXEnd = 128
    cropYTop = 37
    cropYBottom = 79
    img = cv.imread(path)
    img = imutils.rotate_bound(img, -2)
    img = img[cropYTop:img.shape[0] - cropYBottom, cropXBegin:img.shape[1] - cropXEnd, :]
    img = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return img, img_gray
def load_templates(dir_path):
    r_templates = []
    g_templates = []
    for path in os.scandir(dir_path):
        if path.is_file() and path.name.endswith('.png'):
            if(path.name.startswith("r_template")):
                r_templates.append(cv.imread(dir_path+path.name, cv.IMREAD_GRAYSCALE))
            elif (path.name.startswith("g_template")):
                g_templates.append(cv.imread(dir_path + path.name, cv.IMREAD_GRAYSCALE))   
    return (r_templates,g_templates)
def load_captures(dir_path):
    captures = []
    for path in os.scandir(dir_path):
        if path.is_file() and path.name.endswith('.jpg'):
            captures.append(dir_path+path.name)

    return captures

for img_path in load_captures("./Board Captures/"):
    img_rgb,img_gray = load_board_image_cropped(img_path)
    r_templates, g_templates = load_templates("./CV templates/")
    r_locs = []
    templates = r_templates + g_templates
    threshold = 0.8
    for t in templates:
        w, h = t.shape[::-1]
        res = cv.matchTemplate(img_gray,t,cv.TM_CCOEFF_NORMED)
        """cv.imshow("res",res)
        cv.waitKey(0)
        cv.destroyAllWindows()"""
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv.rectangle(img_rgb, pt, (pt[0] + 16, pt[1] + 16), (0,0,255), 2)
        r_locs.extend(loc)
    """print(r_locs)
    for pt in zip(*r_locs[::-1]):
        print(pt)
        cv.rectangle(img_rgb, pt, (pt[0] + 16, pt[1] + 16), (0,0,255), 2)"""
    cv.imshow("test",img_gray)
    cv.waitKey(0)
    cv.destroyAllWindows()



        