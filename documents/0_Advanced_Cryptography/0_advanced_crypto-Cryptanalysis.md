
## Chapter 5 Cryptanalysis (Conventional)

In this chapter we review some notions of cryptanalysis for block ciphers. More precisely, we describe differential and linear cryptanalysis. We apply it to DES reduced to 8 rounds. Then, we present some theory on the analysis with the notion of distinguisher. We discuss about the optimal one and see how to analyze the security of block ciphers with the notion of decorrelation.

## 5.1 Block Ciphers

One technique for symmetric encryption is based on *block ciphers*. This treats messages by blocks of fixed length, e.g., ℓ bits. Formally, a block cipher is a deterministic algorithm taking as input a plaintext block x *∈ {*0, 1}ℓ and a secret key K and returning y = CK(x), a ciphertext block y ∈ {0, 1}ℓ. It comes with another deterministic algorithm denoted by C−1 such that C−1
K (CK(x)) = x for all x and K. So, for each K, CK is a permutation of the set {0, 1}ℓ.

The *perfect cipher* has 2ℓ! possible keys and is such that every possible permutation over {0, 1}ℓ
has a key defining it. In terms of security, this is the best block cipher that we can dream of. Unfortunately, it is by far impractical as the key would be way too long to be representable. Indeed, we know the Stirling formula

$$n!\sim{\sqrt{2\pi n}}n^{n}e^{-n}$$
which implies that log2(n!) can be approximated by n log2 n when n is large. So, the most efficient binary representation of the keys requires log2(2ℓ!) bits for a key, which is approximately ℓ2ℓ. For
ℓ = 64, which is nowadays considered as a too short block length, we obtain that we need more than one million of Petabytes to store a single key.

Instead of using the perfect cipher, we can still try to make ciphers look like the perfect one for the given usage. For instance, if the cipher is meant to be used only once, it is fair enough to require that for any x, the random variable CK(x), defined over the random choice of the key K, is uniformly distributed.

If the cipher is meant to be used only twice, we can simply require that for any x1, x2 with x1 ̸= x2, (CK(x1), CK(x2)) is uniformly distributed among all pairs (y1, y2) satisfying y1 ̸= y2.

This is the notion of *pairwise independent permutation*.

This generalizes to n*-wise independent permutations*: for all x1*, . . . , x*n which are pairwise different, the tuple (CK(x1)*, . . . , C*K(xn)) is uniformly distributed among all (y1*, . . . , y*n) of pairwise different ciphertext blocks. If a cipher satisfies this criterion and if an adversary gets to learn no more than n pairs (xi, yi), then what he sees has the same distribution as what he would see if C
was the perfect cipher. So, the cipher would ideally look like the perfect one, up to n samples.

## 5.2 Differential Cryptanalysis

Differential cryptanalysis was invented by Eli Biham and Adi Shamir. In 1990 [8], it was used to break some ciphers looking like DES. In 1992 [9], an attack was proposed (with a complexity too high for the technology of that time) against DES. In 1993 [10], it was observed that any slight variant of DES would be subject to a more efficient and actually practical attack. Then, in 1994, Don Coppersmith (one of the designers of DES), released a technical report [16] showing that DES was built to resist to this type of attack. Indeed, this report showed that the technique of differential cryptanalysis was already taken into account by the DES designers in the 70's, even though it was not publicly known.

Differential cryptanalysis is a key recovery attack with *chosen* plaintexts. First, it requires to split the block cipher into three elements: a key schedule transforms K into K1 and K2; X is processed by the core encryption using K1; then the result Z is processed by the post-encryption using K2. This yields Y = CK(X) (see Fig. 5.1). Second, we must find a deviant property of the core encryption of the form Pr[Z′ − Z = b|X′ − X = a] is large, when X and X′ are random, Z
resp. Z′ is the core encryption of X resp. X′, and a and b are constants. Here, we use the XOR
⊕ as a notion of difference. I.e., Z′ − Z = Z′ ⊕ Z and X′ − X = X′ ⊕ X. To find this deviant property, we will use heuristics (see below). Third, we isolate some verifiable information based on Y and Y ′ and a piece of information κ of K2. This is a predicate R(κ, π(*Y, Y* ′)) which is true whenever Z′ ⊕ Z = b and κ is correct, and which is exceptionally true otherwise. The function π
is used to compress Y and Y ′ to the required information needed in order to evaluate R. Finally, we run the attack based on statistics.

Precomputation:
1: initialize SubCandidateu to empty set for all u
2: for all u and all κ such that R(*κ, u*), insert κ in SubCandidateu Collection phase:
3: collect n pairs ((x, y), (x′, y′)) of plaintext-ciphertext pairs, with x′ = x ⊕ a Analysis phase:
4: initialize counters mκ to 0
5: **for** each pair ((x, y), (x′, y′)) do
6:
compute u = π(*y, y*′)
7:
for all κ ∈ SubCandidateu increment mκ
8: end for
9: sort all possible κ in decreasing order of mκ
Search phase:
10: for each sorted κ, exhaustively look for K
In the precomputation phase, we prepare some tables SubCandidateu to quickly yield all possible κ
such that R(*κ, u*) holds. In the collection phase, we collect pairs of pairs (*x, y*) and (x′, y′) such that y = CK(x), y′ = CK(x′), and x′⊕x = a. This is done by chosen plaintext attack. Then, during the analysis phase, we compute u = π(*y, y*′) and increment the counter of each key in SubCandidateu.

