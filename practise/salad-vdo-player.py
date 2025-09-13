import cv2 as cv
capture=cv.VideoCapture('videos/pizza.mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow('Pizza maker',frame)
    if cv.waitKey(20) & 0xFF==('s'):
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(20)

