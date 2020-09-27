


def isat(matrix,i,j):
    c=0
    #Row and Column Attack
    #----------------------------------------------------------------------
    for x in range(n):
        if x != i:
            if matrix[x][j]==1:
                c+=1
                print("Q[",str(x+1),",", str(j+1) ,"],")
        
            
    for x in range(n):
        if x != j:
            if matrix[i][x] ==1:
                c+=1
                print("Q[",str(i+1),",", str(x+1) ,"],")
    #---------------------------------------------------------------------         

    #3rd Quanquadrant Diagonal Attack
    #----------------------------------------------------------------------
    
    for x, y in zip(range(i, -1, -1), range(j, -1, -1)):
        if matrix[x][y] == 1:
            if x!=i and y!=j:
                c+=1
                print("Q[",str(x+1),",", str(y+1) ,"],") 
    #----------------------------------------------------------------------
                
    #4th Quanquadrant Diagonal Attack
    #----------------------------------------------------------------------
                
    for x, y in zip(range(i, n, 1), range(j, -1, -1)): 
        if matrix[x][y] == 1: 
            if x!=i and y!=j:
                c+=1
                print("Q[",str(x+1),",", str(y+1) ,"],") 
    #----------------------------------------------------------------------
    
    #2nd Quanquadrant Diagonal Attack
    #----------------------------------------------------------------------
                
    for x, y in zip(range(i, -1, -1), range(j, n, 1)):
        if matrix[x][y] == 1:
            if x!=i and y!=j:
                c+=1
                print("Q[",str(x+1),",", str(y+1) ,"],") 
    #----------------------------------------------------------------------
    
    #1st Quanquadrant Diagonal Attack
    #----------------------------------------------------------------------
    for x, y in zip(range(i, n, 1), range(j, n, 1)): 
        if matrix[x][y] == 1: 
            if x!=i and y!=j:
                c+=1
                print("Q[",str(x+1),",", str(y+1) ,"],") 
    #----------------------------------------------------------------------
    return c









n= int(input("Enter N for N Queen problem-"))



matrix = [ ]








#------------------------------------------------------------------------------
#----------- TO TAKE THE INPUT AS A SINGLE STRING PATTERN USE PART- 1
#------------------------------------------------------------------------------


#--------------------------------- ( PART- 1 ) --------------------------------
"""print("Enter Pattern-")


for i in range(n):          
    a =[ ]
    temp=input()
    for j in range(n):
        if j == int(temp)-1:
            a.append(1)
        else:
            a.append(0)

    matrix.append(a)      
    
print(matrix)
matrixT = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

matrix=matrixT"""
#------------------------------------------------------------------------------











#------------------------------------------------------------------------------
#----------- TO TAKE THE INPUT FOR EACH INDEX USE PART- 2
#------------------------------------------------------------------------------


#--------------------------------- ( PART- 2 ) --------------------------------

"""for i in range(n):          

    a=[]
    for j in range(n):
        
         print("For ["+str(i+1)+","+ str(j+1) +"]- ")
         a.append(int(input()))

    matrix.append(a)"""

#------------------------------------------------------------------------------







print(matrix)

print()
print("----------Can Attack----------")
totalna=0
for i in range(n):
    for j in range(n):      
        if matrix[i][j] ==1:
            print("Queen["+ str(i+1)+","+str(j+1)+"]:")
            c=isat(matrix,i,j)
            print("Number of attack- "+str(c))
            totalna+=(7-c)
            print("Number of non-attack- "+str(7-c))
            

    print( )
print("Sum- ",str(totalna))   
totalnonap=totalna/2
print("Fitness- ",str(totalnonap))