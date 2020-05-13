import cv2
import numpy as np
captura = cv2.VideoCapture(0)
redBajo1 = np.array([0, 100, 20], np.uint8)
redAlto1 = np.array([8, 255, 255], np.uint8)
redBajo2=np.array([175, 100, 20], np.uint8)
redAlto2=np.array([179, 255, 255], np.uint8)
while True:
  (grabbed, imagen) = captura.read()
  cv2.imshow('Video DroidCam', imagen)
  if grabbed==True:
    imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    maskRed1 = cv2.inRange(imagenHSV, redBajo1, redAlto1)
    maskRed2 = cv2.inRange(imagenHSV, redBajo2, redAlto2)
    maskRed = cv2.add(maskRed1, maskRed2)
    maskRedvis = cv2.bitwise_and(imagen, imagen, mask= maskRed)    
    cv2.imshow('imagen', imagen)
    cv2.imshow('maskRed', maskRed)
    cv2.imshow('maskRedvis', maskRedvis)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
cap.release()
cv2.destroyAllWindows()
