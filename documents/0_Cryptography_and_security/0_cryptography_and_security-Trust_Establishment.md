
## Chapter 8 Trust Establishment

This chapter shows how to build trusted information infrastructure using cryptographic primitives. It focuses on access control, secure password-based key setup, secure communication, and key infrastructures.

## 8.1 Access Control

Password access control.

Access control can be done by sending an identifier ID and a password w. To avoid leakage from the database, we can avoid storing the password by saving only a hash of it. To secure against multi-target attacks and time-memory tradeoffs, we can add a salt which has to be stored as well. So, the database contains some (ID, salt, H(ID∥salt∥w)) triplets
(see Fig. 8.1).

The advantage is that the server does not keep w and that the client does not need to compute anything (which is nice for a human client). The drawback is that the channel to transmit w must be secure. Challenge/response access control.

Another popular technique consists of sending a challenge c to the client to which he must answer by some r = fK(c), where K is his key and f is a pseudorandom function (PRF). This requires that the server keeps K in a database. The client has to do some computation. This is rather done by a device than a human being. For instance, the client can be a special hardware (e.g., a SIM card, for GSM telephony, see Section A.3). It can work with high-entropy shared secret K.

The advantage is that it resists to passive adversaries. The drawback is that it does not resist to relay attacks. In addition to this, the client must do some cryptographic operation. This cannot be done by a human client. One-time password (OTP).

In between password access control and challenge/response protocols, we have the *one-time password* protocol. Essentially, we have a long list of passwords and each password can only be used only once. There may also be a chronological order to use these passwords. Typically, the sequence is generated from a secret seed backward: from the last-to-beused password to the first one. Each password is the image of the next password by a one-way function. So, the server only stores the last used password and checks that the new one hashes onto the stored one.

This resists to passive adversaries, not to relay attacks, it requires no computation on the client side, but managing a long list of password may not always be well accepted by human users. Strong Authentication.

We call *strong authentication* the techniques using several factors.

We can use factors based on *what we know* (e.g., a password), on *what we process* (e.g., a secure token), or on *what we are* (e.g., with biometric recognition). For example, a smart card doing some authentication and that has to be unlocked by a PIN code is a strong authentication.

## 8.2 Password-Based Cryptography

Since passwords have low entropy, we must live with *online attacks* in which an adversary impersonates a honest user by guessing the password. What we want to avoid is that the protocol leaks some information which could be used as a stop test predicate in an *offline* exhaustive search.

In access control, if we use a challenge/response protocol like above, it leaks some information making offline exhaustive search easy. If we run the Diffie-Hellman protocol where the exchanged public keys are authenticated using a MAC with the password as a key, this also leaks some information leading to an offline attack.

There exists protocols not leaking information still doing the authentication. Interestingly, we can combine the password-based authentication with key agreement to set up an ephemeral symmetric key. This cryptographic primitive is called a password-based authenticated key exchange (PAKE).

For instance, in the EKE protocol by Bellovin and Merritt [15], Alice generates an ephemeral secret/public key pair, encrypts her public key with the password and sends it to Bob. Bob can decrypt it with the password, then use it to encrypt the session key K. The encrypted key can be re-encrypted using the password and sent to Alice. Then, she can recover the encrypted key and decrypt it with her ephemeral secret key to obtain K (see Fig. 8.2). This is an authenticated key agreement protocol. Note that the choice for the public-key encryption and symmetric encryption may be tricky as many instances are weak.

It is indeed very delicate to construct a secure protocol. With the EKE paradigm, we could easily imagine to use RSA with a constant exponent e and encrypt the modulus N. Let C be the encrypted modulus. As a result, and guess w for the password such that Decw(C) has small prime factors (e.g. it is even) would corresponds to an invalid RSA modulus. Hence, those guesses for w could be ruled out and we could keep a small partition of plausible w value. This attack is called a *partition attack*. Its principle is to rule out many possible w. By iterating the attack, we can then isolate the unique possible value of w.

There exists many password-based authenticated key agreement protocols. One popular one
(in standards) is the Secure Remote Password (SRP) protocol [92]. Probably, the simplest and most elegant one is SPAKE2 [10]. (See Fig. 8.3.)

