# Linear Regression 

## Model: Linear Regression What Is It?

Linear regression is a model that assumes a linear relationship between inputs and the output.

## Why Learn About Linear Regression?

Plenty of reasons: simple, easy to understand, most widely used, easily generalized to non-linear models. Most importantly, you can learn almost all fundamental concepts of ML with regression alone.

## Simple Linear Regression

With only one input dimension, we get simple linear regression.

$$y_{n}\approx f(\mathbf{x}_{n}):=w_{0}+w_{1}x_{n1}$$
Here, w = (w0, w1) are the two parameters of the model.

They describe f.

## Multiple Linear Regression

If our data has multiple input dimensions, we obtain multivariate linear regression.

$y_{n}\approx f(\mathbf{x}_{n})$

$:=w_{0}+w_{1}x_{n1}+\ldots+w_{D}x_{nD}$

$=w_{0}+\mathbf{x}_{n}^{\top}\left(\begin{array}{c}w_{1}\\ \vdots\\ w_{D}\end{array}\right)$

$=:\tilde{\mathbf{x}}_{n}^{\top}\tilde{\mathbf{w}}$

Note that we add a tilde over the input vector, and also the weights, to indicate they now contain the additional offset term (a.k.a. bias term).

## Learning / Estimation / Fitting

Given data, we would like to find $˜w= [w0, w1, . . . , wD]$.

This is called learning or estimating the parameters or fitting the model. To do so, we need an optimization algorithm, which we will discuss in the chapter after the next.

## Matrix Multiplication

To go any further, one must revise matrix multiplication. Remember that multiplication of M × N matrix with a N × D matrix results in a M × D matrix. Also, two matrices of size M × N1 and N2 × M can only be multiplied when N1 = N2.

## The *D > N* Problem

Consider the following simple situation: You have N = 1 and you want to fit y1 ≈ w0 + w_1 x_{11}, i.e. you want to find w = (w0, w1) given one pair (y_1, x_{11}). Is it possible to find such a line?

This problem is related to something called *D > N* problem (in statistics typically named *p > n*). It means that the number of parameters exceeds number of data examples. In other words, we have more variables than we have data information. For many models, such as linear regression, this makes the task *under-determined*. We say that the model is over-parameterized for the task.

Using regularization is a way to avoid the issue described, which we will learn later.