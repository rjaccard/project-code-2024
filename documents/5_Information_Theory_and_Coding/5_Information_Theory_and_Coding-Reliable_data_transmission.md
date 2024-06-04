# Lecture 10 Bis: Reliable Data Transmission

So far, we have learned how to efficiently represent data and compress it whilst maintaining all its statistic properties. Now, we will introduce a new, yet related topic, which involves communicating this data accross a given communication channel.

## 1 Reliable Transmission Of Information 1.1 Introduction

Suppose we wish to transmit a single bit X *∈ {*0, 1} over a communication channel. The scheme can be seen on the figure below:
When we transmit a bit x, with probability 1 − p we get the same bit on the other side, and with probability p we get something else that we will call the error bit e. This scenario is commonly called the Binary Erasor Channel (BEC(p)). We can thus write that the received bit will be

$Y=\begin{cases}x&\text{w.p.}1-p\\ e&\text{w.p.}p.\end{cases}$

We can also have another scenario where instead of generating an unknown bit e, we can write the opposite one. Namely, when a bit x is sent, it is received correctly with probability 1 − p and the opposite is received with probability p. In general, the channel is described by |X| probability distributions on Y , one for each x ∈ X. We denote this p(Y |X).

## 1.2 Definitions

Memoryless and stationary channels : To describe the behaviour of the channel when it is fed a sequence x1, x2, . . ., we need to specify more information. Namely, p1(Y1|X1), p2(Y2|X2, X1, Y1), p3(Y3|X3, X2, X1, Y2, Y1), . . ., pn(Yn|Xn, Y^{n−1}, X^{n−1}), . . .

Definition 1 : A channel is called memoryless if
$$p_{n}(Y_{n}|X_{n},Y^{n-1},X^{n-1})=p_{n}(Y_{n}|X_{n})$$

Definition 2 : A memoryless channel is also called stationary if
$$p_{n}(Y_{n}|X_{n},Y^{n-1},X^{n-1})=p_{(}Y_{n}|X_{n})$$

Notice the disappearance of the subscript n in the second definition. This essentially means that the way the channel handles random variables will not change over time. 

Feedback channels : The last part of the process when sending information accross a communication channel is the feedback. In this part, the receiver will communicate a feedback to the sender who will take it into account for the remainder of the communication process. This allows the sender to be sure that the receiver has received the message and understood it the way the sender wanted it to be. In a particular channel, p(x1), p(x2|x1), p(x3|x2, x1)*, . . .* are the x's without feedback. And, p(x1), p(x2|x1, y1), p(x3|x2, x1, y2, y1)*, . . .* are the x's with feedback. This means that the xi's are based both on the previous inputs and the previous outputs.

Theorem 3 : If we have a memoryless channel used without feedback, then
$Pr(Y^{n}=y^{n}|X^{n}=x^{n})=\prod_{i=1}^{n}Pr_{i}(Y_{i}|X_{i})$.
