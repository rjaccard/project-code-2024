
## Chapter 4 The Power Of Interaction

An essential cryptographic protocol is the notion of *interactive proof*. Typically, a client would prove his credentials to a server. Here, the client plays the role of a prover and the server is a verifier. Ideally, his credential should not leak from the protocol, even to the verifier who could be malicious. This is the notion of *zero-knowledge protocol*. In this chapter, we formalize the notions of interaction, proof, zero-knowledge, and provide building blocks.

## 4.1 Interactive Proofs

We consider

- an **alphabet** Z, i.e., a set of **letters**;
- the set Z∗ of finite strings made of elements in Z, i.e. the set of all **words**; - the subsets of Z∗ are called **languages**, i.e. sets of words.
Given a language L and a word x, we consider the problem of deciding whether or not x belongs to L. This is the **membership problem**.

Languages for which the membership problem can be decided by a deterministic algorithm within a time bounded by a polynomial in terms of |x|, the length of the string x, are called P
languages.

Sometimes, we will consider x as a *statement* and L be the language of statements which are true.

True statement may be proven by a *proof* w which will be called a **witness**.

Given a predicate R(*x, w*) checking whether w is a correct proof for x, the language L is defined by

$$L=\{x\in Z^{*};\exists w\in Z^{*}\quad R(x,w)\}$$
(For convenience, proofs are encoded into a word so that we can also assume that the witness is a word.)
Languages such as the above, where R can be evaluated in a time bounded by some polynomial in terms of |x|, and where the witness must have a length also bounded by a polynomial, are called NP languages. The complement of an NP language is called a co-NP language. It is known that

$${\mathcal{P}}\subseteq{\mathcal{N P}}\cap{\mathsf{co}}{\mathsf{\text{-}}}{\mathcal{N P}}$$
i.e., any P language is both an NP language and a co-NP language. This is illustrated on Fig. 4.1.

A big open question in complexity is whether P = NP or not. There is an inclusion, but it is not known if all NP language can be recognized in polynomial time or if some of these languages do not have any polynomial-time algorithm to decide membership. Another open question is to wonder if NP = co-NP or not. I.e., for languages for which membership can be checked with a witness in polynomial time, can we always check non-membership with a witness as well? Note that if P = NP then P = NP = co-NP.

We already used the notion of Turing reduction but there is another notion due to Karp.

We say that a language L1 reduces to a language L2 if there exists a function f computable by a deterministic polynomial-time algorithm such that for all words x, x ∈ L1 is equivalent to f(x) ∈ L2. Compared to the Turing reduction, this means that the oracle for L2-membership can be invoked only once.

There exist languages L which are NP**-hard**. This means that for each L′ *∈ NP*, L′ reduces
(in the sense of Karp) to L. There even exist NP**-hard** languages in the class NP itself. These languages are called NP**-complete**. For example, assuming a way to encode Boolean terms on Boolean variables in the form of a word, the language SAT of encoded terms that can evaluate to
"true" by at least one assignment of the variables is NP-complete [22]. Consequently, P = NP
is equivalent to SAT *∈ P*.

Next, we define an interactive machine as follows.

Definition 4.1. An interactive machine is an algorithm A taking as input some x, a list of incoming messages m1, . . . , mn of variable length, and a (long enough) sequence of random coins r and computing an outgoing message A(x, m1, . . . , mn; r). The tuple (x, m1, . . . , mn; r) is called the partial view of A.

We assume a special symbol in the alphabet.

Messages ending with this symbol are called terminal messages. We assume that if mn is a terminal message, then A(x, m1, . . . , mn; r) is a terminal message as well.

If A(x, m1, . . . , mn; r) is a terminal message, (x, m1, . . . , mn; r) *is called the* final view of A.

A pair of interactive machines (A, B) (with A called the initiator) is called an interactive system. An experiment exp =

A(rA)
x
←→ B(rB)

is characterized by an input x and the coins rA and rB for each participant. It consists of iteratively defining

$$\begin{array}{r c l}{{a_{i}}}&{{=}}&{{{\mathcal{A}}(x,b_{1},\ldots,b_{i-1};r_{A})}}\\ {{b_{j}}}&{{=}}&{{{\mathcal{B}}(x,a_{1},\ldots,a_{j};r_{B})}}\end{array}$$
for i = 1*, . . . , n*A, where nA is the smallest i such that ai is a terminal message, and j = 1*, . . . , n*B, where nB is the smallest j such that bj is a terminal message. Namely, A initiates the interaction with the message a1 = A(x; rA) to B.

Then, B sends the message b1 = A(*x, a*1; rB) to A.

