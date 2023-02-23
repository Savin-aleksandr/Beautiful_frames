
'''This module allows you to create more beautiful frames on the image compared to simple squares.'''


import numpy as np
import cv2
R_basic=0
G_basic=0
B_basic=0
thickness_basic=2

def settings(R, G, B, thickness):
    global R_basic
    global G_basic
    global B_basic
    global thickness_basic
    R_basic=R
    G_basic=G
    B_basic=B
    thickness_basic=thickness


def frame(img, x, y, w, h):
    global R_basic
    global G_basic
    global B_basic
    global thickness_basic
    line_length=int(((x + w)-x)/6)
    cv2.rectangle(img, (x, y), (x + w, y + h), (B_basic/2, G_basic/2, R_basic/2), thickness_basic) #BGR
    #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)  # BGR


    #int(thickness_basic * 4 * (line_length/50))
    cv2.line(img, (x, y), (int(line_length +x), int(y)), (B_basic, G_basic, R_basic), thickness_basic * 3 )
    cv2.line(img, (x, y), (int(x), int(y + line_length)), (B_basic, G_basic, R_basic), thickness_basic * 3)

    cv2.line(img, (x + w, y), (int((x + w)-line_length), int(y)), (B_basic, G_basic, R_basic), thickness_basic * 3)
    cv2.line(img, (x + w, y), (int(x + w), int(line_length+y) ), (B_basic, G_basic, R_basic), thickness_basic * 3)



    cv2.line(img, (x, y+ h), (int(line_length + x), int(y+ h)), (B_basic, G_basic, R_basic), thickness_basic * 3)
    cv2.line(img, (x, y+ h), (int(x), int((y+w)- line_length)), (B_basic, G_basic, R_basic), thickness_basic * 3)

    cv2.line(img, (x + w, y+ h), (int((x + w) - line_length), int(y+ h)), (B_basic, G_basic, R_basic), thickness_basic * 3)
    cv2.line(img, (x + w, y+ h), (int(x + w), int((y+ h)-line_length)), (B_basic, G_basic, R_basic), thickness_basic * 3)

    '''The image itself, on which the line is drawn.
    The coordinate of the first point (x1, y1).
    The coordinate of the second point (x2, y2).
    The color of the line (GBR/RGB depending on the selected color model).
    Line thickness.'''

    return img
