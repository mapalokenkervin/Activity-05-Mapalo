import cv2 as cv
import numpy as np


def start():
    readImage()


def readImage():

    img = cv.imread('gustavo.jpg')

    status = img.shape

    if len(status) == 3:
        modifyPx(img)

    else:
        print("Invalid...")


def modifyPx(img):
    x = int(input("X Value: "))
    y = int(input("Y Value: "))
    z = int(input("Color Attributes: "))

    cv.imshow("Before", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    px = img.item(x, y, z)
    print("Image Value", x, y, z)
    print("Pixel Value:", px)

    img.itemset((x, y, z), 120)
    px = img.item(x, y, z)
    print("Modified Pixel Value:", px)

    dimention(img)


def dimention(img):

    size = img.shape

    x = 600
    y = 600

    if size[0] > x and size[1] > y:
        print("Invalid image dimention...")

    else:
        imageType(img)


def imageType(img):
    dtype = img.dtype
    print("The Image data type is", dtype)

    imageSize(img)


def imageSize(img):

    requiredSize = 1080000
    size = img.size

    if size <= requiredSize:
        print("The Image size is Validated...")
        cv.imshow("After", img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    else:
        print("The Image size is Invalid...")


start()