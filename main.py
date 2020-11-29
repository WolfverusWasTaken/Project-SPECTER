import numpy as np
import cv2
from tkinter import filedialog

import tkinter as tk
from PIL import ImageTk,Image

image = filedialog.askopenfilename()
image = cv2.imread(image)


# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# image = Image.fromarray(image)
# image = ImageTk.PhotoImage(image)

def nothing(x):
    pass


def creategui():
    # Create a window
    cv2.namedWindow('image')

    # create trackbars for color change
    cv2.createTrackbar('GMin', 'image', 0, 255, nothing)
    cv2.createTrackbar('RMin', 'image', 0, 255, nothing)
    cv2.createTrackbar('BMin', 'image', 0, 255, nothing)
    cv2.createTrackbar('BMax', 'image', 0, 255, nothing)
    cv2.createTrackbar('RMax', 'image', 0, 255, nothing)
    cv2.createTrackbar('GMax', 'image', 0, 255, nothing)


def setdefaultvalues():
    # Set default value for MAX HSV trackbars.
    cv2.setTrackbarPos('BMax', 'image', 255)
    cv2.setTrackbarPos('GMax', 'image', 255)
    cv2.setTrackbarPos('RMax', 'image', 255)

    # Set default value for MIN HSV trackbars.
    cv2.setTrackbarPos('BMin', 'image', 0)
    cv2.setTrackbarPos('GMin', 'image', 0)
    cv2.setTrackbarPos('RMin', 'image', 0)


creategui()

setdefaultvalues()

# Initialize to check if BGR min/max value changes
B_Min = G_Min = R_Min = B_Max = G_Max = R_Max = 0

output = image
wait_time = 33

while True:

    B_Min = cv2.getTrackbarPos('BMin', 'image')
    G_Min = cv2.getTrackbarPos('GMin', 'image')
    R_Min = cv2.getTrackbarPos('RMin', 'image')

    B_Max = cv2.getTrackbarPos('BMax', 'image')
    G_Max = cv2.getTrackbarPos('GMax', 'image')
    R_Max = cv2.getTrackbarPos('RMax', 'image')

    # Set minimum and max BGR values to display
    lower = np.array([B_Min, G_Min, R_Min])
    upper = np.array([B_Max, G_Max, R_Max])

    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    #image = Image.fromarray(image)
    #image = image.convert("RGBA")
    #datas = image.getdata()

    #for item in datas:
        #if item[0] == 255 and item[1] == 255 and item[2] == 255:
            #datas.append((255, 255, 255, 0))

    #image.putdata(datas)



    # Display output image
    cv2.imshow('image', output)



    if cv2.waitKey(wait_time) & 0xFF == ord('q'):

        print("Image Converted to Greyscale")
        break

cv2.destroyAllWindows()


