
## Chapter 5 Symmetric Encryption

This chapter presents block ciphers, stream ciphers, and modes of operation. It also introduce elementary algorithms to use brute force for key recovery attacks.

## 5.1 A Cryptographic Primitive

In this chapter, we consider encryption algorithms which use the same key to encrypt and to decrypt. We have already seen the Vernam cipher, requiring a fresh key for every new encryption. Of course, there are other types of encryption in which we can reuse a key. We will distinguish two categories: block ciphers and stream ciphers.

## 5.2 Block Ciphers

Block ciphers encrypt/decrypt data by *blocks* of fixed length. Typically, 64 bits or 128 bits. DES.

The DES block cipher (now, supposed to be obsolete but still widely used) was published as a US standard in 1977 [6]. It encrypts blocks of 64 bits with a key of 56 effective bits (actually, the key has 64 bits but one bit per byte is used for the checksum). Internally, the 56-bit key is expanded into a number of 16 48-bit subkeys. The encryption goes through 16 rounds, each of which uses one subkey as a round key. The rounds follow the *Feistel scheme*: the block is split into two halves. The right half goes through a round function with the round key. The output of this round function is XORed to the left half. Then, the two halves are exchanged before the next round starts. In the last round, the exchange of halves is omitted. As an illustration, Fig. 5.1
depicts a Feistel scheme with 3 rounds.

In the case of DES, the first *round function* F takes 32 bits of a half-block and the 48-bit round key K1 to produce 32 bits which are XORed onto the other half-block.

There are some nice things with the Feistel scheme. First of all, whatever round function F, this defines a transform which is invertible (which is what we want since we want to be able to decrypt). This is shown by just constructing the inverse function. Second, the inverse transform is actually another Feistel scheme with the same round function in which we just reverse the order of the round keys. For instance, consider the 3-round Feistel scheme on Fig. 5.1 with the round functions FK1, FK2, then FK3 in this order. By applying it on any input block, then applying to the result of this computation another Feistel scheme with the round functions FK3, FK2, then FK1, we obtain the original input block. This can be shown by seeing that the output of the two FK3 will XOR the same value at the same place and cancel each other. Then, the two halves exchange and cancel each other. Then, the two FK2 applications will XOR the same value at the same place, etc. So, the hardware to implement the decryption algorithm is just the same as the hardware to implement the encryption algorithm in which we just have to feed the round keys in a reverse order.

Since 56 bits for a secret key are considered as too short, people considered triple encryption.

This defined the *triple-DES* standard. There are two variants: triple-DES with two keys K1 and K2 (so, 112 bits in total), and triple-DES with three keys K1, K2, and K3 (so, 168 bits in total).

The latter is defined by

$\mathsf{3DES}_{K_{1},K_{2},K_{3}}(X)=\mathsf{DES}_{K_{3}}\left(\mathsf{DES}_{K_{2}}^{-1}\left(\mathsf{DES}_{K_{1}}\left(X\right)\right)\right)$

use $K_{1}=K_{3}$. For the regular DES, we just use 
With two keys, we just use K1 = K3. For the regular DES, we just use K1 = K2 = K3 to have backward-compatibility.

A block cipher should be secure against *key recovery* and *decryption attacks*. For both attack goals, we may consider different scenarios: *ciphertext only attacks* (i.e., the adversary only gets ciphertexts), *known plaintext attacks* (i.e., the adversary gets some (*x, y*) pairs where x is random and y is the encryption of x), *chosen plaintext attacks* (i.e., the adversary has access to an encryption black box to which he could submit any x and get the encryption of it in return), and chosen ciphertext attacks (i.e., the adversary has access to a decryption black box in addition to an encryption black box). In the latter case, for decryption attacks, the adversary is not allowed to use the decryption black box to decrypt the ciphertext he is supposed to decrypt. He can use it for any other ciphertext though.

There are many attacks known against DES. A few weak keys were identified (these do a poor job in encrypting messages). The exhaustive search with optimized hardware was proposed by Hellman in 1980. It was implemented in 1998. (A key recovery took 4 days.) Biham and Shamir invented differential cryptanalysis and did a key recovery using 247 chosen plaintexts. Matsui developed linear cryptanalysis to make key recovery using 243 known plaintexts. This was later optimized by Junod in 2001, using a bit less than 240 known plaintexts. There are some attacks on 3DES as well. These are not covered in this lecture.

AES.

The new standard is called *Advanced Encryption Standard (AES)*. It was published in
2001 [5]. It encrypts blocks of 128 bits using keys of 128, 192, or 256 bits. Its structure consists of a keylength-dependent number of rounds (Nr = 10, 12, or 14 rounds, respectively), in which a round key is used. So, the secret key is transformed into a sequence of round keys W0*, . . . , W*Nr.

In AES, a message block and a round key are represented as a 4 × 4 matrix of bytes (i.e.,
128 bits in total). Each byte actually represents an element of GF(28) with reference polynomial P(X) = X8 + X4 + X3 + X + 1.

