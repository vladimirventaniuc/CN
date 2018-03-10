from decimal import *

import numpy


def precizie(i):
    m=0
    u = 1 / (10**m)
    while i>0:
        m=m+1
        u=1/(10**m)
        i=i-1
    return u,m


def read_file(path):
    arr = []
    diagonal_elements=[]
    try:
         file = open(path, "r")
    except IOError:
        print("Error: File does not appear to exist.")
        return 0
    n=int(file.readline())
    #vector de dictionare
    matrix = [{} for i in range(n)]
    file.readline()
    i=2

    for lines in file:
        if(i>1 and i<n+2):
            str=lines
            str = str[:len(str) - 1]
            arr.append(Decimal(str))
        else:
            if(lines!="\n"):
                lines=lines.replace(" ","")
                pair=lines.split(",")
               # print(pair)
                pair=(Decimal(pair[0]), int(pair[1]),int(pair[2]) )

                if(pair[2] in matrix[pair[1]]):
                    matrix[pair[1]][pair[2]]+=pair[0]
                else:
                    matrix[pair[1]][pair[2]] = pair[0]

        i=i+1


    return n, arr,matrix

def createVector(n):
    result = []
    for i in range(n):
        result.append(n-i)
    return result




def copyObject(x):
    matrix = [{} for i in range(len(x))]
    for i in range(len(x)):
        for key, value in x[i].items():
            matrix[i][key] = value
    return matrix

def createFile(file,matrix, vector):
    f = open(file, "w+")
    f.write(str(len(vector)))
    f.write('\n')
    f.write('\n')
    for i in range(len(vector)):
        f.write(str(vector[i])+'\n')

    f.write('\n')

    for i in range(len(matrix)):
        for key, value in matrix[i].items():
            f.write(str(value)+", "+str(i)+", "+str(key) +"\n")

def formPrincipalColumn(X):
    for i in range(X):
        max= 0 , i
        for j in range(X):
            if( X[j][i] > max[0] ):
                max[0]=X[i][j]
                max[1]=j
        X=changeLines(i,max[1])
    return X



def changeLines(i,j,X):
    aux = X[i]
    X[i]=X[j]
    X[j]=aux
    return X


def Gauss_Seidel(matA,matB):
    u=precizie(15)[0]
    print(u)
    res = [0 for i in range(len(matA))]
    ok=False
    j=0
    while ok == False:
        j=j+1
        ok=True
        for i in range(len(matA)):
            xi=matB[i]
            for key,value in matA[i].items():
                if(key!=i):
                  xi-=value*res[key]

            xi=xi/matA[i][i]
            if(abs(xi - res[i]) > u):
                ok=False
            res[i]=xi

    return res, j

def multiplyMatrixes(a,b):
    result = [{} for i in range(len(a))]


    for i in range(len(a)):
            for key, value in a[i].items():
                for key2, value2 in b[key].items():
                    if key2 in result[i]:
                        result[i][key2]=result[i][key2]+value*value2
                    else:
                        result[i][key2] = value * value2

    return result


def multiplyMatrixVector(a,x):
    result = []
    for i in range(len(a)):
        sum = 0
        for key, value in a[i].items():
               sum+= a[i][key]*x[key]
        result.append(sum)
    return result

def verifyNorm(matA, XGS, matB):
    prod=multiplyMatrixVector(matA, XGS)
    u=precizie(14)[0]
    prod=numpy.array(prod)
    matB=numpy.array(matB)
    norm = dist(prod,matB)
    if(norm<u):
        return True
    else:
        return False


def dist(x,y):
    return numpy.sqrt(numpy.sum((x-y)**2))

def verifyDiagonal(X):
    for i in range(len(X)):
        if((i not in X[i].keys())):
            return False
    return True

def responsed(path):
    dim, arr, matrix = read_file(path)
    if verifyDiagonal(matrix) == False:
        return -1
    else:
        XGS, iterations = Gauss_Seidel(matrix, arr)
        if verifyNorm(matrix, XGS , arr)==False:
            return 0
        else:
            createFile(XGS, "tema_patru/files/gauss_seidel.txt")
            return iterations

def createFile(matrix,file):
    f = open(file, "w+")
    f.write(str(len(matrix)))
    f.write('\n')
    f.write('\n')
    for i in range(len(matrix)):
        f.write(str(matrix[i])+'\n')

    f.write('\n')



