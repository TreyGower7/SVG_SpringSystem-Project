# SVG_Solver-Project
A repository containing Python scripts to achieve singular value decomposition to then solve a spring-mass system.

Below I have provided examples from the lecture notes to show that my code is accurate. For further testing of your own KU=F system, visit this GitHub link and clone the repository to your machine: https://github.com/TreyGower7/SVG_SpringSystem-Project 

My SVD code compared to Numpy Pythons Blackbox:
For easy comparison, I have included a script SVDcompare.py for any user inputted matrix to be decomposed with my SVDDecomposition.py script and Nunpys blackbox call. For example:
 
As you can see the signs for my V matrix and Blackbox’s V matrix are slightly different. However, this does not matter as when doing the math the signs work themselves out. On homework 2, I had a similar issue but after reconstructing the A matrix we get the desired result.
Example of a fixed/fixed system:
 
As can be seen this example is directly following our lecture slides. It provides us with the correct K matrix with a stable conditioning, then back solves for elongation and internal forces. This can also be scaled up and take non integer values as well:
 
Example of a fixed/free system:
 
As can be seen this example is directly following our lecture slides as well. It provides us with the correct K matrix with a stable conditioning, then back solves for elongation and internal forces. This can also be scaled up and take non integer values just as the first case.

Example of a free/free system:
For the free/free system since we are using our SVD decomposition we get returned a pseudo-inverse matrix. However, there exists no real inverse of the stiffness matrix for a free/free system. This is because the conditioning of the Stiffness matrix for the free/free system is unstable. If we were to use a decomposition method such as LU factorization we would get returned an error telling us exactly that. This is why using SVD we need to ensure the condition number falls within an acceptable range to ensure solvability.
 
![image](https://github.com/TreyGower7/SVG_SpringSystem-Project/assets/70235944/3b3d4688-25b8-4b5e-8e9c-2d86beb225b2)
