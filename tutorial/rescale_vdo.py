import cv2 as cv
capture=cv.VideoCapture('videos/peacock.gif')

def rescaleFrame(frame,scale=0.5):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
while True:
    
    isTrue,frame=capture.read()
    resized=rescaleFrame(frame)
    cv.imshow('Original',frame)
    cv.imshow('Rescaled',resized)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break
capture.release()
cv.destroyAllWindows()