Then A carries on with a2 = A(*x, b*1; rA) and so on. We define the outputs of both participants OutA(exp) = anA and OutB(exp) = bnB, and the final views ViewA(exp) = (x, b1*, . . . , b*nA−1; rA)
and ViewB(exp) = (x, a1*, . . . , a*nB; rB).

We are now ready to define an interactive proof.

Definition 4.2. Given a language L over an alphabet Z*, an* interactive proof system is an interactive system (P, V), where P *is called a* prover and V *is called a* verifier, such that there exists a polynomial P and some real numbers α and β such that 0 ≤ β < α ≤ 1 and

- ( termination) for any x and every coins, the experiment P
x↔ V makes V terminates within
a complexity bounded by P(|x|);
- ( α-completeness) for any x ∈ L, the experiment P
x↔ V makes V *output "*accept" with
probability at least α (the probability is taken over the random coins);
- ( β-soundness) for any x ̸∈ L and any interactive machine P∗, the experiment P∗
x↔ V
makes V *output "*accept" with probability at most β (the probability is taken over the random
coins).
This means that a prover P can convince a verifier V that x ∈ L, with probability at least α, and that no malicious prover P∗ can convince the verifier when this is not true, with probability larger than β. We note that we assume no complexity bound on P or P∗. We often consider α = 1 in which case we say we have *perfect completeness*.

It is trivial to see that languages in P and NP have an interactive proof system: for a language in P, we just consider a prover doing nothing and a verifier running the verifying predicate defining the language by himself. For a language in NP, we just consider a prover finding the witness w then sending it to the verifier and the verifier checking that this is a correct witness. The protocol is as follows:

**Prover**

\begin{tabular}{c c c}  & **Verifier** \\  & $x$ & \\ find $w$ & $w$ (terminal) & \\  & & \\  & & \\ \end{tabular}

It can be much more complicated to see if languages in co-NP have an interactive proof system.

One non-trivial example is the Goldwasser-Micali-Rackoff proof GMR85 [33] for non-quadratic residuosity. Here, we consider words encoding a pair (*n, v*) of integers and the language

$$L=\{(n,v)\ \mbox{integers};v\in{\bf Z}_{n}^{*},v\not\in{\sf QR}(n)\}$$

We recall that

$${\sf QR}(n)=\{y\in{\bf Z}_{n}^{*};\exists x\quad y=x^{2}\ {\rm mod}\ n\}$$
To construct a proof system we consider the following verifier:

1: pick r ∈U Z∗
n, e ∈U {0, 1}, compute y = ver2 mod n and send y
2: receive f. If gcd(*v, n*) = 1 and e = f, output the terminal message "accept", otherwise, output
the terminal message "reject"
The prover is defined by
1: receive y, solve the equation y = x2 mod n, if it is solvable, output the terminal message f = 1,
otherwise, output the terminal message f = 0
The protocol runs as follows:
Prover Verifier (*n, v*) pick r, e = 0 or 1 solve y = x2 mod n y ←−−−−−−−−−−−−−− y = ver2 mod n f (terminal) −−−−−−−−−−−−−−→ f =  0 if solvable 1 otherwise accept (terminal) ←−−−−−−−−−−−−−− if e = f and gcd(*v, n*) = 1
Termination and perfect completeness are trivial. To prove 1
2-soundness, we consider an arbitrary prover P∗ receiving y and sending f as a function of *n, v, y*.

We assume that (*n, v*) ̸∈ L.

If v ̸∈ Z∗
n, it is clear that the verifier always rejects. If now v ∈ Z∗
n, since (*n, v*) ̸∈ L, we can write v = w2 mod n for some w. So, the distribution of y = (wer)2 mod n is uniform in QR(n), no matter the value of e. Hence, f is independent from e. Thus, Pr[e = f] = 1
2.

Soundness amplification.

For simplicity, we consider perfect completeness. I.e., α = 1. In the case of the GMR85 protocol, it may be unsatisfactory to have a proof in which a prover could cheat with probability 1
2. To solve that, we can amplify the soundness by *sequential composition*.

Namely, we could construct a new interactive proof in which we sequentially run the previous proof n times and accept only if all executions accepted. We could show that the new soundness probability would become βn.

Amplification works very well for sequential composition but there are tricky things if we consider *parallel composition*, i.e., if we run the n executions in parallel. As for interactive proofs as we defined them, it works, but for slightly different notions of interactive proofs (e.g., variants in which the prover is computationally bounded), it does not.

So, we must be careful when considering parallel composition of interactive systems.

As an example, we define the DD game of Bellare, Impagliazzo, and Naor [5].

A verifier commits to a random bit e, then a prover commits to a random bit e′, then both open their commitment and the verifier accepts the "proof" if e ̸= e′:

