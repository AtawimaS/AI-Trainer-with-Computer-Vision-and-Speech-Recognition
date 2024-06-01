import cv2
import time
import numpy as np
import PoseModule as pm

class Training:
    def __init__(self):
        # self.cap = cv2.VideoCapture("AITRAINER/The Perfect Push Up _ Do it right!.mp4")
        # self.cap = cv2.VideoCapture("http://192.168.226.41:4747/video") #kamera hp dengn droid cam
        self.cap = cv2.VideoCapture(0) #kamera laptop bawaan
        self.detector = pm.poseDetector()
        self.count = 0
        self.dir = 0
        self.pTime = 0

    def start_training(self):
        while True:
            success, img = self.cap.read()
            if not success:
                print("Gagal membaca frame dari kamera.")
                break
            img = cv2.resize(img, (1280, 720))
            img = self.detector.findPose(img, False)
            lmlist = self.detector.findPosition(img, False)

            if len(lmlist) != 0:
                # Tangan kanan
                #angle = detector.findAngle(img, 12,14,16)
                # Tangan Kiri
                angle = self.detector.findAngle(img, 11, 13, 15)
                per = np.interp(angle, (190, 250), (0, 100))

                if per == 100:
                    if self.dir == 0:
                        self.count += 0.5
                        self.dir = 1
                if per == 0:
                    if self.dir == 1:
                        self.count += 0.5
                        self.dir = 0

                cv2.putText(img, str(int(self.count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 7, (255, 0, 0), 5)

            cv2.imshow("image", img)
            cv2.waitKey(1)



# cap = cv2.VideoCapture("AITRAINER/PushUpShort.mp4")
# # cap = cv2.VideoCapture(0) #kamera laptop bawaan
# # cap = cv2.VideoCapture("http://192.168.226.41:4747/video") #kamera hp dengn droid cam
# detector = pm.poseDetector()
# count = 0
# dir = 0
# pTime = 0
#
# while True:
#     success, img = cap.read()
#     if not success:
#         print("Can't read a frame from camera.")
#         break
#     img = cv2.resize(img, (307,560))
#     # img = cv2.imread("AITRAINER/pushup.jpg")
#     img = detector.findPose(img, False)
#     lmlist = detector.findPosition(img, False)
#     print("lmlist = ", lmlist)
#     # print(lmlist)
#     if len(lmlist) !=0:
#         #tangan kanan
#         angle1 = detector.findAngle(img, 12,14,16)
#         #tangan kiri
#         angle2 = detector.findAngle(img, 11, 13, 15)
#         per = np.interp(angle1,(190,250),(0,100))
#         # max2=angle2
#         # print(max2)
#         time.sleep(0.5)
#         # min2= angle2
#         # print("ceok",min2)
#         # per = np.interp(angle2, (min2, max2), (0,100))
#         # print(angle, per)
#
#         if per ==100:
#             if dir ==0:
#                 count +=0.5
#                 dir = 1
#         if per ==0:
#             if dir == 1:
#                 count +=0.5
#                 dir = 0
#
#         cv2. putText(img, str(int(count)), (50,100), cv2.FONT_HERSHEY_PLAIN, 7, (255,0,0),5)
#         # cv2.putText()
#
#     cv2.imshow("image", img)
#     cv2.waitKey(1)
