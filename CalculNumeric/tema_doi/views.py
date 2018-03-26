import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from tema_doi.functions import *
def index(request):

    context={}
    return render(request,'tema_doi/index.html',context)

@csrf_exempt
def terms(request):
    print("*******************************************")
    response_data={}
    print(request)
    received_json_data = json.loads(request.body)
    print(received_json_data)
    print("############################################")
    matA = received_json_data['matA']
    matB = received_json_data['matB']
   # matA = convert(matA)
    #matB = convert(matB)
    matB=convertMatrixToArray(matB)
    print(matA)
    print(matB)
    rsp = response(matA, matB)
    if(rsp!=-1):
        ver1 = verificare(matA, matB, rsp)
        ver2 = verificare2(matA, matB, rsp)
        ver3 = verificare3(matA, matB, rsp)

    try:
        response_data['result']=rsp
        if (rsp != -1):
          response_data['ver1'] = ver1
          response_data['ver2'] = ver2
          response_data['ver3'] = ver3
    except:
        response_data['result']= "nup"
    return HttpResponse(json.dumps(response_data),content_type="application/json")