
## Chapter 1 The Cryptographic Zoo 1.1 The Menagery

Cryptographic primitives.

Cryptographic primitives are described by

- components (parameters, participants in protocols, algorithms, domains, etc); - a functionality (describing what happens if all participants play their role in an honest
manner);
- security properties (describing what shall *not* happen if some participants are malicious, this
is typically not easy to formalize).
The functionality often comes with a notion of *correctness*. This notion assumes honest participants and executions. Contrarily, security notions follow some model involving an *adversary* who behaves maliciously.

Confidentiality is addressed by *encryption*, may it be symmetric or not. If it is symmetric, the same key is used to encrypt and to decrypt. So, it must remain secret. If it is asymmetric, a key pair is generated and the encryption key can be publicly revealed.

Message authentication and integrity are addressed by MAC (message authentication codes)
- with a symmetric key - or by *digital signatures* - with a key pair, the verifying key becoming public.

Probabilistic algorithms sometimes need to flip a coin to make a decision. For convenience, we write A(x; r) to say that A runs on input x with a prepared sequence of random coins r. The sequence r must be large enough for A to complete. In this notation, r is separated from the regular inputs by a semicolon.

To formally define what it means to say that a computation is "easy" or "hard", we commonly refer to the notion of a polynomially bounded algorithm. A computation is easy if it can be done by an algorithm which runs in a time O(sn) for some integer n, depending on a parameter s.

Normally, this parameter s is called the *security parameter*. As "polynomially bounded" usually refers to a polynomial in terms of the input length, we provide s written in unary (we write it 1s)
to make sure that the length is s (and not log2 s). So, to be precise, we write A(1s, x; r) but it is more convenient to take 1s implicit and omit it from the notation. A similar asymptotic notion is the one of *negligible* measures. We say that a function f(s) is negligible (implicitly: as s goes to infinity), if for every integer n we have that f(s) = O(s−n).

Participants running the cryptographic primitives are probabilistic polynomially bounded (PPT)
algorithms, in terms of the security parameter s. This also includes adversaries. We say we use the computationally bounded adversarial model. However, we may sometimes assume no complexity bound and use the *information theoretic adversarial model*.

Symmetric encryption schemes.

The components of symmetric encryption schemes are: a key length (the security parameter), the plaintext domain (it can be messages of the same specified length, e.g.

for block ciphers, or messages of variable length), the key domain, and a nonce domain if applicable (typically, for stream ciphers), two participants (a sender and a receiver), and three algorithms: a key generator (it is quite often implicit: it consists of picking a key in the key domain with uniform distribution), an encryption algorithm, and a decryption algorithm.

The functionality specifies that for every message X, Pr[DecK(EncK(X)) = X] = 1 over the distribution of K. The security must formalize the notion of *confidentiality*.

Typically, a symmetric encryption is required to be length-preserving in the sense that the plaintext and the ciphertext always have equal lengths.

However, some modes of encryption providing authentication at the same time require to stretch a bit. The ciphertext typically consists of a part of same length as the plaintext which is concatenated to a tag of length determined by the security level.

Message authentication codes (MAC).

The description of a message authentication code is similar. Typically, a message X is sent by appending a tag MACK(X). To authenticate X, one sends AuthK(X) = X∥MACK(X). Upon reception, the same operation is performed and compared with the received tag. To verify X∥t, one executes CheckK(*X, t*) which checks that t = MACK(X)
and produces X as an output. The security corresponds to the notions of message authentication and message integrity.

The goal of an adversary could be to recover the key (*key recovery*), to forge the valid tag of some random X (*universal forgery*), or to forge the valid tag of some particular message (existential forgery). Its capabilities could be to collect authenticated messages or to choose the message to be authenticated. The stronger security model is the resistance to existential forgeries under chosen message attacks.

Public-key cryptosystems.

In a public-key cryptosystem, a key generator produces a key pair (pk, sk). An encryption algorithm is probabilistic. A decryption algorithm is deterministic.

