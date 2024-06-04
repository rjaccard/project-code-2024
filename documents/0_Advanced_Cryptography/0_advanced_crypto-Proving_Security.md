
## Chapter 6 Proving Security

Foundations of cryptography, as presented in the previous chapter about interaction, show that proving techniques heavily rely on the notion of modeling, simulation, interactive Turing machine rewinding, complexity reduction, etc. In a former chapter, we intuitively introduced some notions of security for encryption and signature. In the present chapter, we present some techniques to achieve provable security.

## 6.1 The Random Oracle Model

In the *random oracle model (ROM)*, all participants in the game can query an oracle H, but do not see the queries of others. The oracle is responding randomly (so the name), but consistently. That is, the answer to a fresh query will be random, but forthcoming identical queries will produce the same response.

So, a random oracle models a deterministic function which is selected at random before the game starts. Formally, the response is a "long enough" bitstring. In most of applications, we assume it is a string of pre-determined length. The trick in the random oracle model is that reductions can simulate the random oracle (so that it looks like a real random oracle) but with some hidden but useful information. Signatures with Full-Domain Hash (FDH).

The FDH signature scheme [7] is based on RSA (see Fig. 6.1): we consider that the random oracle H returns random Z∗
N elements, given the RSA modulus N. The signature of a message m is the RSA signature of H(m). The verification algorithm then follows.

Theorem 6.1. If the RSA decryption problem is hard, then FDH is EF-CMA-secure. I.e., it resists to existential forgeries under chosen message attacks.

Proof. We give here the proof by Coron [23]. We consider an adversary A playing the EF-CMA
game. I.e., he is given oracle access to H and the challenger also makes hash queries. He receives some public key (*e, N*). He can make signing oracle queries: he chooses one message m and gets its signature σ by an oracle call. Then, he produces one pair (*m, σ*) and wins if σ is a valid signature for m and m was not queried to the signing oracle.

By changing A a bit, we reduce without loss of generality to cases where either the attack aborts or the final output is always valid, m was not queried to the signing oracle, and m was queried to the hash oracle.

Then, we construct an algorithm B to solve the RSA decryption problem: B receives a public key (*e, N*) and a ciphertext y and must decrypt it. For that, B simulates A receiving (*e, N*) as a public key, then playing with a simulation for the hashing oracle and the signing oracle.

B simulates H as follows: he answers consistently to repeating queries. For a fresh query m, B picks r ∈U Z∗
N and flips a biased coin b such that Pr[b = 1] = p for some magic parameter p to be later explained. Then, B answers as if H(m) = ybre mod N. It is clear that H(m) is perfectly distributed, even if b is fixed. So, this is a valid simulation of H. More importantly, B keeps a record of y and b such that H(m) = ybre mod N as they will play a role.

B simulates the signing oracle as follows: to sign a message m, he queries m to H and takes y and e such that H(m) = ybre mod N. Then, if b = 1, B aborts. Otherwise, we have H(m) =
re mod N, and the signature of m is clearly r. We can thus simulate without the signing key, unless we abort. Clearly, this simulation is also perfect, except when aborting.

Since the simulations are perfect, A behaves with the same probability as in the EF-CMA
game and either aborts or produces a forgery (*m, σ*).

Finally, when the simulation of A terminates on (*m, σ*), B takes y and e such that H(m) =
ybre mod N. Then, if b = 0, B aborts. Otherwise, we have H(m) = yre mod N. Since σ is a valid signature, we also have H(m) = σe mod N. So, y = (σ/r)e mod N. Hence, the decryption of y is
σ/r mod N.

The probability that B succeeds is the probability that all hashing queries by the challenger used b = 0, that the hashing query related to the forged signature used b = 1, and that A succeeds.

By assumption, the message in the forgery was not queried to the signing oracle. So, this happens p(1−p)qS times the success probability of A, where qS is the number of signing queries. By taking p =
1
qS+1, we have