I.e., a bitstring a7 *· · ·* a1a0 represents the polynomial a =
a7X7 + *· · ·* + a1X + a0 and additions and multiplications are done modulo 2 and modulo P(X).

So, the addition in the field corresponds to the XOR of the bitstrings. Multiplication by the byte
0x01 is trivial: a × 0x01 = a. We have already seen how to multiply a by the byte 0x02: we just shift the byte a by one bit the the left and XOR to 0x1b if there is a carry bit. Finally, to multiply by 0x03, we can just multiply by 0x01 and by 0x02 and add (i.e., XOR) the two results. In AES, we only need to multiply by 0x01, 0x02, and 0x03.

Each round consists of four types of successive transform: AddRoundKey which adds (i.e., XOR)
the round key to the block; SubBytes which substitutes every byte a by the byte S(a), following a table S (called the S-box); ShiftRows which consists of a circular shift of every row of the block by a variable number of positions; and MixColumns which consists of multiplying all columns of the block to the left by the matrix

M =   0x02 0x03 0x01 0x01 0x01 0x02 0x03 0x01 0x01 0x01 0x02 0x03 0x03 0x01 0x01 0x02       . So, we only need the multiplication by 0x01, 0x02, and 0x03. More precisely, the AES encryption of a block $s$ with a sequence of subkeys $W_{0},\dots,W_{W_{W}}$ is implemented as follows.

**AES encryption$(s,W)$**
1: AddRoundKey(*s, W*0)
2: **for** r = 1 to Nr − 1 do
3:
SubBytes(s)
4:
ShiftRows(s)
5:
MixColumns(s)
6:
AddRoundKey(*s, W*r)
7: end for
8: SubBytes(s) 9: ShiftRows(s)
10: AddRoundKey(*s, W*Nr)
with the following subroutines:
SubBytes(s)
1: **for** i = 0 to 3 do
2:
for j = 0 to 3 do
3:
si,j ← S(si,j)
4:
end for
5: end for ShiftRows(s)
1: replace [s1,0, s1,1, s1,2, s1,3] by [s1,1, s1,2, s1,3, s1,0]
2: replace [s2,0, s2,1, s2,2, s2,3] by [s2,2, s2,3, s2,0, s2,1] 3: replace [s3,0, s3,1, s3,2, s3,3] by [s3,3, s3,0, s3,1, s3,2]
AddRoundKey(*s, k*)
1: **for** i = 0 to 3 do
2:
for j = 0 to 3 do
3:
si,j ← si,j ⊕ ki,j
4:
end for
5: end for MixColumns(s)
1: **for** i = 0 to 3 do
2:
let v be the 4-dimensional vector with coordinates s0,is1,is2,is3,i
3:
replace s0,is1,is2,is3,i by M × v
4: end for Interestingly, the function S in SubBytes is an affine transformation of the function x 7→ x254 in GF(28). (Note that for x ̸= 0, x254 = x−1.) But we rather keep the full table of S instead of applying the formula.

To decrypt, we just have to invert all subroutine processes.

This is quite straightforward, except for MixColumns for which the matrix has to be replaced by its inverse

$$M^{-1}=\left(\begin{array}{l l l}{{0\mathrm{x0e}}}&{{0\mathrm{x0b}}}&{{0\mathrm{x0d}}}&{{0\mathrm{x09}}}\\ {{0\mathrm{x09}}}&{{0\mathrm{x0e}}}&{{0\mathrm{x0b}}}&{{0\mathrm{x0d}}}\\ {{0\mathrm{x0d}}}&{{0\mathrm{x09}}}&{{0\mathrm{x0e}}}&{{0\mathrm{x0b}}}\\ {{0\mathrm{x0b}}}&{{0\mathrm{x0d}}}&{{0\mathrm{x09}}}&{{0\mathrm{x0e}}}\end{array}\right).$$
So, we now have to learn how to multiply by 0x09, 0x0b, 0x0d, and 0x0e. Here is a decryption algorithm: AES decryption(*s, W*)
1: AddRoundKey(*s, W*Nr)
2: **for** r = Nr − 1 down to 1 do
3:
InvSubBytes(s)
4:
InvShiftRows(s)
5:
AddRoundKey(*s, W*r)
6:
InvMixColumns(s)
7: end for
8: InvSubBytes(s) 9: InvShiftRows(s)
10: AddRoundKey(*s, W*0)
Modes of operation.

Once we have a block cipher, we can encrypt/decrypt a message block.

If we want to encrypt a message which consists of several blocks (or even fractions of blocks), we need to plug the block cipher into a *mode of operation*. The principle of these modes of operation is that we can encrypt/decrypt messages "on-the-fly", without buffering some important part of it, but still be able to treat variable-length messages. Some modes of operation require an initial vector IV, as we will see. All modes internally split the plaintext into a sequence of blocks before processing.

