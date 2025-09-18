import cv2 as cv

img = cv.imread("C:/Users/admin/Documents/Python/opencv/Photos/transparent_butterfly.png", cv.IMREAD_UNCHANGED)
print("Shape:", img.shape)

if img.shape[2] == 4:
    print("This image has an alpha channel ✅")
else:
    print("No alpha channel ❌")

