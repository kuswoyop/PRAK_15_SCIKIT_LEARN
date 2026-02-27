import os
from time import sleep
import cv2
DATA_DIR = 'C:\SEMESTER6\prak.kontrol.cerdas\mingguke3\DATA'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
number_of_classess = 2
dataset_size = 100
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera tidak bisa dibuka")
    exit()

for j in range(number_of_classess):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))
    print('Collectingdata for class {}'.format(j))

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Gagal membaca frame")
            break
        cv2.putText(frame, 'Ready? Press "Q" !', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3)
        cv2.imshow('frame',frame)
        if cv2.waitKey(15) == ord('q'):
            break

        counter = 0
        while counter < dataset_size:
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            cv2.waitKey(10)
            cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)
            counter += 1

cap.release()
cv2.destroyAllWindows()