The most straightforward mode of operation is the *Electronic Codebook (ECB) mode*. It consists of encrypting each block separately, using the block cipher. (See, Fig. 5.2.) This is however insecure for most of applications: indeed, in the messages that applications want to encrypt, it is very likely that some blocks of data repeat. For instance, in an image file representing a picture on a uniform background, the blocks which are only filled with background pixels will repeat, and their position will draw a uniform background on the ciphertext picture. The non-background blocks will look random and make the picture appear like a phantom.

Since each block goes through the same encryption process, the equality of these blocks can be seen by looking at the sequence of ciphertext blocks. This ECB mode should only be used in very rare cases.

In the *Cipher Block Chaining (CBC) mode*, each block of plaintext is XORed to the previous ciphertext block before being encrypted. The first plaintext block is XORed to an initial vector IV.

So, if the message is the sequence of blocks x1*, . . . , x*n, the ciphertext is the sequence y1, . . . , yn
(sometimes with IV, as detailed below), where yi = EncK(xi ⊕ yi−1), i = 2*, . . . , n*, and y1 =
EncK(x1 ⊕ IV), where EncK is the block cipher. (See, Fig. 5.3.) There are three ways to use IV:

- use a constant, publicly known IV (e.g., IV = 0); - use a secret IV (so, the secret key becomes (IV, K)); - use a fresh random IV for every message x and add it as a part of the ciphertext (so, the
ciphertext becomes (IV, y1*, . . . , y*n)).
The first two methods may suffer from similar problems as the ECB mode when it comes to look at y1 through many encryptions. The first one is definitely not a good idea, although it is being used in applications (such as the biometric passport). In the second method, we may use a stateful encryption algorithm in which the IV for the next message becomes yn. (So, the secret IV is used only once and we treat the sequence of messages to be encrypted as a unique stream of data to be encrypted.) It is safe if the key is set only once and the state IV keeps updating, like in the TLS
standard (before version 1.3). But this option may suffer from insecurity problems as a chosen plaintext attack could select the message to encrypt based on the predictable IV.

The CBC mode also has the interesting property to be inherently immune to errors.

For instance, if yi is corrupted during transmission, decryption will mess up xi and xi+1 but all subsequent blocks will be correct! Similarly, if yi is lost, the decryption will result in one block missing and one block incoherent, at the place of the missing block.

The *Output Feedback (OFB) mode* uses an IV.

It consists of defining the sequence ki =
EncK(ki−1), i = 2*, . . .*, and k1 = EncK(IV), and to treat the stream k1*, . . .* as a one-time-pad key to encrypt x. (See, Fig. 5.4.) Clearly, this requires IV to be unique, due to the properties of one-time-pad. So, we call IV a *nonce*.1 We can either use a random one (but by making sure that the probability to repeat an IV is negligible) or a counter-based one. In the case of a random IV, it can either be privately synchronized between the sender and the receiver, or sent in clear (so, part of the ciphertext). In the case of a counter-based IV, we can either assume that the sender and the receiver are synchronized on the counter, or just send the IV in clear again. The OFB mode works even if the last plaintext block is incomplete. This is an advantage over other encryption modes.

The *Cipher Feedback (CFB) mode* is defined by yi = xi ⊕ EncK(yi−1), i = 2*, . . . , n*, and y1 = x1 ⊕ EncK(IV). (See, Fig. 5.5.) The nonce IV options are the same as for the OFB mode.

The CFB mode works even if the last plaintext block is incomplete.

The *Counter (CTR) mode* uses a nonce ti for every block.

The encryption of xi is yi =
xi ⊕EncK(ti). (See, Fig. 5.6.) As its name indicates, the nonce ti is based on a counter: it encodes a counter for the block to encrypt and a counter for the message to encrypt. Again, the CTR mode works even if the last plaintext block is incomplete.

There exists many other modes of operation. A quite popular one, which is used to encrypt hard disks, is the *XEX-based tweaked-codebook mode (TCB) with ciphertext stealing (CTS)*, which is shortened to XTS [7].2 It assumes that the hard disk is split into sectors and that sectors are split into several blocks and up to one incomplete block, the incomplete one being the last one. It uses two keys K1 and K2. Except for the last two blocks of a sector, the jth block xi,j of the ith sector is encrypted into yi,j = EncK1(xi,j ⊕ ti,j) ⊕ ti,j

where $t_{i,j}=\alpha^{j}\times\mathsf{Enc}_{K_{i}}(i)$ (see Fig. 5.7), $\alpha$ being a constant in the XTS standard, and the operations being done in a $\mathsf{GF}$ structure. So, this encryption looks like the CTR mode, so far. For the last two blocks $x_{i,n_{i}-1}$ and $x_{i,n_{i}}$ of a sector, it works the same if $x_{i,n_{i}}$ is a complete block.

2It was meant to be called XTC for XEX-TCB-CTS, but this acronym was already used to refer to ecstasy drug.

