import cv2 as cv
#using scale factor method
img=cv.imread('Photos/dog.jpg')
'''
resized_img=cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_AREA)
cv.imshow("resized",resized_img)
cv.waitKey(0)
cv.destroyAllWindows() '''

# when exact pixel size is known
resized_img=cv.resize(img,(500 , 500), interpolation=cv.INTER_AREA)
cv.imshow('Result',resized_img)
cv.waitKey(0)
cv.destroyAllWindows()
