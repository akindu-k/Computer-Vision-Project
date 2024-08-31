import cv2 as cv

#img = cv.imread("Photos/ep1.png")

#cv.imshow("Episode 1", img)


capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if (cv.waitKey(20) & oxFF==ord("d")):
        break

capture.release()
cv.destroyAllWindows()