The functionality says that Decsk(Encpk(X)) = X with probability 1. Security works like in the symmetric case, except that the minimal adversarial capabilities are chosen plaintext attacks, since the adversary can do the encryption by himself by using the public key.

Digital signature schemes.

In a digital signature scheme, a key generator produces a key pair (pk, sk). A signing algorithm is probabilistic. A verifying algorithm is deterministic. The functionality says that Verpk(X, Sigsk(X)) = ok with probability 1. Security formalizes the notion of *non-repudiation*: a signer who signed a document cannot later claim that he did not sign. This implies that signatures are *unforgeable*, otherwise, the signer can claim that the signature was forged. We have similar security models as for message authentication codes.

Key agreement protocols.

A key agreement protocol is an interactive protocol between two participants called Alice and Bob. The two algorithms use no input and produce one output K. The correctness notion is that both outputs K are equal when there is no malicious behavior. The security informally means that no adversary looking at the protocol messages can infer K.

Key agreement protocols do not resist to *man-in-the-middle attacks* in which the adversary simulates one participant to the other. They should resist to *passive adversaries* who only look at communication without interfering with.

Commitment schemes.

A commitment scheme can be described by a single probabilistic function Commit(X; r) taking the input X and the coins r. The commitment protocol between a sender and a receiver uses only one input X (which is on the sender side) and produces only one output X (which is on the receiver side). It works in two phases: in the commitment phase, the sender with input X picks r and sends c = Commit(X; r) to the receiver; in the opening phase, the sender reveals X and r, the receiver checks that c = Commit(X; r) and outputs X. Security should capture the notion of a *hiding* commitment (i.e., the receiver has no clue about X before the opening phase) and of a *binding* commitment (i.e., the sender cannot open the commitment on two different values X). This should be equivalent to putting a document X in a safe c closed with a key r, then giving the safe to the receiver, then handing out the key r to open it.

Pseudorandom number generators (PRNG).

A PRNG can be defined by an algorithm mapping a state (seed) to a new state (new seed) and a generated number. There exists several security notions. One of these is the notion of *unpredictability*: an adversary receiving a sequence of generated numbers cannot predict with good probability what will be the next generated number. Another notion is the one of *indistinguishability*: an adversary producing a bit given a sequence of number produces X, when the sequence consists of generated numbers, and Y , when the sequence consists of truly random numbers. The advantage of the adversary is Pr[X = 1] − Pr[Y = 1]. For indistinguishability, we need that all adversaries have a negligible advantage. Hash functions.

A hash function can be used to construct a commitment scheme, a pseudorandom generator, a *key derivation function (KDF)*, or to expand the domain of a primitive (e.g., a signature scheme). Since there are so many ways to use hash functions, there are also many different security notions. We can consider resistance to *first preimage attacks* (given y, find x such that H(x) = y), to *second preimage attacks* (given x, find x′ ̸= x such that H(x) = H(x′)), and to *collision attacks* (find x and x′ such that x ̸= x′ and H(x) = H(x′)).

## 1.2 The Math Toolbox

Finite Abelian groups.

We work with finite Abelian groups. I.e., finite sets with an operation such that the set is closed under the operation, the operation is associative, there exists a neutral element, all elements are invertible, and the operation is commutative. Examples are Zn, Z∗
p, GF(q)∗, and the elliptic curve Ea,b(K) for a finite field K.

Since there is a single operation, we have groups with additive notations (e.g., the neutral element is 0, and we consider multiplying an integer n with a group element a by n.a = a+*· · ·*+a)
and groups with multiplicative notations (e.g., the neutral element is 1, and we consider raising a group element a to the power of an integer n by an = a *× · · · ×* a).

Groups can be constructed in many ways. Given a big group, we can consider smaller groups
(subgroups) generated by some elements. We can make the product of groups, raise a group to some power, and make the quotient of an Abelian group by one of its subgroups.

