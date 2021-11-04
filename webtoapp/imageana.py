import sys
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image
import re


def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z.]')
    string = charRe.search(string)
    return not bool(string)

def maincalculation(im):
    text = pytesseract.image_to_string(im)
    arraystring = text.split()
    Button_number = 0
    Cardview_number = 0
    button_heights = []
    button_widths = []
    for x in range(len(arraystring)):
        if arraystring[x] == 'Button':
            Button_number= Button_number+1
            buttonstr = arraystring[x + 1]
            button = list(buttonstr)
            print(button)
            for a in range(len(button)):
                if button[a] == '/':
                    button_height = button[:a]
                    button_width = button[a:]
            button_width.remove('/')
            button_height_int = 0
            for a in range(len(button_height)):
                button_height_int = 10 * button_height_int + int(button_height[a])
            print(button_height_int)
            button_width_int = 0
            for a in range(len(button_width)):
                button_width_int = 10 * button_width_int + int(button_width[a])
            print(button_width_int)
            button_heights.append(button_height_int)
            button_widths.append(button_width_int)
        if arraystring[x] == 'CardView':
            Cardview_number = Cardview_number + 1
            cardviewstr = arraystring[x + 1]
            cardview = list(cardviewstr)
            print(cardview)
            for a in range(len(cardview)):
                if cardview[a] == '/':
                    cardview_height = cardview[:a]
                    cardview_width = cardview[a:]
            cardview_width.remove('/')
    return button_heights, button_widths

def imagedata(image):
    axisdata = []
    axis = pytesseract.image_to_boxes(image)
    for x in range(len(axis)):
        if is_allowed_specific_char(axis[x]):
             axisdata.append(axis[x])
             while axis[x+2] != ' ':
                 axisdata.append(axis[x+2])
                 x = x+1
    return axisdata


def imagedata2(image):
     axisdatay = []
     axis = pytesseract.image_to_boxes(image)
     for x in range(len(axis)):
         if is_allowed_specific_char(axis[x]):
             axisdatay.append(axis[x])
             count = 0
             for a in range(x, len(axis)):
                 if axis[a] == ' ':
                     count  = count + 1
                 if count == 2:
                     a = a+1
                     axisdatay.append(axis[a])
                     a = a + 1
                     x = x+1
     for x in axisdatay:
         if x == ' ':
             axisdatay.remove(x)
     return axisdatay


def buttonletter(image):
    text = pytesseract.image_to_string(image)
    arraystring = text.split()
    buttonstring = []
    print(arraystring)
    for x in range(len(arraystring)):
        if arraystring[x] == 'Button':
            buttonstring.append( arraystring[x+3])
    return buttonstring


def buttonpixel(image):
    x = imagedata(image)
    y = imagedata2(image)
    buttonx = []
    buttony = []
    for i in range(len(x)):
        if is_allowed_specific_char(x[i]):
            buttonx.append(x[i])
            arrayvalue = 0
            array = []
            i = i+1
            for a in range(i, len(x)):
                if not is_allowed_specific_char(x[a]):
                    array.append(x[i])
                    i = i+1
                else:
                    break
            for a in range(len(array)):
                arrayvalue = 10 * arrayvalue + int(array[a])
            buttonx.append(arrayvalue)
    for i in range(len(y)):
        if is_allowed_specific_char(y[i]):
            buttony.append(y[i])
            arrayvalue = 0
            array = []
            i = i+1
            for a in range(i, len(y)):
                if not is_allowed_specific_char(y[a]):
                    array.append(y[i])
                    i = i+1
                else:
                    break
            for a in range(len(array)):
                arrayvalue = 10 * arrayvalue + int(array[a])
            buttony.append(arrayvalue)
    return buttonx, buttony


def precise(image):
    x, y = buttonpixel(image)
    buttoninx = []
    buttoniny = []
    for i in range(len(x)):
       if x[i] == "B" and x[i+2] == "u" and x[i+4] == "t" and x[i+6] == "t" and x[i+8] == "o" and x[i+10] == "n":
             buttoninx.append(x[i+1])
    for i in range(len(y)):
        if y[i] == "B" and y[i+2] == "u" and y[i+4] == "t" and y[i+6] == "t" and y[i+8] == "o" and y[i+10] == "n":
            buttoniny.append(y[i+1])
    return buttoninx, buttoniny

