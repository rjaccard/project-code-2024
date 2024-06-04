# Lecture 6: Review Of Stochastic Theory And Entropy Rate

In today's lecture, we will recall a few important notions from stochastic processes and talk about entropy rate. Ultimately, we will introduce the notion of typicality and typical sets.

## 1 Data Processing Theorem

The data processing inequality is an theoretical concept in information theory which states that the information content of a signal cannot be increased via a local physical operation. In other words, *post-processing cannot increase information*. The theorem is stated as follows:

**Theorem 1**: _Suppose three independent random variables $U$, $V$ and $W$ form a Markov chain $U$-$V$-$W$. Then_
$$I(U;W)\leq I(U;V).$$

## 2 Entropy Rate And Random Processes

Recall that \frac{1}{n} H(U1, . . . , Un) ± ϵ_n with ϵ_n → 0 appeared as both upper and lower bounds on the number of bits per letter necessary/sufficient to represent (U1, . . . , Un).

## 2.1 Entropy Rate

Definition 2 : Given an information source (i.e. a random process, an infinite sequence of random variables), we define its **entropy rate** as

$\lim\limits_{n\to\infty}\frac{1}{n}H(U_{1},\ldots,U_{n})=H(U)$.
provided that the limit exists. 

The question that arises from the above definition is: for what source of random processes does the entropy rate exist ?

## 2.2 Examples Of Entropy Rate Values

Let us provide some examples, which will require some review of stochastic processes.

Suppose U1, U2*, . . .* are i.i.d random variables, then
$$H(U_{1},\ldots,U_{n})=H(U_{1})+H(U_{2}|U_{1})+\ldots+H(U_{n}|U^{n-1})$$ $$=H(U_{1})+H(U_{2})+\ldots+H(U_{n})\text{by independence}$$ $$=nH(U_{1})\text{as they are i.i.d.},$$
so the limit exists and equals H(U1).