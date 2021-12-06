'''
A program showing a front camera window picture
Could be used as a simple mirror when no real one is available
'''
import cv2

name = "My Mirror (C) 2020 ELS"
cv2.namedWindow(name, cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow(name, frame)
    cv2.resizeWindow(name, 1024, 768)
    if cv2.waitKey(25) in [27, 1048603]:
        cv2.destroyAllWindows()
        break

print("Done")