$$p(1-p)^{q s}\geq{\frac{e^{-1}}{q s+1}}$$
Since the RSA decryption problem is hard, we deduce that Pr[A succeeds]/(qS + 1) is negligible.

Since qS is polynomially bounded, this means that Pr[A succeeds] is negligible as well. So, A
cannot win in the EF-CMA game except with negligible probability.

⊓⊔
Hybrid RSA encryption in ROM.

We consider a cryptosystem based on RSA, in which the encryption of m is a pair (*s, c*) such that s is the RSA encryption of some random r, and c = m ⊕ H(r) (where messages have a fixed length and H(r) is assumed to be as long as the message). (See Fig. 6.2.)
Theorem 6.2. If the RSA decryption problem is hard, then the above cryptosystem is IND-CPA secure.

Proof. Let A be an adversary playing the IND-CPA game and wining with probability 1
2 + ε. We want to show that ε is negligible. Following the rules of the game, A receives a public key (*e, N*), makes some hash queries to H, selects m0 and m1, gets a ciphertext (*s, c*) which encrypts mb, and makes a guess for b.

We let E be the event that A makes a query r to H that is such that re mod N = s. Note that by running A, we can always check if E occurs once A terminates. Clearly, if E occurs, the

2. We deduce that decryption of (*s, c*) must be c ⊕ H(r). So, we can construct another adversary who always answer by b′ such that mb′ = c ⊕ H(r) when E occurs. Without loss of generality, we assume that this is what A does.

We note that if E holds, A always win. If E does not occur, we have that r = sd mod N is not queried to H by A and c = mb ⊕H(r) with H(r) random. Note that H(r) is uniformly distributed and only used to compute c. So, c is statistically independent from b. Therefore, the view of A is independent from b and the probability that A guesses b is exactly 1

$${\frac{1}{2}}+\varepsilon=\operatorname*{Pr}[{\mathcal{A}}\;{\mathsf{w i n s}}|E]\operatorname*{Pr}[E]+\operatorname*{Pr}[{\mathcal{A}}\;{\mathsf{w i n s}}|\neg E](1-\operatorname*{Pr}[E])={\frac{1}{2}}+{\frac{1}{2}}\operatorname*{Pr}[E]$$
So, ε = 1
2 Pr[E].

We construct an algorithm B to solve the RSA decryption problem. This algorithm receives an instance (*e, N, y*). Then, he picks r0 ∈ Z∗
N and runs A playing with a simulation of H and the challenger.

To simulate H receiving a query r, if (r/r0)e mod N = y, the simulation stops and B answers r/r0 mod N. Otherwise, the simulation of H is natural.

To simulate the challenger receiving m0 and m1 by A, B picks c of same length and answers by (*s, c*) where s = yre
0 mod N.

Clearly, this perfectly simulates A playing the IND-CPA game in the case that E does not occur. When E occurs, B wins. Now, since the RSA decryption problem is hard, Pr[E] must be negligible. So, ε is negligible as well.

⊓⊔
Fiat-Shamir signatures [27].

A Σ-protocol (*R, P, V,* E, S) in which the set of challenges E is large enough can be transformed into a signature scheme in the random oracle model. Concretely, we are given a pair (*x, w*) such that R(*x, w*) holds, x is a public key and w is the secret key. To sign a message m, we simulate the prover P who sends a = P(*x, w*), receives e = H(*m, a*), and sends z (see Fig. 6.3). The signature is (*a, z*). To verify the signature, we check that V (x, a, H(m, a), z)
holds.

Theorem 6.3. If the problem of finding a witness for x is hard and if 1/#E is negligible, then the above signature scheme is EF-CMA-secure. This construction can be applied to some parallel repetitions of the Fiat-Shamir Σ-protocol. (Indeed, the Fiat-Shamir Σ-protocol has only 2 possible challenges, so we need some parallel repetitions to make 1/#E negligible.) This is based on the problem of finding square roots in Z∗
n.