The order of a group is its cardinality. The order of an element x is the order of the group it generates. It is also the smallest *n >* 0 such that xn = 1 (with multiplicative notations). The group exponent is the smallest *n >* 0 such that xn = 1 for every element x. The order of an element divides the exponent of the group. The Lagrange theorem implies that the exponent of the group divides the order of the group.

Rings.

A commutative ring has two operations + and ×.

It must be a group for +.

The multiplication must be associative, have a neutral element, be commutative. Furthermore, there must be a distributivity of multiplication over addition. Examples include Z, Zn, Z[x], Zp[x].

Instead of subrings, we consider *ideals*. We can make the product of rings, raise a ring to some power, and make the quotient of a ring by an ideal.

In Z, a number p is prime if *p >* 1 and

$$\forall a,b\in\mathbf{Z}\quad p=a b\Longrightarrow|a|=1{\mathrm{~or~}}|b|=1$$
In K[x], a polynomial P(x) is *irreducible* if

$\forall A(x),B(x)\in\mathbf{K}[x]\quad P(x)=A(x)B(x)\Longrightarrow\deg(A)=0$ or $\deg(B)=0$.

The notion of irreducibility is more general in rings.

Euclidean rings have a Euclidean division. For instance, Z and K[x] are Euclidean rings. Euclidean rings are principal rings. I.e., every ideal can be generated by a single element. In principal rings, all elements have a *unique factorization* into irreducible elements, up to multiplication by units and permutations. More precisely, if x = p1 *· · ·* pm = q1 · qn are two factorizations of x into a product of irreducible elements pi and qj, there must exist a bijection f : {1, . . . , m} → {1, . . . , n}
and some units u1*, . . . , u*m such that qf(i) = uip1 for all i.

Given a ring R, we consider the group R∗ of elements which are invertible for the multiplication.

This forms a group for the ring multiplication.

Finite fields.

A finite field is a finite ring in which every nonzero element is invertible. The Galois theorem says that finite fields have a cardinality which is the power of a prime number and that finite fields with same cardinality are isomorphic. Furthermore, given a prime power q = pn, we can construct such field GF(q) by taking an irreducible monic (i.e., with leading coefficient 1)
polynomial P(x) of Zp[x] of degree n then defining GF(q) = Zp[x]/(P(x)). In practice, we will use either Zp or GF(2n).

The Zn ring.

In Zn, x is invertible if and only if gcd(*x, n*) = 1. The cardinality of Z∗
n is φ(n)
and its exponent is λ(n). If the pi's are prime and pairwise different, we have

$$\varphi(p_{1}^{\alpha_{1}}\ldots p_{r}^{\alpha_{r}})=(p_{1}-1)p_{1}^{\alpha_{1}-1}\times\cdots\times(p_{r}-1)p_{r}^{\alpha_{r}-1}$$ $$\lambda(p_{1}^{\alpha_{1}}\ldots p_{r}^{\alpha_{r}})=\mbox{lcm}\,(\lambda(p_{1}^{\alpha_{1}}),\ldots,\lambda(p_{r}^{\alpha_{r}}))$$
with λ(pα) = φ(pα) except for λ(2α) with α ≥ 3, for which λ(2α) = 1
2φ(2α). We know that for all x ∈ Z∗
n, we have xφ(n) mod n = 1 and xλ(n) mod n = 1.

The Zp field.

Zp is a field if and only if p is a prime. In that case, we know that Z∗
p is a cyclic group. I.e., there exists elements g (called generators) such that all elements can be written as a power of g in the group. We have that xp−1 mod p = 1 for all x ∈ Z∗
p. When *p >* 2, p is odd and the set QR(p) of quadratic residues of Z∗
p (i.e., the set of the square of all Z∗
p elements) is a group of order p−1
2
mod p = 1.

2 . Actually, x ∈ Z∗
p is a quadratic residue if and only if x p−1
The Chinese Remainder Theorem.

