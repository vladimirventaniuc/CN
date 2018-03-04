import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import json
from tema_doi.functions import *
# Create your views here.
from tema_trei.functions import *


def index(request):

    context={}
    return render(request,'tema_trei/index.html',context)

@csrf_exempt
def upload(request):
    print("*******************************************")
    response_data={}
    print(request)
    data1 = request.FILES['myFile1'].read().decode("utf-8").replace('\n',"")
    file = open("tema_trei/files/a.txt","w+")
    file.write(data1)
    data2 = request.FILES['myFile2'].read().decode("utf-8").replace('\n', "")
    file = open("tema_trei/files/b.txt", "w+")
    file.write(data2)

    createSumProductFiles("tema_trei/files/a.txt","tema_trei/files/b.txt","tema_trei/files/sum.txt","tema_trei/files/prod.txt")





    print("############################################")
    try:
        response_data['result']="merge"
    except:
        response_data['result']="nup"
    return HttpResponse(json.dumps(response_data),content_type="application/json")

def getSum(request):
    message="Merge sum"
    with open("tema_trei/files/sum.txt", 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/plain")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename("tema_trei/files/sum.txt")
        return response

def getProd(request):
    message="Merge sum"
    with open("tema_trei/files/prod.txt", 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/plain")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename("tema_trei/files/prod.txt")
        return response

@csrf_exempt
def check(request):
    print("*******************************************")
    response_data={}
    print(request)
    data1 = request.FILES['myFile12'].read().decode("utf-8").replace('\n',"")
    file = open("tema_trei/files/check1.txt","w+")
    file.write(data1)
    data2 = request.FILES['myFile22'].read().decode("utf-8").replace('\n', "")
    file = open("tema_trei/files/check2.txt", "w+")
    file.write(data2)


    val1,val2 = verificare("tema_trei/files/check1.txt","tema_trei/files/check2.txt")
    name1=request.FILES['myFile12'].name
    name2=request.FILES['myFile22'].name


    print("############################################")
    try:
        response_data['result1']=val1
        response_data['result2']=val2


    except:
        response_data['result']="nup"
    return HttpResponse(json.dumps(response_data),content_type="application/json")