Then, we can look at the score of all candidates and sort them by decreasing score. Finally, the search phase will treat each κ in the sorted list as the potential value corresponding to K. The idea is that with enough samples, the highest score will be made by the correct value.

Given a function f mapping p bits to q bits, we define a function DPf by

$\mbox{DP}^{f}(a,b)=\mbox{Pr}[f(X\oplus a)=f(X)\oplus b]$
for a ∈ {0, 1}p, b *∈ {*0, 1}q, and X uniformly distributed in {0, 1}p.

This is the differential probability. Clearly, we have the following properties:

- DPf(0, 0) = 1 and DPf(0, b) = 0 for all b ̸= 0;
b DPf(*a, b*) = 1 for all a;
- P
- 2p × DPf(*a, b*) is an even integer.
The last property comes from the fact that the number of x such that f(x ⊕ a) = f(x) ⊕ b must be even: if x satisfies the relation, then x ⊕ a as well, so all these x's come in pairs. Clearly, the deviant property which is used in differential cryptanalysis can be expressed by DPC′
K1 (*a, b*) being high.

To find the deviant property, we write the block cipher as a computation circuit, we look at the propagation of differences of plaintexts X and X′ in this circuit, and we follow some heuristics.

Clearly, if we have a linear gate M mapping an input X to an output Y , if two inputs are within a difference of ∆X, the resulting outputs will be within a difference of ∆Y = M × ∆X. This can be applied to a duplicate gate mapping X to M ×X = (*X, X*), so M = (1 1)t,1 or to a XOR gate, mapping (*X, Y* ) to M × (*X, Y* ) = X ⊕ Y , so M = (1 1). When crossing a non-linear gate, we look at a plausible difference transform (by studying the differential properties of that gate) and we do the heuristic approximation that the difference propagation through all non-linear gates will be independent. So, we approximate DPCK(*a, b*) by the product of the probabilities that these propagations hold.

For the differential cryptanalysis for DES reduced to 8 rounds (instead of 16), we find a deviant property with a probability close to 2−13.4. We can further show that κ has 30 bits and that each key pair increases the score of 210 counters mκ. We assume that the selection of these counters look like random. So, each counter (for a wrong value) is incremented with probability p2 ≈ 210
230 = 2−20 by each pair, and that the counter for the correct value κ is incremented with probability p1 = 2−13.4. The final score of this value will be np1 on average, where n is the number of pairs. Typically, the distance to the expected value will be of order √np1. This comes from the total score being the sum of n independent, identically distributed, random boolean variables with expected value p1. So, the expected value of the sum is np1 and the standard deviation of the sum is p np1(1 − p1) ≈ √np1. Similarly, the expected value of mκ for a bad κ will be within a distance of √np2 to np2. Clearly, p1 ≫ p2. So, np1 − np2 ≈ np1 and √np1 ≫ √np2. Hence, whenever √np1 ≪ np1, we can separate the good counter from the bad ones and deduce κ (see Fig. 5.2). The condition for this to be the case is thus that n ≫ 1/p1.

## 5.3 Linear Cryptanalysis

In 1990 [30, 60], Henri Gilbert and his colleagues invented a way to break FEAL, a block cipher looking like DES. This inspired Mitsuru Matsui to develop *linear cryptanalysis* in 1993 [42], then
1where (1 1)t denotes the transposed matrix of (1 1)

to successfully apply it to DES in 1994 [43]. His attack is a key recovery *known* plaintext attack requiring 243 known plaintexts.

Like for differential cryptanalysis, it first requires to split the block cipher into three elements:
a key schedule transforms K into K1 and K2; X is processed by the core encryption using K1; then the result Z is processed by the post-encryption using K2 (see Fig. 5.3). This yields Y = CK(X).

Second, we must find a deviant property of the core encryption of the form "
Pr[a · X = b · Z] − 1
2

is large", when X is random, Z is the core encryption of X, a and b are constants, and x · y is the modulo 2 dot product between the vectors x and y. Third, we isolate some way to compute a · X ⊕ b · Z from X, Z, and a piece of information κ of K2. This is a function P(κ, π(*X, Y* ))
which is equal to a · X ⊕ b · Z whenever κ is correct, and which is uniformly distributed otherwise.

Finally, we run the attack based on statistics.

Collection phase:

1: **for** all possible u = π(*x, y*) do
2:
initialize a counter nu to zero
3: end for 4: collect n plaintext-ciphertext pairs (*x, y*) 5: **for** each (*x, y*) do
6:
compute u = π(*x, y*)
7:
increment nu
8: end for
Analysis phase:
9: **for** all possible κ do u s.t. P (κ,u)=0 nu
10:
compute mκ = P
11: end for
12: sort all κ in decreasing order of |mκ − n
2 |
Search phase:
13: for each sorted κ exhaustively look for K
In the collection phase, we just count how many pairs (*x, y*) give π(*x, y*) = u, for each u. Then, for each κ we compute mκ which is how many times P(κ, π(*x, y*)) is equal to 0. Then, we can look at the score of all candidates and sort them by decreasing distance to n
2 . Finally, the search phase will treat each κ in the sorted list at the potential value corresponding to K. The idea is that with enough samples, the highest score will be made by the correct value.

Given a function f mapping p bits to q bits, we define a function LPf by

$$\mathsf{L}\mathsf{P}^{f}(a,b)=\left(2\Pr[a\cdot X=b\cdot f(X)]-1\right)^{2}$$

