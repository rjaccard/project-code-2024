
## Chapter 2 Cryptographic Security Models

In this chapter we formalize more precisely the cryptographic primitives and their security notions. We discuss various security models. We present some general paradigm to formally prove security. We review some public-key cryptographic schemes and study their security, following our formalism.

## 2.1 Security Definitions

Symmetric encryption.

We define block ciphers and also variable-input-length symmetric encryption.

Definition 2.1. A block cipher is a tuple ({0, 1}k(s), Ds, Enc, Dec) with a key domain {0, 1}k(s),
a plaintext domain Ds = {0, 1}n(s), and two polynomially bounded (in terms of s) deterministic
algorithms Enc and Dec.
   It is such that

$\forall s\quad\forall K\in\{0,1\}^{k(s)}\quad\forall X\in{\cal D}_{s}\quad{\sf Dec}_{s}(K,{\sf Enc}_{s}(K,X))=X$
We stress that the encryption is deterministic, here. In the above definition, s appears explicitly as argument of all parameters: the key length k is a function of s, the plaintext domain D is a function of s, and algorithms are *efficient* (i.e. polynomially bounded) in terms of s. Later on, we will take s as an implicit parameter for better readability. We observe the correctness notion in the definition.

We now define variable-input-length symmetric encryption. For completeness, we define it based on a *nonce* (i.e., an extra input which should not be used more than once).

As it is quite common, we restrict to length-preserving encryption. As already announced, the security parameter s is now implicit, and hidden from notations.

Definition 2.2. A (nonce-based, variable-length, length-preserving) symmetric encryption scheme is a tuple ({0, 1}k, D, N, Enc, Dec) with a key domain {0, 1}k, a plaintext domain D ⊆ {0, 1}∗, a nonce domain N*, and two polynomially bounded deterministic algorithms* Enc *and* Dec.

It is such that

$$\forall K\in\{0,1\}^{k}\quad\forall X\in{\mathcal{D}}\quad\forall N\in{\mathcal{N}}\quad{\begin{cases}{\mathsf{Dec}}(K,N,{\mathsf{Enc}}(K,N,X)){=}X\\ {|{\mathsf{Enc}}(K,N,X)|{=}|X|}\end{cases}}$$
Again, this definition includes a correctness notion.

We distinguish several security models, depending on the goal of the adversary (e.g., to do a key recovery or to decrypt a target ciphertext) and on the capabilities of the adversary. The adversary can only collect ciphertexts (in a ciphertext only attack), collect plaintext/ciphertext pairs (in a known plaintext attack), play with an encryption black box and choose the plaintext to be encrypted (in a chosen plaintext attack), or even play with a decryption black box and choose the ciphertext to be decrypted (in a chosen ciphertext attack). Playing with the two black boxes can further be done adaptively or nor. Hence, we describe 6 types of capabilities for 2 possible goals, leading us to 12 security models! To have the highest security, we should protect against the weakest attacks, e.g. decryption under adaptive chosen plaintext / ciphertext attacks.

We first define what is means for a symmetric encryption to be secure against *key recovery*. Key recovery is the goal of the adversary. We consider two types of adversaries, given their capabilities: those making chosen plaintext attacks, and those making chosen plaintext and ciphertext attacks.

Definition 2.3. *A symmetric encryption scheme* ({0, 1}k, D, N, Enc, Dec) is secure against key recovery under chosen plaintext attacks (CPA) if for any PPT algorithm A*, the advantage* Adv is negligible, where we define Adv = Pr[game returns 1]
In the following game: Game
1: K
$←− {0, 1}k
2: Used ← ∅
3: AOEnc → K′
4: **return** 1K=K′
Oracle OEnc(N, X):
5: if N ∈ Used **then return** ⊥
▷ nonce-respecting: cannot reuse N
6: Used ← Used ∪ {N}
7: *return* Enc(*K, N, X*)
The probability is over the random selection of K and the random coins of A.

The symmetric encryption scheme is secure against key recovery under chosen plaintext/ciphertext attacks (CPCA) if for any similar A*, the advantage* Adv is negligible in the following game:
Game Oracle OEnc(N, X):
Oracle ODec(N, Y ):
1: *return* Dec(*K, N, Y* )
1: K
$←− {0, 1}k
1: if N ∈ Used **then return** ⊥ 2: Used ← Used ∪ {N}
3: *return* Enc(*K, N, X*)
2: Used ← ∅
3: AOEnc,ODec → K′
4: **return** 1K=K′
In this definition, we say that an adversary is *nonce-respecting* if he never makes two encryption queries with the same nonce. In practice, this may come from the nonce being picked by the encryption device, so under no control of the adversary. He may make several decryption queries with the same nonce though.

The motivation to introduce CPCA security is to be able to assess the security of the scheme when used in an application. Indeed, the decryptor will receive input from insecure places which can depend on the adversary, so the worst case consists of saying that the adversary selects the input. Similarly, the result will go to some processing and produce visible reactions to the adversary. In the worst case, we assume that the adversary sees the output of decryption.

We now define security against decryption attacks, in which the goal of the adversary is to decrypt one given ciphertext.

Definition 2.4. *A symmetric encryption scheme* ({0, 1}k, D, N, Enc, Dec) is secure against decryption under CPA [resp. CPCA] if for any PPT algorithm A*, the advantage* Adv is negligible, where we define Adv = Pr[game returns 1]
In the following game:
Game Oracle OEnc(N, X):

$i\colon\,K\xleftarrow{\mathbb{S}}\{0,1\}^k$

$\mathcal{D}\colon\,X_0\xleftarrow{\mathbb{S}}\mathcal{D},\,N_0\xleftarrow{\mathbb{S}}\mathcal{N}$

$\mathcal{D}\colon\,Y_0\gets\mathsf{Enc}(K,\,N_0,\,X_0)$
1: if N ∈ Used **then return** ⊥
2: Used ← Used ∪ {N}
3: *return* Enc(*K, N, X*)
Oracle ODec(N, Y ):

3: $Y_0\gets\mathsf{Enc}(K,N_0,X_0)$
4: $\mathsf{Used}\gets\{N_0\}$
5: $\mathsf{ACE}[,\mathsf{ODec}](N_0,Y_0)$
...

5: AOEnc[,ODec](N0, Y0) → X
6: *return* 1X=X0
4: if (*N, Y* ) = (N0, Y0) then return ⊥
5: *return* Dec(*K, N, Y* )
(The ODec oracle is only used in the CPCA model.)
We can easily see that security against decryption attacks is stronger than security against key recovery.

