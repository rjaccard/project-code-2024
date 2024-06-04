# Neural Nets - Regularization, Data Augmentation, And Dropout

## Dataset Augmentation

Data is scarce and valuable and the more data we have the better we can train. In some instances we can generate new data from the data we are given.

Consider a classification task with training set S_t = {(xn, yn)}.
Assume that there exists a transformation τ : R^D → R^D
that keeps the labels unchanged. 

E.g., consider a hand-writing recognition task. We are given small squares (see Figure 1) each containing a digit from 0 to 9. The absolute position of the digit inside the square and the exact orientation of the digit do not matter and can be changed without changing the label. 

We can therefore take the data we are given, create variants of it, and add it to the date. Figure 1 shows some characters from the MNIST data set. Figure 2 shows some rotated variants and Figure 3 shows some shifted variants.

This way we can significantly increase our data which helps in training. In addition, if we train our network on this augmented data set then the network will automatically learn to become invariant to these transformations.

These transformations, if they exist, are very task specific. If we consider image recognition task some other possible transformations are cropping or *resizing*. More subtle, we can use the PCA and "compress" the image by only keeping the components corresponding to the largest singular values. This changes the photo globally but introduces only a minimal distortion (in the L2 sense). In a similar sense, we can add some small amount of noise to our data. There is another way in which we can "augment" our data.

Assume that we have several distinct but related tasks. In this case we can train a network jointly whose "core" is used jointly for all tasks and where only the last layer is task specific. This is shown in Figure 4. The idea here is that for related tasks the same features are useful for the task.

## Dropout

Dropout is a method both to avoid overfitting as well as to do model averaging (Hinton et al, 2012). By now, many variants have been proposed. Here is the original version.

Define the probability $p_i^{(l)}$. It is the probability of "keeping" the node i in layer l. Typical values are $p_i^{(0)} = 0.8$ (i.e., we keep in expectation 80 percent of all input nodes) and $p_i^{(l)} = 0.5$ for l ≥ 1, (i.e., we keep in expectation 50 precent of all hidden nodes).

At every training step decide for each node i at level l according to the probability $p_i^{(l)}$ whether to keep this node or not. This defines a "subnetwork." Run one step of SGD (or perhaps a minibatch) and update the weights. Iterate until training is done. 

For the prediction phase several variants are possible. Either generate K subnets in the same manner as before, predict for each and average the prediction. Alternatively use the whole network for the prediction. But in this case scale the output of node i at level l by the factor $p_i^{(l)}$. This guarantees that the expected input at each node stays the same as the expected input during training. 

There are two benefits to this "dropout" procedure. First, it has been observed that this procedure limits overfitting. Intuitively, nodes cannot "rely" on other nodes being present. Second, note that there is an exponential number of "subnetworks." This is shown in Figure 5 for a very small toy network. The effect of dropout is that we are performing an average over several (sub)networks. We either do this explicitly by running over several of them, computing the output, and then average. Or we do this implicitly by using the whole network but with reduced weights. We therefore get the advantage that comes with model averaging. 

Averaging over many models is a standard ML trick and it is called *bagging*. It typically leads to improved performance.
But dropout is quite different from standard bagging since we do not train K networks and then average. Rather, all these networks share the same weights. In fact, this characteristic seems to be an important component to explain their good performance. 

In dropout we remove whole nodes. It is of course also possible to remove individual edges independently from each other.