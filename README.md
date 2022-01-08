# Solving a Linear Sytem of Equations

The purpose of this project was to demonstrate a general understanding of matricies as well as gain experience with using python and nested loops. The program solves a linear system of equations by first using inverse matrix method with Ax = b and I being an identity matrix:  

x = Ix                    </br>
x = (A<sup>-1</sup>*A)*x  </br>
x = A^<sup>-1</sup>*(A*x) </br> 
x = A^<sup>-1</sup>*b     </br>

The program will also iterate through and set the augmented matrix into row echelon form by means of Gaussin elimination. Both methods will arrive at the same set of solutions. The code also has checks in place to see if the vectors within matrix A are linearly dependent as well as whether or not the system is inconsistent meaning it has no solutions. 
