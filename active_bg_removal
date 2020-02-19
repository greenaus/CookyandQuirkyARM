from imutils import face_utils
import dlib
import cv2
import numpy as np
from numpy import newaxis


video = cv2.VideoCapture(0)

def find_rect(rect):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    return(x,y,w,h)

def shape_to_np_jaw(shape,x1,y1,w,h,dtype = np.int32):
    coords = np.zeros((18,2), dtype = dtype)
    for i in range(0,18):
        if i == 0:
            coords[i][0] = x1
            coords[i][1] = y1
        elif i == 17:
            coords[i][0] = x1+w
            coords[i][1] = y1
        else:
            coords[i][0] = shape.part(i).x
            coords[i][1] = shape.part(i).y
    new_coords = coords.reshape(1,18,2)

    return new_coords

landmark_model = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(landmark_model)

while True:
    check, frame = video.read()
    check2, frame2 = video.read()
    rects = detector(frame, 0)
    for (i,rect) in enumerate(rects):
        (x1,y1,w,h) = find_rect(rect)
        shape = predictor(frame,rect)
        shape2 = shape_to_np_jaw(shape,x1,y1,w,h)
        shape = face_utils.shape_to_np(shape)

        cv2.fillPoly(frame, shape2, (255,255,255))
        ret,thresh = cv2.threshold(frame,254,255,cv2.THRESH_TOZERO)

        masked_img = cv2.bitwise_and(thresh,frame2)

    cv2.imshow("out",masked_img)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
video.release()
