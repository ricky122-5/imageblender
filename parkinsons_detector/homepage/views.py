from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from homepage.create_image import merge
from django.urls import reverse

global theFile
import pickle
import os
import matplotlib.pyplot as plt
import matplotlib as mpl


# Create your views here.l
def homepage(request):
    cond1 = False
    cond2 = False
    if (request.method == "POST" and request.FILES['file1']):
        global fileString1
        theFile = request.FILES["file1"]
        fs = FileSystemStorage()
        filename = fs.save(theFile.name, theFile)
        uploaded_file_url = fs.url(filename)
        fileString1 = str(uploaded_file_url)
        print(fileString1)
        cond1 = True
    if (request.method == "POST" and request.FILES['file2']):
        global fileString2
        theFile = request.FILES["file2"]
        fs = FileSystemStorage()
        filename = fs.save(theFile.name, theFile)
        uploaded_file_url = fs.url(filename)
        fileString2 = str(uploaded_file_url)
        print(fileString2)
        cond2 = True
    if cond1 and cond2:
        return HttpResponseRedirect('upload')
    return render(request, 'base.html', {})


def upload(request):
    merge('C:\\Users\\Rikki\\parkinsondetector-dir\\parkinsons_detector\\' + fileString1,
          'C:\\Users\\Rikki\\parkinsondetector-dir\\parkinsons_detector\\' + fileString2)
    path = settings.MEDIA_ROOT
    img = path+'\mergedimg.jpg'
    context = {'image':img}
    return render(request, 'results.html', context)
def redirect(request):
    print('hello')
    return HttpResponseRedirect(reverse('upload'))

# WORK IN THE create_image FILE