Prover Verifier pick r, e = 0 or 1 pick r′, e′ = 0 or 1 y ←−−−−−−−−−−−−−− y = commit(e; r) y′ = commit(e′; r′) y′ −−−−−−−−−−−−−−→ r,e ←−−−−−−−−−−−−−− r′,e′ −−−−−−−−−−−−−−→ check y′ = commit(e′; r′) accept (terminal) ←−−−−−−−−−−−−−− if e ̸= e′
If the prover is computationally bounded and the commitment is hiding and binding, there is no way to prove with probability significantly larger than 1
2. So, we could think that for two parallel composition of this protocol, there is no way to prove with probability larger than 1
4. However, this is not the case as the following strategy shows.

The prover just repeats the two parallel commitments of the verifier in the opposite order and win with probability 1
2:

$$\begin{array}{ll}\textbf{Prover}&\textbf{Verifier}\\ &\text{pick}r_1,r_2,\,e_1,e_2=0\text{or}1\\ \text{set}y'_1=y_2,\,y'_2=y_1&\begin{array}{ll}\vspace{0.2cm}y_1,y_2&\vspace{0.2cm}y_i=\texttt{commit}(e_i;r_i)\\ \vspace{0.2cm}y'_1,y'_2&\vspace{0.2cm}\end{array}\\ \vspace{0.2cm}\xleftarrow{}&\begin{array}{ll}\vspace{0.2cm}y'_1,y'_2&\vspace{0.2cm}\end{array}\\ \vspace{0.2cm}\xleftarrow{}&\begin{array}{ll}\vspace{0.2cm}r_1,e_1,r_2,e_2\\ \vspace{0.2cm}r_2,e_2,r_1,e_1&\vspace{0.2cm}\end{array}\\ \vspace{0.2cm}\end{array}$$
So, soundness amplification is not so trivial for parallel composition.

The class of languages with an interactive proof.

We define IP, the class of languages for which there exists an interactive proof. There is a famous theorem from 1992, due to Shamir [57], saying that IP corresponds to the class *PSPACE* of languages for which there is a deterministic algorithm deciding on membership or not which run with bounded space complexity, i.e. a polynomially bounded number of memory cells. Intuitively, this class includes the exhaustive search algorithm and others.

## Theorem 4.3. Ip = Pspace.

So, the class IP is much larger than NP and co-NP. This is depicted on Fig. 4.1.

When considering NP languages with an interactive proof, we said that the proof is trivial: the prover finds a witness (e.g., by exhaustive search), gives it to the verifier, and the verifier can check that it is a valid witness. For cryptographic application, this interactive proof is not satisfactory. Ideally, we would like the prover to prove the existence of the witness without revealing it, and without revealing anything that the verifier could not find by himself. This it the next notion to study: zero-knowledge.

## 4.2 Zero-Knowledge

We define a notion corresponding to interactive proofs where the verifier learns no information except the membership status of the input x.

Definition 4.4. *An interactive proof system* (P, V) is ∗-zero-knowledge if for any p.p.t. interactive machine V∗ there exists a p.p.t. algorithm S *(called a* simulator) such that for any x ∈ L

$$\operatorname{View}_{\mathcal{V}^{*}}\left(\mathcal{P}(r_{P})\not\in\mathcal{V}^{*}(r_{V})\right)$$
and S(x; r) produce ∗-identical distributions.

There are three notions of zero-knowledge, depending on the notion of identical distributions (the
∗ in the definition):

- ∗=*perfect*: ∗-identical really means identical! - ∗=*statistical*: ∗-identical means that the statistical distance is negligible in terms of |x|, i.e.,
any adversary has a negligible advantage.1
- ∗=*computational*: ∗-identical means any p.p.t. distinguisher has a negligible advantage.
As an example, we consider the following proof by Goldwasser-Micali-Rackoff (GMR89) [34] for the language of quadratic residues:

## L = {(*N, V*) Integers; V ∈ Qr(N)}

1. the prover finds s such that v = s2 mod n, picks r ∈ Z∗
n, and sends x = r2 mod n to the
verifier;
2. the verifier picks a random e *∈ {*0, 1} and sends it to the prover;
3. the prover sends y = ser mod n;
4. the verifier accepts if gcd(*n, v*) = 1 and y2 ≡ vex (mod n).


show that if a malicious prover P ∗ makes the verifier V accept with probability strictly greater than 1
2, then it must be the case that (*n, v*) ∈ L. Clearly, we have that n and v are coprime.

Now, the probability is an average over the random coins of P ∗, so there must be some fixed coins making V accept with probability strictly greater than 1
2. This actually means that there must be a P ∗ which is deterministic. By running the proof twice with P ∗, with different e's, we thus obtain the same x, but some answer y0 to e = 0 and some answer y1 to e = 1 which satisfy y2
0 ≡ x
(mod n) and y2
1 ≡ vx (mod n). So, y1/y0 mod n is a square root of v, so (*n, v*) ∈ L.

