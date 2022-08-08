#!/usr/bin/env python

import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)

cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    frame = cv2.imread('colour_venn_diagram.jpg')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([110, 100, 100])
    u_b = np.array([130, 255, 255])
    
    l_r = np.array([000, 100, 100])
    u_r = np.array([20, 255, 255])
    
    l_g = np.array([40, 100, 100])
    u_g = np.array([80, 255, 255])

    l_y = np.array([10, 100, 100])
    u_y = np.array([50, 255, 255])
    
    l_c = np.array([80, 100, 100])
    u_c = np.array([100, 255, 255])
    
    l_m = np.array([140, 100, 100])
    u_m = np.array([170, 255, 255])
    
    l = np.array([l_h, l_s, l_v])
    u = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l, u)
    mask2 = cv2.inRange(hsv, l_b, u_b)
    mask3 = cv2.inRange(hsv, l_r, u_r)
    mask4 = cv2.inRange(hsv, l_g, u_g)
    mask5 = cv2.inRange(hsv, l_y, u_y)
    mask6 = cv2.inRange(hsv, l_c, u_c)
    mask7 = cv2.inRange(hsv, l_m, u_m)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    res2 = cv2.bitwise_and(frame, frame, mask=mask2)
    res3 = cv2.bitwise_and(frame, frame, mask=mask3)
    res4 = cv2.bitwise_and(frame, frame, mask=mask4)
    res5 = cv2.bitwise_and(frame, frame, mask=mask5)
    res6 = cv2.bitwise_and(frame, frame, mask=mask6)
    res7 = cv2.bitwise_and(frame, frame, mask=mask7)

    cv2.imshow("frame",frame)
    #cv2.imshow("mask",mask)
    #cv2.imshow("res",res)
    cv2.imshow("blue",res2)
    cv2.imshow("red",res3)
    cv2.imshow("green",res4)
    cv2.imshow("yellow",res5)
    cv2.imshow("cyan",res6)
    cv2.imshow("mag",res7)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()    