Theorem 2.5. *Let* E = ({0, 1}k, D, N, Enc, Dec) be a symmetric encryption scheme. If E is secure against decryption under chosen plaintext (resp. chosen plaintext/ciphertext) attacks, then E is secure against key recovery under chosen plaintext (resp. chosen plaintext/ciphertext).

Proof. Let E be a symmetric encryption scheme which is secure against decryption attacks. Let A be a key recovery adversary. We define the following decryption adversary B:
Input: (*N, Y* )
1: run A → K′
2: compute X′ = Dec(K′*, N, Y* )
3: **return** X′
Clearly, any key recovery implies arbitrary decryption capabilities. So, Pr[BEnc(*K,.,.*)(N, Enc(K, N, X)) →
X] ≥ Pr[AEnc(*K,.,.*) → K]. If the former is negligible (because the encryption is secure against decryption attacks), the latter must be negligible as well. So, E is secure against key recovery.

⊓⊔
Finally, we formalize security against distinguishers, where the goal of the adversary is to distinguish whether the *real* cipher Enc is used or the *ideal* one Π.

Definition 2.6. *A symmetric encryption scheme* ({0, 1}k, D, N, Enc, Dec) is secure against distinguisher (real or ideal) under CPA [resp. CPCA] if for any PPT algorithm A, the advantage Adv is negligible, where we define

$$\mathrm{Adv}=\mathrm{Pr}[\Gamma_{1}\,\,\,{\mathrm{_returns}}\,\,1]-\mathrm{Pr}[\Gamma_{0}\,\,\,{\mathrm{_returns}}\,\,1]$$
Oracle OEnc(N, X):
Game Γb
1: if N ∈ Used **then return** ⊥
1: K
$←− {0, 1}k
2: Used ← Used ∪ {N}
3: if b
=
0
then return
ΠN(X)
2: for every N, pick a lengthpreserving permutation ΠN
over D
4: *return* Enc(*K, N, X*)
Oracle ODec(N, Y ):
3: Used ← ∅
4: AOEnc[,ODec] → z
5: **return** z
5: if b
=
0
then return
Π−1
N (Y )
6: *return* Dec(*K, N, Y* )
We can show that this notion is stronger than security against decryption attacks.

Theorem 2.7. *Let* E = ({0, 1}k, D, N, Enc, Dec) be a symmetric encryption scheme. If E is secure under chosen plaintext (resp. chosen plaintext/ciphertext) attacks, then E is secure against decryption under chosen plaintext (resp. chosen plaintext/ciphertext) attacks.

Proof. Let E be a symmetric encryption scheme which is secure. Let A be a decryption adversary.

We define the following distinguisher BO(·) having access to an oracle O(·):
1: pick X, query Y *← O*(X)
▷ encrypt X
2: run AO(·)(Y ) → X′
3: output 1X=X′
We have

$$\Pr[\mathcal{B}^{\mathsf{Bnc}(K,\ldots)}\to1]-\Pr[\mathcal{B}^{\mathsf{H}(\ldots)}\to1]=\Pr[\mathcal{A}^{\mathsf{Bnc}(K,\ldots)}(N,\mathsf{Enc}(K,N,X))=X]-\Pr[\mathcal{A}^{\mathsf{H}(\ldots)}(N,\mathsf{H}(N,X))=X]$$ $$\geq\Pr[\mathcal{A}\text{wing}]-\mathsf{negl}(s)$$
because we show below that Pr[AΠ(.,.)(N, Π(*N, X*)) = X] = negl(s). So, if E is secure against distinguishers, we deduce that Pr[A wins] must be negligible, so E is secure against decryption attacks as well.

The Pr[AΠ(.,.)(N, Π(*N, X*)) = X] = negl(s) bound is obtained as follows:

$$\Pr[\mathcal{A}^{\Pi(\cdots)}(N,\Pi(N,X))=X]=\Pr[\mathcal{A}^{\Pi(\cdots)}(N,Y)=\Pi^{-1}(N,Y)].$$
where Y is random. Then, we wonder if Y was answered by the encryption oracle to any query by A. We have Pr[AΠ(.,.)(N, Π(*N, X*)) = X]
=
Pr[AΠ(.,.)(*N, Y* ) = Π−1(N, Y ), Y not answered] + Pr[AΠ(.,.)(*N, Y* ) = Π−1(N, Y ), Y answered]
≤
Pr[AΠ(.,.)(*N, Y* ) = Π−1(N, Y ), Y not answered] + Pr[Y answered]
=
Pr[AΠ(.,.)(*N, Y* ) = Π−1(*N, Y* )|Y not answered] Pr[Y not answered] + Pr[Y answered]
≤
Pr[AΠ(.,.)(*N, Y* ) = Π−1(*N, Y* )|Y not answered] + Pr[Y answered]
≤
1
#D − q + Pr[Y answered]
=
1
#
i=1
Y answered to ith fresh query

