'''import cv2 as cv
img=cv.imread('Photos/tannies.jpg')
file_saved=cv.imwrite('savedImage.jpg',img)
result=cv.imread('savedImage.jpg')
cv.imshow('output',result)
cv.waitKey(0)
cv.destroyAllWindows()'''


import cv2 as cv
img=cv.imread('Photos/mirinda.jpg')
file_saved=cv.imwrite('savedImage2.jpg',img)
result=cv.imread('savedImage2.jpg')
output=cv.imshow('Result',result)
cv.waitKey(0)
cv.destroyAllWindows()