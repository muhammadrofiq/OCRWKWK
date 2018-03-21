import numpy as np
import cv2
import main
from datetime import datetime
import os
cap = cv2.VideoCapture(0)

detector = cv2.CascadeClassifier('cscd/plat-80-25stage.xml')


################## plate region detection using harr ################
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = frame
    imagecopy = gray.copy()
    rects = detector.detectMultiScale(frame, scaleFactor=1.01,minNeighbors=1, minSize=(75, 75))
    for (i, (x, y, w, h)) in enumerate(rects):
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Our operations on the frame come here


    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
time=str(datetime.now())
first=time[:10]
end=time[11:-7]
print time

if not os.path.exists("input"):
    os.makedirs("input")

path='input/'+first+"-"+end+".jpg"
cv2.imwrite(path,imagecopy)
cv2.imshow('capture'+first+"-"+end,gray)
main.main(path)
cv2.waitKey(0)
