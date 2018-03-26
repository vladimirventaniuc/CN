import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from tema_cinci.functions import *

#from CalculNumeric.tema_cinci.functions import generateInverse


def index(request):

    context={}
    return render(request,'tema_cinci/index.html',context)

@csrf_exempt
def inverse(request):
    print("*******************************************")
    response_data = {}
    received_json_data = json.loads(request.body)
    matA = received_json_data['matA']
    ok,res= generateInverse(matA, 1)
    print(ok)
    print(res)
    try:
        if(ok ==True ):
            response_data['ok'] = 1
            response_data['nrIteratii'] = res[0]
            response_data['inversa'] = res[1]
        else:
            response_data['norma'] = res[0]
            response_data['ok'] = 0
            response_data['nrIteratii'] = res[1]
    except:
        response_data['result'] = "nup"
    return HttpResponse(json.dumps(response_data), content_type="application/json")