To prove zero-knowledge, we construct a simulator S based on a malicious verifier V ∗ as follows: S first picks a guess e0 *∈ {*0, 1} for e and a random y ∈ Z∗
n, then simulate the prover giving x = y2v−e0 mod n to V ∗. If V ∗ gives e ̸= e0, this is bad luck and S restarts. Otherwise, e = e0 and S can continue by giving y to V ∗ and obtain the final view of V ∗. We have to prove that the bad luck happens with probability 1
2 and that the obtained distribution is identical to the one obtained by running P and V ∗.

We note here that the simulator S is a *black-box* simulator. I.e., it is constructed by using V ∗
as a subroutine and does not depend on V ∗. All the zero-knowledge protocols that we will see use a black-box simulator.

It was shown in 1986 by Goldreich, Micali, and Wigderson [35], that all NP languages have a computational zero-knowledge proof.

Theorem 4.5. For every language L in NP, there exists a computational zero-knowledge interactive proof system.

They show it by the following GMW86 protocol for an NP-complete language: the language of
3-colorable graphs. A graph (*V, E*) is specified by a vertex set V and an edge set E ⊆ V 2. A
3-coloring is a mapping φ : V *→ {*1, 2, 3} such that for every edge (*u, v*) ∈ E, we have φ(u) ̸= φ(v).

The GMW86 protocol runs as follows:

1. the prover finds a 3-coloring φ of (*V, E*); 2. P and V run #E times the following protocol;
(a) the prover picks a random permutation π of {1, 2, 3}, some coins ru for each u ∈ V , computes Ru = commit(π(φ(u)), ru), and sends all Ru to the verifier;

(b) the verifier picks a random (*u, v*) ∈ E and sends it to the prover;
(c) the prover sends ru, rv, cu = π(φ(u)), and cv = π(φ(v));
(d) the verifier checks that Ru = commit(cu, ru), Rv = commit(cv, rv), and cu ̸= cv;
3. if all iteration succeeded, the verifier accepts.
Prover Verifier (*V, E*) find φ repeat #E times pick π ∈ S3 ru for each u ∈ V cu = π(φ(u)) Ru = commit(cu, ru) R −−−−−−−−−−−−−−→ u,v ←−−−−−−−−−−−−−− pick (u, v) ∈ E if (u, v) ∈ E cu,cv,ru,rv −−−−−−−−−−−−−−→ check Ru, Rv check cu ̸= cv
The protocol is based on a commitment scheme which is computationally hiding and perfectly binding.

Finally, instead of proving membership, we would like that a prover proves his knowledge of a witness.

Definition 4.6. Given a language L ∈ NP over an alphabet Z defined by a relation R, an interactive proof of knowledge for L is a pair (P, V) of interactive machines such that there exists a polynomial P, α, β such that 0 ≤ β < α ≤ 1 and
- termination: this is like for interactive proof systems

- α-completeness: this is like for interactive proof systems
* $\beta$-soundness: _there exists an oracle algorithm $\mathcal{E}$ called_ **extractor** _verifying what follows. For any $\mathcal{P}^{*}$ we let_ $$\varepsilon(x)=\Pr_{r,r,r}\Big{[}\mathtt{Out}_{\mathcal{V}}\left(\mathcal{P}^{*}(r_{\mathcal{P}})\ \triangle\ \mathcal{V}(r_{\mathcal{V}})\right)=\mathtt{accept}\Big{]}$$ _If $\varepsilon(x)>\beta$ then $\mathcal{E}^{\mathcal{P}^{*}}(x)$ outputs $w$ such that $R(x,w)$ holds with complexity at most $P(|x|)/(\varepsilon(x)-\beta)$._
Our typical prover starts with finding w then runs a polynomial-time algorithm. So, an equivalent notion could be to say that P has a private input with w and that P is a polynomially bounded algorithm. Indeed, if we want to prove knowledge of w, we must give w to P! We give examples of proof of knowledge in the next section.

## 4.3 Zero-Knowledge Construction From Σ Protocol

We consider simple protocols running in three phases: the prover sends some message a, the verifier sends some random challenge e selected from a set E, the prover sends back an answer z, and the verifier decides to accept or not. With additional properties, this defines Σ-protocols.

Definition 4.7. Given a language L ∈ NP over an alphabet Z defined by a relation R, a Σ-
protocol for L is a pair (P, V ) of interactive machines such that

