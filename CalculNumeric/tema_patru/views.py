import os
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from tema_patru.functions import *
def index(request):

    context={}
    return render(request,'tema_patru/index.html',context)

@csrf_exempt
def upload(request):
    print("*******************************************")
    response_data={}

    data1 = request.FILES['myFile3'].read().decode("utf-8").replace('\n', "")
    file = open("tema_patru/files/file.txt", "w+")
    file.write(data1)
    rsp = responsed("tema_patru/files/file.txt")

    try:
                response_data['result']=rsp
    except:
         response_data['result']="nup"
    return HttpResponse(json.dumps(response_data),content_type="application/json")

def getFile(request):
    message="Merge sum"
    with open("tema_patru/files/gauss_seidel.txt", 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/plain")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename("tema_patru/files/gauss_seidel.txt")
        return response