for $a\in\{0,1\}^{p}$, $b\in\{0,1\}^{q}$, and $X$ uniformly distributed in $\{0,1\}^{p}$. This is the _linear probability_. Clearly, the deviant property which is used in linear cryptanalysis can be expressed by $\mathsf{L}\mathsf{P}^{C_{k}}_{1}(a,b)$ being high.

To find the deviant property $\Pr[a\cdot X=b\cdot Z]$ far from $\frac{1}{2}$, we proceed in a way which is the _dual_ of what we did for differential cryptanalysis, we write the block cipher as a computation circuit.

2, we proceed in a way which is the dual of what we did for differential cryptanalysis: we write the block cipher as a computation circuit, set the output mask b, and follow the computation backward to see what input mask to set. If we have a linear gate M mapping X to Y = MX, we know that

$b\cdot Y=b\cdot(MX)=(M^t b)\cdot X=a\cdot X$
when a = M tb. So, an output mask b to M corresponds to an input mask M tb. When crossing a non-linear gate S with output mask b, we look at the possible masks a making Pr[a·X = b·S(X)]
far from 1
2. We obtain b · S(X) = (a · X) ⊕ B for a biased bit B. When piling up all equations, the final relation around the core encryption looks like

$$(a\cdot X)\oplus(b\cdot Z)=\operatorname{bit}(K)\oplus\bigoplus_{i=1}^{n}B_{i}$$
for some Boolean function bit(K) of the key K and some biases bits Bi corresponding to the non-linear gates. To measure the bias of a random bit B, we define

$$\mathsf{LP}(B)=\left(2\Pr[B=0]-1\right)^{2}$$

Then, we make the _heuristic_ assumption that all $B_{i}$'s are independent${}^{2}$ and apply the following result:
Lemma 5.1 (Piling-up Lemma). Given some independent random bits B1, . . . , Bn, we have

$$\mathsf{LP}(B_{1}\oplus\cdots\oplus B_{n})=\mathsf{LP}(B_{1})\times\cdots\times\mathsf{LP}(B_{n})$$

Proof.: To prove this, we observe that $\mathsf{LP}(B)=\left(E\left((-1)^{B}\right)\right)^{2}$ and apply the properties of independent variables.

It is interesting to see how differential and linear cryptanalysis are dual of each other. On one case, we were doing the computation forward on differences, applying the linear transforms M, computing DP's. On the other case, we were doing the computation backward on masks, applying the transposed linear transforms M t, computing LP's. Unsurprisingly, there is a nice link between DP's and LP's. Actually, one is the *discrete Fourier transform* of the other, which is expressed by the following result.

Theorem 5.2. If f is a function mapping p bit to q bits, we have

α,β (−1)a·α⊕b·βLPf(*α, β*) DPf(*a, b*) = 2−q X a,b (−1)a·α⊕b·βDPf(*a, b*) and LPf(*α, β*) = 2−p X
Proof. We first observe that

LPf(*α, β*) =  E  (−1)(α·X)⊕(β·f(X))2 = E  (−1)(α·(X⊕Y ))⊕(β·(f(X)⊕f(Y )))
where X and Y are independent and uniformly distributed in {0, 1}p. Then, we compute

  α,β (−1)a·α⊕b·βLPf(*α, β*) = E α,β (−1)(α·(a⊕X⊕Y ))⊕(β·(b⊕f(X)⊕f(Y ))) X X 
Given X and Y , the inner sum over α and β is always zero, except if X ⊕Y = a and f(X)⊕f(Y ) =
b, in which case the sum is 2p+q. So, X

α,β (−1)a·α⊕b·βLPf(*α, β*) = 2p+qE  1X⊕Y =a,f(X)⊕f(Y )=b  = 2qDPf(*a, b*) α′,β′ (−1)a·α′⊕b·β′LPf(α′, β′)
which gives the first equation.

To obtain the second, we compute the right-hand side of the equation and replace DFf by the expression we have just got:
X

a,b (−1)a·α⊕b·β X a,b (−1)a·α⊕b·βDPf(*a, b*) = 2−q X a,b (−1)a·(α⊕α′)⊕b·(β⊕β′) α′,β′ LPf(α′, β′) X = 2−q X
The inner sum is zero except for α = α′ and β = β′, for which it is 2p+q. So, this expression is equal to 2p × LPf(*α, β*).

⊓⊔
We could do a complexity analysis of the linear attack method. What we would obtain is that the required number of samples to find the correct κ with good probability has of order of magnitude 1/LPC′
K1 (*a, b*). Again, this is a result similar to the one of differential cryptanalysis where it was the inverse of DPC′
K1 (*a, b*).

## 5.4 Hypothesis Testing In Cryptography

In cryptography, we are often concerned about *distinguishing* if some random samples follow a given distribution P0 or a given distribution P1. Concretely, we have a random source generating independent samples x1*, . . . , x*q following the same distribution P. Then, an algorithm A called a distinguisher analyzes x1*, . . . , x*q and tries to guess whether P = P0 or P = P1. I.e., A(x1*, . . . , x*q)
is a bit. The ability to distinguish P0 from P1 is measured by the notion of *advantage*: we define

$\mbox{Adv}_{\cal A}(P_{0},P_{1})=\Pr[{\cal A}(x_{1},\ldots,x_{q})=1|P=P_{1}]-\Pr[{\cal A}(x_{1},\ldots,x_{q})=1|P=P_{0}]$
We say that P0 and P1 are (*q, ε*)-indistinguishable if for any A limited to q samples, we have |AdvA(P0, P1)| ≤ ε.

