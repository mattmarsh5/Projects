#Solving a linear system of equations using the inverse matrix method and by transforming matrix to row echelon form.

#Start of code to solve using inverse matrix method.
print("Solving system using inverse matrix method")
print("")

import numpy as np
import random

#Asking user how many rows/columns they want. Needs to be a square coefficient matrix.
dim = int(input("How many rows/columns: "))
totaldim = (dim*dim)

#Initializing the coefficient matrix
i = 0
A = np.empty((0,dim),float)
print(A)

#Ask user for coefficient values or random fill and then add them to the coefficient matrix
print("Coefficient values for matrix:")
print("")

ans = ""
while ans not in ["Rand", "rand", "Own", "own"]:
    ans = input("Random values or assign your own? Use Rand or Own: ")
    if ans not in ["Rand", "rand", "Own", "own"]:
        print("Use Rand or Own")

while i < totaldim:
    if ans in ["Own", "own"]:
        val = float(input("Value: "))
    if ans in ["Rand", "rand"]:
        val = random.randint(-100,100)
    A = np.append(A,val)
    i = i + 1
A = A.reshape(dim,dim)


#Now Input values for the solution matrix
i = 0
print("")

ans = ""
while ans not in ["Rand", "rand", "Own", "own"]:
    ans = input("Random values or assign your own? Use Rand or Own: ")
    if ans not in ["Rand", "rand", "Own", "own"]:
        print("Use Rand or Own")

sol = np.empty((0,dim),float)
print("Coefficient values for Solutions:")
while i < dim:
    if ans in ["Own", "own"]:
        val = float(input("Value: "))
    if ans in ["Rand", "rand"]:
        val = random.randint(-20,20)
    sol = np.append(sol,val)
    i = i + 1
sol = sol.reshape(dim,1)

#Combining the coefficients and the solutions to form the final matrix for row echelon form calculations.
matt = np.append(A,sol,axis=1)

#Testing the ranks of coefficient matrix and augmented matrix for inconsistent solution
if np.linalg.matrix_rank(A) != np.linalg.matrix_rank(matt):
    print("")
    print("System is inconsistent.")
    exit()

#Testing for linear dependence by searching for nonzero determinant
det = np.linalg.det(A)
#print(det)
if det >= -.00000001 and det <= .00000001:
    print("")
    print("System is linearly dependent with infinite solutions.")
    exit()

#printing the equations as well as their solutions.
print("")
print("Coefficients are:")
print(A)
print("")
print("Solutions are:")
print(sol)
print("")


#First calculating the inverse of the coefficient matrix. To solve need X = (A^-1)*b
A_inv = np.linalg.inv(A)
print("Inverse of Matrix A is:")
print(A_inv)

#Multiplying the inverse matrix by the solutions
Ans = A_inv.dot(sol)
print("")

#printing the solution for the system
print("Solution to for the system using Inverse Matrix Method:")
print(Ans)
print("")

#Solving using row echelon form
print("Now solving matrix using row echelon form.")
print("")

#Below loops will form the matrix into row echelon form.
i = 0
coldim = dim + 1

while i < dim:
    k = 1
    while k < (dim-i):
        j = 0
        s = matt[k + i][i] / matt[i][i]
        while j < (coldim-i):
            matt[k + i][j+i] = matt[k + i][j+i] - s*matt[i][j+i]
            j = j+1
        k = k + 1
    i = i + 1


#printing the matrix that is now in row echelon form.
print("Matrix in row echelon form:")
print(matt)
print("")

#calculating the last solution for the matrix in order to initiate the loop to solve
last = matt[dim-1][dim]/matt[dim-1][dim-1]
solution = []
solution = np.append(solution, last)

#Solving the system
i = i - 2
count = 1

while i >= 0:
    #Reshaping the solution to multiply and iterate through.
    solution = solution.reshape(count,1)
    #Blank total matrix to produce a new "product" on each loop
    total = []
    j = dim - 1
    k = dim - 1
    while j > i:
        new = np.multiply(matt[k-count][j],solution[k-j][0])
        total = np.append(total,new)
        j = j - 1

    #Finding the product by summing the values in the total matrix
    product = total.sum()

    #finding the new solution.
    newsol = (matt[j][dim]-product)/matt[j][j]

    #Flattening the solution matrix and appending the new solution.
    solution = solution.flatten()
    solution = np.append(solution, newsol)
    i = i - 1
    count = count + 1

#Reshaping the solution matrix so it's not flattened.
solution = solution.reshape((dim),1)

#Solutions are upside down. Need to reorder
i = 0
final = []
while i < dim:
    final = np.append(final,solution[dim-1-i][0])
    i = i + 1

#Final solution matrix
final = final.reshape((dim),1)
print("Solution using Row Echelon Form:")
print(final)



