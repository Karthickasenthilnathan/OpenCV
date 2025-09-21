import numpy as np
import cv2 as cv


img = np.array([[10, 10, 10, 10, 10],
                [10, 50, 50, 50, 10],
                [10, 50,100, 50,10],
                [10, 50, 50, 50, 10],
                [10, 10, 10, 10, 10]], 
                dtype=np.float32)

height, width = img.shape
gx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3) 
gy = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)  

mag, ang = cv.cartToPolar(gx, gy, angleInDegrees=True)

print("gx:\n", gx)
print("gy:\n", gy)
print("Gradient Magnitude:\n", mag)
print("Gradient Angle:\n", ang)


nms = np.zeros_like(mag)

for i in range(1, width-1):
    for j in range(1, height-1):
        angle = ang[j,i]

       
        angle = angle % 180

        
        if (0 <= angle < 22.5) or (157.5 <= angle <= 180):
            before = mag[j, i-1]
            after  = mag[j, i+1]
        elif 22.5 <= angle < 67.5:
            before = mag[j-1, i-1]
            after  = mag[j+1, i+1]
        elif 67.5 <= angle < 112.5:
            before = mag[j-1, i]
            after  = mag[j+1, i]
        else:
            before = mag[j-1, i+1]
            after  = mag[j+1, i-1]

        if mag[j,i] >= before and mag[j,i] >= after:
            nms[j,i] = mag[j,i]
        else:
            nms[j,i] = 0

print("After Non-Maximum Suppression:\n", nms)

weak_th = 20
strong_th = 50
edges = np.zeros_like(nms)

for i in range(height):
    for j in range(width):
        if nms[i,j] >= strong_th:
            edges[i,j] = 255 
        elif nms[i,j] >= weak_th:
            edges[i,j] = 100
        else:
            edges[i,j] = 0    

print("Edges after Thresholding:\n", edges)