We state the following result:
Theorem 1.1. If m and n *are two relatively prime integers (i.e.,* gcd(*m, n*) = 1), then the ring Zmn of residues modulo mn is isomorphic to the product ring Zm × Zn. One isomorphism is the function mapping x ∈ {0, . . . , mn − 1} *to the pair* (x mod *m, x* mod n).

This simple fact has many important consequences:

- For every (*a, b*) pair, there exists a unique integer x (up to a multiple of mn) such that
x mod m = a and x mod n = b at the same time. We can compute x by inverting f. One
way consists of computing
$x=\left(an(n^{-1}\bmod m)+bm(m^{-1}\bmod n)\right)\bmod(mn)$
- The group of units of both rings have the same cardinality. Namely, φ(mn) = φ(m)φ(n).
We stress that this holds for gcd(*m, n*) = 1.

Random variables.A random variable is a process$X$transforming some random seeds (e.g., coin flips) into an element of some set $\mathcal{Z}$. The _support_ of $X$ is the set of all possible $\mathcal{Z}$ elements which can be taken by $X$. The _distribution of_$X$ is a function from a set including the support of $X$ to $\mathbf{R}$, mapping a value $x$ to the probability $\Pr[X=x]$ that $X$ takes the value $x$. In this lecture, we can write a _discrete_ random variables. This assumes that $\mathcal{Z}$ is enumerable.

Two random variables $X$ and $Y$ are called _independent_ if for all $x$ and $y$, we have $\Pr[X=x,Y=y]=\Pr[X=x]\Pr[Y=y]$.

We now consider random variables with a support in a vector space over the reals. The expected value of $X$ is

$$E(X)=\sum_{\text{seed}}\Pr[\mathsf{seed}]X(\mathsf{seed})=\sum_{x\in\mathsf{support}(X)}x\Pr[X=x]$$
(we recall that X transforms some seed into a value X(seed) of support(X).) The variance of X is

$$V(X)=\left(E(X-E(X))^{2}\right)=E(X^{2})-E(X)^{2}$$

The expected value is a linear operator. I.e., for all $\lambda,\mu\in{\bf R}$, we have $E(\lambda X+\mu Y)=\lambda E(X)+\mu E(Y)$. The variance is quadratic. I.e., for all $\lambda$, we have $V(\lambda X)=\lambda^{2}V(X)$. When $X$ and $Y$ are independent, we have $E(XY)=E(X)E(Y)$.

For a function $f$ and a random variable $X$, $f(X)$ is a new random variable. We have

$$E(f(X))=\sum_{x\in{\sf support}(X)}f(x)\Pr[X=x]$$
When X is Boolean (i.e., its support is included in {0, 1}), we have E(X) = p and V (X) =
p(1 − p) where p = Pr[X = 1].

## 1.3 The Algorithmic Toolbox

Algorithms over big numbers.

Assuming a binary representation, the addition of x and y can be done with complexity O(ℓ), where ℓ is the bitlength of the numbers. The multiplication can be done with complexity O(ℓ2), as well as the Euclidean division. This includes the computation of x mod y, for instance. The *extended Euclid algorithm* computes from x and y two integers a and b such that ax + by = gcd(*x, y*). This is done with complexity O(ℓ2).

Modular arithmetic.

We consider Zn where n has a bitlength ℓ and elements are represented as numbers between 0 and n − 1. The addition in Zn can be done with complexity O(ℓ). The multiplication with schoolbook algorithm is done in complexity O(ℓ2). There exists a multiplication algorithm based on the fast Fourier transform, which is asymptotically better, but not better in practice for the numbers we use.

The inversion of an invertible element is done with complexity O(ℓ2), using the extended Euclid algorithm. Actually, x ∈ Zn is invertible if and only if gcd(*x, n*) = 1, so if and only if the algorithm fed with x and n returns some a such that (ax) mod n = 1.

The computation of xe mod n is done with complexity O(ℓ2 log e) using the schoolbook multiplication.

If the factorization of n is provided, we can compute square roots of quadratic residues with complexity O(ℓ3) (with schoolbook multiplication).

