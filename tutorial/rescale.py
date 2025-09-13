import cv2 as cv

#method 1
img=cv.imread('Photos/dog.jpg')
resized=cv.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv.INTER_AREA)
cv.imshow('original',img)
cv.imshow('resized',resized)
cv.waitKey(0)
cv.destroyAllWindows()

#method 2 giving the exact dimension in which the resized image has to be
#resized=cv.resize(img,(300,500),interpolation=cv.INTER_AREA)