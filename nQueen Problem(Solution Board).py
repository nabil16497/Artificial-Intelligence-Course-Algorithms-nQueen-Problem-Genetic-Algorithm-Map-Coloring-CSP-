

def solve(): 
	
	if colcheck(matrix, 0) == False: 
		print ("Solution does not exist") 
		return False

	output(matrix) 
	return True

def colcheck(matrix, col): 

	if col >= n: 
		return True

	for i in range(n): 

		if attackcheck(matrix, i, col): 
	
			matrix[i][col] = 1

			if colcheck(matrix, col + 1) == True: 
				return True


			matrix[i][col] = 0

	return False

def attackcheck(matrix, row, col): 

	for i in range(col): 
		if matrix[row][i] == 1: 
			return False

	for i, j in zip(range(row, -1, -1), 
					range(col, -1, -1)): 
		if matrix[i][j] == 1: 
			return False

	for i, j in zip(range(row, n, 1), 
					range(col, -1, -1)): 
		if matrix[i][j] == 1: 
			return False

	return True


def output(matrix): 
	for i in range(n): 
		for j in range(n): 
			print (matrix[i][j], end = " ") 
		print() 

n=int(input("Enter Number of Queens- "))
matrix =[ ]
for i in range(n):          

    a=[]
    for j in range(n):
        
         a.append(0)

    matrix.append(a)

solve() 


