import cv2 as cv
initial_img=cv.imread('Photos/mirinda.jpg')
'''result=cv.rotate(initial_img,cv.ROTATE_90_CLOCKWISE)
cv.imshow("OUTPUT",result)'''
result2=cv.rotate(initial_img,cv.ROTATE_90_COUNTERCLOCKWISE)
cv.imshow("OUTPUT",result2)
cv.waitKey(0)
cv.destroyAllWindows()