We can test the primality of an integer n of bitlength ℓ. If we use up to k iterations in the Miller-
Rabin primality test algorithm, the probability of having an incorrect answer is bounded by 4−k.

Every iteration has a complexity of O(ℓ3) (with schoolbook multiplication). A composite number is rejected with complexity O(ℓ3) (with schoolbook multiplication). So, using the prime number theorem, we can generate random primes of length ℓ with complexity O(ℓ4) (with schoolbook multiplication).

Birthday effect.

Given a random function over a set of size N, we can find collisions with complexity
√
N using the birthday paradox. So, is a hash function producing digests of n bits (so that N = 2n), we can find collisions with O(2
n
2 ) hashes. So, the *bit-equivalent* security is of n
2 .

This adapts to many different situations. For instance, to find some values x and y in their respective domains such that f(x) = g(y), we need to explore subsets of size
√
N.

There are also algorithms to find collisions which do not require to store many attempts.

They can find with constant memory, with a constant multiplicative overhead in terms of time complexity. Generic attacks.

For some encryption function based on a key of size n, we can do a key recovery of complexity O(2n) using *exhaustive search*. For a random hash function with range
{0, 1}n, we can make a preimage attack with complexity O(2n). As already mentioned, collisions can be found with complexity O(2
n
2 ). Finally, for a message authentication code based on a key of size n, we can do a key recovery of complexity O(2n).

## 1.4 The Complexity Theory Toolbox

**Membership problem.** A _language_ is a set of _words_, i.e., finite sequences of letters taken from a given alphabet. A membership problem is defined by a language $L$. An instance of the problem is a word $x$. The problem consists of deciding whether $x\in L$ or not. Languages in the class $\mathcal{N}\mathcal{P}$ are of form

$$L=\{x;\exists w\quad R(x,w)\}$$
for some *predicate* R which can be evaluated in polynomial time. (A more precise definition will be given in Chapter 4.) A value w such that R(*x, w*) holds is a *witness* for x to be member of L.

A problem is NP-hard if solving it in polynomial time implies solving any problem in the class NP.

Membership problems are problems consisting of computing one bit (i.e., whether the instance is in the language of not). We can consider problems consisting of computing several bits. For instance, the factoring problem consists of computing one non-trivial factor of the integer represented by the instance. The discrete logarithm problem consists, given g and y belonging to a group, in computing an integer x such that gx = y. None of these problems are known to be NP-hard. Nevertheless, they might by hard to solve.

The best algorithm to solve the factoring problem is the NFS algorithm. Factoring n takes

$$e^{\mathcal{O}\left((\ln n)^{\frac{1}{3}}(\ln\ln n)^{\frac{2}{3}}\right)}$$
There is another powerful factoring algorithm which is better to find a small factor p of n: the Elliptic Curve Method (ECM). It works with complexity

$$e^{\mathcal{O}\left(\left(\ln p\right)\frac{1}{2}\left(\ln\ln p\right)\frac{1}{2}\right)}$$

The best algorithm to solve the discrete logarithm problem in the group $\mathbf{Z}_{p}^{*}$ is index calculus. It works in complexity

$$e^{\mathcal{O}\left(\left(\ln p\right)\frac{1}{2}\left(\ln\ln p\right)\frac{1}{2}\right)}$$
Turing reduction.

A problem (language) L1 reduces to a problem (language) L2 if there exists a polynomial-time oracle machine AO solving L1, given the oracle O assumed to solve L2. That is, there exists an efficient algorithm to solve L1 using as a subroutine an algorithm solving L2
and with running time set to one unit. This notion of reduction is very useful to compare the difficulty of problems. Namely, if L1 reduces to L2, then L1 is at most as hard to solve as L2.

That is, if we can solve L2, then we can solve L1 as well. Conversely, if L1 is hard to solve, then L2 is hard to solve as well.

The notion of reduction could be used to compare the complexity of two problems. Typically, we would compare the complexity of breaking a cryptosystem to the complexity of some well-known computational problem such as integer factoring.