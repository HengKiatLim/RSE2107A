#!/usr/bin/env python

import matplotlib.pylab as plt
import cv2
import numpy as np


image = cv2.imread('road_lane.jpg')
#converter
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#terminal show height, width
print(image.shape)
height = image.shape[0]
width = image.shape[1]
#region of interest location
region_of_interest_vertices = [
    (0, 885),
    (790, height/2),
    (1095, height/2),
    (1790, 900)
]

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    #match_mask_color = (255,) * channel_count
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image
#draw line
def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), 
                            dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:                 #color R G B
            cv2.line(blank_image, (x1,y1), (x2,y2), (0,0,255), 
            thickness=30)
    #merge image with weight(src1,alpha,src2,beta,gamma)
    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img
#convert image to gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#Canny Edge Detector(image,1 threshold,2 threshold)
canny_image = cv2.Canny(gray_image, 120, 300)

cropped_image = region_of_interest(canny_image, 
                np.array([region_of_interest_vertices], 
                np.int32))
#detect straight lines
lines = cv2.HoughLinesP(cropped_image,
                        rho=6,
                        theta=np.pi/60,
                        threshold=160,
                        lines=np.array([]),
                        minLineLength=40,
                        maxLineGap=25)

image_with_lines = draw_the_lines(image, lines)
#load image
plt.imshow(image_with_lines)
plt.show()

"""
image = cv2.imread('road_lane.jpg')
#converter
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#terminal show height, width
print(image.shape)
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (0, 885),
    (790, height/2),
    (1095, height/2),
    (1790, 900)
]

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    channel_count = img.shape[2]
    match_mask_color = (255,) * channel_count
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

cropped_image = region_of_interest(image, 
                np.array([region_of_interest_vertices], 
                np.int32))

plt.imshow(cropped_image)
plt.show()
"""