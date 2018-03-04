
def createSumProductFiles(filea, fileb, fileSum, fileProd):
    na, vecta, matrixa = read_file(filea)
    nb, vectb, matrixb = read_file(fileb)
    xa = createVector(na)
    xb = createVector(nb)
    sumMatrix = addMatrixes(matrixa, matrixb)
    prodMatrix = multiplyMatrixes(matrixa, matrixb)

    prodSumVect = multiplyMatrixVector(sumMatrix, xa)
    prodProdVect = multiplyMatrixVector(prodMatrix, xb)

    createFile(fileSum, sumMatrix, prodSumVect)
    createFile(fileProd, prodMatrix, prodProdVect)


def precizie(i):
    m=0
    u = 1 / (10**m)
    while i>0:
        m=m+1
        u=1/(10**m)
        i=i-1
    return u,m


def verifyDimension(a,b,sum):
    for i in range(len(a)):
        if (len(a[i]) + len(b[i])) < len(sum[i]):
          return False
    return True

def verifySum(sum, sumFile):
    u = precizie(11)[0]
    print(u)
    for i in range(len(sumFile)):
        for key, value in sumFile[i].items():
            if key in sum[i]:
               if (abs(value - sum[i][key]) > u):
                   return False

            else:
                return False
    return True

def verifyVect(vElement , vx):
    u= precizie(8)[0]
    for i in range(len(vx)):
        if(abs(vElement[i] - vx[i])) > u:
           return False
    return True

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
            arr.append(float(str))
        else:
            if(lines!="\n"):
                pair=lines.split()
                pair=(float(pair[0][:len(pair[0])-1]),  int(pair[1][:len(pair[1])-1]),int(pair[2]) )
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

def addMatrixes(a, b):
    c = copyObject(a)
    for i in range(len(b)):
        for key,value in b[i].items():
            if (key in c[i]):
                c[i][key] += value
            else:
                c[i][key] = value
    return c

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


def verificare(file1, file2):
    n, vect, matrix = read_file(file1)
    n2, vect2, matrix2 = read_file(file2)

    val1 = verifySum(matrix, matrix2)
    val2 = verifyVect(vect,vect2)
    return val1, val2

