
import random


def isat(matrix,i,j):
    c=0
    #Row and Column Attack
    #----------------------------------------------------------------------
    for x in range(n):
        if x != i:
            if matrix[x][j]==1:
                c+=1
        
    for x in range(n):
        if x != j:
            if matrix[i][x] ==1:
                c+=1
    #---------------------------------------------------------------------         

    #3rd Quanquadrant Diagonal Attack
    #----------------------------------------------------------------------
    
    for x, y in zip(range(i, -1, -1), range(j, -1, -1)):
        if matrix[x][y] == 1:
            if x!=i and y!=j:
                c+=1
    #----------------------------------------------------------------------
                
    #4th Quanquadrant Diagonal Attack
    #----------------------------------------------------------------------
                
    for x, y in zip(range(i, n, 1), range(j, -1, -1)): 
        if matrix[x][y] == 1: 
            if x!=i and y!=j:
                c+=1
    #----------------------------------------------------------------------
    
    #2nd Quanquadrant Diagonal Attack
    #----------------------------------------------------------------------
                
    for x, y in zip(range(i, -1, -1), range(j, n, 1)):
        if matrix[x][y] == 1:
            if x!=i and y!=j:
                c+=1
    #----------------------------------------------------------------------
    
    #1st Quanquadrant Diagonal Attack
    #----------------------------------------------------------------------
    for x, y in zip(range(i, n, 1), range(j, n, 1)): 
        if matrix[x][y] == 1: 
            if x!=i and y!=j:
                c+=1
    #----------------------------------------------------------------------
    return c
def fitnessinparcent(fit):
    sumfit=0
    for f in fit:
        sumfit+=f
    for f in fit:
        fitinparcent.append(round(f*100/sumfit))

def fitness(tempx):
    
    matrix = [ ]
    for temp in tempx:          
        a =[ ]
        for j in range(n):
            if j == int(temp)-1:
                a.append(1)
            else:
                a.append(0)
        matrix.append(a)      
    matrixT = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    matrix=matrixT
    totalna=0
    for i in range(n):
        for j in range(n):      
            if matrix[i][j] ==1:
                c=isat(matrix,i,j)
                totalna+=(7-c) 
    totalnonap=totalna/2
    print("Fitness- ",str(totalnonap))
    fit.append(totalnonap)
    
def crossover(p1,p2):
    a=random.randint(0,6)
    b=random.randint(a,7)
    for i in range(a,b):
        temp = p1[i]
        p1[i]=p2[i]
        p2[i]=temp
    temppopulation.append(p1)
    temppopulation.append(p2)

def mutation(p):
    a=random.randint(0,7)
    b=random.randint(1,7)
    p[a]=b
    temppopulation.append(p)
    

n= 8
population=[]

table=int(input("Enter Population- "))
numberg=int(input("Enter Number of Genaration- "))
for i in range(table):
    a =[ ]
    for j in range(n):
         a.append(random.randint(1,8))
    population.append(a)
print(population)


fit= [ ]
fitinparcent = [ ]

    
for board in population:
    fitness(board)
fitnessinparcent(fit)
print("In Parcentage- ")
for parcent in fitinparcent:
    print(parcent,"%")
    
    
for i in range(0, numberg-1):
    fit= [ ]
    fitinparcent = [ ]
    temppopulation = [ ]
    i=0
    while i<=7:
        parent1=population[i]
        parent2=population[i+1]
        crossover(parent1,parent2)
        i+=2
    population=temppopulation
    temppopulation = [ ]
    for p in population:
        mutation(p)
    population=temppopulation
    print(population)
    for board in population:
        fitness(board)
    fitnessinparcent(fit)
    print("In Parcentage- ")
    for parcent in fitinparcent:
        print(parcent,"%")
