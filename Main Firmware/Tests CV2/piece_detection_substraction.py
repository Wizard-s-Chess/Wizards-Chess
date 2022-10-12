from chess import Board
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import imutils
import os
import math
from sklearn.cluster import KMeans

def centroid_histogram(clt):
	# grab the number of different clusters and create a histogram
	# based on the number of pixels assigned to each cluster
	numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
	(hist, _) = np.histogram(clt.labels_, bins = numLabels)
	# normalize the histogram, such that it sums to one
	hist = hist.astype("float")
	hist /= hist.sum()
	# return the histogram
	return hist
	# initialize the bar chart representing the relative frequency
	# of each of the colors
	bar = np.zeros((50, 300, 3), dtype = "uint8")
	startX = 0
	# loop over the percentage of each cluster and the color of
	# each cluster
	for (percent, color) in zip(hist, centroids):
		# plot the relative percentage of each cluster
		endX = startX + (percent * 300)
		cv.rectangle(bar, (int(startX), 0), (int(endX), 50),
			color.astype("uint8").tolist(), -1)
		startX = endX
	
	# return the bar chart
	return bar
def load_images(dir_path):
    captures = []
    for path in os.scandir(dir_path):
        if path.is_file() and path.name.endswith('.jpg'):
            captures.append(dir_path+path.name)
    return captures
def crop_img(img):
    cropXBegin = 125
    cropXEnd = 110
    cropYTop = 25
    cropYBottom = 50
    img_cropped = imutils.rotate_bound(img, -1.5)
    img_cropped = img_cropped[cropYTop:img.shape[0] - cropYBottom, cropXBegin:img.shape[1] - cropXEnd, :]
    img_cropped = cv.rotate(img_cropped, cv.ROTATE_90_COUNTERCLOCKWISE)
    return img_cropped
    r_templates = []
    g_templates = []
    for path in os.scandir(dir_path):
        if path.is_file() and path.name.endswith('.png'):
            if(path.name.startswith("r_template")):
                r_templates.append(cv.imread(dir_path+path.name, cv.IMREAD_GRAYSCALE))
            elif (path.name.startswith("g_template")):
                g_templates.append(cv.imread(dir_path + path.name, cv.IMREAD_GRAYSCALE))   
    return (r_templates,g_templates)
def classify_square(square):
    flat_square = square.reshape((square.shape[0] * square.shape[1], 3))
    clt = KMeans(n_clusters = 2)
    clt.fit(flat_square)
    hist = centroid_histogram(clt)
    (min_value,min_color) = min(zip(hist,clt.cluster_centers_), key=lambda x:x[0])
    return ("x",min_value,min_color.astype("uint8").tolist()) if min(hist) >=0.08 and len(hist)>1 and (color_distance(clt.cluster_centers_[0].astype("uint8").tolist(),clt.cluster_centers_[1].astype("uint8").tolist())>40) else (".",1,[0,0,0])
def classify_color(color):
    #BGR
    distance_red = color_distance(color, [0,0,255])
    distance_green = color_distance(color, [0,255,0])
    distance_black = color_distance(color, [0,0,0])

    return "R" if (distance_red < distance_green and distance_red<distance_black) else "G" if(distance_green<distance_black) else "."
def color_distance(color1,color2):
    #color is array of int in format BGR
    return math.sqrt((color1[0]-color2[0])**2+(color1[1]-color2[1])**2+(color1[2]-color2[2])**2)
def get_uci_from_coordinates(coordinates):
    y = 7-coordinates[0]
    x = coordinates[1]
    uci = chr(x+ord('a'))+str(y+1)
    return uci



img_paths = load_images("./test/")
img_paths.sort()
last_path = "empty.jpg"

for img_path in img_paths:
    print(img_path)
    current_path = img_path
    board = crop_img(cv.imread(current_path))
    background = crop_img(cv.imread(last_path))
    subtracted = cv.absdiff(board, background)
    square_shape = (subtracted.shape[0]//8,subtracted.shape[1]//8)
    blank = np.zeros(subtracted.shape,dtype=np.uint8)
    blank.fill(255)
    res = []
    for x in range(8):
        for y in range(8):
            square = subtracted[x*square_shape[0]:square_shape[0]*(x+1),y*square_shape[1]:(y+1)*square_shape[1],:]
            resp,value,color = classify_square(square)
            if resp != "." :
                #cv.circle(blank,(int(y*square_shape[1]+square_shape[1]*0.5),int(x*square_shape[0]+square_shape[0]*0.5)), 8, color, -1)
                cv.putText(img=blank, text=str(value), org=(int(y*square_shape[1]+square_shape[1]*0.5),int(x*square_shape[0]+square_shape[0]*0.5)), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=0.25, color=color,thickness=1)

                res.append(get_uci_from_coordinates((x,y)))    
    left_display = blank
    right_display = subtracted
    merged = np.hstack((left_display, right_display))
    if len(res) == 2:
        print(res)
    #cv.imshow('sub', merged)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    last_path = current_path