It can also be applied to the Schnorr Σ-protocol to obtain the Schnorr signature scheme (see

Fig. 6.4). The only change to make to obtain the Schnorr protocol is to use (*e, s*) as a signature for m instead of (*r, s*). This is valid since we can compute (*m, e, s*) from (*m, r, s*) and vice versa. It is more interesting to use (*m, e, s*) because the hash e is typically much shorter than the group element r. It is based on the discrete logarithm problem.

The idea of the proof of this last theorem is that we transform an EF-CMA adversary into a witness finding algorithm as follows:

- First, we transform it into an EF adversary making no chosen message queries. To do this,
we simulate the original adversary. We also keep track of the history of queries to H and
their responses. Whenever it makes a signing query m, the simulator can select a random
e ∈ E and run S(*x, e*) = (*a, e, z*), then insert ((m, a), e) in the table collecting the queries
to H, as if we had queried H(*m, a*) and obtained e. The simulator can then answer (*a, z*)
to the signing query. Additionally, any query H(*m, a*) should be intercepted and the answer replaced by e.
Technically, we must check that there is no prior (*m, a*) query to H which would conflict with this simulation.

- Then, we run the adversary making no chosen message query and simulate the random oracle
H. We show that the message m from the final forgery (*a, z*) must be queried together with
a to H(*m, a*) (otherwise, there is a negligible probability that the forgery is correct). Then,
we run again with the same coins and same simulation for H, until this query (*m, a*) is responded differently. The magic in this trick, called the *forking lemma* [49], is that we are likely to obtain two simulations producing the same m and a with two different H(*m, a*).

Then, we can call the extractor E to create a witness w.

For this, we will first show two lemmas. Lemma 6.4. Given a relation R s.t. it is hard to find witnesses and a Σ-protocol for its language s.t. 1/#E = negl, we consider the signature scheme obtained by the Fiat-Shamir construction using a random oracle.

There is a compiler which can transform an adversary A playing the EF-CMA game into another adversary A′ making no chosen message queries such that the complexity of A′ is the one by A multiplied by some polynomial and

## Pr[A′ Wins] = Pr[A Wins] − Negl

Proof. The EF-CMA game is depicted by the interaction between the adversary A, a challenger, and a random oracle H (see Fig. 6.5). The challenger selects x and w and sends x to A, then answers to any signature query m by computing some signature with the help of the random oracle: the challenger picks r, computes a = P(*x, w*; r), queries m∥a to H, gets e, computes z = P(*x, w, e*; r), and answers (*a, e, z*) to A.

We denote by (*m, a, z*) be the final forgery produced by A.

We first define an equivalent adversary A1 as follows:

- A1 simulates A until A yields its final forgery. - If m was queried to the challenger (A1 can see it), A1 aborts. So, there is no oracle query
from challenger of form (*m, a*′).
- If (*m, a*) was not queried to H by A, query it to get e = H(*m, a*).
- If V (*x, a, e, z*) returns false, abort. - Yield the forgery (*m, a, z*).
We obtain a new EF-CMA adversary A1 with similar complexity and same success probability, who either aborts or yields a valid forgery (*m, a, z*), and who always queries (m∥a) to H.

We let ε = Pr[A wins] = Pr[A1 wins].

We now define another adversary A2 as follows:

- A2 simulates A1 and makes a list of all queries to the random oracle. During this simulation,
A2 will have to forward queries m from A1 to the challenger and the response (*a, z*) back to
the simulation of A1. By doing so, A2 can deduce the query (*m, a*) made by the challenger
to the random oracle.
- If the challenger does a query (*m, a*) (as observed, A2 can deduce it) which was made to the
random oracle before A2 aborts. We let ε′ be the probability that such a repeating query
happens during the game.
We obtain a new EF-CMA adversary A2 with similar complexity and success probability ε − ε′
such that the challenger makes queries which are fresh.

Since the total number of queries to H must be polynomially bounded, we have ε′ ≤ poly ×
maxa pa where pa = Pr[P(*x, w*; r) = a]. If we prove that pa is negligible for all a, we deduce that
ε′ is also negligible.