In the theory of *hypothesis testing*, A is testing the null hypothesis

$$H_{0}:\quad P=P_{0}$$

against the alternate hypothesis $$H_{1}:\quad P=P_{1}$$.

The frequentist approach studies two types of errors:

- the type I error: α = Pr[A(x1*, . . . , x*q) = 1|P = P0], the error made by A thinking that the
distribution is P1 when it is actually P0;
- the type II error: β = Pr[A(x1*, . . . , x*q) = 0|P = P1] the error made by A thinking that the
distribution is P0 when it is actually P1.
The Bayesian approach rather considers that both hypotheses have a probability $\pi_0$ resp. $\pi_1$ and studies the probability of error $$P_e=\alpha\pi_0+\beta\pi_1$$. 
In the typical case that we will use in this course, we have π0 = π1 = 1
2, so

$$\mathrm{Adv}_{\mathcal{A}}(P_{0},P_{1})=1-2P_{e}=1-(\alpha+\beta)$$
When limited to q = 1 sample a natural way to distinguish P0 from P1 is to take a decision based on whether P0(x) ≤ P1(x): if this inequality holds, then it is more likely that P = P1 so we can output 1. This strategy is actually optimal as we can show. First, we can assume without loss of generality that A is deterministic. So, A is characterized by the set A−1(1) of values of x producing the output 1. We have

$$\mathsf{Adv}_{\mathcal{A}}(P_{0},P_{1})=\sum_{x\in\mathcal{A}^{-1}(1)}(P_{1}(x)-P_{0}(x))$$ $$\leq\sum_{x:P_{1}(x)\subseteq P_{1}(x)}(P_{1}(x)-P_{0}(x))$$ $$=\frac{1}{2}\sum_{x}|P_{1}(x)-P_{0}(x)|$$

with equality when $\mathcal{A}^{-1}(1)=\{x:P_{0}(x)\leq P_{1}(x)\}$, which corresponds to the above natural strategy. Given some real functions $f_{0}$ and $f_{1}$, we define the _statistical distance_ (or $L_{1}$ distance) between $f_{0}$ and $f_{1}$ by

$$d(f_{0},f_{1})=\frac{1}{2}\sum_{x}|f_{1}(x)-f_{0}(x)|$$
We obtain the following result:
Theorem 5.3. For any A *limited to* q = 1 *sample, we have* AdvA(P0, P1) ≤ d(P0, P1).

The equality is reached for the algorithm producing 1 if and only if P0(x) ≤ P1(x).

Proof.: We have already proven the inequality. To study the equality case, we have to see what it implies in the proof for inequality. Clearly, equality implies that

$$\sum_{x\in A^{-1}(1)}(P_{1}(x)-P_{0}(x))=\sum_{x:P_{0}(x)\leq P_{1}(x)}(P_{1}(x)-P_{0}(x))$$
which means that A−1(1) contains all x such that P0(x) *< P*1(x) and maybe some extra x such that P0(x) = P1(x).

⊓⊔

Given a distribution $P$ on values $x$ and an integer $q$, we define $P^{\otimes q}$ a distribution on $q$-tuples of values $(x_{1},\ldots,x_{q})$ by

$$P^{\otimes q}(x_{1},\ldots,x_{q})=P(x_{1})\cdots P(x_{q})$$
We can see the general case as a particular case of the q = 1 one: q samples can be considered as one sample of a q-tuple! So, we obtain the following result [2]:
Theorem 5.4. For any A limited to q *independent samples, we have* AdvA(P0, P1) ≤ d(P ⊗q
0
, P ⊗q
1
).

The equality is reached for the algorithm producing 1 if and only if P0(x1) · · · P0(xq) ≤ P1(x1) · · · P1(xq).

One remaining question is the following: how large must be q so that d(P ⊗q
0
, P ⊗q
1
) is significant for cryptanalysis? We can easily show by induction that d(P ⊗q
0
, P ⊗q
1
) ≤ qd(P0, P1). So, we need at least q > 1/d(P0, P1), but it is not guaranteed that this would be enough. In what follows, we want to have a more precise estimate, based on some notions from the theory of large deviations.

Given a sample vector x = (x1*, . . . , x*q), we define the *observed distribution* (which is sometimes called a *type*) Px by Px(y) = 1
q#{i : xi = y}. Given two distributions P0 and P1, we define the Kullback-Leibler divergence

$$D(P_{0}\|P_{1})=\sum_{x\in\operatorname{Supp}(P_{0})}P_{0}(x)\log{\frac{P_{0}(x)}{P_{1}(x)}}$$
where the log is in basis 2. Although this is not symmetric, this is very similar to a notion of distance: it is non-negative and equal to 0 if and only if P0 = P1. We define

$$\Pi=\{P:D(P\|P_{1})\leq D(P\|P_{0})\}$$
the set of distributions which are "closer" to P1 than to P0. We can easily see that the strategy from the above theorem outputs 1 if and only if the observed distribution of x = (x1*, . . . , x*q) is in
Π. Indeed,

$$D(P_{x}||P_{1})-D(P_{x}\|P_{0})=\sum_{y\in\mathsf{Supp}(P_{x})}P_{x}(y)\log\frac{P_{0}(x)}{P_{1}(x)}=\frac{1}{q}\sum_{i=1}^{q}\log\frac{P_{0}(x_{i})}{P_{1}(x_{i})}=\frac{1}{q}\log\frac{P_{0}(x_{1})\cdots P_{0}(x_{q})}{P_{1}(x_{1})\cdots P_{1}(x_{q})}$$
We can take some simple examples.