- V is polynomially bounded
- 3-move: P starts with a message a, V answers with a challenge e ∈U E, P terminates with
a response z, V accepts (always for x ∈ L) or reject only depending on (*x, a, e, z*)
- special soundness: there exists a polynomially bounded algorithm E *called* extractor such that
for any x, if (x, a, z; r) and (x, a, z′; r′) are two accepting views for V such that e ̸= e′ where e = V (x, a; r) and e′ = V (x, a; r′) then E(x, a, e, z, e′, z′) yields w such that R(*x, w*)
- special honest-verifier zero-knowledge (HVZK): there exists a polynomially bounded algorithm S *called* simulator such that for any x ∈ L and e, the transcript (a, e, z) of the
interaction P(rP )
x↔ V (rV ) conditioned to e has same distribution as S(x, e; r).
To fully define a Σ-protocol we thus need

- a relation R defining the language;
- a function for a = P(*x, w*; rP );
- a samplable domain E for e;
- a function for z = P(*x, w, e*; rP );
- a verification relation V (*x, a, e, z*);
- a function E(x, a, e, z, e′, z′); - a function S(*x, e*; r).
The properties to satisfy are:

1. R, P, V , E, S and sampling are polynomially computable in |x|;
2. ∀(x, w) ∈ R ∀rP ∀e ∈ E
V (*x, a, e, z*),
with a and z defined by a = P(*x, w*; rP ) and z = P(*x, w, e*; rP );
3. ∀x ∀e, e′ ∈ E ∀a, z, z′
(e ̸= e′, V (x, a, e, z), V (x, a, e′, z′)) =⇒ R(x, E(x, a, e, z, e′, z′));
4. ∀(x, w) ∈ R ∀e ∈ E
distribrP (*a, e, z*) = distribr(S(*x, e*; r)),
with a and z defined by a = P(*x, w*; rP ) and z = P(*x, w, e*; rP ).
What is nice with Σ-protocols is that they are already proofs of knowledge, honest-verifier zero-knowledge, and composable in parallel. This is stated in the results below. Before anything more, we provide an example.

Goldreich-Micali-Wigderson for graph isomorphism.

One example of Σ-protocol is the Goldreich-Micali-Wigderson protocol GMW86 for graph isomorphism from 1986 [35]. It is for the language of pairs of isomorphic graphs (G0, G1). Clearly, a witness can just be the isomorphism
φ from G0 to G1. The obtained protocol could hold for any notion of isomorphism, not only for graphs. We just require that φ is a bijection, that φ(G0) = G1, and that it must be hard to find
φ given G0 and G1 (which is believed to be the case for graphs).

In the GMW86 protocol, the set of challenges is E = {0, 1}. The prover starts by selecting a random permutation π and sending H = π(G0). After receiving e, he answers by σ = π if e = 0
and σ = π ◦ φ−1 if e = 1. So, σ = π ◦ φ−e. Then, the verifier accepts if and only if H = σ(Ge).

σ = π ◦ φ−e σ −−−−−−−−−−−−−−→ σ(Ge) ?= H
The extractor works based on σ0, the answer to e = 0 for some H, and on σ1, the answer to e = 1 for the same H. Since H = σ0(G0) and H = σ1(G1), we have that σ−1
1
◦σ0 is a valid witness for (G0, G1) since σ−1
1
◦ σ0(G0) = G1.

The simulator works based on G0, G1, and e. It picks σ uniformly and sets H = σ(Ge).

Clearly, a malicious prover could cheat by predicting whether the challenge is 0 or 1. More generally, we can always consider the following malicious prover P ∗:
1: pick eguess ∈ E
▷ a guess for e
2: run S(*x, e*guess) → (*a, e*guess, z)
3: send a to the verifier
4: receive the challenge e
5: if e ̸= eguess: abort
▷ the prover failed
6: send z to the verifier Clearly, P ∗ succeeds with probability β =
1
#E . We show below that the Σ-protocol is actually a proof of knowledge with soundness probability β.

Theorem 4.8. A Σ-protocol (P, V ) for an NP language L defined by a relation R is an interactive proof of knowledge for L*. The soundness probability is* β =
1
#E , where E is the set of possible challenges in the Σ-protocol.

Proof. Termination and 1-completeness are straightforward. It is less easy to show the soundness of the proof of knowledge. For that, we define the knowledge extractor EP ∗ as follows. We denote by ε(x) the probability that P ∗ makes V accept on the instance x and we assume that ε(x) *> β*.

To define the extractor, we first pick some random rP , rV , r′
V and make the oracle P ∗ run twice with the same random coins rP and interact with a simulation of V , first with V (rV ), then with V (r′
V ). By construction, the a set by P ∗(rP ) is the same in both executions since rP is the same and no message from V is used to compute a. We let e resp.e′ be the challenge set by V (rV ) resp.

