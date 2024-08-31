import cv2 as cv

capture = cv.VideoCapture("Videos/Discrete Time Convolution.mp4")

while True:
    isTrue, frame = capture.read()
    
    if not isTrue:
        print("Failed to grab frame or end of video reached")
        break
    
    cv.imshow("Video", frame)

    
    if cv.waitKey(20) & 0xFF == ord("d"):
        break


capture.release()
cv.destroyAllWindows()
