import cv2 as cv
#img = cv.imread('Photos/peacock.jpg')   #if u have imgs of large size than ur monitor they'll overflow
#cv.imshow('Dog',img)

capture=cv.VideoCapture('videos/dog.gif')
while True:
    isTrue, frame=capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllwindows()

cv.waitKey(0) #u'll see a -215 assertion failed msgcuz cv couldnt find no more frames after the gif has run so it abruptly breaks from the while True loop and gives us that error