import numpy as np

def combineMatrixes(A,B):
    C = [[0 for x in range(len(A)+1)] for y in range(len(A))]
    for i in range(0,len(A)):
        for j in range(0,len(A)+1):
            if(j==len(A)):
                C[i][j]=B[i]
            else:
                C[i][j]=A[i][j]
    return C

def changeLines(X,i,j):
    for k in range(0, len(X)+1):
        aux=X[i][k]
        X[i][k]=X[j][k]
        X[j][k]=aux
    return X

def multiplyRowOfMatrix(X,i,value):
    vec=[0 for l in range(len(X)+1)]
    for j in range( 0, len(X)+1):
        vec[j]=X[i][j]*value
    return vec

def substractRowOfMatrix(X,i,vec):
    #print(vec)
    for k in range(0,len(vec)):
        X[i][k]=X[i][k]-vec[k]
    return X



def forwardElimination(X):
    n=len(X)
    for i in range(0,n-1):
        max=abs(X[i][i]),i

        for j in range(i,n):
            if(abs(X[j][i])>max[0]):
                max=abs(X[j][i]),j
        #print(" "+str(i) +" "+str(max))
        X=changeLines(X,i,max[1])
        for k in range(i+1,n):
            value = X[k][i]/X[i][i]

            vec = multiplyRowOfMatrix(X,i,value)

            X=substractRowOfMatrix(X,k,vec)
    return X

def backSubstitution(X):
    rsp=[0 for x in range(len(X)+1)]
    for i in range(len(X)-1,-1,-1):

        sum=X[i][len(X)]
        for j in range(i+1,len(X)):
            sum=sum-X[i][j]*rsp[j]
        try:
         rsp[i]=sum/X[i][i]
        except ZeroDivisionError as err:
            return -1

    return rsp[0:len(X)]



def response(A,B):
    X= combineMatrixes(A, B)
    X=forwardElimination(X)
    sol = backSubstitution(X)
    return sol





def verificare(A,B,vect):
    C=combineMatrixes(A,B)
    vectc=list(vect)
    for i in range(0,len(vectc)):
        vectc[i]=[vectc[i]]
    Bc=list(B)
    for i in range(0, len(Bc)):
         Bc[i] = [Bc[i]]
    mx = np.matrix(A)
    my = np.matrix(vectc)
    matProdus = mx*my
    dist = np.linalg.norm(matProdus - Bc)
    return dist

def verificare2(A,B,xgauss):
    a=np.array(A)
    b=np.array(B)
    x=np.linalg.solve(a,b)
    print(x)

    dist=np.linalg.norm(xgauss-x)

    return dist

def verificare3(A,B,xgauss):
    Bc = list(B)
    for i in range(0, len(Bc)):
        Bc[i] = [Bc[i]]
    ainv=np.linalg.inv(A)
    print(ainv)

    matPod=(np.matrix(ainv)*np.matrix(Bc))
    ymatP=np.array(matPod)

    return np.linalg.norm(xgauss-ymatP)

def convert(mat):
    print(len(mat))
    A=[[float(y) for y in x] for x in mat]
    return A

def convertMatrixToArray(X):
    arr=[0 for x in range(len(X)*len(X[0]))]
    k=0
    for i in range(0,len(X)):
        for j in range(0,len(X[i])):
            arr[k]=X[i][j]
            k=k+1
    return arr