- For the distribution of a coin flip (head or tail) with P0 being uniform and P1 being biased,
e.g. P1(head) = 1
2(1 + ε), if qhead and qtail are the number of occurrences in i.i.d. samples,
the likelihood ratio is less than 1 if and only if qhead log(1 + ε) + qtail log(1 − ε) ≥ 0. This is
roughly equivalent to qtail *< q*head.
- If P0 is uniform over a set A ⊂ B and P1 is uniform over the set B, the likelihood ratio is
less than 1 if and only if all samples belong to A.
- Using normal distributions, if P0 = N(*µ, σ*) and P1 = N(µ′, σ), the likelihood ratio for one
sample is computed using the pdf:
$$\varphi_{\mu,\sigma}(x)={\frac{1}{\sqrt{2\pi}}}e^{-{\frac{(x-\mu)^{2}}{2\sigma^{2}}}}$$
2
.

The likelihood ratio is less than 1 if and only if x ≥ µ+µ′

- Using n i.i.d. samples of Bernoulli variables of expected value p0 or p1, with p0 ≈ p1 and
p0 *< p*1, the vector of samples is equivalent to their sum. Their sum can be approximated to a normal distribution of expected value npb and standard deviation σb =
p
n − Pb(1 − pb),
for b = 0, 1. Using σ0 ≈ σ1, the previous case says that the likelihood ratio is less than 1 if
and only if x
2
.
n ≥ p0+p1

## 5.5 Decorrelation

We assume that a distinguisher is given access to an oracle implementing some random function from a set A to a set B. We know that either it has the distribution of a random function F or a distribution of an ideal random function F ∗. For instance, F is a random cipher C (set up with a random key) on the set A (and B = A) and F ∗ is the perfect cipher C∗ over A. As another example, F is a function defined by a MAC with a random key and F ∗ is a uniformly distributed random function. We assume that the distinguisher is limited with the number of queries q that he can make. The distinguisher is not limited in complexity.

Given a random function F from A to B and an integer q, we define a (huge) real matrix [F]q in which rows have an index corresponding to a tuple x = (x1*, . . . , x*q) of q inputs and columns have an index corresponding to a tuple x = (y1*, . . . , y*q) of q outputs.

The element [F]q x,y at position (*x, y*) is the real number Pr[F(x1) = y1*, . . . , F*(xq) = yq]. Decorrelation to the order q is the distance between [F]q and [F ∗]q.

It is convenient to define the distance in terms of a matrix norm. Matrix norms are norms (i.e.,
∥M∥ is always positive, equal to 0 if and only if M = 0, ∥λM∥ = |λ*| × ∥*M∥, and ∥M + M ′∥ ≤
∥M∥+∥M ′∥) with the additional property that ∥MM ′∥ ≤ ∥M∥×∥M ′∥. For instance, the ∞-norm over the vectors ∥v∥∞ = maxy |vy| induces a companion matrix-norm

y |Mx,y| |||M|||∞ = max ∥v∥∞≤1 ∥Mv∥∞ = max x X
This norm bridges the theory of decorrelation with the theory of best non-adaptive distinguishers as the following result shows. A distinguisher is non-adaptive if it prepares all its queries at once.

Namely, it does not adapt a query xi based on the response from previous queries.

Theorem 5.5 ([62]). For any random functions F and G, the best advantage of a non-adaptive distinguisher between F and G, limited to q *queries, is equal to* 1
2|||[F]q − [G]q|||∞.

Proof. A non-adaptive distinguisher can be assumed to prepare the q queries x1*, . . . , x*q before making any query. Then, he obtains a vector (Y1*, . . . , Y*q) of random variables defined by Yi = F(xi) in the F case and Yi = G(xi) in the G case. So, this reduces to distinguish the distributions of (F(x1)*, . . . , F*(xq)) and (G(x1)*, . . . , G*(xq)). We know from Th. 5.3 that the best advantage is half of the statistical distance between the two distributions, hence

$$\text{Adv}=\frac{1}{2}\sum_{y_{1},\ldots,y_{q}}|\text{Pr}[F(x_{1})=y_{1},\ldots,F(x_{q})=y_{q}]-\text{Pr}[G(x_{1})=y_{1},\ldots,G(x_{q})=y_{q}]|$$
The best advantage over the choice of x1*, . . . , x*q is

$$\text{Adv}=\frac{1}{2}\max_{x_{1},\ldots,x_{q}}\sum_{y_{1},\ldots,y_{q}}|\text{Pr}[F(x_{1})=y_{1},\ldots,F(x_{q})=y_{q}]-\text{Pr}[G(x_{1})=y_{1},\ldots,G(x_{q})=y_{q}]|$$
which is 1
2|||[F]q − [G]q|||∞.

⊓⊔
To compute the advantage of a distinguisher which can be adaptive, we use the norm

$$||M||_{a}=\operatorname*{max}_{x_{1}}\sum_{y_{1}}\cdot\cdot\cdot\operatorname*{max}_{x_{q}}\sum_{y_{q}}|M_{((x_{1},...,x_{q}),(y_{1},...,y_{q}))}|$$
This is indeed a matrix norm [62]. Just like the previous theorem, we can prove the following result. Theorem 5.6 ([62]). For any random functions F and G, the best advantage of a distinguisher between F and G, limited to q *queries, is equal to* 1
2∥[F]q − [G]q∥a.

Decorrelation enjoys the following property.