Let us now prove that for all a, pa is negligible. The algorithm running S(*x, e*; r) and S(*x, e*′; r′)
with random e, e′*, r, r*′ yields a twice with probability p2
a. When it is the case, it can then run E
to extract w. This works with probability p2
a(1 −1/#E). Since we assumed that finding a witness was hard, this must be negligible. So, pa is negligible.

We finally define A′ as follows:

- A′ simulates A2 until a query m to the challenger is made. - Upon the query m, A′ picks r, e, computes (*a, e, z*) = S(*x, e*; r), and returns (*a, z*). Since a
has the correct distribution, (*m, a*) must look like a fresh query to H. Since e was selected
at random, it looks like a correct response from H. So, A′ just takes note that (*m, a*) is
supposed to hash onto e.
- If A2 makes a (*m, a*) query to H, A′ intercepts it and answer e. Since this cannot be the
query corresponding to the final forgery, this does not affect the correctness of the final forgery.
Clearly, this simulation of the challenger queries to H are made with the correct distribution. So, it does not affect the probability of success. We thus obtain an EF-CMA adversary A′ making no chosen message query, with similar complexity and success probability ε−ε′. Since ε′ is negligible, we obtain the result.

⊓⊔
The Forking Lemma was first proposed by Pointcheval and Stern in 1996 [49]. We give here a generalized version of it.

Lemma 6.5 (Forking Lemma). *We consider a finite tree and a mapping* dist which maps any leaf λ *of the tree to one of its ancestors* dist(λ)*. We call it a* distinguished ancestor. We assume we are given a distribution which defines a random leaf X*. We let* visit(ν) be the event that the descent from the root to X goes through ν, i.e. that ν is an ancestor of X*. We let* succ(λ) be true if and only if dist(λ) ̸= λ*. When it occurs we say that* λ is successful*. We let* p = Pr[succ(X)],
¯d = E(depth(X))*, and* f(ν) = Pr[succ(X) and dist(X) = ν|visit(ν)].

For any real number θ > 0, we have

$$\Pr\Big{[}f(\mathsf{dist}(X))>(1-\theta)\frac{p}{d}\Big{]}\mathsf{succ}(X)\Big{]}\geq\theta.$$

So, if a random descent going to $X$ is successful, another random descent starting from the distinguished ancestor of $X$ is likely to be successful (with probability at least $(1-\theta)\frac{p}{d}$) with the very same distinguished ancestor. We can even estimate the probability that the two consecutive descents are successful with the same distinguish ancestor:

$$E(f(\mathsf{dist}(X)))=\int_{0}^{1}\Pr[f(\mathsf{dist}(X))\geq t,\mathsf{succ}(X)]\;dt$$ $$=\int_{0}^{1}\Pr[f(\mathsf{dist}(X))\geq t[\mathsf{succ}(X)]\;dt$$ $$\geq\;p\int_{0}^{1}\frac{1}{2}\times1_{t\leq\frac{p}{2d}}\;dt$$ $$=\frac{p^{2}}{4d}$$
So, if p is not negligible and ¯d is polynomial, then E(f(dist(X))) is not negligible. This will be used later to prove the theorem.

Proof. We have Pr[dist(X) = ν|succ(X)] = f(ν) Pr[visit(ν)]
¯d. We have

Proof.: We have $\Pr[\mathsf{dist}(X)=\nu|\mathsf{succ}(X)]=f(\nu)\frac{\nu\mathsf{true}\mathsf{true}\mathsf{true}}{p}$. We let $\mathsf{Bad}$ be the set of $\nu$'s such that $f(\nu)\leq(1-\theta)\frac{\mathsf{P}}{d}$. We have

$$\Pr[\mathsf{dist}(X)\in\mathsf{Bad}|\mathsf{succ}(X)]=\sum_{\nu\in\mathsf{Bad}}f(\nu)\frac{\Pr[\mathsf{dist}(\nu)]}{p}$$ $$\leq(1-\theta)\frac{\sum_{\nu}\Pr[\mathsf{visit}(\nu)]}{d}$$ $$\leq1-\theta$$
so, Pr[dist(X) ̸∈ Bad|succ(X)] ≥ θ.

⊓⊔
We can now fully prove the Fiat-Shamir signature security.

Proof (of Th. 6.3). By first applying Lemma 6.4, we reduce to the case where the adversary makes no chosen message queries. So, we are in the situation of Fig. 6.6.

We define an algorithm B(x) as follows (see Fig. 6.7):

- B simulates A with initial x and simulates H to A. - If A does not output any (*m, a, z*), B aborts. Otherwise, B runs A again with same random
coins. The answers from H use the same random answers until (*m, a*) is queried to H. Then,
they use fresh coins.
- If A does not output any (*m, a, z*′), B aborts. Otherwise, B gets two forgeries (*a, z*) and (*a, z*′)
with same a so he can get the corresponding e and e' then extract w = E(x, a, e, z, e′, z′).
We build the tree of the A executions depending on the random answers from H (each node ν
corresponds to a query by A, each leaf λ corresponds to a termination).

A random descent in the tree corresponds to a complete execution of A interacting with H.

This descent ends up to a random leaf X. This defines a distribution on leaves. We say that X is successful and write succ(X) is the leaf corresponds to an execution yielding a valid forgery
(*m, a, z*). By construction, (*m, a*) must have been queried. The query to (*m, a*) corresponds to a distinguished ancestor dist(X) of X. If X is not successful, we just define dist(X) = X. So, the second execution of A corresponds to a second descent starting from dist(X). Let Y be the leaf obtained in this second descent. If Y is successful and dist(X) = dist(Y ), then we have two forgeries (*m, a, z*) and (*m, a, z*′) with the same (*m, a*), corresponding to some e and e′. If e ̸= e′, the extractor finds a witness and B succeeds.

Since Pr[e = e′] = negl, the success probability of B is greater than E(f(dist(X)))−negl. Since extracting a witness is assumed to be hard, E(f(dist(X))) must be negligible. Thanks to the Forking Lemma, we deduce that Succ(X) is negligible as well. So, A has a negligible probability of success.

⊓⊔
Controversy about the random oracle model.

This model has been controversial, because random oracles are never used in practice. They are replaced by a practical hash function. However, we can construct schemes which are secure in the random oracle model but insecure whenever the random oracle is replaced by *any* hash function. We give as an example a construction proposed by Canetti, Goldreich, and Halevi in 1998 [14].

We use a construction similar as FDH. To sign a message m, we first interpret m as the code of an algorithm implementing a function hm (we must define a programming language and add safeguards so that the execution of these algorithms always terminate in due time). Then, we pick some r, query H(r), and compute hm(r). If H(r) = hm(r), the signature is set to the RSA secret exponent d. Otherwise, the signature is H(m)d mod N. Clearly, in the random oracle model, there is nearly no chance that H(r) becomes accidentally equal to hm(r), so the security proof works like for FDH. When we replace H by a concrete hash function h, we could consider the code m implementing it (i.e., m such that hm = h), and we suddenly obtain h(r) = hm(r) whatever the selection of r. So, any signing query will obtain the RSA secret exponent which is enough to make forgeries. So, this is EF-CMA insecure.

## 6.2 Hybrid Elgamal

We can now consider a variant of the ElGamal cryptosystem which encrypts strings of m bits (and not group elements). To encrypt M, one has to pick some random r and random n and compute
(gr, M ⊕ hn(yr), n) where h is a family of universal hash functions (see Fig. 6.8).1 The idea is that yr when written as a bitstring, which has a terrible distribution but some decent min-entropy H∞(yr), can be replaced by some hn(yr) with n random to have a better distribution.2 This is called the *leftover hash Lemma*. Lemma 6.6 (Leftover Hash Lemma, Impagliazzo-Levin-Luby 1989 [38]). Given a random variable X*, if* m ≤ H∞(X) − 2 log 1
ε (where H∞ denotes the min-entropy), if h is a family of functions from the support of X to {0, 1}m *such that* Pr[hN(x) = hN(x′)] = 2−m for all x ̸= x′, where N is uniformly distributed, then (hN(X), N) and (U, N) are ε-indistinguishable, where U is uniformly distributed in {0, 1}m.

Proof. We let P0 be the distribution of (hN(X), N) and P1 be the distribution of (*U, N*). We denote by N the support of N. We compute the Euclidean distance between P0 and P1:

k,n  Pr X,N[hn(X) = k, N = n] − 1 2 2m#N ∥P1 − P0∥2 2 = X =   k,n Pr X,N[hn(X) = *k, N* = n]2 2m#N X  − 1 = Pr X,X′*,N,N* ′[hN(X) = hN ′(X′), N = N ′] − 1 2m#N = 1 x,x′ Pr[X = x, X′ = x′, hN(x) = hN(x′)] − 1 #N 2m#N X = 1 − 2−m x Pr[X = x]2 #N X
which we obtain by splitting x = x′ and x ̸= x′. So,

$$\|P_{1}-P_{0}\|_{2}^{2}\leq\frac{1-2^{-m}}{\#\mathcal{N}}\max_{x}\Pr\{x\}\leq\frac{1-2^{-m}}{\#\mathcal{N}}2^{-H_{\infty}(X)}\leq\frac{1}{2^{m}\#\mathcal{N}}\varepsilon^{2}$$

We then use $d(\mathsf{distr}(X),\mathsf{uniform})\leq\|\mathsf{distr}(X)-\mathsf{uniform}\|_{2}\sqrt{\#\mathsf{domain}}$ to obtain $d(P_{0},P_{1})\leq\varepsilon$.

By using this lemma and some bridging steps, we can prove that this variant of the ElGamal cryptosystem is IND-CPA secure if the DDH problem is hard.

Theorem 6.7. Assuming that the DDH assumption in the group spanned by g is hard and that hn is a family of functions from this group to {0, 1}m such that for all x ̸= x′ and a uniformly distributed N, Pr[hN(x) = hN(x′)] = 2−m. The ElGamal Cryptosystem Variant of Fig. 6.8 is IND-CPA secure.

Proof. We let Γb
0 denote the IND-CPA game using bit b. We want to show that Γ0
0 and Γ1
0 return
0 with probabilities with negligible difference. The game Γb
0 works as follows:
game Γb
0:
1: run key generation and get y
2: pick random coins ρ and set view = (y; ρ)
3: run A(view) = (m0, m1)
4: pick r ∈U Zq and set u = gr
5: pick n ∈N N and set v = mb ⊕ hn(yr)
6: set view = (*y, u, v, n*; ρ)
7: run A(view) = b′
8: **return** b′
We first bridge to the following game by reordering the steps.

game Γb
1:
1: pick x ∈U Zq and set y = gx
2: pick r ∈U Zq and set u = gr
3: set X = gxr and erase x and r
4: pick random coins ρ and set view = (y; ρ)
5: run A(view) = (m0, m1)
6: pick n ∈N N and set v = mb ⊕ hn(X)
7: set view = (*y, u, v, n*; ρ)
8: run A(view) = b′
9: **return** b′
We use the indistinguishability in the DDH assumption to reduce to the following variant.

game Γb
2:
1: pick x ∈U Zq and set y = gx
2: pick r ∈U Zq and set u = gr 3: pick s ∈U Zq, set X = gs, and erase x and r
4: pick random coins ρ and set view = (y; ρ)
5: run A(view) = (m0, m1)
6: pick n ∈N N and set v = mb ⊕ hn(X)
7: set view = (*y, u, v, n*; ρ)
8: run A(view) = b′
9: **return** b′
We bridge again by reordering steps.

game Γb
3:
1: pick x ∈U Zq and set y = gx 2: pick r ∈U Zq and set u = gr
3: pick random coins ρ and set view = (y; ρ)
4: run A(view) = (m0, m1)
5: pick s ∈U Zq and set X = gs
6: pick n ∈N N, set v0 = hn(X), and erase x and r
7: set v = mb ⊕ v0
8: set view = (*y, u, v, n*; ρ)
9: run A(view) = b′
10: **return** b′
We then use the Leftover hash Lemma to obtain what follows.

game Γb
4:
1: pick x ∈U Zq and set y = gx
2: pick r ∈U Zq and set u = gr
3: pick random coins ρ and set view = (y; ρ)
4: run A(view) = (m0, m1)
5: pick U
6: pick n ∈N N, set v0 = U, and erase U 7: set v = mb ⊕ v0
8: set view = (*y, u, v, n*; ρ)
9: run A(view) = b′
10: **return** b′
We reorder again the steps.

game Γb
5:
1: pick x ∈U Zq and set y = gx
2: pick r ∈U Zq and set u = gr
3: pick random coins ρ and set view = (y; ρ)
4: run A(view) = (m0, m1)
5: pick n ∈N N
6: pick v0
7: set v = mb ⊕ v0 and erase v0
8: set view = (*y, u, v, n*; ρ)
9: run A(view) = b′
10: **return** b′
We use the indistinguishability between v0 and v.

game Γb
6:
1: pick x ∈U Zq and set y = gx
2: pick r ∈U Zq and set u = gr
3: pick random coins ρ and set view = (y; ρ)
4: run A(view) = (m0, m1)
5: pick n ∈N N
6: pick v
7: set view = (*y, u, v, n*; ρ)
8: run A(view) = b′
9: **return** b′
Finally, Γb
6 never uses b, so Γ0
6 and Γ1
6 are identical. We have the following chain:

Γ0
 0
    bridge
    ⌢
         Γ0
          1
             DDH
              ≈
                  Γ0
                   2
                      bridge
                       ⌢
                           Γ0
                            3
                               lemma
                                ≈
                                     Γ0
                                      4
                                         bridge
                                          ⌢
                                              Γ0
                                               5
                                                  domain
                                                   =
                                                        Γ0
                                                         6

=

             Γ1
              0
                 bridge
                  ⌢
                       Γ1
                        1
                           DDH
                           ≈
                                Γ1
                                 2
                                    bridge
                                    ⌢
                                         Γ1
                                          3
                                             lemma
                                              ≈
                                                   Γ1
                                                    4
                                                       bridge
                                                       ⌢
                                                            Γ1
                                                             5
                                                                domain
                                                                 =
                                                                      Γ1
                                                                       6
Piling everything together, we have that Pr[Γ0
                                        0(A) = 0] − Pr[Γ1
                                                       0(A) = 0] is negligible. Hence, we
have IND-CPA security.
                                                                                    ⊓⊔

## 6.3 The Fujisaki-Okamoto Transform

In 1999, Fujisaki and Okamoto proposed a standard way to transform a weakly secure cryptosystem into an IND-CCA secure one [28, 29]. More precisely, they start from a cryptosystem $(\mathsf{Gen}_{0},\mathsf{Enc}_{0},\mathsf{Dec}_{0})$ which is secure against decryption under CPA and also $\gamma$-spread. This latter notion is actually new. It means that there is no ciphertext value which is taken too often. More precisely

$$\forall\mathsf{pk},\mathsf{pt},\mathsf{ct}\qquad\mathsf{Pr}[\mathsf{Enc}_{\mathsf{pk}}(\mathsf{pt})=\mathsf{ct}]\leq2^{-\gamma}$$

The construction also uses a one-time secure cipher (which we take as one-time pad below) and two random oracles $G$ and $H$. The new cryptosystem is defined with $\mathsf{Gen}=\mathsf{Gen}_{0}$ as follows:
Encpk(pt):
Decsk(ct1, ct2):

1: pick σ
2: ct2 ← pt ⊕ G(σ)
3: ct1 ← Enc0,pk(σ; H(σ, ct2))
4: return (ct1, ct2)

1: σ ← Dec0,sk(ct1)
2: if σ = ⊥ then return ⊥
3: if
       ct1
             ̸=
                  Enc0,pk(σ; H(σ, ct2))
   then return ⊥

4: pt ← ct2 ⊕ G(σ)
5: return pt

Theorem 6.8 (Fujisaki-Okamoto [28, 29]). If (Gen0, Enc0, Dec0) is OW-CPA secure and γ-
spread, in the random oracle model, the above cryptosystem (Gen, Enc, Dec) is IND-CCA secure.

Proof (sketch). We modify the decryption oracle so that it does not use sk but only the oracle
tables: if there is no (σ, ct2, h) ∈ H such that ct1 = Enc0,pk(σ; h), then the decryption oracle
returns ⊥. Otherwise, it decrypts by using G. We then modify F and G on the challenge σ
point.
                                                                                               ⊓⊔

In 2016, Targhi and Unruh revisited the Fujisaki-Okamoto transform so that it additionally resist to quantum attacks on the random oracle [61]. The modification essentially adds a third component in the ciphertext.

Encpk(pt):
Decsk(ct1, ct2, ct3):

1: σ ← Dec0,sk(ct1)
2: if σ = ⊥ then return ⊥
3: if
       ct1
             ̸=
                  Enc0,pk(σ; H(σ, ct2))
   then return ⊥

1: pick σ
2: ct2 ← pt ⊕ G(σ)
3: ct1 ← Enc0,pk(σ; H(σ, ct2))
4: ct3 ← H′(σ)
5: return (ct1, ct2, ct3)

4: if ct3 ̸= H′(σ) then return ⊥
5: pt ← ct2 ⊕ G(σ)
6: return pt

   In 2017, Hofheinz, H¨ovelmanns, and Kiltz reshaped the Fujisaki-Okamoto transform in a mod-
ular way [37]. We present three of their transformations here.
   First of all, Sℓ transforms a OW-CPA secure cryptosystem into an IND-CPA secure one.

## Owcpa Sℓ −→ Indcpa

Encpk(pt):
Decsk(ct0*, . . . ,* ctℓ):

1: pick x1, . . . , xℓ
2: ct0 ← pt ⊕ F(x1*, . . . , x*ℓ)
1: xi ← Dec0,sk(cti), i = 1, . . . , ℓ
2: pt ← ct0 ⊕ F(x1*, . . . , x*ℓ)
3: **return** pt
3: cti
$
←− Enc0,pk(xi), i = 1, . . . , ℓ
4: **return** (ct0*, . . . ,* ctℓ)
The OWCPA → INDCPA reduction is loosing a factor q1/ℓ in the advantage, where q is the number of random oracle queries the adversary can make. This factor can be huge. We can increase ℓ to make it smaller but it makes encryption more costly.

Second, T transforms a IND-CPA secure and γ-spread cryptosystem into an IND-PCVA secure one.

INDCPA
T−→ OWPCVA

Encpk(pt):
Decsk(ct):

1: ct ← Enc0,pk(pt; G(pt))
2: **return** ct

1: pt ← Dec0,sk(ct)
2: if pt = ⊥ then return ⊥
3: if ct ̸= Enc0,pk(pt; G(pt)) then
   return ⊥

4: return pt

Finally, U transforms a OW-PCVA secure cryptosystem into an IND-CCA secure KEM.

## Owpcva U−→ Indcca(Kem)

Encpk(pt):
Decsk(ct):

1: pick pt at random 2: ct
$
←− Enc0,pk(pt)

1: pt ← Dec0,sk(ct)
2: if pt = ⊥ then return ⊥
3: K ← H(pt, ct)
4: return K

3: K ← H(pt, ct)
4: return (K, ct)