$$\begin{array}{ccccc}\mbox{pick}x\in{\bf Z}_{q}^{*},\ X\gets g^{x}&\mbox{pick}y\in{\bf Z}_{q}^{*},\ Y\gets g^{y}\\ X^{*}\gets Xg_{2}^{wx}&\stackrel{{X^{*}}}{{\longrightarrow}}&Y^{*}\gets Yg_{3}^{wx}\\ K_{A}\gets(Y^{*}/g_{3}^{w})^{x}&\stackrel{{Y^{*}}}{{\longrightarrow}}&K_{B}\gets(X^{*}/g_{3}^{w})^{y}\\ K_{A}^{\prime}\gets\mathsf{KDF}(A,B,X^{*},Y^{*},w,K_{A})&K_{B}^{\prime}\leftarrow\mathsf{KDF}(A,B,X^{*},Y^{*},w,K_{B})\end{array}$$
A
output: K′
B
(public parameters: q prime, g, g2, g3 generators of the same order-q group)

## 8.3 From Secure Channel To Secure Communications

The main security properties that we must obtain for secure communication are:

- *confidentiality*: only the legitimate receiver can retrieve the message; - *authentication*: only the legitimate sender can create a new message; - *integrity*: the received message must be equal to the sent one.
Confidentiality is enforced by symmetric encryption.

We could enforce integrity using a hash function (but the digest must be sent with integrity protection), but it is not necessary since integrity and authentication are enforced at the same time by a MAC. We can however find some unorthodox authentication means which do not protect integrity. For instance, people sometimes say that GSM, Bluetooth and WiFi authenticate by encryption: no adversary can create a new message which can make sense after decryption. Indeed, the idea is to use one-time-pad on the message X concatenated with a (linear) CRC function.

An adversary could however modify an existing message so that it will not be decrypted like the original one. So, integrity is not protected.1 Good authentication means (such as the ones based on a MAC) should be preferred as they protect integrity at the same time. Finally, we can combine symmetric encryption and MAC (or use some authenticated encryption methods) to obtain the three properties at the same time.

The authenticated encryption techniques that we can use are the encrypt-then-MAC (see Fig. 8.4), MAC-then-encrypt (see Fig. 8.5), or the authenticated modes of operation such as CCM or GCM.

There are other properties that we need for secure communication, depending on applications:

- *freshness*: when a message is received, the receiver would like to be ensured that it is a new
(fresh) message and not a replayed one;
- *liveliness*: when a message is sent, the sender would like to be ensured that it will be
delivered, eventually;
- *timeliness*: in addition to liveliness, the sender would like the delivery time to be bounded; - *deniability*: no evidence of sending a message leaks; - *non-repudiation*: the sender of a message cannot prove he did not send his message (this is
somehow opposite to deniability);
- *forward secrecy*: secrecy remains even if some long-term keys leak in the future; - *postcompromise security*: security can heal after some secret keys leak.
These properties must be satisfied at the packet level. When it comes to order the packets in a communication session, we need further properties:

- *key establishment*: we need a way to set up the symmetric key which will be used during the
session;
- *session integrity*: we must guaranty that the sequence of packets is the same on both sides,
to avoid attacks based on packet swaps or packet drops;
- *privacy*: sometimes, we want to hide the identity of the sender and the receiver, or just the
fact that some sessions are made by the same person, or even the total duration or volume of communication. There are many notions of privacy.
When it comes to address session integrity, there is a property which is easy to obtain: *sequentiality*.

It makes sure that whenever a participant has received a message Xt in a sequence of messages X1*, . . . , X*t, then his counterpart must have seen the exact same sequence of messages, at least in the past (i.e., maybe he has sent another message which has not been delivered yet). Sequentiality can be obtained by using packet counters and by authenticating the counters. For instance, in the previous versions of TLS, a packet X was set as

$$Y=\operatorname{Enc}\left(X\|\operatorname{MAC}(\operatorname{seq}\|X)\right)$$
where seq is a synchronized packet counter. In TLS 1.3, we use

$$Y=\operatorname{AE.Enc}(\operatorname{seq},X)$$
with authenticated encryption AE, where seq is the additional data to be authenticated.2 What is missing to obtain full session integrity is the notion of *termination fairness*: to make sure that the last message of the communication is the same.