Theorem 5.7 ([62]). If C1 and C2 are independent random permutations, to be compared with a uniformly distributed random permutation C∗, for any matrix norm, we have that

∥[C2 ◦ C1]q − [C∗]q∥ ≤ ∥[C1]q − [C∗]q∥ × ∥[C2]q − [C∗]q∥
Proof. We first observe that [C2 ◦ C1]q = [C1]q × [C2]q.

Then, we notice that [C∗]q has an absorbing property.

Indeed, [C1]q × [C∗]q is equal to
[C∗ ◦ C1]q.

Since C∗ and C1 are independent, in the group of permutations, and that C∗ is uniformly distributed, C∗ ◦ C1 and C∗ have the same distribution. So, [C∗ ◦ C1]q = [C∗]q from which we deduce [C1]q × [C∗]q = [C∗]q. We similarly show that [C∗]q × [C2]q = [C∗]q.

Now, we have
([C1]q − [C∗]q) × ([C2]q − [C∗]q) = [C2 ◦ C1]q − [C∗]q by expanding the product, thanks to the absorbing property of [C∗]q. Due to the matrix norm multiplicative property, we have

∥[C2 ◦ C1]q − [C∗]q∥ ≤ ∥[C1]q − [C∗]q∥ × ∥[C2]q − [C∗]q∥ ⊓⊔
We can apply this result on the Luby-Rackoff Theorem.

Theorem 5.8 (Luby-Rackoff 1986 [41]). Let F ∗
                                          1 , F ∗
                                             2 , F ∗
                                                3 be three independent round functions
with uniform distributions from the set of ℓ

2 .

                                               2-bit strings to itself. We consider the 3-round Feistel
scheme C = Ψ(F ∗
                  1 , F ∗
                      2 , F ∗
                           3 ) to be compared with the ideal cipher C∗. For all distinguisher limited
to q queries, the advantage to distinguish C from C∗ is bounded by q2.2− ℓ

Proof. We split an input xi into xi = (z0
                                        i , z1
                                            i ). Similarly, we split and output yi = (z4
                                                                                      i , z3
                                                                                         i ). We
further define z2
               i = z0
                     i ⊕ F ∗
                           1 (z1
                              i ). Clearly, xi maps to yi if and only if z3
                                                                           i = z1
                                                                                 i ⊕ F ∗
                                                                                      2 (z2
                                                                                          i ) and
z4
 i = z2
      i ⊕F ∗
           3 (z3
              i ) (see Fig. 5.4). Let E be the event that for i = 1, . . . , q, we have z3
                                                                                 i = z1
                                                                                      i ⊕F ∗
                                                                                           2 (z2
                                                                                              i )
and z4
     i = z2
          i ⊕ F ∗
                3 (z3
                   i ). We obtain that [C]q
                                          x,y = Pr[E].
   Let Y be the set of all y = (y1, . . . , yq) such that for all i ̸= j, yi and yj define some z3
                                                                                        i and z3
                                                                                               j
such that z3
           i ̸= z3
                j . If we take a uniformly distributed random y, the probability that it is not in

2 . So, we have

2
    times Pr[z3
               i = z3
                     j ] = 2− ℓ

Y is Pr[∃i < j z3
          i = z3
             j ]. This is bounded by q(q−1)

$$\operatorname*{Pr}[y\in{\mathcal{Y}}]\geq1-\varepsilon$$
with ε = q(q−1)
2
2− ℓ
2 .

Let x be arbitrary and let y *∈ Y* be arbitrary but in Y. We define the event E2 that all z2
i are pairwise different. Just like above, we have Pr[E2] ≥ 1 − ε. Then, we have

[C]q x,y = Pr[E] ≥ Pr[*E, E*2] = Pr[E|E2] Pr[E2]

If the z2
       i are pairwise different, the F ∗
                                        2 (z2
                                            i ) are uniform and independent. Since we also know that
the z3
     i are pairwise different, the F ∗
                                     3 (z3
                                        i ) are also uniform and independent. Hence Pr[E|E2] = 2−ℓq.
We deduce
                                 [C]q
                                     x,y ≥ (1 − ε)2−ℓq = (1 − ε)[F ∗]q
                                                                       x,y

   Therefore, we have found a set Y such that Pr[y ∈ Y] ≥ 1 − ε and [C]q
                                                                       x,y ≥ (1 − ε)[F ∗]q
                                                                                        x,y for
all y ∈ Y. By applying Lemma 5.9 below, we deduce that the best advantage to distinguish C
(denoted by F in Lemma 5.9) from F ∗ limited to q queries is bounded by 2ε = q(q − 1)2− ℓ

                                                                                                                    2 .
    In Lemma 5.10, we show that the best advantage to distinguish C∗ from F ∗ is bounded by
q2

2 2−ℓ. For q ≤ 2
                  ℓ
                  2 , the sum is bounded by q2− ℓ

2 . For q ≥ 2
                ℓ
                2 , it is bounded by 1, so by q2− ℓ

                                                                                                                       2 as
well. So, the best advantage to distinguish C from C∗ limited to q queries is bounded by q22− ℓ

                                                                                                                          2 .
For q larger, this bound is larger than 1 so the advantage is also bounded by this.
                                                                                                                          ⊓⊔

The lemma below is inspired by Patarin's "H coefficient technique" [46].

Lemma 5.9. Let F be a random function from a set M1 to a set M2. We let X be the subset
of Mq
    1 of all (x1, . . . , xq) with pairwise different entries. We let F ∗ be a uniformly distributed
