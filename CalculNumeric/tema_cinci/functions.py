import numpy as np


def generateMatrix(n):
    matrix= [[0 for x in range(n)] for y in range(n)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(i==j):
                matrix[i][j]=1
            if(i+1==j):
                matrix[i][j]=4

    return matrix

def printMatrix(matrix):
    for i in range(len(matrix)):
        line="| "
        for j in range(len(matrix[i])):
            line=line+str(matrix[i][j])+" "
        line=line+"|"
        print(line)

def generalV0(matrix):
    transpose = transposeOfMatrix(matrix)
    a1 = A1(matrix)
    ainf = Ainfinity(matrix)
    prod = a1 * ainf
    return divideMatrixBy(transpose, prod)


def transposeOfMatrix(matrix):
    transpose = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range (len(matrix[i])):
            transpose[j][i]=matrix[i][j]
    return transpose

def A1(matrix):
    max=-9999999999999999999999999999999

    for i in range(len(matrix)):
        sum=0
        for j in range(len(matrix[i])):
            sum = sum + abs(matrix[i][j])
        if(max < sum):
            max  = sum

    return max
def Ainfinity(matrix):
    max = -9999999999999999999999999999999
    for j in range(len(matrix)):
        sum = 0
        for i in range(len(matrix[j])):
            sum = sum + abs(matrix[i][j])
        if(max < sum):
            max = sum
    return max

def divideMatrixBy(matrix, n):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] / n
    return matrix
def multiplyMatrixBy(matrix, n):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] * n
    return matrix

def verifyLineDominance(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(i!=j and matrix[i][i] <= matrix[i][j]):
                return False;
    return True
def verifyColumDominance(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(i!=j and matrix[i][i] <= matrix[j][i]):
                return False
    return True

def V0IfDominance(matrix):
    v0 = [[0 for x in range(len(matrix[y]))] for y in range(len(matrix))]
    for i in range(len(matrix)):
        v0[i][i] = 1/matrix[i][i]
    return v0

def checkIfMatrixIsSymetrical(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j]!=matrix[j][i]):
                return False
    return True

def CheckExistenceOfPositivePivots(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j]==0):
                continue
            elif matrix[i][j] <0:
                return False
            break
    return True

def checkDeterminantsOfAllUpper_leftSubMatrixes(matrix):
    for k in range(1,len(matrix)+1):
        subMatrix = [[matrix[i][j] for i in range(k)] for j in range(k)]
        if ( np.linalg.det(subMatrix) < 0):
            return False
    return True

def Af(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum = sum+  pow(matrix[i][j],2)

    return pow(sum,1/2)

def V0IfMatrixIsSymetricalAndPositiveDefined(matrix):
    af = Af(matrix)
    In = generateIn(len(matrix))
    return divideMatrixBy(In, af)

def generateIn(n):
    matrix = [[0 for x in range(n)] for y in range(n)]
    for i in range (n):
        matrix[i][i] = 1
    return matrix

def substractTwoMatrixes(a,b):
    if(len(a)!=len(b) or len(a[0])!=len(b[0])):
        return False
    c=[[a[j][i] for i in range(len(a[j]))] for j in range(len(a))]
    for i in range(len(c)):
        for j in range(len(c[i])):
            c[i][j] = c[i][j] - b[i][j]
    return c

def verifyV0(matrix):
    if(verifyLineDominance(matrix) or verifyLineDominance(matrix)):
        print(1)
        v0= V0IfDominance(matrix)
    elif(checkIfMatrixIsSymetrical(matrix) and CheckExistenceOfPositivePivots(matrix) and checkDeterminantsOfAllUpper_leftSubMatrixes(matrix)):
        print(2)
        v0=V0IfMatrixIsSymetricalAndPositiveDefined(matrix)
    else:
        print(3)
        v0 = generalV0(matrix)
  #  print(v0)
    In = generateIn(len(matrix))
   # print(np.matmul(matrix, v0))
    dist = np.linalg.norm(np.matmul(matrix, v0) - In)
    return v0, dist

def test(matrix):
    In = generateIn(len(matrix))
    v01 = V0IfDominance(matrix)
    v02 = V0IfMatrixIsSymetricalAndPositiveDefined(matrix)
    v03 = generalV0(matrix)
    d1=np.matmul(matrix, v01)
    d2 = np.matmul(matrix, v02)
    d3 = np.matmul(matrix, v03)
    print("--------------------------------")
    printMatrix(v01)
    print("--------------------------------")
    printMatrix(v02)
    print("--------------------------------")
    printMatrix(v03)
    print("--------------------------------")
    print("********************************")
    printMatrix(d1)
    print("********************************")
    printMatrix(d2)
    print("********************************")
    printMatrix(d3)
    print("********************************")
    print(np.linalg.norm(d1 - In))
    print(np.linalg.norm(d2 - In))
    print(np.linalg.norm(d3 - In))

def generateInverseSchultz(matrix,v0):
    k=0
    kmax=10000
    v1=v0
    while(k<kmax):
        v0=v1
        matrixProduct = np.matmul(matrix, v0)
       # a = multiplyMatrixBy(generateIn(len(matrix)), 2)
       # printMatrix(substractTwoMatrixes(a,matrixProduct))
        v1=np.matmul(v0,(substractTwoMatrixes( multiplyMatrixBy(generateIn(len(matrix)),2),matrixProduct)))
        norm = np.linalg.norm(v1 - v0)
        k=k+1
        if(norm<0.0000000000001):
            return k,v1, True
        if(norm > pow(10,10)):
            return k,v1, False
    return k,v1, False

def generateInverseLiLi(matrix,v0):
    k = 0
    kmax = 10000
    v1 = v0
    while (k < kmax):
        v0 = v1
        matrixProduct = np.matmul(matrix, v0)
        # a = multiplyMatrixBy(generateIn(len(matrix)), 2)
        # printMatrix(substractTwoMatrixes(a,matrixProduct))
        v1 = np.matmul(v0, substractTwoMatrixes( multiplyMatrixBy( generateIn(len(matrix)) , 3)     ,np.matmul(matrixProduct, substractTwoMatrixes(  multiplyMatrixBy( generateIn(len(matrix)) , 3) , matrixProduct))))
        norm = np.linalg.norm(v1 - v0)
        k = k + 1
        if (norm < 0.0000000000001):
            return k, v1, True
        if (norm > pow(10, 10)):
            return k, v1, False
    return k, v1, False

def generateInverse(matrix, method):

    v0,dist = verifyV0(matrix)
    if(method==1):
        k,inverse,convergence = generateInverseSchultz(matrix,v0)
    else:
        k, inverse,convergence = generateInverseLiLi(matrix,v0)
    if(convergence==False):
        return False,[calculateNorm(matrix,inverse), k]
    else:
        return True,[k,convertToMatrix(inverse)]

def calculateNorm(matrix, inverse):
    prod = np.matmul(matrix,inverse)
    substract = substractTwoMatrixes(prod, generateIn(len(matrix)))

    return A1(substract)

def convertToMatrix(array):
    print(len(array))
    mat = [[array[i][j] for i in range(len(array[j]))] for j in range(len(array))]
    return mat