Fair termination can be required in a contract signing protocol: both parties want to terminate the protocol by agreeing on either the contract is valid or the transaction failed. We do not want that one participant thinks there is a contract and the other thinks the negotiation aborted. For this, they essentially need to terminate with a bit which must be the same on both ends. This can be done with a synchronization protocol such as the *keep-in-touch protocol* [13]: both participants have a bit. For a participant, if the bit is 0, he does nothing. Otherwise he goes through the keep-in-touch protocol. If it completes, the final bit is set to 1. In the case of any time-out in the protocol, a participant changes his bit to 0 and aborts the protocol. In the protocol, Alice picks a random number N and sends it encrypted.

Then, both participants exchange a total number of messages equal to N. After the Nth message is sent, the sending participant waits for a delay before completing the protocol. His counterpart can complete upon reception of the Nth message. It was proven that if the channel is already secure (but for termination fairness) and we want that both participants end on the same bit except with a probability bounded by some p, then we need an average number of exchanged messages to be Ω( 1
p). This is for any protocol and the keep-in-touch protocol achieves this bound. So, it is pretty expensive to achieve termination fairness in general. In most of secure channel implementations, this is not done.

## 8.4 Setup Of Secure Channels

To setup a symmetric key for a secure channel, we need a (less) secure channel. Indeed, with public-key cryptography, we only need an authenticated-integer channel to transmit a public key. Then, we can do key transfer or key exchange using a public-key cryptosystem or a key agreement protocol. If we don't have this authenticated-integer channel, we can still use the insecure channel but it will not protect against active adversaries playing the man-in-the-middle. We will still be protected against passive adversaries who only see the exchanged messages without interfering.

In practice, this authenticated-integer channel is either a real secure channel (e.g. a setup cable between two devices, or some short range wireless technology such as NFC) or relying on a third participant such as a human user (like in the Bluetooth pairing which is presented in Section A.6), a secure token (e.g., a SIM card), a key server or a certificate authority.

Finally, we can say that, except for the beginning and the end of a secure conversation (where we must setup a key and have fair termination, respectively), all other properties are pretty easy to achieve using good cryptography.

## 8.5 Setup By Narrowband Secure Channel

Secure communication (by means of symmetric cryptography) requires to set up a symmetric key through a fully secure channel. We can relax the confidentiality requirement on this channel by using public-key cryptography, but this still requires to set up a public key through a channel protecting authentication and integrity.

Public keys may be large (e.g. too large to be spelled by human beings). We could rely on a fully secure narrowband channel and use a password-based authenticated key agreement protocol. The secure narrowband channel would be used to set up a password. We have seen in a previous chapter how these primitives can set up a symmetric key using a securely set up password, even a password with low entropy.

The final step to complete the picture is to relax the confidentiality requirement on the narrowband secure channel. Using a narrowband channel protecting only authentication and integrity, we can transmit a *short authenticated string (SAS)*.

The Bluetooth example (which is presented in Section A.6) illustrates a technique which is quite interesting: to set up a secure communication channel by using a short string which was authenticated through an alternate channel (here: user monitoring). This short string actually a SAS. This type of protocol is used to set up personal area networks (e.g., with Bluetooth SSP in the version 2.1 or in the 802.11 standard in the version 3). It is also used to manually authenticate public keys. For instance, this is used in voice over IP protocol (e.g. ZRTP).

In a *message authentication protocol*, one sender wants to authenticate a message of arbitrary length by using a SAS. An example is when people print a SAS on their visit card which could be used to authenticate their public key, which can be retrieved online (over an insecure channel). Typically, we just authenticate the digest of the public key. Instead, by authenticating the hash of the commitment on the message (with public opening), we can have a secure protocol without relying on the collision resistance on the hash function. I.e., we could hash onto 80 bits only. To shrink the SAS further, we need interaction. One message authentication protocol was proposed by Vaudenay in 2005 [82] and proven secure, even with a SAS of 20 bits. Since then, other protocols have appeared.

## 8.6 Setup By A Trusted Third Party

Setting up a key using a third party can have several forms. First, we have seen human users playing the role of a third party (with a password or a SAS), which could make sense in some applications. We can have a pervasive third party in the form of a secure token such as a smart card, a secureID device, or a trusted computing platform (TPM). We can also use remote services.

With Kerberos [50], we have a key server to help two participants to communicate. With public-key infrastructures (PKI), we can rely on a certificate authority.

