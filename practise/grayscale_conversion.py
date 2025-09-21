import cv2 as cv
#img=cv.imread('Photos/mirinda.jpg')
'''cv.imshow('Original',img)
cv.waitKey(0)'''

#using cv.COLOR_RGB2GRAY
'''grayScale=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('Greyscale',grayScale)
cv.waitKey(0)
cv.destroyAllWindows()'''

#using flag=0 in imread()
'''img=cv.imread('Photos/mirinda.jpg',0)
cv.imshow('Grayscale',img)
cv.waitKey(0)'''


#using pixel manipulation
img=cv.imread('Photos/mirinda.jpg')
(rows,cols)=img.shape[0:2]
for i in range(rows):
    for j in range (cols):
        img[i,j]=sum(img[i,j])*0.33
cv.imshow('Grayscale',img)
cv.waitKey(0)
cv.destroyAllWindows()

