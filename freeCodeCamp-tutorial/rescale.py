import cv2 as cv

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height): # works only for live video
    capture.set(3,width)
    capture.set(4,width)



img  = cv.imread("Photos/ep1.png")
resized_image = rescaleFrame(img)
cv.imshow("Episode 1", resized_image)

cv.waitKey(0)



capture = cv.VideoCapture("Videos/Discrete Time Convolution.mp4")

# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame)
#     if not isTrue:
#         print("Failed to grab frame or end of video reached")
#         break
    
#     #cv.imshow("Video", frame)
#     cv.imshow("Video resized", frame_resized)

    
#     if cv.waitKey(20) & 0xFF == ord("d"):
#         break


# capture.release()
# cv.destroyAllWindows()