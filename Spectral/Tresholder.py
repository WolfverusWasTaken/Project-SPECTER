# ==========================================================================================================
#                                            IMPORTED LIBRARIES                                            
# ==========================================================================================================
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageTk


def CV2TkConvert(master, cvimage):
    cvimage = cv2.cvtColor(cvimage, cv2.COLOR_BGR2RGB)
    tkimage = ImageTk.PhotoImage(master=master, image=Image.fromarray(cvimage))
    return tkimage

def RGBTreshold(image, R_Min, R_Max, G_Min, G_Max, B_Min, B_Max):
    lower_range = np.array([R_Min, G_Min, B_Min])#Need to edit
    upper_range = np.array([B_Max, G_Max, R_Max])#Need to edit

    color_mask = cv2.inRange(image, lower_range, upper_range)
    edited_image = cv2.bitwise_and(image, image, mask=color_mask)

    return edited_image

def invertbgimg(cvimage, opt):
    height, width, _ = cvimage.shape

    for i in range(height):
        for j in range(width):
            # img[i,j] is the RGB pixel at position (i, j)
            # check if it's [0, 0, 0] and replace with [255, 255, 255] if so
            if cvimage[i, j].sum() == 0:
                if opt:
                    cvimage[i, j] = [0, 0, 0]
                else:
                    cvimage[i, j] = [255, 255, 255]
            else:
                if opt:
                    cvimage[i, j] = [255, 255, 255]
                else:
                    cvimage[i, j] = [0, 0, 0]

    return cvimage

def removebinoise(cvimage, iter):
    for i in range(0, iter):
        cvimage = cv2.fastNlMeansDenoising(cvimage, h = 20,templateWindowSize = 7 ,searchWindowSize = 21)
    return cvimage

def removecolnoise(cvimage):
    cvimage = cv2.fastNlMeansDenoisingColored(cvimage, h = 20,templateWindowSize = 7 ,searchWindowSize = 21)
    return cvimage

def removespecks(cvimage):
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    cvimage = cv2.erode(cvimage, element, iterations=1)
    cvimage = cv2.dilate(cvimage, element, iterations=1)
    cvimage = cv2.erode(cvimage, element)

    return cvimage

'''def AlphaMasking(cvimage):
    # Coinvert from BGR to BGRA
    bch,gch,rch = cv2.split(cvimage)

    cvimage = cv2.cvtColor(cvimage, cv2.COLOR_BGR2BGRA)

    # Slice of alpha channel
    alpha = cvimage[:, :, 3]

    # Use logical indexing to set alpha channel to 0 where BGR=0
    alpha[np.all(cvimage[:, :, 0:3] == (0, 0, 0), 2)] = 1

    cvimage = cv2.merge((bch , gch, rch, alpha))
    cvimage = cv2.cvtColor(cvimage, cv2.COLOR_BGR2BGRA)

    return cvimage'''