V (r′
V ), and z resp. z′ be the response of P ∗(rP ). We let b resp. b′ be the acceptance bit from the verification. Clearly, if e ̸= e′ and b = b′ = 1, we can execute the Σ-extractor E(x, a, e, z, e′, z′)
and obtain a witness w for x which is given as output of the knowledge extractor. Clearly, all this is polynomially bounded. Below, we prove that Pr[e ̸= e′, b = b′ = 1] ≥ ε(x)(ε(x) − β). Since
ε(x) *> β* and β is a constant, we need O

1
ε(x)−β

attempts of the above process to succeed to extract a witness. This shows the result.

Now, we analyze Pr[e ̸= e′, b = b′ = 1]. When P ∗(rP ) interacts with V (rV ), we have Pr[b =
1] = ε(x). We denote ε(*x, r*P ) = Pr[b = 1|rP ]. Hence, E(ε(*x, r*P )) = ε(x) over a random rP .

Since rV and r′
V are independent, we have Pr[b = b′ = 1|rP ] = ε(*x, r*P )2. So,

Pr[b = b′ = 1, e ̸= e′|rP ] = ε(*x, r*P )2 − Pr[b = b′ = 1, e = e′|rP ]
We note that if e = e′, then P ∗ will give z = z′ so b = b′. Hence,

$$\Pr[b=b^{\prime}=1,e=e^{\prime}|r_{P}]=\Pr[b=1,e=e^{\prime}|r_{P}]$$

Let $A$ be the set of all $e$ for which $P^{*}$ produce a $z$ leading to $b=1$. We have

$$\Pr[b=1,e=e^{\prime}|r_{P}]=\sum_{e\in A}\left(\Pr[\mathsf{pick}\ e]\right)^{2}=\sum_{e\in A}\Pr[\mathsf{pick}\ e]\beta=\varepsilon(x,r_{P})\beta$$
since the challenge is uniformly distributed so Pr[pick e] = β for all e. So, we have

${\rm Pr}[b=b^{\prime}=1,e\neq e^{\prime}|r_{P}]=\varepsilon(x,r_{P})(\varepsilon(x,r_{P})-\beta)$
We consider the random variable Z = ε(*x, r*P ) defined by a random rP . We have Pr[b = b′ = 1, e ̸=
e′|rP ] = f(Z) for f(z) = z(z−β). Since f ′′(z) > 0, f is a convex function, we can apply the Jensen inequality to obtain E(f(Z)) ≥ f(E(Z)). This gives Pr[b = b′ = 1, e ̸= e′] ≥ ε(x)(ε(x) − β).

⊓⊔
Theorem 4.9. Given an integer t and a Σ-protocol with set of challenges E, we consider the
Σt-protocol consisting in executing t times in parallel the Σ-protocol and having the verifier accept if and only if all executions accept. This define a new Σ-protocol in which the set of challenges is Et.

So, the soundness probability is seriously amplified.

Definition 4.10. An interactive proof system (P, V ) is ∗-**honest verifier zero-knowledge** if there exists a PPT algorithm S such that

View
$\left(P(r_P)\overset{x}{\leftrightarrow}V(r_V)\right)$

i.e. 
and S(x, r) produce ∗-identical distributions.

This is just the regular zero-knowledge property, but only guaranteed when the verifier is following the honest protocol.

Theorem 4.11. A Σ-protocol (P, V ) for an NP language L defined by a relation R is honest verifier zero-knowledge. Proof. Since the honest V does not depend on a to select e, we can just run V with some dummy a0 and random coins rV to get e with the good distribution, then run the Σ simulator S(*x, e*; r) on some random r to obtain a transcript (*a, e, z*) with the correct distribution. We can then produce
(*x, a, z*; rV ), the simulated view of V . Clearly, it has the good distribution.

⊓⊔
We can say more if E is small.

Theorem 4.12. A Σ-protocol with a challenge set E with polynomially bounded size is zeroknowledge.

Proof. The simulator works as usual.

1: pick some random coins ρ to set up the verifier
2: pick eguess ∈ E
▷ a guess for e
3: run S(*x, e*guess) → (*a, e*guess, z)
4: send a to the verifier
5: receive the challenge e = V(a; ρ) 6: if e ̸= eguess: rewind and try again
▷ the simulation failed this trial
7: send z to the verifier 8: output (*a, z*; ρ)
In each iteration, we know that (*a, e*guess, z) has a distribution identical to the transcript (*a, e, z*) of an honest execution. Hence, a is statistically independent of eguess. This implies that e = V(a; ρ) is also independent from eguess. Since eguess is uniformly distributed, this implies that a trial succeeds with probability 1/#E. So, it terminates with expected polynomial time. Furthermore, it gives some (*a, z*) which is distributed like for the honest prover. So, we perfectly simulate the protocol.

To summarize what happens with parallel or sequential composition, we recall the following facts.

