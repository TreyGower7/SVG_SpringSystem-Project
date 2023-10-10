# SVG_Solver-Project
## A repository containing Python scripts to achieve singular value decomposition to then solve a spring-mass system.

***`Below I have provided examples to show that my code is accurate. For further testing of your own KU=F system, visit this GitHub link and clone the repository to your machine: https://github.com/TreyGower7/SVG_SpringSystem-Project`***

# My SVD code compared to Numpy Pythons Blackbox:
For easy comparison, I have included a script SVDcompare.py for any user inputted matrix to be decomposed with my SVDDecomposition.py script and Nunpys blackbox call. For example:

<img src = https://user-images.githubusercontent.com/70235944/273966824-fd3c820b-1bef-4a5c-bd2b-ac6837b9b74c.png>
 
As you can see the signs for my V matrix and Blackbox’s V matrix are slightly different. However, this does not matter as when doing the math the signs work themselves out. On homework 2, I had a similar issue but after reconstructing the A matrix we get the desired result.

# Example of a fixed/fixed system:
 <img src= https://user-images.githubusercontent.com/70235944/273966810-ecd2f34c-1441-4971-a0c5-38e9607371cb.png>
 <img src= https://user-images.githubusercontent.com/70235944/273966796-32220b39-8b6e-427b-9586-c3c4e24c1ec7.png>

As can be seen this example is directly following our lecture slides. It provides us with the correct K matrix with a stable conditioning, then back solves for elongation and internal forces. This can also be scaled up and take non integer values as well:
 
# Example of a fixed/free system:
 <img src= https://user-images.githubusercontent.com/70235944/273966789-6c5836f2-d1a7-496e-9c5e-858366dc054e.png>

As can be seen this example is directly following our lecture slides as well. It provides us with the correct K matrix with a stable conditioning, then back solves for elongation and internal forces. This can also be scaled up and take non integer values just as the first case.

# Example of a free/free system:
<img src= https://user-images.githubusercontent.com/70235944/273966773-53139a7c-195a-4dca-9fae-efe167534ca7.png>

For the free/free system since we are using our SVD decomposition we get returned a pseudo-inverse matrix. However, there exists no real inverse of the stiffness matrix for a free/free system. This is because the conditioning of the Stiffness matrix for the free/free system is unstable. If we were to use a decomposition method such as LU factorization we would get returned an error telling us exactly that. This is why using SVD we need to ensure the condition number falls within an acceptable range to ensure solvability.
 
