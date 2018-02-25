import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from tema_unu.functions import *
# Create your views here.
def index(request):
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    uuu=ex1()[0]
    asociativ=ex2Add(1.0,uuu,uuu)
    print("11111111111111111111111111111111111111111")
    if(asociativ==False):
        asociativ="neasociativa"
    else:
        asociativ="asociativa"

    context={'uuu':uuu,'asociativ':asociativ}
    return render(request,'tema_unu/index.html',context)
@csrf_exempt
def multiply(request):
    print("*******************************************")
    response_data={}
    print(request)
    received_json_data = json.loads(request.body)
    matA=received_json_data['matA']
    matB = received_json_data['matB']
    matA=convert(matA)
    matB=convert(matB)
    matC = recursive(matA,matB)
    print("############################################")
    try:
        response_data['result']=matC
    except:
        response_data['result']="nup"
    return HttpResponse(json.dumps(response_data),content_type="application/json")