- The soundness of proof systems amplifies well for both types of composition. - Parallel composition works well with Σ-protocols, but not sequential composition as it destroys the structure of Σ-protocols.
- Zero-knowledge does not always amplify with parallel composition (indeed, we know that Σ-
protocols are zero-knowledge on small challenge sets but could become not zero-knowledge on a large one, e.g. after parallel composition), but amplifies well with sequential composition.
Fiat-Shamir for modular square root.

Another famous example is the FS86 protocol by Fiat and Shamir [27] for the language of pairs of integers (*n, v*) such that v ∈ Z∗
n and there exists s (the witness) such that s2v mod n = 1. Again the set of challenges is E = {0, 1}. The prover starts by selecting a random r ∈ Z∗
n and sending x = r2 mod n. After receiving e, he answers by y = r if e = 0 and y = rs mod n if e = 1, i.e., y = rse mod n. The verifier accepts if y2ve mod n = x, and v, y ∈ Z∗
n.

Prover Verifier s st s2v mod n = 1 (*n, v*) pick r ∈ Z∗ n pick e ∈ {0, 1} x = r2 mod n x −−−−−−−−−−−−−−→ e ←−−−−−−−−−−−−−− y = rse mod n y −−−−−−−−−−−−−−→ y2ve mod n ?= x, v, y ?∈ Z∗ n y0
The extractor is based on the answer ye to e = 0, 1 with the same x. It computes y1/y0 mod n which is such that y1

2 v mod n = 1
so, a valid witness. The simulator picks y ∈ Z∗
n and computes x = y2ve mod n from e.

Schnorr for discrete logarithm.

Finally, another famous protocol is the Schnorr protocol from 1989 [55, 56] for the language of (*G, q, g, y*) tuples with the following properties:

- G is a group in which it is easy to do operations (product and inverse) and comparisons; - g is an element of G of prime order q;
- it is easy to check if a value belongs to ⟨g⟩; - y *∈ ⟨*g⟩.
The relation R is defined by R((G, q, g, y), x) if and only if y = gx. I.e., x is the discrete logarithm of y.

The Schnorr protocol has a parameter t which must be such that *q >* 2t. The set of challenges is E = {1*, . . . ,* 2t}. The prover starts by selecting a random k ∈ Zq and sending r = gk. After receiving e, he answers by s = ex + k mod q. The verifier accepts if rye = gs and y *∈ ⟨*g⟩.

The extractor is based on the answers s and s′ to e and e′, for e ̸= e′, and with the same r. Since q is prime and 1 ≤ e, e′ ≤ 2t < q, e − e′ is invertible modulo q and we can show that s−s′
g e−e′ = y. So, s−s′
e−e′ mod q is the extracted witness. The simulator picks s ∈ Zq and computes r = gsy−e.

Strengthening Σ-protocols.

A malicious verifier could select his challenge e based on the first message sent by the prover. If the set of challenges is very small, this is not a problem and we can actually show that honest-verifier zero-knowledge and zero-knowledge are equivalent. When the set of challenges is large, this is no longer equivalent. In the Schnorr protocol, a malicious verifier could select e = f(*y, r*) and his view may become unforgeable by a simulator. As we will see later, this could indeed be used to construct a signature scheme with unforgeable signatures. However if we do want to obtain a zero-knowledge protocol, we must enrich the Σ-protocol with a commitment.

One solution could be that the verifier first commits to his challenge (without revealing it).

Then, after receiving the first message from the prover, he would open his commitment and let the protocol continue as before. If the commitment is binding (i.e., a malicious verifier could not change his mind), this protocol becomes fully zero-knowledge. However, we now have troubles to prove soundness as we need to extract two answer with the same message from a malicious prover who would have received a commitment of the challenge. One solution to get around this is that we use a trapdoor commitment: a commitment in which there exists a trapdoor to break the binding property. The construction runs as follows:

1. P generates a commitment trapdoor τ and its associated key h and sends h to V ; 2. V selects his challenge e and commit to it with key h; the commit value is sent to P; 3. P starts the Σ-protocol and sends the message a; 4. V opens his commitment to e; 5. P answers to the challenge by z and also discloses τ.
Prover Verifier w st R(*x, w*) x pick rP pick e ∈ E pick τ h = gτ mod p h −−−−−−−−−−−−−−→ Commith(e;r) ←−−−−−−−−−−−−−− pick r a = P(*x, w*; rP ) a −−−−−−−−−−−−−−→ verify Commit(e; r) e,r ←−−−−−−−−−−−−−− z = P(*x, w, e*; rP ) z,τ −−−−−−−−−−−−−−→ V (*x, a, e, z*)?, h ?= gτ mod p
This protocol becomes computationally zero-knowledge and remains a proof-of-knowledge. One example for a trapdoor commitment is the following one.

