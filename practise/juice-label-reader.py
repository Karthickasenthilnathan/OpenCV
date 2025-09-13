import cv2 as cv
img=cv.imread('Photos/dog.jpg')
cv.imshow('Juice label',img)
cv.waitKey(0)
cv.destroyAllWindows()