In Kerberos, every participant (server or client) shares a symmetric key with the authority.

When Alice wants to talk to Bob, she sends a request to the authority who will select a symmetric key K for them. Then, it will encrypt for Alice a "ticket" and K. The ticket contains K and is encrypted for Bob. In addition to this, it also contains the identity of Alice and a validity period for using K.

In PKIs, the certificate authority has a public key which is assumed to be securely distributed.

A server setting up his key must securely deposit his public key to the authority. The authority will in return sign a certificate assessing that the key was well deposited by this server. Then, a client receiving this certificate can check the signature and extract the public key of the server (see Fig. 8.6). This is typically used to establish a semi-authenticated channel: the client authenticates the server, then they set up a secure channel.

In practice, things do not work so smoothly. Indeed, there exist many certificate authorities and they are all equally recognized by browsers. Some servers may lose their keys, meaning that the (valid) certificate must be revoked. There are essentially two approaches for that: having regular certificate revocation lists (CRL) issued by the authority or using the online certificate status protocol (OCSP). Another problem is that some authorities may be corrupted.

There exist alternatives to the PKI model.

For instance, in the identity-based encryption model [24], the authority issues common parameters (see Fig. 8.7). To encrypt to Bob, Alice needs these common parameters, Bob's identity and the current time period in the system. To decrypt, Bob receives a new secret key from the authority every time period. This model has the problem that the authority owns the secret key of every user, but we can mix up this model with others. In the certificateless encryption model [12], Alice needs the common parameters, Bob's identity and the time period, and Bob's public key (which requires no certificate in this model). To decrypt, Bob needs the secret given by the authority and his own secret key (see Fig. 8.8). So, this

model resists to two possible attacks: adversaries modifying the public key and honest-but-curious authorities (who do not modify the public key).

As an example of a concrete construction, we mention the Boneh-Franklin [24] identity-based encryption scheme. It is the very first efficient scheme of this type. It is based on a pairing e, in a group of prime order q generated by some point P. The scheme is depicted on Fig. 8.9. It is set up by picking a master secret s ∈ Z∗
q then computing the main public parameter Kpub = sP.

Encryption of a message m for an identity ID is made by first extracting the public key QID = H1(ID) (meaning that a public function H1 generates a group element from a string ID), picking a random r ∈ Z∗
q. The encryption computes u = rP and v = m⊕H2(e(QID, Kpub)r). The ciphertext is (*u, v*). To decrypt, one needs the secret key dID = sQID. (As we can see, the authority can compute the secret of any user.) Essentially, we use that

$e(Q_{\rm ID},K_{\rm pub})^{r}=e(Q_{\rm ID},sP)^{r}=e(sQ_{\rm ID},rP)=e(d_{\rm ID},u)$
to decrypt m = v ⊕ H2(e(dID, u)).

## 8.7 Trust Management And Cryptography

The PKI model is very fragile as it requires to rely on a very long trust chain: the certificate authority, the browser editor, the hardware manufacturer, the retailer, the operating system in its real environment, and the human user who is not always careful.

The consequence is that there are phishing attacks on the network: some hackers make fake servers imitating the real ones, with either no secure connection (which is not always detected) or a secure one with an untrusted certificate (which may be accepted by the human user anyway), or with a revoked certificate or a certificate from a corrupted authority.

The PKI model is mainly the one used by TLS.3 The SSH protocol relies more on the fact that the public key does not change over time: the first connection may be problematic, but then the public key is locally stored and the client checks that it does not change. With the PGP software, public keys are cross-signed by a community of users. So, new keys may be checked based on reputation, in addition to comparison with a local key ring like with SSH.

There are other causes of security problems. For instance, the lack of cryptographic diversity
(everybody is using the same algorithms) makes the algorithms highly exposed. If one is broken, security may collapse. Some cryptographic protocols badly interact and their composition may be insecure even though they may be secure alone. Adversaries are making constant progresses, with their equipment, knowledge about algorithms, etc. Finally, many cryptographic algorithms are published with proofs which are incorrect, or models which are not appropriate, and it takes a long time before we realize it.

On top of these, the quantum threat is there. We know for sure that most of cryptographic schemes that we use today will be broken once quantum computers will be built. This means that the data which is sent today will eventually be decrypted. There is an urgent need for good cryptography which resists quantum attacks: post-quantum cryptography.