Pedersen commitment 1991 [47].

We set up the commitment with some parameters (*p, q, g*), where p and q are prime, q divides p − 1, and g is an element of Z∗
p of order q. The trapdoor is an element τ ∈ Zq.

The key is h = gτ mod p.

To commit on X with coins r ∈ Zq, we compute c = gXhr mod p. This is unconditionally hiding, and computationally binding (breaking the binding property is equivalent to computing τ, i.e., solving the discrete logarithm problem for h). With τ, we can equivocate a commitment to X0 with coins r0 to any X. We just set r = r0 + X0−X
τ
mod q and we have

$c=g^{X_0}h^{r_0}\bmod{p}=g^Xh^r\bmod{p}$. 

## 4.4 Setup Models

In the previous strengthened model, the use of an ephemeral trapdoor in the commitment looks artificial, since we never need the equivocation property of the commitment in practice.

Furthermore, it is dangerous for security. We could adopt a more practical approach by having the commitment key to be set up once and for all participants, with the trapdoor held by nobody. This is in line with what we call the *common reference string (CRS)* model. In that case, there is a CRS (e.g., the commitment public key) which is set up for all participants.

To show soundness/zero-knowledge, we may need to assume that the extractor/simulator can use the trapdoor. This is fine, except that one property of zero-knowledge may be a bit trickier: deniability. This assumes that having run the protocol can be denied as the verifier can extract no evidence of having run it in the protocol. Normally, zero-knowledge protocols are inherently deniable since whatever the verifier extracts can be simulated. However, when the simulator needs the trapdoor, since no participant has the trapdoor in practice, what the practical verifier extracts may become non-simulatable. Clearly, this does not expose the secret of the prover but could still leak evidence of having run the protocol.

Besides the CRS, another setup model is the *Random Oracle Model (ROM)*. In this model, we have an oracle H who answers at random to any query, but consistently. I.e., making the same query several times will produce the same response. This oracle can be accessed by all participants. In the notion of zero-knowledge proof of knowledge, the extractor/simulator may further simulate the behavior of H. I.e., they answer at the place of H to all queries, but they must do it in a way which is indistinguishable from querying a real random oracle. Again, we may loose deniability. But otherwise, we can have more efficient protocols. In the strengthening, we commit to e by disclosing H(e∥r) and open by revealing e and r.

There are other setup models. For instance, we can assume that all participants are initialized with a public/private key pair. We can assume the existence of a public directory, to which we could register public keys. We can assume the existence of secure hardware tokens. Etc.

## 4.5 A Building Block For Making Cryptographic Primitives

In 1986, Fiat and Shamir [27] proposed to transform (what is now called) a Σ-protocol into a proof which is non-interactive. This is the notion of a *Non-Interactive Zero-Knowledge proof (NIZK)*.

The idea is that the verifier is now simulated by a hash function. That is, the challenge e used in the Σ-protocol is computed by e = H(x∥a). Namely, to prove x, the prover computes a as usual, then e = H(x∥a), then the answer z. The (*a, z*) pair is the proof. It is verified as usual, by re-computing e.

Note that here, the verifier is choosing e adaptively based on a, which is normally not allowed.

Consequently, we may loose the simulatability. Even worse: we do need to loose this property. Otherwise, a malicious prover could forge a proof by running this simulation!

The Fiat-Shamir construction is also used to create a signature scheme. Essentially, we take e = H(message∥x∥a) and do the same. I.e., the signature is the (*a, z*) pair. We will prove (Th. 6.3
in the next chapter), in the random oracle model, that this construction is secure against existential forgeries under chosen message attacks (EF-CMA), when the relation of the Σ-protocol is such that finding a witness w for x is a hard problem.

Σ-protocols can also be used to construct other cryptographic primitives. As an example, we construct a trapdoor commitment. Assuming that finding a witness for R is hard and that we have a Σ protocol for R, we take as a common reference string and instance x and as a trapdoor a witness w for this instance. So, R(*x, w*) holds. We can commit on elements of the set of challenges E. To commit on e ∈ E, we pick some random coins r and compute (*a, e, z*) = S(*x, e*; r). The commit value is a and the opening value is (*e, z*). For opening, we just check that V (*x, a, e, z*)
holds. We can check that the commitment is perfectly hiding as the distribution of a is like in the correct interactive proof, so independent from e. We can also check that the commitment is computationally binding. Indeed, being able to open a commitment a on two values of e would lead (thanks to the Σ extractor) to a witness for x, which is assumed to be hard to find. Finally, using w we can equivocate the commitment by just running the correct interactive protocol: P produces a, the commit value. Then, if we want to open to e, we just compute the correct z by using w.