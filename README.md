Lenianet: Extension of Lenia

Lenianet is an extension of Lenia, which simulates Lenia on the surface of 3D meshes.
Requirements

    scipy
    numpy

Implementation

This extension allows for the simulation of game states using 3D meshes, providing a more generalized method by converting 3D faces into a 2D weighted distance matrix.

Let $G$ be a Cuboid Voxel mesh, with vertices $V$, faces $F$, and centroids of $F$ is $C$.

$\text{Dist}(F) (i \in n) = \begin{cases} \mid F_i - F_j \mid & \text{if } F_j \subset B(0,\sqrt{2}) \text{ for some } j \in n \\ 0 & \text{otherwise} \end{cases}$
Where $n$ is the number of faces. Then let the game rules have a radius of $R$.

Using Dijkstra's algorithm, up to $R$ depth,

$$\text{Dist}_R(F) =   \text{Diijstra}(\text{Dist}(F),R ) $$

Using the Gaussian bell function we derive the weights for shell kernel centered on $F_i (i \in n) $.

$$K =  \frac{1}{\bar{K_i}}\text{Bell}(\text{Dist}_R(F),\mu = 0.5,\sigma = 0.15)  $$

Where $\bar{K_i}$ is the row-wise mean of $K$.

To use this extension, simply download the code from the repository and run the lenia_extension.py file.
Credits

This extension was developed by Katie Whitelock based on the original Lenia code by Bert Wang-Chak Chan.
