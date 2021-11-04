from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pytesseract
from PIL import Image
from rest_framework import generics

from . import models
from .models import insertbutton, buttoninfo
from .imageana import buttonletter,buttonpixel,precise, maincalculation
from .serializers import ButtonSerializers


def button(request):
    return render(request,'home.html')


def external(request):
    imagetry=request.FILES['image']
    fs=FileSystemStorage()
    filename=fs.save(imagetry.name,imagetry)
    im = Image.open(imagetry)
    button_height, buttonwidths = maincalculation(im)
    bletter = buttonletter(im)
    letterpixelx, letterpixely = buttonpixel(im)
    print("letterpixelx", letterpixelx)
    print("letterpixely", letterpixely)
    buttonx, buttony = precise(im)
    print("ButtonLetter", bletter)
    print("button height width", button_height, buttonwidths)
    print(buttonx, buttony)
    for i in range(len(buttonx)):
        buttondescription = buttoninfo()
        buttondescription.Button_letter = bletter[i]
        buttondescription.Button_height = button_height[i]
        buttondescription.Button_width = buttonwidths[i]
        buttondescription.Button_Starting_xpoint = buttonx[i]
        buttondescription.Button_Starting_ypoint = buttony[i]
        buttondescription.save()
    return render(request, 'details.html')


def another(request):
    if request.method == "POST":
        if request.POST.get('buttonColor'):
            saveValue = insertbutton()
            saveValue.buttonColor = request.POST.get('buttonColor')
            saveValue.save()
            return render(request, 'another.html')
    else:
            return render(request, 'another.html')

class ListButton(generics.ListCreateAPIView):
    queryset = models.buttoninfo.objects.all()
    serializer_class = ButtonSerializers

class DetailsButton(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.buttoninfo.objects.all()
    serializer_class = ButtonSerializers