Otherwise, we employ the *ciphertext stealing* trick: we compute EncK1(xi,ni−1⊕ti,ni−1)⊕ti,ni−1 = yi,ni∥u to define an incomplete block yi,ni of same length as xi,ni, and yi,ni−1 = EncK1((xi,ni∥u)⊕
ti,ni) ⊕ ti,ni (see Fig. 5.8).

## 5.3 Stream Ciphers

Stream ciphers are used to encrypt streams of data on the fly. Typically, we encrypt bit-by-bit, or byte-by-byte. The main principle is that we use one-time-pad with a pseudorandom key-stream, defined from a secret key and a nonce. Again, either the nonce is based on a counter, and we may assume synchronization, or send the nonce in clear with the ciphertext, or the nonce is random, and sent in clear with the ciphertext, or the nonce is secret, but used only once. RC4.

One of the most popular stream ciphers is RC4, designed by Ronald Rivest in 1994. It was originally a trade secret, but it came in so many implementations that it is now well-known.

It generates a key-stream of bytes from a secret key (to be used only once) which is a sequence of bytes of total length between 40 bits and 256 bits. It is based on operations in the Z256 group.

Let ℓ be the length (in bytes) of the key k0*, . . . , k*ℓ−1. RC4 starts with a KSA algorithm defined by
1: j ← 0
2: **for** i = 0 to 255 do
3:
S[i] ← i
4: end for 5: **for** i = 0 to 255 do
6:
j ← j + S[i] + ki mod ℓ
7:
swap S[i] and S[j]
8: end for Except the i mod ℓ operation, all others are to be considered modulo 256.

Then, the PRGA
(pseudorandom generator algorithm) generates the stream:
1: i ← 0 2: j ← 0
3: loop
4:
i ← i + 1
5:
j ← j + S[i]
6:
swap S[i] and S[j]
7:
output S[S[i] + S[j]]
8: end loop As we can see, the RC4 algorithm is an automaton based on a *state*, defined by two bytes i and j, and a byte permutation S.

