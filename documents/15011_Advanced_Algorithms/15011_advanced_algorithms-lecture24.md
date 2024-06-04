# Introduction to Spectral Graph Theory 

Spectral Graph Theory studies how the eigenvalues and eigenvectors of the adjacency matrix (or related matrices), which are purely algebraic quantities, relate to combinatorial properties of the graph. This is a very active research area with numerous modern applications such as image segmentation, finding min/max cuts, and clustering (community detection).

Let us start with some images to increase our appetite for learning more about this area. The following two graphs are drawn using the coordinates of two eigenvectors corresponding to large eigenvalues of the adjacency matrix
and the following graph is drawn using the coordinates of two eigenvectors corresponding to small eigenvalues of the adjacency matrix

Notice that when we draw graphs using eigenvectors corresponding to large eigenvalues of the adjacency matrix (first two drawings), we have that adjacent vertices are depicted nearby. When we select eigenvectors corresponding to small eigenvalues, the opposite seems to happen (last drawing). In this lecture, our goal is to explain some of these behaviors.

Before continuing, let me remark that there is a lot to say about spectral graph theory (and we have only two lectures). Two courses devoted to the subject are [1] and [2]. The first two drawings are taken from [1] and the last one from [3].

## 1 The (Normalized) Adjacency Matrix and Eigenvalues/Eigenvectors

Recall the definition of the adjacency matrix of an undirected graph:

Definition 1 The adjacency matrix $A$ of graph $G=(V, E)$ of $|V|=n$ vertices is a matrix in $\mathbb{R}^{n \times n}$ defined by

$$
A_{i j}=1 \text { if and only if }\{i, j\} \in E
$$

for every two vertices $i, j \in V$.

It will also be convenient to work with the so-called normalized adjacency matrix. To simplify notation, we assume throughout the lecture that all graphs that we work with are $d$-regular. That is, the degree of each vertex equals $d$. However, all definitions and results can be generalized to the case when vertices have different degrees.

Definition 2 The normalized adjacency matrix $M$ of a $d$-regular graph is equal to $\frac{1}{d} A$, with $A$ being the adjacency matrix.

Example (2-regular graph):

