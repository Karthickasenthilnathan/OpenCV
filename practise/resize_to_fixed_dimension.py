import cv2 as cv
img=cv.imread('Photos/peacock.jpg')
resized=cv.resize(img,(300,300),interpolation=cv.INTER_AREA)
cv.imshow('original',img)
cv.imshow('300 x 300',resized)
cv.waitKey(0)
cv.destroyAllWindows()