random function from M1 to M2. We assume there exists a subset Y ⊆ Mq
                                                          2 and two positive
numbers ϵ1 and ϵ2 such that

•
#Y
#Mq
2 ≥ 1 − ϵ1
#Mq
2 (1 − ϵ2).
- ∀x ∈ X
∀y ∈ Y
[F]q
x,y ≥
1
Then the best advantage to distinguish F from F ∗ limited to q queries is bounded by ϵ1 + ϵ2.

Proof. We know that for all x *∈ X* and y ∈ Mq
2 we have [F ∗]q x,y = p0 for the constant p0 =
(#M2)−q.

Without loss of generality, the best distinguisher is deterministic. Let xi be its ith query and yi the response from the oracle. (Note that xi can depend on y1*, . . . , y*i−1.) Let A be the set of all y1*, . . . , y*q making the distinguisher output 1. We assume without loss of generality that x ∈ X
(if a query repeats, we can replace it by an arbitrary new one and substitute the answer to the previously known answer of the repeating query). The advantage is

y∈A Adv = X  [F ∗]q x,y − [F]q x,y 

For y ∈ Y, we have [F ∗]q
                     x,y − [F]q
                             x,y ≤ ε2[F ∗]q
                                       x,y. Otherwise, we use [F ∗]q
                                                                x,y − [F]q
                                                                       x,y ≤ [F ∗]q
                                                                                x,y. So,

y̸∈Y [F ∗]q x,y ≤ ε2 + Pr[y *̸∈ Y*] ≤ ε1 + ε2 Adv ≤ ε2 X y∈A,y∈Y [F ∗]q x,y + X y∈A,y̸∈Y [F ∗]q x,y ≤ ε2 X y∈Y [F ∗]q x,y + X ⊓⊔
It is interesting to look at the structure of the [C∗]x,y matrix. We note by Part(x) the partition of {1*, . . . , q*} such that i and j are in the same class if and only if xi = xj. When Part(x) ̸=
Part(y), we have [C∗]x,y = 0. When Part(x) = Part(y) and there are exactly m classes, then
[C∗]x,y =
1
2ℓ(2ℓ−1)···(2ℓ−m+1). Contrarily, if each class in Part(x) is a subset of a class of Part(y), we have [F ∗]x,y = 2−mℓ. Otherwise, [F ∗]x,y = 0. Below, we bound the distance between [C∗]x,y and [F ∗]x,y.

Lemma 5.10. Let F ∗ be a uniformly distributed function from a set M to itself. Let C∗ be a uniformly distributed permutation on M. The best advantage to distinguish C∗ from F ∗ limited to q *queries is bounded by* q(q−1)
2|M| .

Proof. Let A be a distinguisher limited to q queries. We assume w.l.o.g. that A never repeats a query. Let xi be the ith query.

Conditioned to the event E that no F(xi) collide, the distribution of (F(x1)*, . . . , F*(xq))|E and
(C(x1)*, . . . , C*(xq)) are identical. So,

$\Pr[\mathcal{A}^{F}=1]-\Pr[\mathcal{A}^{C}=1]\leq\Pr[\mathcal{A}^{F}=1|E]-\Pr[\mathcal{A}^{C}=1]+\Pr[\neg E]=\Pr[\neg E]$.

by using the property

$$\Pr[A]=\Pr[A,E]+\Pr[A,\neg E]\leq\Pr[A|E]\Pr[E]+\Pr[\neg E]\leq\Pr[A|E]+\Pr[\neg E]$$

Then, we have $\Pr[\neg E]\leq\sum_{1\leq i<j\leq q}^{q}\Pr[F_{i}(x_{i})=F(x_{j})]=\frac{q(q-1)}{2}2^{-\ell}$. 

The Luly-Rackoff Theorem is not so usable in this form s attributed functions $F^{i}$. If we have some independent function 

   The Luby-Rackoff Theorem is not so usable in this form since we don't have uniformly dis-
tributed functions F ∗
                   i .
                       If we have some independent functions F1, F2, F3 such that
                                                                                   1
                                                                                   2∥[Fi]n −
[F ∗
  i ]n∥a ≤ ε, we obtain

1 2∥[Ψ(F1, F2, F3)]n − [C∗]n∥a ≤ 1 2∥[Ψ(F1, F2, F3)]n − [Ψ(F ∗ 1 , F2, F3)]n∥a + 1 2∥[Ψ(F ∗ 1 , F2, F3)]n − [Ψ(F ∗ 1 , F ∗ 2 , F3)]n∥a + 1 2∥[Ψ(F ∗ 1 , F ∗ 2 , F3)]n − [Ψ(F ∗ 1 , F ∗ 2 , F ∗ 3 )]n∥a + 1 2∥[Ψ(F ∗ 1 , F ∗ 2 , F ∗ 3 )]n − [C∗]n∥a
Each of the first three terms in the sum can be considered as the advantage of a distinguisher between Fi and F ∗
i , respectively, so they can be bounded by ε. We thus obtain

$$\frac{1}{2}\|[\Psi(F_{1},F_{2},F_{3})]^{n}-[C^{*}]^{n}\|_{a}\leq3\varepsilon+n^{2}.2^{-\frac{\ell}{2}}$$
Now, we can use the amplification result and obtain the following theorem.

Theorem 5.11 ([62]). Let F1, . . . , F3r be 3r independent round functions such that
                                                                         1
                                                                         2∥[Fi]n −
[F ∗
 i ]n∥a ≤ ε. We consider the 3r-round Feistel scheme C = Ψ(F1, . . . , F3r) to be compared with
the ideal cipher C∗. For all distinguisher limited to q queries, the advantage to distinguish C from
C∗ is bounded by 1

2
 
   2q2.2− ℓ

2 + 6ε
       r
          .

Proof. We have already proven the r = 1 case. We note that C is the product of r independent 3-
round Feistel ciphers. So by using Th. 5.7, we conclude by the equivalence between best advantage
and decorrelation (Th. 5.6).
                                                                                               ⊓⊔

If we wanted to apply this to DES, we would have ℓ = 64. Even in some ideal case with n ≤ 215

and ε = 0, we obtain a distinguisher with advantage bounded by 2−7 for 18 rounds. This is not a
good security result.
  However, we could apply the theorem with q = 2 and obtain interesting results. Namely, every
distinguisher limited to two queries has an advantage bounded by 1

2
 
   6ε + 8.2− ℓ

                                                                                                    2
                                                                                                      r
                                                                                                         . Applying this
to linear and differential distinguishers with a single iteration, we deduce that for every a and b,
E(DPC(a, b)) and E(LPC(a, b)) are low. Namely, we have the following result.

Theorem 5.12 ([62]). For a ̸= 0 and b ̸= 0, we have

$$E({\sf DP}^{C}(a,b))\leq\frac{1}{2^{\ell}-1}+\frac{1}{2}||||C|^{2}-[C^{*}]^{2}||_{\infty}$$ $$E({\sf LP}^{C}(a,b))\leq\frac{1}{2^{\ell}-1}+2||||C|^{2}-[C^{*}]^{2}||_{\infty}$$
So, decorrelation theory can already be used to show that there is no good E(DPC(*a, b*)) and E(LPC(*a, b*)) for differential or linear cryptanalysis.

*Proof.* We write $$E(\mathsf{DPC}^C(a,b))=2^{-\ell}\sum_{x_1,x_2,y_1,y_2}1_{x_2\oplus x_1=a,y_2\oplus y_1=b}[C]^2_{x,y_1}$$ So, we (easily) deduce that $E(\mathsf{DPC}^{\prime\prime}(a,b))=\frac{1}{2^{\ell}-}$. 
2ℓ−1.

We consider the non-adaptive distinguisher picking x1 and x2 of difference a then querying x1
and x2 to obtain y1 and y2 and producing 1 if and only if y2 ⊕ y1 = b. Clearly, the advantage is E(DPC(a, b)) −
1
2ℓ−1. Due to the equivalence between advantage and decorrelation, we have

$$E(\mathsf{D P}^{C}(a,b))-{\frac{1}{2^{\ell}-1}}\leq{\frac{1}{2}}||||[C]^{2}-[C^{*}]^{2}||||_{\infty}$$
For the LP, we use the Fourier transform:

$$E({\sf LP}^{C^{*}}(\alpha,\beta))=2^{-\ell}\sum_{a,b}(-1)^{a\cdot\alpha\oplus b\cdot\beta}E({\sf DP}^{C^{*}}(a,b))$$ $$=2^{-\ell}+2^{-\ell}\sum_{a,b\neq0}(-1)^{a\cdot\alpha\oplus b\cdot\beta}\frac{1}{2^{\ell}-1}$$ $$=\frac{1}{2^{\ell}-1}$$
then

$$E\left(\mathsf{L}\mathsf{P}^{C}(a,b)\right)=E\left(\left((-1)^{a\cdot x\oplus b\cdot C(x)}\right)^{2}\right)$$ $$=E\left((-1)^{a\cdot x_{1}\oplus b\cdot C(x_{1})}(-1)^{a\cdot x_{2}\oplus b\cdot C(x_{2})}\right)$$ $$=E\left((-1)^{a\cdot(x_{1}\oplus x_{2})\oplus b\cdot(C(x_{1})\oplus C(x_{2}))}\right)$$ $$=E\left(2\times1_{a\cdot(x_{1}\oplus x_{2})=b\cdot(C(x_{1})\oplus C(x_{2}))}-1\right)$$ $$=2\left(2^{-2\ell}\sum_{x_{1},x_{1},y_{1},y_{2}}1_{a\cdot(x_{1}\oplus x_{2})=b\cdot(y_{1}\oplus y_{2})}[C]_{x,y}^{2}\right)-1$$
so

$$E\left(\mathsf{L}\mathsf{P}^{C}(a,b)\right)-\frac{1}{2^{\ell}-1}=E\left(\mathsf{L}\mathsf{P}^{C}(a,b)\right)-E\left(\mathsf{L}\mathsf{P}^{C^{*}}(a,b)\right)$$ $$=2\times2^{-2\ell}\sum_{x_{1},x_{1},y_{1},y_{2}}1_{a\cdot(x_{1}\oplus x_{2})=b\cdot(y_{1}\oplus y_{2})}\left([C]^{2}_{x,y}-[C^{*}]^{2}_{x,y}\right)$$ $$\leq2\max_{x_{1},x_{2}}\sum_{y_{1},y_{2}}\left|[C]^{2}_{x,y}-[C^{*}]^{2}_{x,y}\right|$$ $$=2||[C]^{2}-[C^{*}]^{2}||_{\infty}$$
⊓⊔
As an application, we can consider the DFCv2 cipher, which is an 8-round Feistel scheme for which was can prove |||[C]2 − [C∗]2|||∞ ≤ 2−115.