![](https://cdn.mathpix.com/cropped/2024_05_17_4cf1da64bb22c4806ff0g-2.jpg?height=187&width=195&top_left_y=1441&top_left_x=347)

$$
A=\left(\begin{array}{cccc}
0 & 1 & 0 & 1 \\
1 & 0 & 1 & 0 \\
0 & 1 & 0 & 1 \\
1 & 0 & 1 & 0
\end{array}\right) \quad M=\left(\begin{array}{cccc}
0 & \frac{1}{2} & 0 & \frac{1}{2} \\
\frac{1}{2} & 0 & \frac{1}{2} & 0 \\
0 & \frac{1}{2} & 0 & \frac{1}{2} \\
\frac{1}{2} & 0 & \frac{1}{2} & 0
\end{array}\right)
$$

The normalized adjacency matrix $M$ is also called the random walk matrix of a graph. The reason for this becomes clear if we consider the above example graph. Suppose you start at vertex $a$ corresponding. Hence, the distribution over the vertices where you are standing can be represented by the vector $(1,0,0,0)$ you are with probability 1 at vertex $a$ and probability 0 at any other vertex. Now suppose you go to a random neighbor in your graph, then with probability $1 / 2$ you end up at vertex $b$ and with probability $1 / 2$ you end up at vertex $d$. Thus after one random step, the distribution of your location is represented by the vector $(0,1 / 2,0,1 / 2)$. Now notice that in the example above

$$
M\left(\begin{array}{l}
1 \\
0 \\
0
\end{array}\right)=\left(\begin{array}{c}
0 \\
1 / 2 \\
0 \\
1 / 2
\end{array}\right)
$$

More generally, for any starting distribution $p \in \mathbb{R}^{n}$ (where $p_{i}$ denotes the probability to be at vertex $i \in V$ initially), $M p$ is the probabilitydistribution after a single random step. Repeating this argument gives that $M^{k} p$ is the distribution after $k$ random steps.

### 1.1 Basic properties of eigenvectors/eigenvalues of $M$

The normalized adjacency matrix $M$ has some special structure, which we will exploit:

Observation $3 M$ is a real symmetric matrix.

Recall the definition of eigenvalue and eigenvector of a matrix.

Definition $4 A$ vector $v$ is an eigenvector of a matrix $M$ with eigenvalue $\lambda$ if

$$
M v=\lambda v
$$

The following is a fact derived using standard linear algebra (and not proved in this course):

Fact 5 If $M \in \mathbb{R}^{n \times n}$ is symmetric, then:

1. $M$ has $n$ non-necessarily distinct real eigenvalues $\lambda_{1} \geq \lambda_{2} \geq \ldots \geq \lambda_{n}$.
2. If $v_{1}, v_{2}, \ldots, v_{i-1}$ are eigenvectors for $\lambda_{1}, \lambda_{2}, \ldots, \lambda_{i-1}$, then $\lambda_{i}$ equals the maximum value $\lambda$ such that there is a vector $v_{i}$ orthogonal to $v_{1}, \ldots, v_{i-1}$ such that $M v_{i}=\lambda v_{i}$. Moreover, any such vector $v_{i}$ can be selected to be the eigenvector corresponding to $\lambda_{i}$.

This means in particular that no matter how the first eigenvector $v_{1}$ is chosen, we can always find an orthonormal basis (corresponding to eigenvectors).

Example: (using the same 4-cycle)

$$
\begin{gathered}
\lambda_{1}=1, \lambda_{2}=0, \lambda_{3}=0, \lambda_{4}=-1 \\
v_{1}=\left(\begin{array}{c}
\frac{1}{2} \\
\frac{1}{2} \\
\frac{1}{2} \\
\frac{1}{2}
\end{array}\right) v_{2}=\left(\begin{array}{c}
0 \\
-\frac{1}{\sqrt{2}} \\
0 \\
\frac{1}{\sqrt{2}}
\end{array}\right) v_{3}=\left(\begin{array}{c}
-\frac{1}{\sqrt{2}} \\
0 \\
\frac{1}{\sqrt{2}} \\
0
\end{array}\right) v_{4}=\left(\begin{array}{c}
-\frac{1}{2} \\
\frac{1}{2} \\
-\frac{1}{2} \\
\frac{1}{2}
\end{array}\right)
\end{gathered}
$$

In the next section, we will get a better intuition regarding the eigenvalues of the normalized adjacency matrix and relate them to basic combinatorial properties.

## 2 Relating the eigenvalues to basic combinatorial properties

The following gives a very good intuition to keep in mind when dealing with spectral graph theory. It already tells you that for a large eigenvalue, we would like adjacent vertices to have similar values (as we saw in the drawings).

Observation 6 Consider $x \in \mathbb{R}^{n}$ which assigns a value $x(i)$ to each vertex $i \in V$ and let $y=M x$, where $M$ is the normalized adjacency matrix of a graph $G=(V, E)$. Then

$$
y(i)=\sum_{\{i, j\} \in E} \frac{x(j)}{d}
$$

which is the average value according to $x$ of $v$ 's neighbours.

Using this observation, the following properties become quite easy to prove

Lemma 7 Let $M$ be the normalized adjacency matrix of a $d$-regular graph $G$ and let $\lambda_{1} \geq \lambda_{2} \geq \ldots \geq \lambda_{n}$ be its eigenvalues. Then:

1. $\lambda_{1}=1$.
2. $\lambda_{2}=1 \Longleftrightarrow G$ is disconnected.
3. $\lambda_{n}=-1 \Longleftrightarrow$ one component of $G$ is bipartite.

Proof of 1: Since $M\left(\begin{array}{c}1 \\ 1 \\ \ldots \\ 1\end{array}\right)=1 \times\left(\begin{array}{c}1 \\ 1 \\ \ldots \\ 1\end{array}\right), 1$ is an eigenvalue and therefore $\lambda_{1}$, the greatest of all eigenvalues, must be greater or equal to 1 .

Additionally, if we consider any eigenvector $x$ and $i \in V$ such that $x(i)$ is maximized and $y=M x$, we have $y(i)=\sum_{\{i, j\} \in E} \frac{x(j)}{d} \leq \sum_{\{i, j\} \in E} \frac{x(i)}{d}=x(i)$. Therefore, $\lambda_{1} \leq 1$.

Proof of 2: By the proof of property 1 we saw that we can select the first eigenvector $v_{1}$ corresponding to $\lambda_{1}=1$ to be the all 1 's vector. We will show that there is a vector $v_{2} \perp v_{1}$ so that $M v_{2}=v_{2}$ if and only if $G$ is disconnected. In other words, $\lambda_{2}=1$ if and only if $G$ is disconnected.

Suppose first that the graph $G$ is disconnected and so that there is a subset $S \subsetneq V$ of vertices that are not connected to vertices in $V \backslash S$. define $v_{2}$ by

$$
v_{2}(i)= \begin{cases}1 /|S| & \text { if } i \in S \\ -1 /|V \backslash S| & \text { if } i \in V \backslash S\end{cases}
$$

Notice that $v_{2}$ is perpendicular to the all 1 's vector $v_{1}$, i.e., $v_{2} \perp v_{1}$. We now show that $M v_{2}=v_{2}$. Fix a vertex $i$ and let $y=M v_{2}$. We have that

$$
y(i)=\frac{1}{d} \sum_{\{j, i\} \in E} v_{2}(j)=\frac{1}{d} \sum_{\{j, i\} \in E} v_{2}(i)=v_{2}(i)
$$

where the second inequality follows from that every neighbor of $i$ has the same value (with respect to $v_{2}$ ) by definition. Hence, we have $\lambda_{2}=1$ if $G$ is disconnected.

Now suppose that $G$ is connected. Now let $v_{2}$ be an eigenvector corresponding to the second eingevalue $\lambda_{2}$. We have that $v_{2}$ is is perpendicular to the all 1 's vector $v_{1}$, We now show that $\lambda_{2}<1$. Indeed, since $v_{2} \perp v_{1}, v_{2}$ cannot assign the same value to all vertices. Therefore, as $G$ is connected, there must be a vertex $i$ that has at least one neighbor $j$ for which $v_{2}(i) \neq v_{2}(j)$. Select such a vertex $i$ that maximizes $v_{2}(i)$. By the selection of $i$ we have that for any $\{i, j\} \in E$ we have $v_{2}(i) \geq v_{2}(j)$ and for at least one neighbor $j^{*}$ we have $v_{2}(i)>v_{2}\left(j^{*}\right)$. Again let $y=M v_{2}$. It follows that

$$
y(i)=\frac{1}{d} \sum_{\{j, i\} \in E} v_{2}(j) \leq \frac{1}{d}\left(\sum_{\{j, i\} \in E: j \neq j^{*}} v_{2}(i)+v_{2}\left(j^{*}\right)\right)<v_{2}(i)
$$

and thus $\lambda_{2}<1$.

The proof of property 3 is left as an exercise.

Remark The second property can be generalized: $\left|\left\{i \mid \lambda_{i}=1\right\}\right|$ is the number of connected components in G.

