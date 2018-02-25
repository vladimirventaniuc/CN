def ex1():
    m=0
    u = 1 / (10**m)
    while (1 + u) !=1:
        m=m+1
        u=1/(10**m)

    print(u)
    print(m)
    return u,m


def ex2Add(x,y,z):
    if( (x+y)+z!=x+(y+z)):
        return False
    return True
def ex2Mul(x,y,z):
    print( (x * y) * z)
    print((y*(x*z)))
    if(( (x * y) * z) !=((y*z) * x) ):
        return False
    return True

def ex3(X,Y):
    p1=(X[0][0]+X[1][1])*(Y[0][0]+Y[1][1])
    p2=(X[1][0]+X[1][1])*Y[0][0]
    p3=X[0][0]*(Y[0][1]-Y[1][1])
    p4=X[1][1]*(Y[1][0]-Y[0][0])
    p5=(X[0][0]+X[0][1])*Y[1][1]
    p6=(X[1][0]-X[0][0])*(Y[0][0]+Y[0][1])
    p7=(X[0][1]-X[1][1])*(Y[1][0]+Y[1][1])

    Z=[[0,0],[0,0]]
    Z[0][0]=p1+p4-p5+p7
    Z[0][1]=p3+p5
    Z[1][0]=p2+p4
    Z[1][1]=p1+p3-p2+p6

    return Z

def add(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def subtract(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def recursive(X,Y):
    print("intra")
    if len(X)<=2:
        return ex3(X,Y)
    print(len(X))
    A = [[X[y][x] for x in range(len(X)//2)] for y in range(len(X)//2)]
    B = [[X[y][x] for x in range(len(X) // 2,len(X))] for y in range(len(X) // 2)]
    C = [[X[y][x] for x in range(len(X) // 2)] for y in range(len(X) // 2,len(X))]
    D = [[X[y][x] for x in range(len(X) // 2,len(X))] for y in range(len(X) // 2,len(X))]
    E = [[Y[y][x] for x in range(len(X) // 2)] for y in range(len(X) // 2)]
    F = [[Y[y][x] for x in range(len(X) // 2, len(X))] for y in range(len(X) // 2)]
    G = [[Y[y][x] for x in range(len(X) // 2)] for y in range(len(X) // 2, len(X))]
    H = [[Y[y][x] for x in range(len(X) // 2, len(X))] for y in range(len(X) // 2, len(X))]

    print(A)
    print(B)
    print(C)
    print(D)
    print(E)
    print(F)
    print(G)
    print(H)
    p1=recursive(add(A,D),add(E,H))
    p2=recursive(add(C,D),E)
    p3=recursive(A,subtract(F,H))
    p4=recursive(D,subtract(G,E))
    p5=recursive(add(A,B),H)
    p6=recursive(subtract(C,A),add(E,F))
    p7=recursive(subtract(B,D),add(G,H))

    Z = [[0, 0], [0, 0]]
    C11 = add(subtract(add(p1,p4),p5),p7)
    C12 = add(p3 , p5)
    C21 = add(p2 , p4)
    C22 = add(subtract(add(p1,p3),p2),p6)

    Z = [[0 for x in range(len(X))] for y in range( len(X))]
    Z = [[C11[0][0],C11[0][1],C12[0][0],C12[0][1]],
         [C11[1][0],C11[1][1],C12[1][0],C12[1][1]],
         [C21[0][0],C21[0][1],C22[0][0],C22[0][1]],
         [C21[1][0],C21[1][1],C22[1][0],C22[1][1]]]
    return Z

def convert(mat):
    print(len(mat))
    A=[[int(y) for y in x] for x in mat]
    return A