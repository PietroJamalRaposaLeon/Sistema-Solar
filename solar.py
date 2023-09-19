import cv2 

jpg=cv2.imread("solar-system.jpg")

cv2.imshow("Sistema solar", jpg)

print(jpg)

cv2.waitKey(0)