Lenianet: Extension of Lenia

Lenianet is an extension of Lenia, which simulates Lenia on the surface of 3D meshes.
**Implementation**

    scipy
    numpy

**Implementation**

This extension allows for the simulation of game states using 3D meshes, providing a more generalized method by converting 3D faces into a 2D weighted distance matrix. 

Let $A$ be a Cuboid Voxel mesh, faces $F$, and face centroids,$C$.

$\text{Dist}(F) (i \in n) = \begin{cases} \mid F_i - F_j \mid & \text{if } F_j \subset B(0,\sqrt{2}) \text{ for some } j \in n \\ 0 & \text{otherwise} \end{cases}$

Where $n$ is the number of faces.
Let $R$ be the kernel radius.


We calculate the distance up to $R$ depth Dijkstra's algorithm,
$$\text{Dist}_R(F) =   \text{Diijstra}(\text{Dist}(F),R ) $$
Using the Gaussian bell function we derive the weights for shell kernel centred on $F_i (i \in n) $.

$$K =  \frac{1}{\bar{K_i}}\text{Bell}\left(\frac{\text{Dist}_R(F)}{R},\mu = 0.5,\sigma = 0.15 \right)  $$
Where $\bar{K_i}$ is the row-wise mean of $K$.

Let $V_t$ the values of cells at time $t$.
Then $$V_{t+\Delta t} = \operatorname{clip}\left(\mathbf{V}_t+\Delta t \ \mathbf{G}(\phi), 0,1\right)$$

Where $\phi = \sum_j (KV_t)_{i,j} $

To use this extension, simply download the code from the repository and run the lenia_extension.py file. 
**Credits**

This extension was developed by Katie Whitelock based on the original Lenia code by Bert Wang-Chak Chan.