$$\frac{\cdot}{\#\mathsf{D}-q}+\Pr\left[\bigvee_{i=1}^{q}\right.$$ $$\leq\frac{1}{\#\mathsf{D}-q}+\sum_{i=1}^{q}\Pr[Y\text{answered to}i\text{th fresh query}]$$ $$=\frac{1}{\#\mathsf{D}-q}+\sum_{i=0}^{q-1}\#\mathsf{D}-i$$ $$\leq\frac{q+1}{\#\mathsf{D}-q}$$ $$\leq\mathsf{negl}(s)$$
Message authentication code.

We similarly define a MAC.

Definition 2.8. A message authentication code *is a tuple* ({0, 1}k, D, {0, 1}τ, MAC) with a key domain {0, 1}k, a message domain D ⊆ {0, 1}∗, an output domain {0, 1}τ, and one polynomially bounded deterministic algorithm MAC implementing a function

$$\begin{array}{r l r l}{{\mathsf{M A C}}:}&{{}\{0,1\}^{k}\times{\mathcal{D}}}&{{}\longrightarrow}&{}&{\{0,1\}^{\tau}}\\ {}&{{}}&{{}}&{{}(K,X)}&{{}\longmapsto}&{{\mathsf{M A C}}_{K}(X)}\end{array}$$
Definition 2.9. *A message authentication code* ({0, 1}k, D, {0, 1}τ, MAC) is secure against key recovery under chosen message attacks if for any PPT algorithm A*, the advantage* Adv is negligible, where we define Adv = Pr[game returns 1]
In the following game: Game
1: K
$←− {0, 1}k
2: AOMac → K′
3: **return** 1K=K′
Oracle OMac(X):
4: *return* Mac(*K, X*)
Of course, there is a similar notion with *known message attacks*.

Definition 2.10. *A message authentication code* ({0, 1}k, D, {0, 1}τ, MAC) is secure against forgery under chosen message attacks if for any PPT algorithm A*, the advantage* Adv is negligible, where we define Adv = Pr[game returns 1]
In the following game:
Game
1: K
$←− {0, 1}k
2: Queried ← ∅
3: AOMac → (*X, t*)
4: if X ∈ Queried **then return** 0
5: *return* 1Mac(K,X)=t Oracle OMac(X):
6: Queried ← Queried ∪ {X}
7: *return* Mac(*K, X*)
Of course, there is a similar notion with *known message attacks*.

Theorem 2.11. *Let* M = ({0, 1}k, D, {0, 1}τ, MAC) be a message authentication code. If M is secure against forgery under chosen message attacks, then E is secure against key recovery under chosen message attacks.

Proof. Let M be a MAC which is secure against forgery attacks. Let A be a key recovery adversary. We define the following forgery adversary B:
1: run AO(·) → K
2: get an arbitrary X
3: compute t = MAC(*K, X*)
4: **return** (*X, t*)
Clearly, negl(s) = Pr[BMAC(K,.) forges] ≥ Pr[AMAC(K,.) → K]. So, M is secure against forgery attacks.

⊓⊔
Just like for symmetric encryption, there is also a notion of security against distinguishers.

However, the most appropriate security notion for MAC is unforgeability.

When it is secure against distinguishers, we rather call them as *PRF*, for *pseudorandom functions*.

Definition 2.12. *A message authentication code* ({0, 1}k, D, {0, 1}τ, MAC) *is a* pseudorandom function (PRF) if for any PPT algorithm A*, the advantage* Adv is negligible, where we define Adv = Pr[Γ1 *returns* 1] − Pr[Γ0 *returns* 1]
In the following game:

Oracle O(N, X):
Game Γb

1: K
$←− {0, 1}k

1: if b = 0 *then return* F ∗(X)
2: **return** F(*K, X*)

2: pick F ∗ : D → {0, 1}τ
3: AO → z
4: **return** z Theorem 2.13. *Let* M = ({0, 1}k, D, {0, 1}τ, MAC) be a message authentication code. If M is a PRF and 2−τ is negligible, then E is secure against forgery under chosen message attacks.

Proof. Let M be a PRF. Let A be a forgery adversary. We define the following distinguisher B:
1: run AO(·) → (*X, t*)
2: query t′ ← O(X)
▷ authenticate X
3: output 1t=t′
We have

$$\begin{array}{rcl}\mbox{negl}(s)&=&\Pr[\mathcal{B}^{\mbox{MAC}}(K_{\cdot}.)\to1]-\Pr[\mathcal{B}^{F}(\cdot)\to1]\\ &=&\Pr[\mathcal{A}^{\mbox{MAC}}(K_{\cdot}.)\mbox{wins}]-\Pr[\mathcal{A}^{F}(\cdot)\mbox{wins}]\end{array}$$
Since Pr[AF (·) wins] = 2−τ = negl(s), we obtain that Pr[A wins] − 2−τ = negl(s). So, the MAC is secure against forgery attacks.

⊓⊔
Key agreement.

For the security of key agreement, we consider *passive adversaries* who let the honest execution of the protocol run and watch the *transcript* of the protocol (i.e., the list of exchanged messages between Alice and Bob). We can consider *key recovery* attacks, the purpose of which is to recover K from the transcript, and *distinguishers*, who try to recognize if a given value K′ is equal to the unknown value of K or just a random value. More formally, for key recovery attacks A, the advantage is Adv = Pr[Game returns 1] in the game Game
1: pick ra, rb
2: execute A(1s; ra) ↔ B(1s; rb)
3: get transcript and K
4: run A(1s, transcript)
$−→ K′
5: **return** 1K=K′
For distinguishers A, the advantage is Adv = Pr[Γ1 returns 1] − Pr[Γ0 returns 1] in the game Game Γb
1: pick ra, rb
2: execute A(1s; ra) ↔ B(1s; rb)
3: get transcript and K1
4: pick K0 of same length as K1 at random
5: run A(1s, transcript, Kb)
$−→ z
6: **return** z Security against *active adversaries* is more subtle. Actually, if an adversary is active and can modify on-the-fly messages which are sent between Alice and Bob, since none of them has any private input, he can simulate Bob to interact with Alice and simulate Alice to interact with Bob.

The adversary would end up sharing an output K1 with Alice and an output K2 with Bob. This type of *man-in-the-middle* attack is unavoidable, simply because communication is not authenticated. So, we cannot consider security against this type of attack. There may be a more subtle active attack making sure that K1 = K2. If such attack is possible, then the adversary can corrupt the key agreement phase and later remain passive while Alice and Bob communicate based on the agreed key. Protocols should resist to this type of man-in-the-middle attacks making K1 = K2.

Public-key cryptosystem.

Just like for symmetric encryption, we can propose formal definitions.

Definition 2.14. A public-key cryptosystem *is a tuple* (Gen, M, Enc, Dec) with a plaintext domain M *and three polynomially bounded algorithms* Gen, Enc*, and* Dec*. The algorithm* Dec is deterministic and outputs either something in M or an error ⊥. It is such that

$$\forall\mathsf{pt}\in{\mathcal{M}}\quad\Pr_{r_{g},r_{c}}[\mathsf{Dec}(\mathsf{sk},\mathsf{Enc}(\mathsf{pk},\mathsf{pt};r_{c}))=\mathsf{pt}]=1$$
where (pk, sk) = Gen(1s; rg).

We could define security against key recovery or decryption attacks, but we rather proceed directly to security against distinguishers.

Definition 2.15. *A PKC* (Gen, M, Enc, Dec) is secure under chosen plaintext attacks (IND-CPA-
secure) if for if for any PPT algorithm A*, the advantage* Adv is negligible, where we define

$$\mathrm{Adv}=\mathrm{Pr}[\Gamma_{1}\,\,\,{\mathrm{_returns}}\,\,1]-\mathrm{Pr}[\Gamma_{0}\,\,\,{\mathrm{_returns}}\,\,1]$$
In the following game:

$Game\ \Gamma_b$  
$\textsf{1:}\ \textsf{Gen}\stackrel{\mathbb{S}}{\rightarrow}(\textsf{pk},\textsf{sk})$  
$\textsf{2:}\ \mathcal{A}_1(\textsf{pk})\stackrel{\mathbb{S}}{\rightarrow}(\textsf{pt}_0,\textsf{pt}_1,\textsf{st})$  
$\textsf{3:}\ \textsf{if}\ |\textsf{pt}_0|\ \not=|\textsf{pt}_1|\ \textsf{then return}$  
$\begin{array}{ll}0\\ \textsf{4:}\ \textsf{ct}\stackrel{\mathbb{S}}{\leftarrow}\textsf{Enc}(\textsf{pk},\textsf{pt}_b)\\ \ \ \ 5\text{:}\ \mathcal{A}_2(\textsf{st},\textsf{ct})\stackrel{\mathbb{S}}{\rightarrow}z\\ \ \ 6\text{:}\ \textsf{return}\ z\end{array}$  
.

It is secure under chosen plaintext/ciphertext attacks (IND-CCA-secure) if the same holds with the following game.

$$G a m e\ \Gamma_{b}$$
Oracle ODec1(ct):
1: *return* Dec(sk, ct)

* [11]**Gen $\stackrel{{\mbox{\scriptsize$\mathbf{\hat{S}}$}}}{{\rightarrow}}$ (pk, sk)**
* [12]**ODec $\cdot$ (pk)**
Oracle ODec2(ct):

$\textsf{2:}\mathcal{A}^\textsf{ODE_1}_1(\textsf{pk})$
$\stackrel{\text{3}}{\to}(\textsf{pt}_0,\textsf{pt}_1,\textsf{st})\\ \hspace{3.3in}if\ |\textsf{pt}_1|\ \not=\textsf{pt}_1|\ \textsf{then\ ret}_1$
3: if |pt0| ̸= |pt1| then return
0
2: if ct = ct∗ **then return** ⊥
3: *return* Dec(sk, ct)

4: $\mathsf{ct^*}\xleftarrow{\$}\mathsf{Enc}(\mathsf{pk},\mathsf{pt_b})$

5: $\mathcal{A}^{\mathsf{ODec_2}}_2(\mathsf{st},\mathsf{ct^*})\xrightarrow{\$}z$

6: $\mathsf{return}\ z$
6: **return** z
(The IND-CPA game is depicted in Fig. 2.1. The IND-CCA game is in Fig. 2.2.) As we can see from this definition, no deterministic encryption can be IND-CPA secure, because the adversary could encrypt pt0 and pt1 by himself and compare with c. So, modern cryptosystems are probabilistic.

For cryptosystems encrypting plaintexts of variable length, it is required that the length of pt0
and pt1 is the same, since it is impossible to perfectly hide the length of a plaintext on infinite message spaces.

The *semantic security* aims at saying that every bit of information is hard to compute. It was proposed with the Goldwasser-Micali cryptosystem [31, 32], which only encrypts a bit.

There exist stronger security notions.

For instance, we may consider the non-malleability security [25]. Intuitively, it means that an adversary cannot replace a ciphertext ct (with unknown Dec(ct) to him) into another ciphertext ct ̸= ct′ such that Dec(ct) and Dec(ct′) are "related". This actually looks like an integrity protection for the plaintext.

One example where this notion of security is not satisfied is the traditional family of stream ciphers, where ct = pt ⊕ k. Indeed, replacing ct by ct′ = ct ⊕ δ leads to Dec(ct) and Dec(ct′) to be within a difference of δ. We can call this a relation and then have the malleability property.

There is a theorem saying that non-malleability is equivalent [4] to the *IND-CCA security* [51].

IND-CCA security historically followed another notion called IND-CCA1 security or lunchtime attack [44], where the adversary was not allowed to make decryption queries after having received the challenge y.
 
In general, "textbook cryptosystems" are not IND-CCA-secure because they are malleable, with some kind of homomorphic property. For instance, the ElGamal cryptosystem has the property that if x is the decryption of (*u, v*), then xw is the decryption of (*u, vw*). So, the adversary can take the challenge y = (*u, v*), compute y∗ = (*u, vw*), make a decryption query with y∗, divide the result by w and compare with x0 and x1 to deduce b.

Digital signature scheme.

We have similar definitions as for MAC.

Definition 2.16. A digital signature scheme *is a tuple* (Gen, D, Sig, Ver) with a message domain D ⊆ {0, 1}∗ *and three PPT algorithms* Gen, Sig*, and* Ver*. The algorithm* Ver is deterministic and outputs 0 (reject) or 1 (accept). It is such that

$\forall X\in D$$\Pr\left[\text{Ver}(\text{pk},X,\text{Sig}(\text{sk},X;r_{s}))=\text{ok}\right]=1$
where (pk, sk) = Gen(1s; rg).

We proceed directly to the security against forgery attacks.

Definition 2.17. *A digital signature scheme* (Gen, D, Sig, Ver) is secure against existential forgery under chosen message attacks (EF-CMA) if for any PPT algorithm A*, the advantage* Adv is negligible, where we define Adv = Pr[*game returns* 1]
In the following game:

Game
1: Gen
$−→ (pk, sk)
2: Queries ← ∅
3: AOSig(pk) → (*X, σ*)
4: if X ∈ Queries **then return** 0
5: *return* 1Ver(pk*,X,σ*)
Oracle OSig(X):
6: σ ← Sig(sk, X) 7: Queries ← Queries ∪ {X}
8: **return** σ
There is also a stronger security notion, in which the adversary could have obtained a signature of X from the oracle, but the forgery must be *another* signature.

Definition 2.18. *A digital signature scheme* (Gen, D, Sig, Ver) is strongly secure against existential forgery under chosen message attacks (strong EF-CMA) if for any PPT algorithm A, the advantage Adv is negligible, where we define

$$\mathrm{Adv}=\mathrm{Pr}[g a m e\ r e t u r n s\ 1]$$
In the following game:
Game
1: Gen
$−→ (pk, sk)
2: Queries ← ∅
3: AOSig(pk) → (*X, σ*)
4: if (*X, σ*) ∈ Queries **then return** 0
5: *return* 1Ver(pk*,X,σ*)
Oracle OSig(X):
6: σ ← Sig(sk, X) 7: Queries ← Queries ∪ {(X, σ)}
8: **return** σ

## 2.2 The Game Proof Methodology

There is a common technique to prove security based on game reduction. It was formalized by Shoup in 2004 [59]. Indeed, most of the security results can be formalized in terms of an adversary running a game (defined by rules), with a final winning condition. We assume that the game and the winning condition can be efficiently computed by a simulator. The proof technique consists of building up a sequence of games and their associated adversaries in such a way that the initial game is the one to be proven, the final one is trivial to analyze, and we can show that every step makes the winning probabilities similar, except with some negligible gap. There are several tools for making these different steps.

First of all, we can consider an *indistinguishability step*. We start with a game Γ with an adversary A, in which there is somewhere the selection of some random variable X based on some fresh coins which are not used any longer. We build a new game Γ′ with the same adversary A, but the selection of X is replaced by the selection of some Y such that X and Y have indistinguishable distributions. Assuming that X or Y come from outside the game, the simulation of the entire game with an outcome set to the winning condition becomes a distinguisher between X and Y .

So, the winning probability must be very close for both games.

Second, we can use the *difference Lemma*. In a game Γ, we consider a "failure event F", for some event F which can be efficiently checked and such that the game becomes somehow simpler when F does not occur. We define a new game Γ′ in which ¬F is an extra condition for winning.

If ¬F occurs, the game Γ′ works exactly like in Γ. The gap between the winning probability is bounded by Pr[F]. Indeed, the probability to win in Γ is

$$\operatorname*{Pr}[{\mathsf{w i n}}]=\operatorname*{Pr}_{\Gamma}[{\mathsf{w i n}},F]+\operatorname*{Pr}_{\Gamma}[{\mathsf{w i n}},\neg F]$$
The first probability is bounded by Pr[F]. The second one is equal to PrΓ′[win], the winning probability in Γ′.

Finally, we can consider *bridging steps* where a game Γ and an arbitrary adversary A are replaced by a game Γ′ and an adversary C(A) such that the simulation of Γ(A) and Γ′(C(A)) are exactly the same. Here are some examples.

- We can permute two independent steps.
- We can make a "double bridge": bridge Γβ(A) to Γ′
β(C(A)) for β = 0, 1, because it will be
easier to connect Γ′
0(C(A)) to Γ′
1(C(A)).

## 2.3 Goldwasser-Micali Cryptosystem

In the Goldwasser-Micali cryptosystem [31, 32], the public key consists of a pair (*x, N*) where N = pq, the product of two large primes, and x ∈ Z∗
N which is neither a quadratic residue modulo p nor modulo q (see Fig. 2.3). To encrypt b, we select r ∈ Z∗
N and give y = r2xb mod N. To decrypt, we just find b such that (−1)b = (y/p). This is semantically secure. (Actually, since we encrypt a bit, semantic security is equivalent to the hardness of the decryption problem.)
The semantic security definition is a bit complicated but it was shown to be equivalent to the IND-CPA one.

In the case of the Goldwasser-Micali cryptosystem, the message space has only two elements:
the message 0 and the message 1.

So, the only relevant case reduces to x0 = 0 and x1 =
1.

Therefore, IND-CPA security is equivalent to the decryption hardness: to having Pr[b =
A(pk, Enc(b; r); ρ)] − 1
2 negligible. For the Goldwasser-Micali cryptosystem, this means Pr[b =
A(*x, N, r*2xb mod N; ρ)] = 1
2 + negl(λ).

There is an equivalent definition proposed with a slightly different game [53] in which the adversary only proposes one plaintext x0, and either this one is selected, or a random x1 one (see Fig 2.4).

Definition 2.19. *A cryptosystem* (Gen, Enc, Dec) is IND$-CPA-secure if for any PPT algorithm A*, the advantage* Adv is negligible, where we define

$$\mathbf{\hat{z}}$$

$\mathrm{Adv}=\Pr[\Gamma_{1}\ returns\ 1]-\Pr[\Gamma_{0}\ returns\ 1]=2\left(\Pr[z=b]-\frac{1}{2}\right)$
In the following game:

1: Gen
$−→ (pk, sk)
2: A1(pk)
$−→ (pt0, st)
3: pick pt1 *of same length as* pt0
4: ct
$←− Enc(pk, ptb)
5: A2(st, ct)
$−→ z
6: **return** z
This game is often called the *real-or-random* encryption game while the previous IND-CPA game is called the *left-or-right* encryption game.

Theorem 2.20. IND-CPA security and IND$-CPA security are equivalent.

Proof. To show this, we first show that IND-CPA security implies IND$-CPA security. We consider an adversary A in the real-or-random game. Let us transform it into an adversary A′ in the leftor-right game (see Fig. 2.5). To define A′(pk; ρ′), we first run pt0 = A(pk; ρ) and select pt1 of same length of pt0. To define ρ from ρ′, we just run A(pk; ρ′) by watching at which coins in ρ′ are used by A. The next unused coins are taken to select pt1. Finally, ρ is just ρ′ without the coins used for pt1 (that is, the left over coins are let in ρ for the next part). Then, we set (pt0, pt1) = A′(pk; ρ′)
and we define A′(pk, ct; ρ′) = A(pk, ct; ρ). Clearly, A′ simulates well the selection of pt1. So, A and A′ win with exactly the same probabilities in their respective game. Due to IND-CPA security, A′ wins with probability 1
2 + negl. So, A wins with probability 1
2 + negl. Since this applies to any A, we obtain IND$-CPA security.

Then, we show that IND$-CPA security implies IND-CPA security. For that, we consider an adversary A in the left-or-right game. We define an adversary A′ in the real-or-random game as follows. We let A′(pk; ρ′) = ptβ where A(pk; ρ) = (pt0, pt1) and β is one coin from ρ′ which is just removed to define ρ. I.e., ρ′ = β∥ρ. Then, A′(pk, ct; ρ′) = A(pk, ct; ρ) ⊕ β. We let b be the bit selected by the challenger to define ct = Enc(ptβ) if b = 0 or ct = Enc(random) otherwise.

(See Fig. 2.6.) Let p be the probability for A to win in the IND-CPA game. In our construction, when b = 0, we have Pr[b = A′(pk, ct; ρ′)|b = 0] = p since this case perfectly simulates the IND-
CPA game. When b = 1, ct gives no information about β, so Pr[b = A′(pk, ct; ρ′)|b = 1] = 1
2 = 1
2.

So, Pr[b = A′(pk, ct; ρ′)] − 1
2(p − 1

                                          2). Due to IND$-CPA security, A′ wins with probability
1
2 + negl. So, A wins with probability p =
                                                  1
                                                  2 + negl.
                                                              Since this applies to any A, we obtain
IND-CPA security.
                                                                                                        ⊓⊔

The Goldwasser-Micali cryptosystem is not IND-CCA secure. Given y = r2xb mod N, we can compute s2xcy mod N for a random s and a random bit c. This would be a valid encryption of b ⊕ c with a correct distribution. If we can decrypt this new ciphertext, then XOR the result to c, we obtain b.

## 2.4 Rsa Security

The textbook RSA cryptosystem is depicted in Fig. 3.1.

To assess the security of RSA, we essentially consider two problems:

- the RSA decryption problem: given an RSA public key (*e, N*) and a ciphertext y, compute
x such that y = xe mod N.
- the RSA key recovery problem: given an RSA public key (*e, N*), find a number d such that
for all x ∈ Z∗
N we have xed mod N = x.1
We will compare them with some problems from number theory:

- the RSA factoring problem: given an RSA modulus N, find the factors p and q. - the RSA order problem: given an RSA modulus N, compute φ(N), the order of Z∗
N.
- the RSA exponent multiple problem: given an RSA modulus N, find an integer k which is
a positive multiple of λ(N).
As for the last problem, we recall that the set of all k's such that ∀x ∈ Z∗
N
xk mod N = 1
is an ideal of the ring Z and that λ(N) is the smallest positive such k. Since Z is a principal ring, this ideal is generated by λ(N). Consequently, k is a multiple of λ(N) if and only if ∀x ∈
Z∗
N
xk mod N = 1.

We can show, using Turing reductions, that the three above problems from number theory are equivalent to the RSA key recovery problem and that the RSA decryption problem reduces to the RSA key recovery problem. However, these two problems are not known to be equivalent although both are believed to be hard to solve.

RSA decryption reduces to RSA key recovery.

This is essentially trivial: assuming that we have an oracle solving the RSA key recovery problem, given an instance (*e, N, y*) of the RSA
decryption problem, we can submit (*e, N*) to the oracle and get d such that for all y ∈ Z∗
N, yed mod N = y. So, by taking x = yd mod N, we obtain that xe mod N = y. This is just a complicated way to say that if we can recover the secret key, then we can apply the decryption algorithm to decrypt y! RSA key recovery reduces to the RSA order problem.

Assuming that we have an oracle which can compute φ(N) from the RSA modulus N, given an RSA public key (*e, N*), we can first get φ(N) using the oracle, then compute d = e−1 mod φ(N). Clearly, for all x ∈ Z∗
N, we have xed mod N = x. So, this solves the RSA key recovery problem.

The RSA exponent multiple problem reduces to RSA key recovery.

Given an oracle which computes d from (*e, N*), the number k = ed − 1 satisfies xk mod N = 1 for all x ∈ Z∗
N. So, we can solve the RSA exponent multiple problem by taking a valid e. I.e., if we take a random e and that by any chance we have gcd(*e, φ*(N)) = 1, we solve the problem. It is not guaranteed what happens when e is not valid since we don't know that the oracle returns (if it returns anything)
in that case. What we could do is to iterate on random e's and compute the lcm of all obtained k's. Since eventually we will have a good e, it will return a solution k and the lcm will be another solution.

1Actually, using the Chinese Remainder Theorem, it is easy to see that if we have xed mod N = x for all x ∈ Z∗
N, then we have it for all x ∈ ZN.

xt mod n - ̸= 1 SQ - ̸= 1 SQ - ̸= 1 · · · - ̸= 1 SQ - ̸= 1 SQ - 1 at most s z }| { ? 6 is it *≡ −*1?
The RSA order problem reduces to RSA factoring.

Given an oracle computing p and q from N, it is clear that we can compute φ(N) = (p − 1)(q − 1).

RSA factoring reduces to the RSA order problem.

Conversely, given an oracle computing
φ(N) from N, we notice that p + q = N − φ(N) + 1 and pq = N. So, the quadratic equation X2 − (N − φ(N) + 1)X + N = 0 over R has p and q as roots. Since it is easy to solve these equations in R, we solve the RSA factoring problem. RSA factoring reduces to the RSA exponent multiple problem.

This is the most tricky reduction. Assuming an oracle giving an exponent multiple k from N, we factor N as follows:
first, we write k = 2st for some integers s and t such that t is odd (i.e., we iteratively divide by
2, s times in total, until the result t becomes odd). We know that for all x ∈ Z∗
N, if we square iteratively s times the residue xt mod N, we must obtain 1. We pick x ∈ ZN *− {*0} at random.

If gcd(*x, N*) ̸= 1, we find either p or q by some incredible chance and can stop. Otherwise, we deduce that x ∈ Z∗
N. We compute y = xt mod N. If y = 1, this is bad luck and we try again.

Otherwise, we iteratively square y until y2 mod N = 1. If y *≡ −*1 (mod N), this is bad luck and we try again. Otherwise, y is a square root or 1 which is neither 1 nor −1. So, (y − 1)(y + 1) is a multiple of N = pq such that neither y − 1 nor y + 1 is a multiple of N. So, gcd(y − 1, N) is either p or q and we solve the factoring problem (see Fig. 2.7).

To prove that this works, we define sp and sq such that p−1
2sp and q−1
2sq are odd, then s′ =
max(sp, sq) − 1. Since k is a multiple of λ(N) = lcm(p − 1, q − 1), it is a multiple of p − 1, so a multiple of 2sp as well. So, sp ≤ s. Similarly, sq ≤ s. Hence, 0 ≤ s′ < s. The mapping x 7→ x2s′t over Z∗
p is a group homomorphism. Let Hp be the set of images of this function. Clearly, Hp is a subgroup of {1, −1}. If s′ ≥ sp, this is Hp = {1}. Otherwise, for s′ = sp − 1, we know that a non-quadratic residue x modulo p would map to −1, so Hp = {1, −1}. We define Hq similarly.

Without loss of generality, we assume that sp ≥ sq. So, Hp = {1, −1}. Then we consider the mapping x 7→ x2s′−1t over Z∗
N. This is a group homomorphism onto a group H which is isomorphic to Hp × Hq due to the Chinese remainder theorem. If sp = sq, we have Hq = {1, −1}. So, H
contains four elements, including 1 and −1, and two "interesting" ones. (I.e., equal to 1 modulo either p or q but not both, and equal to −1 modulo either p or q but not both.) Otherwise, for sp *> s*q, we have Hq = {1}. So, H contains two elements, including 1 and an "interesting" one.

In both cases, half of the element are "interesting". I.e., they are non-known square roots of 1.

Since the mapping x 7→ x2s′−1t is homomorphic, it is balanced from Z∗
N to H. Hence, mapping a random element x gives an "interesting" element of H with probability 1
2. So, the above produce works with probability at least 1
2 in one iteration. By iterating enough, it works, eventually.

To conclude, RSA key recovery is equivalent to RSA factoring and to computing φ(N) or any multiple. RSA decryption reduces to this but may be simpler. The equivalence is an open research problem.

Previously, we considered the security of encryption in terms of *key recovery* and decryption problems. These security notions may be insufficient. For instance, a cryptosystem doing nothing
(i.e., with a ciphertext y equal to the plaintext x no matter x or the secret key) makes key recovery hard but is clearly insecure. A cryptosystem only encrypting one part of the message may make the full decryption hard but would leak sensitive information and be considered as insecure. Recovering one particular bit of the plaintext may be sensitive, and still be feasible without decrypting completely.

In RSA, we can prove that recovering the least significant bit of the plaintext is equivalent to decrypting completely. So, if the decryption problem is hard, the least significant bit is called a hard-core bit.

More precisely, we define lsb(x) to be the least significant bit of x and lsbdec(y) to be the lsb of the decryption of y. We show below that the RSA decryption problem reduces to computing lsbdec. For that, we assume that we have a subroutine to compute lsbdec and we show that we can decrypt y given the public key (*e, N*).

Let us now assume that we know that the decryption x of y is in some interval a ≤ *x < b* with a = k
2i N and b = k+1
2i N for some integers k and i. Note that we can start with k = 0 and i = 0.

We can see now how to update k and increment i. Indeed, we could write 2k+β
2i+1 N ≤ *x <* 2k+β+1
2i+1
N
with β = 0 or β = 1. So, we can update k to 2k + β, meaning updating either a or b to a+b
2 , if we could compute the bit β. Since the inequality implies β N
2 ≤ 2ix − *kN <* (β + 1) N
2 . So,
β is such that β N
2
≤ 2ix mod *N <* (β + 1) N
2 .

We deduce β = lsb(2i+1x mod N).

Finally,
β = lsbdec(2(i+1)ey mod N). We deduce the following algorithm:
1: a ← 0, b ← N 2: **for** i = 0 to ⌊log2 N⌋ do
3:
if lsbdec(2(i+1)ey mod N) = 1 then
4:
a ← (a + b)/2
5:
else
6:
b ← (a + b)/2

7:
end if
8: end for
9: yield ⌊a⌋
Chor and Goldreich have shown that computing lsbdec with errors also enables the full decryption [15]. It was even shown that each bit of the plaintext has the same property [1]. This shows that every bit of the plaintext is a hard core bit in RSA. However, this only applies to each bit of the binary expansion of x, but not every bit of information about x is a hard-core bit. Indeed, we can define a Boolean function on x which is easy to compute from xe mod N: we can just consider the Jacobi symbol. Indeed, if we define

$N$

$$\mathsf{j}\mathsf{ac}(x)=\left(\frac{x}{N}\right)\quad,\quad\mathsf{j}\mathsf{acode}(y)=\left(\frac{y^{d}\bmod N}{N}\right.$$

then we have $\mathsf{j}\mathsf{acdec}(y)=\mathsf{j}\mathsf{ac}(y)^{d}=\mathsf{j}\mathsf{ac}(y)$ since $d$ must be odd to be invertible modulo $\varphi(N)$. So, it is easy to compute $\mathsf{j}\mathsf{acode}(y)$. So $\mathsf{j}\mathsf{ac}(x)$ is not a hard-core bit.

The RSA cryptosystem (which is deterministic and homomorphic, so with no chance to be IND-CCA secure or even IND-CPA secure) can be transformed into another one called _RSA-OAEP_[6] which is proven to be IND-CCA secure based on some _random oracle_.

## 2.5 Rabin Cryptosystem

The so-called *textbook-Rabin* cryptosystem [50] works as follows (see Fig. 2.8):

- for key generation, we generate two different prime numbers p and q, compute N = pq and
φ(N) = (p − 1)(q − 1).
- for encrypting a number x ∈ ZN, we compute y = x2 mod N.
- for decrypting a number y ∈ ZN, we compute x = √y mod N.
With this description, it is not really a cryptosystem because the √y mod N operation is ambiguous. Actually, there are four square roots of y and it is not clear which one to take for the decryption. A technique to address this problem is to impose some redundancy in the plaintext (e.g., that there are 64 special bit positions all equal to 0). Since it is unlikely that another square root will satisfy this redundancy, we can decrypt non-ambiguously.

To assess the security of the Rabin cryptosystem, we essentially consider two problems:

- the Rabin decryption problem: given a Rabin public key N and a ciphertext y, compute one
x such that y = x2 mod N (we do not consider the redundancy check here).
Game
1: Gen(1s)
$−→ N
2: pick x ∈ ZN
3: y = x2 mod N
4: A(*N, y*)
$−→ z
5: **return** 1z2 mod N=y

- the Rabin key recovery problem: given an Rabin public key N, factor N.
Game
1: Gen(1s)
$−→ N
2: A(N)
$−→ (*p, q*)
3: **return** 11<p<N,N=pq We can show that both are equivalent. Clearly, factoring N allows to compute square roots. So, the Rabin decryption problem reduces to the Rabin key recovery problem. Conversely, if we have an oracle solving the Rabin decryption problem, upon input N, we can pick x ∈ Z∗
N at random then submit y = x2 mod N to the oracle who will return x′ such that x2 ≡ (x′)2. Since x is a random square roots of y and that the oracle has no information on which one it is, we have that x = ±x′ mod N with probability 1
2. In the other cases, we deduce that gcd(x − x′, N) is a non-trivial factor of N, so we can factor N.

On the one hand, we could favor the Rabin cryptosystem as opposed to RSA because the decryption problem is known to be equivalent to factoring, whereas RSA decryption may be easier than factoring. However, the proof of equivalence can also be viewed as a chosen ciphertext attack which breaks the Rabin cryptosystem. This is a pretty paradoxical situation where knowing that decryption is as hard as key recovery also leads to a devastating chosen ciphertext attack!

When introducing plaintext redundancy to avoid decryption ambiguity, the equivalence no longer holds, and nor does the attack. This continues the paradoxical situation... So, it seems that in order to have a better security, decryption should not be as hard as key recovery!

## 2.6 Diffie-Hellman Security

The textbook Diffie-Hellman key agreement protocol [24] works as follows. We assume a standard cyclic group which is generated by some element g. The group parameters and g are generated by an algorithm Gen during setup. Alice has a secret key x ∈ Z and a public key X = gx. Bob has a secret key y ∈ Z and a public key Y = gy. They both exchange X and Y and compute K = gxy:
Alice computes K = Y x and Bob computes K = Xy. The final key shared by Alice and Bob is K.

This protocol relies on several problems which are relative to the group parameters generation algorithm Gen. We start with the *computational Diffie-Hellman (CDH)* problem:

$$\operatorname{Adv}=\operatorname{Pr}[{\mathrm{game~returns~}}1]$$
Game
1: Gen(1s)
$−→ (group, g)
2: pick X, Y ∈ ⟨g⟩ 3: A(group*, g, X, Y* )
$−→ K
4: define *x, y* s.t. X = gx, Y = gy
5: **return** 1K=gxy A related problem is the *discrete logarithm (DL)* problem:

$$\operatorname{Adv}=\operatorname{Pr}[{\mathrm{game~returns~}}1]$$
Game
1: Gen(1s)
$−→ (group, g)
2: pick X ∈ ⟨g⟩ 3: A(group*, g, X*)
$−→ x
4: **return** 1X=gx Clearly, the CDH problem is not harder than the DL problem because from the discrete logarithm x of X we can compute K = Y x.

A more subtle problem is the *decisional Diffie-Hellman (DDH)* problem: instead of computing K, we want to figure out if a guess for K is correct.

$$\mathrm{Adv}=\mathrm{Pr}[\Gamma_{1}\ \mathrm{returns}\ 1]-\mathrm{Pr}[\Gamma_{0}\ \mathrm{returns}\ 1]$$
Game Γb
1: Gen(1s)
$−→ (group, g)
2: pick X, Y, Z ∈ ⟨g⟩
3: define *x, y* s.t. X = gx, Y = gy
4: K ← gxy
5: if b=0 then
6:
A(group*, g, X, Y, Z*)
$−→ c
7: else
8:
A(group*, g, X, Y, K*)
$−→ c
9: end if
10: **return** c Clearly, the DDH problem is not harder than the CDH problem. To formally prove it, let us assume that the DDH problem is hard and let us consider a CDH solver A(*g, X, Y* ) → K. We construct the distinguisher B(*g, X, Y, Z*) as follows:

1: compute $\mathcal{A}(g,X,Y)\to K$
2: output $1_{Z=K}$

Due to the DDH hardness, the advantage of $\mathcal{B}$ is

$$\mathsf{negl}(s)=\Pr_{b=1}[\mathcal{A}(g,X,Y,K)=1]-\Pr_{b=0}[\mathcal{A}(g,X,Y,K)=1]=\Pr[\mathcal{A}\text{succeeds}]-\frac{1}{\#(g)}$$
Since
1
#⟨g⟩ is negligible, we deduce that Pr[A suceeds] is negligible as well. So, the Diffie-Hellman problem is hard.

Depending on Gen, the hardness of DDH, CDH, and DL can change. But it always goes in this difficulty order.

## 2.7 Elgamal Security

The ElGamal cryptosystem is recalled in Fig. 3.5. The key recovery problem is clearly equivalent to the discrete logarithm problem. The decryption problem in ElGamal can be defined as follows. Game
1: Gen(1s)
$−→ (group*, g, y*)
2: pick m ∈ ⟨g⟩
3: Enc(*y, m*)
$−→ (*u, v*)
4: A(group*, g, y, u, v*)
$−→ z
5: **return** 1z=m We can easily show that this is equivalent to the CDH problem.

The ElGamal cryptosystem, in a group ⟨g⟩, is also semantically secure if we assume that the Decisional Diffie-Hellman problem is hard in ⟨g⟩ and if we only encrypt messages which are elements of ⟨g⟩.

Theorem 2.21. If the DDH problem is hard in the group generated by the ElGamal cryptosystem, and if the plaintext space is included in the group, then the cryptosystem is IND-CPA secure.

We remind that the DDH problem is not always hard. For instance, the DDH problem in Z∗
p is easy.

We also observe that that the assumption that we only encrypt messages which are elements of ⟨g⟩ may be a problem because we may have to map bitstrings (arbitrary messages) into group elements in a reversible way.

One possible instance is that we take a strong prime p.

I.e., a large prime number p such that q = p−1
2
is also prime. Then, we consider the subgroup of Z∗
p of order q. Clearly, −1 is not in this subgroup since (−1)q ̸= 1 (because q must be odd). So, for every m, either m or −m is in the subgroup. We can define map(m) = ±m in the subgroup for 1 ≤ m ≤ q. This mapping is invertible. So, we can encrypt integers between 1 and q by encrypting the subgroup element map(m), assuming that the DDH problem is hard in this subgroup.

2 + negl. ⊓⊔
Proof. We show IND$-CPA security. Let A be an adversary for the real-or-random game. We construct a distinguisher A′ for the DDH problem as follows. In the DDH problem, A′ receives an order q and a group generator g, some y = gx for x ∈U Zq, and a pair (*u, v*′) in which u = gr for r ∈U Zq and either v′ = yr or v′ is random in the group generated by g. Clearly, (*q, g, y*) simulates the generation of an ElGamal public key. Let x0 = A(*q, g, y*). Given (*u, v*′), we define v = x0v′.

Clearly, (*u, v*) simulates the ElGamal ciphertext obtained by submitting x0 in the real-or-random game: either it is (gr, x0yr) or it is (gr, random × yr) for random in the subgroup generated by g.

Let b be the guess from A. Clearly, b is a guess for the DDH problem which is correct if and only if A wins. So, the distinguisher has the same advantage of A. Since the DDH problem is hard, the wining probability of A is 1
One problem with the ElGamal cryptosystem is that the DDH problem is not always hard.

Furthermore, when is it (believed to be) hard, it is not easy to use the group as a message domain.

Ideally, we would like to map bitstrings (of bounded length) to a group element in a reversible way in order to encrypt a bitstring. But such mapping is not always easy.

The is one case where we can have such mapping: if p and q are odd primes with p = 2q + 1, the subgroup QRp of Z∗
p is cyclic of order q. It does not contain −1 because (−1)q ̸= 1. Hence, for every integer *m >* 0, we obtain that either +m or −m belongs to QRp but no both. We can map
{1*, . . . , q*} to QRp in a bijective way by having map(m) = ±m. Then, it is easy to map {1, . . . , q}
to bitstrings.