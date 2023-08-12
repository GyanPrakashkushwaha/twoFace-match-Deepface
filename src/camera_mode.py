
# import cv2

# def access_camera():
#     cap = cv2.VideoCapture(0)
#     while cap.isOpened(): # this is infinite loop
#         ret , frame = cap.read()
#         # frame = cv2.resize(src=frame,dsize=(700,400))
#         frame = cv2.flip(src=frame,flipCode=1)
#         cv2.imshow('Video',frame)
#         k = cv2.waitKey(25)
        
#         if k == ord('x'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()


