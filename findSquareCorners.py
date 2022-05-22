import numpy as np
import cv2

img = cv2.imread('IMG_1062.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)

corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

centroids = np.int0(centroids)
corners = np.int0(corners)
img[corners[:,1], corners[:,0]] = [0,255,0]
cv2.imwrite('subpixel5.png',img)