In the TLS protocol (which is discussed in Section A.8), the key is used only once, but the final state after the encryption of a message is kept to serve as the initial (PRGA) state of the encryption of the next message. So, we need synchronization as encryption is stateful. In the WEP protocol (which is discussed in Section A.1, the first three bytes of the key define a nonce to be sent in clear, and the rest is the actual secret key.

There are many known weaknesses in RC4. For instance, some correlations between some key bytes and some output bytes allow to make a passive key recovery attack in WEP. The bad distribution of output bytes allows to make a ciphertext-only decryption attack in TLS when the same plaintext is encrypted many times (this is the case with *secure http cookies*). There are speculations about state agencies being able to fully break RC4. As a result, WEP is obsolete and RC4 is now prohibited in TLS. A5/1.

Another very popular stream cipher, as it is used in GSM communication (which is presented in Section A.3, is the A5/1 algorithm. Again, it was a trade secret but was reverse engineered (and subsequently broken). It uses a 64-bit secret and a 22-bit counter, used as a nonce. The key and the counter are first transformed into an initial state. Then, an automaton based on asynchronous linear feedback shift registers generates a key-stream of bits.

There are many attacks against A5/1. For instance, there are key-recovery known plaintext attacks. There are also active attacks on GSM (attacks which force mobile equipments to change the cipher by keeping the same secret key). There are also ciphertext-only recovery attacks using (optimized) bruteforce. Consequently, we should not expect too much about the privacy of our GSM communication!

## 5.4 Bruteforce Inversion Algorithms

Let K be a set of given size N. Consider the *random key guessing game* during which a challenge selects a key K *∈ K* at random, then an adversary makes guesses for the value of K until it is correct. The game is formalized as follows:
Game:
O(query):
4: **return** 1K=query
1: pick K ∈D K
2: AO → k
3: **return** 1K=k

i N = N + 1 2 i=1
The adversary knows the set K and may know the sampling distribution of K. This distribution may be uniform or arbitrary. For instance, someone trying to open a safe without knowing the combination to open it would just make some guesses until the safe opens.

In the uniform distribution case, the adversary can just enumerate the elements of K until the value K is found. In terms of trials, the worst case complexity is N. The average case complexity is N
X
When the distribution is arbitrary and unknown, the best strategy is to enumerate the values of K in a random order to reach the same average complexity. If the distribution is known, we can enumerate the values of K by decreasing order of likelihood and obtain the optimal average complexity which is called the *guesswork entropy*.

The game may be different if the adversary is given a clue which we call a *witness* w. Then, the optimal strategy is to enumerate all k *∈ K* by decreasing order of Pr[K = k|w]. But then, our strategies must consider the complexity in terms of trials, computation time, memory space, and in terms of the probability of success as well.

In offline key recovery, the adversary can make only one guess. He does so based on a witness w = F(K). The function F may be deterministic or not. For instance, if the adversary is running a chosen plaintext attack, F(K) consists of the ciphertexts which are obtained by the (fixed)
chosen plaintexts. With a deterministic function F, we can consider the offline key recovery game (on the left) and a variant which consists of finding *any* key matching the clue (on the right):
Game:
Game:

1. pick $K\in_{D}K$
2. $W\gets F(K)$
3. $\mathcal{A}(W)\to k$
4. **return**$1_{K=K}$

Let us consider the case of a password-based access control scheme in which the password $K$ has a witness $w=F(K)$ which is stored in clear. In some concrete protocols, we may have $F(K)=\mathsf{Enc}_{K}(0)$, for instance the process controls in hashing (by $F$) the typed password and to compare the result with $w$. A access is granted it matches. In this case, the goal of the above is to measure the process of $k$ such that $w=F(k)$ (but not necessarily the correct choice). This is often found just mention all $k$'s until a solution is found. If $M$ is the size of the output range of $F$ and $F$ is a random function, every new trial is a solution with probability $\frac{1}{M}$. For $M\ll N$, the expected complexity is

$$\sum_{i\geq0}i\Pr[i\text{trials}]=\sum_{i\geq0}\Pr[>i\text{trials}]=\sum_{i\geq0}\left(1-\frac{1}{M}\right)^{i}=M$$
For M ≫ N, collisions on F are rare and the complexity is similar than in the previous case, so close to N
2 .

A *dictionary attack* consists of preparing a complete table for the inverse function w 7→ F −1(w).

That is, we prepare a sorted list of all (F(k), k). The attack then works with constant complexity, but requires a memory of O(N), and a preprocessing time of O(N) as well. The probability of success is 1.

With an incomplete dictionary of size D, the precomputation time is O(D), the memory complexity is O(D), the time complexity of the attack phase is O(1), but the probability of success is D
N . As we can see, already, we may consider tradeoffs.

The attack model can be enriched by considering a multi-target version: instead of targeting a single K, the goal maybe to recover at least one Ki from a list K1*, . . . , K*T of T targets. In that case, the dictionary attack needs a precomputation time of O(D), a memory complexity of O(D), a time complexity of the attack phase of O(T), but the probability of success is 1−

1 − D
N
T ≈ 1−e− DT
N .

This is quite interesting for D ≈ T ≈
√
N) (instead of the regular O(N)) on Ω(
√
N: we have a succeeding attack of overall complexity O(
√
N) targets. Here is a formalization of the multitarget inversion game with a partial dictionary attack. Game:

AF
1 : (preprocessing)
1: **for** D candidates k do

2:
compute F(k)
1: setup F
2: AF
1 → dict
3:
insert (F(k), k) in dict
4: end for
5: **return** dict

3: pick K1, . . . , KT ∈D K
4: wi ← F(Ki) for i = 1, . . . , T
5: AF
     2 (dict, w1, . . . , wT ) → (i, k)

6: return 1F (k)=wi

AF
2 (dict, w1*, . . . , w*T ): (attack)
6: **for** i = 1 to T do
7:
if there is some (wi, k) in dict then
8:
return (*i, k*)

9:
end if
10: **end forreturn** ⊥
When the witness function is not deterministic, the dictionary attack is more complicated, if not impossible. For instance, in password access control, if the password is hashed together with a random *salt* which is stored with the hash, the dictionary must be dedicated to this salt value (which excludes multi-target variants), or to consider all possible salts (which makes the dictionary bigger). In known plaintext attacks, the plaintexts cannot be prepared when making the dictionary. We can conclude with an offline attack to recover K such that F(K; W2) = W1
corresponding to the witness W = (W1, W2) and the salt W2:

1: select a random ordering kσ(1), . . . , kσ(N) of K
2: for i = 1 to N do
3:
        if F(kσ(i); W2) = W1 then

4:
            stop and yield kσ(i)

5:
        end if

 6: end for
 7: search failed
We obtain the expected complexity O(N) again.

## 5.5 Subtle Bruteforce Inversion Algorithms

Meet-in-the-middle attack on double encryption.

Consider a double encryption scheme

$${\mathsf{E n c}}_{K_{1},K_{2}}(x)={\mathsf{E n c}}_{K_{2}}\left({\mathsf{E n c}}_{K_{1}}(x)\right)$$
where the keys belong to a set K of size N. We consider a known-plaintext attack scenario where a pair (*x, z*) with z = EncK1,K2(x) is known. We assume that this equation uniquely characterizes
(K1, K2). (Otherwise, we just consider enough pairs instead of just one.)
The *meet-in-the-middle* algorithm (see below) consists of first preparing a dictionary of (Enck1(x), k1)
pairs. Then, it makes an exhaustive search on k2 to compute y = Enc−1
k2 (z), look for (*y, k*1) in the dictionary and print (k1, k2) if there is such an entry. Interestingly, the complexity is O(N) both in time and space, although the double encryption would expect to have a security of Ω(N 2).

1: **for** all k1 do
2:
compute y = Enck1(x)

3:
insert (*y, k*1) in a hash table (indexed with the first entry)
4: end for
5: **for** all k2 do
6:
compute y = Enc−1
k2 (z)
7:
for all (*y, k*1) in the hash table do
8:
yield (k1, k2) as a possible key
9:
end for
10: end for
Time-memory tradeoffs inversion.

Another subtle inversion algorithm is for the single encryption case with a deterministic function F. (Actually, this can invert any deterministic function F, e.g. a hash function.) Imagine an algorithm preparing ℓ tables of m entries (ks i,0, ks i,t), s = 1*, . . . , ℓ*, i = 1*, . . . , m*. For each table s, a random reduction function Rs is selected so that Rs(F(k)) *∈ K* for all k *∈ K*. Then, for each entry in the table, ks i,0 is randomly selected and we compute ks i,j = Rs(F(ks i,j−1)), j = 1*, . . . , t*. This runs as follows.

1: **for** s = 1 to ℓ do
2:
pick a reduction function Rs at random and define fs : k 7→ Rs(F(k))
3:
for i = 1 to m do
4:
pick k′ at random
5:
k ← k′
6:
for j = 1 to t do
7:
compute k ← fs(k)
8:
end for
9:
insert (*k, k*′) in table Ts
10:
end for
11: end for Clearly, this precomputation takes time *ℓmt* and the memory complexity is ℓm.

During the attack phase, we are given w = F(K) and we want to recover K. For each s we compute Rs(w) then iterate k 7→ Rs(F(k)) at most t times. If one of the values matches on ks i,t, then we can start from the corresponding ks i,0, iterate again until we reach Rs(w). If we do, we obtain a preimage of Rs(w) by Rs ◦ F, thus a preimage of w by F with high probability. So, we recover the key. More precisely, the algorithm runs as follows.

1: **for** s = 1 to ℓ do
2:
set i to 0
3:
set k to Rs(w)
4:
while Ts contains no (*k, .*) entry and *i < t* do
5:
increment i
6:
k ← fs(k)
7:
end while
8:
if Ts contains a (*k, .*) entry then
9:
get the (*k, k*′) entry from table Ts
10:
while F(k′) ̸= y and *i < t* do
11:
increment i
12:
k′ ← fs(k′)
13:
end while
14:
if F(k′) = y then
15:
yield k′ as a possible key
16:
end if
17:
end if
18: end for The complexity is O(ℓt). The optimal selection is for ℓ ≈ m ≈ t ≈ N
1
3 for which we obtain a complexity of O(N
2
3 ).

In the case of DES where N = 256, this attack works with about 237 operations, after having made the tables within 256 operations.

## 5.6 Pushing The Physical Limits

As mentioned before, the number of 2007-machines needed to make an exhaustive search on a 128-bit secret key within the age of the universe is incredibly high. We may expect that the Moore's law improves this, but we shall still keep in mind that there is an energy bill. So far, erasing a single bit of memory on a machine at temperature $T$ (in Kelvin) requires an energy of $kT\ln2$, where

$$k=1.38\times10^{-23}\;JK^{-1}$$
is the constant of Boltzmann. This is the Laudauer result from 1961 [53]. Assuming that each trial in an exhaustive search requires to erase log2 N bits of memory at least, we can estimate the energy needed to do the exhaustive search, whatever the speed. With a machine running at 3 µK
(which is extremely cold), we need 12 × 109 J. To do it within one second requires the full power of a last-generation nuclear powerplant.

Bennett proved in 1973 [16] that in theory, we could compute without spending energy as long as each computation step is reversible (so that we have no erasure), but this requires to accumulate all intermediary results so to waste memory.

We can make an exhaustive search in a reversible manner and save memory as follows. We define three operations which will modify the internal state ⟨*x, y, k, z, t*⟩ of the computer in a reversible manner:

$$\begin{array}{l l l l}{{\mathrm{INC}:}}&{{\langle x,y,k,z,t\rangle}}&{{\mapsto}}&{{\langle x,y,k+1,z,t\rangle}}\\ {{\mathrm{ENC}:}}&{{\langle x,y,k,z,t\rangle}}&{{\mapsto}}&{{\langle x,y,k,z\oplus\mathsf{Enc}(k,x),t\rangle}}\\ {{\mathrm{CMP}:}}&{{\langle x,y,k,z,t\rangle}}&{{\mapsto}}&{{\langle x,y,k,z,t\oplus k\cdot1_{y=z}\rangle}}\end{array}$$
Then, the sequence ENC, CMP, ENC, INC does in fact the operation

$$\langle x,y,k,z,t\rangle\mapsto\langle x,y,k+1,z,t\oplus k\cdot1_{y\oplus z=\mathsf{Enc}(k,x)}\rangle$$
If we execute this operation 2128 times on the initial state ⟨*x, y,* 0, 0, 0⟩, we obtain the XOR of all keys such that y = Enc(*k, x*). Assuming K is unique, we get the final state ⟨x, y, 0, 0, K⟩.

Reversible operations can typically be implemented on a quantum computer. However, there is a better algorithm to do an exhaustive search: the Grover algorithm [43]. This algorithm allows, for a function F over a domain of size N, to find a preimage when it is unique, in a complexity corresponding to O(
√
N) evaluations of F. This algorithm motivates using keys of 256 bits in AES. Indeed, a 128-bit key would be found with a complexity of 264 on a quantum computer.

## 5.7 Formalism

We finish this chapter by introducing some formal definitions about symmetric encryption. First of all, we define a block cipher. For simplicity, we assume that it operates on bitstrings, as this is the most common case.

Definition 5.1. A **block cipher** *is a tuple* ({0, 1}k, {0, 1}n, Enc, Dec) with a key domain {0, 1}k, a block domain {0, 1}n*, and two* efficient *deterministic algorithms* Enc *and* Dec. It is such that
∀K ∈ {0, 1}k
∀X ∈ {0, 1}n Dec(K, Enc(*K, X*)) = X
Write CK(·) = Enc(K, .) *and* C−1
K (·) = Dec(K, .).

So, k is the key length and n is the message block length. We let the notion of efficient algorithm undefined here. The main point is that we are not interested in block ciphers which have too slow or too expensive implementations.

It is important that encryption and decryption are deterministic.

As an equivalent definition, we can just say that CK and C−1
K are defined as permutations over the block space which are inverse of each other for every key K *∈ {*0, 1}k.

Block ciphers are extended into variable-length encryption schemes. Most commonly, these encryption schemes are *length-preserving* in the sense that the ciphertext and the plaintext have always the same length. We could define the encryption over the set of all bitstrings, but sometimes, some message length are not made available. So, we must define the encryption scheme over a subset D of the set of bitstrings {0, 1}∗.

**Definition 5.2**.: _A (variable-length, length-preserving) symmetric encryption scheme is defined by a tuple $\{0,1\}^{k},\mathcal{D},\mathsf{Enc},\mathsf{Dec}\}$ with a key domain $\{0,1\}^{k}$, a plaintext domain $\mathcal{D}\subseteq\{0,1\}^{*}$, and two efficient deterministic algorithms $\mathsf{Enc}$ and $\mathsf{Dec}$._

_It is such that_

$$\forall K\in\{0,1\}^{k}\quad\forall X\in\mathcal{D}\quad\left\{\begin{array}{rcl}\mathsf{Dec}(K,\mathsf{Enc}(K,X))&=&X\\ \mathsf{Enc}(K,X)|&=&|X|\end{array}\right.$$
Write CK(·) = Enc(K, .) *and* C−1
K (·) = Dec(K, .).

In the definition, we denote by |X| the length of X. So, Enc(*K, X*) and X always have the same length.

We have seen that some modes of operation and stream ciphers have an extra input which is used as a *nonce*. So, we must extend our definition.

**Definition 5.3**.: _A (nonce-based, variable-length, length-preserving) symmetric encryption scheme is a tuple $(\{0,1\}^{k},\mathcal{D},\mathcal{N},\mathsf{Enc},\mathsf{Dec})$ with a key domain $\{0,1\}^{k}$, a plaintext domain $\mathcal{D}\subseteq\{0,1\}^{*}$, a nonce domain $\mathcal{N}$, and two efficient deterministic algorithms $\mathsf{Enc}$ and $\mathsf{Dec}$._

_It is such that_

$$\forall K\in\{0,1\}^{k}\quad\forall X\in\mathcal{D}\quad\forall N\in\mathcal{N}\quad\left\{\begin{array}{ll}\mathsf{Dec}(K,N,\mathsf{Enc}(K,N,X)){=}X\\ |\mathsf{Enc}(K,N,X){=}|X|\end{array}\right.$$
N is supposed to be used only once for encryption. We could use a random nonce (we have to be careful about values which could repeat with a random selection by having nonces large enough), or a counter. We could send the nonce in clear with the ciphertext or have the sender and receiver synchronized on the nonce by other means. Some modes of operation use an IV which can be used as a nonce, but an IV which is secret does not fit this notion of a nonce.

Once we defined the encryption scheme with the correctness notion (namely, that the decryption of the ciphertext is equal to the plaintext), we must define the security notion. First of all, we define the security against key recovery, either by chosen plaintext attack or by chosen plaintext and ciphertext attack.

(We could easily define the security by known plaintext attacks or by ciphertext only attacks.) In the following security notion, we see that there is a key K selected at random. The adversary A can play with the encryption function as a black box and he must guess the value of K.

Definition 5.4. *A symmetric encryption scheme* ({0, 1}k, D, N, Enc, Dec) is (*q, t, ε*)-secure against key recovery under chosen plaintext attacks (CPA) if for any algorithm A limited to a time complexity t and to q *queries, the advantage* Adv is bounded by ε, where

## Adv = Pr[*Game Returns* 1]

We say that A is *nonce-respecting* if it never make two encryption queries using the same nonce.

However, he could make decryption queries by using the same nonce many times.

In the definition, the notation Enc(*K, ., .*) as a superscript of A means that the algorithm A has access to an external black box such that by feeding it with a pair (*N, X*), it returns Enc(*K, N, X*) in one unit of time. Similarly, the superscript Enc(*K, ., .*), Dec(*K, ., .*) means a black box access to two oracles: (*N, X*) 7→ Enc(*K, N, X*) and (*N, Y* ) 7→ Dec(*K, N, Y* ).

Here, security is defined by having a bounded advantage ε for adversaries limited to some resources (*q, t*): the limitation holds in the total number of queries q to any oracle and in the time complexity t of the overall attack, i.e. the number of steps of the algorithm.

Clearly, security against chosen plaintext and ciphertext attacks implies security against chosen plaintext attacks. So, security against chosen plaintext and ciphertext attacks is a stronger security notion.

It is not always enough to have security against key recovery.

Indeed, we could define an encryption scheme doing nothing (i.e., by Enc(*K, N, X*) = X for all K, N, and X) and it would be very hard to make a key recovery attack. However, no message is really encrypted. Actually, the key is not used at all. So, we define security against decryption attacks, by using another scenario: a key K, nonce N, and message X are selected at random. The adversary is given Y = Enc(*K, N, X*) and can play with the encryption as a black box. With chosen decryption attacks, he is not allowed to query the decryption oracle Dec(*K, ., .*) with the (*N, Y* ) pair. The goal is to guess the value of X.

Definition 5.5. *A symmetric encryption scheme* ({0, 1}k, D, N, Enc, Dec) is (q, t, ε)-secure against decryption under CPA (resp. CPCA) if for any algorithm A limited to a time complexity t and to q *queries, the advantage* Adv is bounded by ε.

## Adv = Pr[*Game Returns* 1]

Game Oracle OEnc(N, X):
1: K
$←− {0, 1}k
2: X0
$*←− D*, N0
$←− N
1: if N ∈ Used **then return** ⊥ 2: Used ← Used ∪ {N}
3: *return* Enc(*K, N, X*)
Oracle ODec(N, Y ):

3: Used ← {N0}
4: Y0 ← Enc(K, N0, X0)
5: AOEnc(,ODec)(N0, Y0) → X
6: return 1X=X0

4: if (N, Y ) = (N0, Y0) then
   return ⊥

5: return Dec(K, N, Y )

Note that D must be a finite set to select X ∈ D with a uniform distribution.
   As an adversary guessing the key K can always decrypt Y by running himself the Dec algorithm,
security against decryption attack implies security against key recovery attack. So, security against
decryption attack is a stronger security notion.
   Yet, we may want to protect messages against partial decryption, or consider stronger security
notions. For that, we can try to compare the encryption scheme with an ideal one. An ideal
encryption scheme Π would be such that for every nonce value N, Π(N, .) would be a uniformly
distributed length-preserving permutation of D. The goal of an adversary would be to distinguish
if a black-box encryption machine is using the real encryption scheme or the ideal one. We define
the security against distinguishers as follows.

Definition 5.6. *A symmetric encryption scheme* ({0, 1}k, D, N, Enc, Dec) is (*q, t, ε*)-secure against distinguishers under CPA (resp. CPCA) if for any algorithm A limited to a time complexity t and to q *queries, the advantage* Adv is bounded by ε.

## Adv = Pr[Γ1 *Returns* 1] − Pr[Γ0 *Returns* 1]

Oracle OEnc(N, X):
Game Γb
1: K
$←− {0, 1}k
1: if N ∈ Used **then return** ⊥ 2: Used ← Used ∪ {N}
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
4: AOEnc(,ODec) → z
5: **return** z
5: if b
=
0
then return
Π−1
N (Y )
6: *return* Dec(*K, N, Y* )
We conclude by an informal proof that indistinguishability is a stronger security notion that decryption security. We show it for chosen plaintext attacks, but it works with chosen plaintext/ciphertext attacks as well. Indeed, assuming that we have a decryption adversary A, we can define a distinguisher D as follows:
DEnc(K,.):
1: pick X, query Enc(*K, .*) on X to get Y
2: run AEnc(K,.)(Y ) → X′
3: output 1X=X′
The advantage of D is computed as

$$\Pr[\mathcal{D}^{\mathsf{Enc}(K,\cdot)}\to1]-\Pr[\mathcal{D}^{\Pi(\cdot)}\to1]$$ $$=\Pr[\mathcal{A}^{\mathsf{Enc}(K,\cdot)}(\mathsf{Enc}(K,X))=X]-\Pr[\mathcal{A}^{\Pi(\cdot)}(\Pi(X))=X]$$ $$\geq\Pr[\mathcal{A}\text{wins}]-\varepsilon^{\prime}$$
where Pr[AΠ(·)(Π(X)) = X] ≤ ε′. It is a bit technical that we can obtain a pretty low upper bound ε′. This is actually a combinatorial result as it does not depend at all on the Enc design.

Hence, assuming security against distinguishers, we deduce that Pr[A wins] must be small, so a security against decryption attacks.