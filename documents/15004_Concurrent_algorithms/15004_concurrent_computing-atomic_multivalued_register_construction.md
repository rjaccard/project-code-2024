# 7. Atomic multivalued register construction 

In Chapter 5, we described an implementation of an atomic 1WNR register from regular ones that uses sequence numbers growing without bound and, thus, must assume base registers of unbounded capacity. In this chapter, we propose a bounded solution. But let us first recall a few related constructions we discussed earlier.

### 7.1. From single-reader regular to multi-reader atomic

In Chapter 6, we discussed how to construct an atomic bit from only three safe bits. One of the bits is used for storing the value itself, and the other two are used for exchanging control signals between the writer and the reader. In the one-reader case, we can turn a series of atomic 1W1R bits into an atomic bounded multi-valued register using the simple transformation algorithm in Section 4.5.3. But how do we construct a multi-reader multi-valued atomic register?

It is straightforward to get a regular bounded multi-valued multi-reader register from single-reader ones (recall the algorithms in Section 4.4.1). This chapter describes how to construct an atomic one.

We begin with describing a simpler algorithm that, in addition to regular registers used to store the written value itself, employs an atomic bit used for transmitting control signals from the writer to the readers.

### 7.2. Using an atomic control bit

The construction of a multi-reader register using two regular registers $R E G_{1}$ and $R E G_{2}$ and an atomic bit WFLAG is given in Figure 7.1.

```
operation R.write $(v)$ :
(1) WFLAG $\leftarrow$ true;
(2) $R E G_{1} \leftarrow v$
(3) $W F L A G \leftarrow$ false;
(4) $R E G_{2} \leftarrow v$;
operation R.read () :
(5) $v a l \leftarrow R E G_{1}$;
(6) if $\neg W F L A G$ then return(val);
(7) $v a l \leftarrow R E G_{2}$;
(8) return (val)
```

Figure 7.1.: From regular registers and an atomic control bit to an atomic register.

In the algorithm, the value is written twice: first in $R E G_{1}$ and then in $R E G_{2}$. Before writing to $R E G_{1}$, the writer sets WFLAG to true to signal to the readers the beginning of a new write operation. After writing to $R E G_{1}$, the writer sets WFLAG back to false.

A read operation reads $R E G_{1}$ and then checks WFLAG. If WFLAG contained false, then the process returns the value previously read in $R E G_{1}$. If WFLAG contained true, then the process reads and returns the value in $R E G_{2}$.

Intuitively, $W F L A G=$ true means that there is a possibility that the value found earlier in $R E G_{1}$ is written by a concurrent write operation and, therefore, a subsequent read operation might find the older value in $R E G_{1}$, due to new-old inversion on $R E G_{1}$. To prevent, new-old inversion on the implemented register, it is therefore necessary to return a more conservative value read in $R E G_{2}$.

Theorem 17 The algorithm in Figure 7.1 implements a 1WMR atomic register using one 1WMR atomic bit and two 1 WMR regular registers.

Proof Let $H$ be a history of the algorithm in Figure 7.1, and let $L$ be the corresponding execution. Let $\pi$ be any regular reading function defined on read operations on $R E G_{1}$ or $R E G_{2}$. We extend $\pi$ to the high-level read operations on the implemented register $R$ as follows. For each high-level read $r$ returning the value found by a read operation $\rho$ in $R E G_{1}$ or $R E G_{2}$ (in lines 5 or 7 ), let $\pi(r)$ be the high-level write operation $w$ that contains $\pi(\rho)$.

It is immediate from the construction that the resulting extension of $\pi$ on high-level read operations is regular. Indeed, the interval of every such $\pi(\rho)$ belongs to the interval of $w$. Thus, $\rho \rightarrow_{L} \pi(\rho)$ implies $r \rightarrow_{H} \pi(r)$, i.e., $A 0$ is satisfied. Additionally, since every complete write operation contains writes on both $R E G_{1}$ and $R E G_{2}, A 1$ satisfied by $\pi$ defined over reads of $R E G_{1}$ and $R E G_{2}$ implies that for any $w$ and $r$, we cannot have $\pi(r) \rightarrow_{H} w \rightarrow_{H} r$, i.e., $A 1$ is satisfied.

Now we are going to prove $A 2$. By contradiction, suppose that for two high-level operations $r_{1}$ and $r_{2}$, we have $r_{1} \rightarrow_{H} r_{2}$ and $\pi\left(r_{2}\right) \rightarrow_{H} \pi\left(r_{1}\right)$. For $i=1,2$, let $\rho_{i}$ be the read operation on $R E G_{1}$ or $R E G_{2}$ that was used by $r_{i}$ to evaluate the returned value. Clearly, $\rho_{1} \rightarrow_{L} \rho_{2}$.

The following cases are possible:

(1) Both $\rho_{1}$ and $\rho_{2}$ read $R E G_{1}$.

By property $A 1$ of regular functions, $\pi\left(\rho_{1}\right) \nrightarrow_{L} \rho_{2}$ : otherwise we would have $\pi\left(\rho_{2}\right) \rightarrow_{L}$ $\pi\left(\rho_{1}\right) \rightarrow_{L} \rho_{2}$, i.e., $\rho_{2}$ would return an "overwritten" value. By property $A 0, \rho_{1} \nrightarrow_{L} \pi\left(\rho_{1}\right)$. Thus, given that $\rho_{1} \rightarrow_{L} \rho_{2}, \pi\left(\rho_{1}\right)$ is concurrent with both $\rho_{1}$ and $\rho_{2}$.

By the algorithm, just before writing to $R E G_{1}$ in $\pi\left(\rho_{1}\right)$, operation $\pi\left(r_{1}\right)$ has set WFLAG to true. Since $\pi\left(\rho_{1}\right)$ is concurrent with both $\rho_{1}$ and $\rho_{2}$, no write on WFLAG took place in the interval between the response of $\rho_{1}$ and the invocation of $\rho_{2}$. Notice that $r_{1}$ checks WFLAG during this interval and, thus, true was the last written value on WFLAG when it is read within $r_{1}$. Thus, after having read $R E G_{1}, r_{1}$ must have found true in $W F L A G$ and returned the value read in $R E G_{2}$-a contradiction with the assumption that the value read in $R E G_{1}$ is returned by $r_{1}$.

(2) Both $\rho_{1}$ and $\rho_{2}$ read $R E G_{2}$.

Similarly, using $A 0$ and $A 1$, we derive that $\pi\left(\rho_{1}\right)$, updating $R E G_{2}$, is concurrent with both $\rho_{1}$ and $\rho_{2}$. By the algorithm, just before writing to $R E G_{2}, \pi\left(r_{1}\right)$ has set WFLAG to false. Thus, before reading $R E G_{2}, r_{2}$ must have read false in WFLAG and returned the value read in $R E G_{1}-\mathrm{a}$ contradiction with the assumption that the value read in $R E G_{2}$ is returned by $r_{2}$.

(3) $\rho_{1}$ reads $R E G_{2}$ and $\rho_{2}$ reads $R E G_{1}$.

In $\pi\left(r_{1}\right), \pi\left(\rho_{1}\right)$ is preceded by a write $w r_{1}$ on $R E G_{1}: w r_{1} \rightarrow_{L} \pi\left(\rho_{1}\right)$. By $A 0, \rho_{1} \nrightarrow_{L} \pi\left(\rho_{1}\right)$. Now relations $w r_{1} \rightarrow_{L} \pi\left(\rho_{1}\right), \rho_{1} \rightarrow_{L} \pi\left(\rho_{1}\right)$, and $\rho_{1} \rightarrow_{L} \rho_{2}$ imply $w r_{1} \rightarrow_{L} \rho_{2}$.

But, by our assumption, $\pi\left(r_{2}\right) \rightarrow_{H} \pi\left(r_{1}\right)$ and, thus, $\pi\left(\rho_{2}\right) \rightarrow_{L} w r_{1}$, which, together with $w r_{1} \rightarrow_{L} \rho_{2}$, implies $\pi\left(\rho_{2}\right) \rightarrow_{L} w r_{1} \rightarrow_{L} \rho_{2}$, violating $A 1$-a contradiction.

(4) $\rho_{1}$ reads $R E G_{1}$ and $\rho_{2}$ reads $R E G_{2}$.

By the algorithm, after $\rho_{1}$ has returned, $r_{1}$ found false in WFLAG. After that $r_{2}$ read $R E G_{1}$, found true in WFLAG, and then read and returned the value in $R E G_{2}$. Let $r f_{1}$ and $r f_{2}$ be the read operations of WFLAG performed within $r_{1}$ and $r_{2}$, respectively. Thus, $\rho_{1} \rightarrow_{L} r f_{1} \rightarrow_{L}$ $r f_{2} \rightarrow_{L} \rho_{2}$.

Since WFLAG is atomic, there must be a write operation wf on WFLAG changing its value from false to true (line 1) that is linearized between linearizations of $r f_{1}$ and $r f_{2}$ and, thus, $w f \phi_{L} r f_{1}$ and $r f_{2} \succ_{L} w f$. Let $w r_{1}$ and $w r_{2}$ be the write operations on, respectively, $R E G_{1}$ and $R E G_{2}$ that immediately precede $w f$. (Recall that $w r_{1}$ and $w r_{2}$ can belong to the initializing write operation on $R$.

Now we derive that $\pi\left(\rho_{1}\right)$ must be $w r_{1}$ or an earlier write on $R E G_{1}$. Otherwise, we would get $w f \rightarrow_{L} \pi\left(\rho_{1}\right)$ which, combined with $\rho_{1} \rightarrow_{L} r f_{1}$ and $w f \nrightarrow_{L} r f_{1}$, implies that $\rho_{1} \rightarrow_{L} \pi\left(\rho_{1}\right)$-a violation of $A 0$.

On the other hand, by $A 1$, there does not exist $w r$, a write operation on $R E G_{2}$, such that $\pi\left(\rho_{2}\right) \rightarrow_{L}$ $w r \rightarrow_{L} \rho_{2}$.

Similarly, $\pi\left(\rho_{2}\right)$ must be $w r_{2}$ or a later write on $R E G_{2}$. Otherwise, we would get $\pi\left(\rho_{2}\right) \rightarrow_{L} w r_{2}$. But $w r_{2} \rightarrow_{L} w f, r f_{2} \rightarrow_{L} w f$ and $r f_{2} \rightarrow_{L} \rho_{2}$ imply $w r_{2} \rightarrow_{L} \rho_{2}$. Thus, $\pi\left(\rho_{2}\right) \rightarrow_{L} w r_{2} \rightarrow_{L} \rho_{2}-$ a violation of $A 1$.

Therefore, $\pi\left(\rho_{1}\right) \rightarrow_{L} \pi\left(\rho_{2}\right)$ and, thus, $\pi\left(r_{1}\right)=\pi\left(r_{2}\right)$ or $\pi\left(r_{1}\right) \rightarrow_{H} \pi\left(r_{2}\right)$-a contradiction.

Hence, $\pi$ satisfied $A 2$ and the algorithm indeed implements an atomic register.

Notice that we only used the fact that WFLAG is atomic in case (4). By replacing WFLAG with a regular register, or a set of registers providing the functionality of one regular register, we would maintain atomicity in cases (1)-(3). However, as we will see in the next section, taking care of case (4) incurs nontrivial changes in processing the remaining cases.

### 7.3. The algorithm

The bounded algorithm transforming regular multi-valued multi-reader registers into an atomic one is presented in Figure 7.2. Notice that we replaced the atomic control bit WFLAG in the algorithm in Figure 7.1 with several regular registers of bounded capacity:

- $L E V E L=0,1,2$ : a ternary regular register used by the writer to signal to the readers at which "stage of writing" it currently is.
- $F C[1, \ldots, n]$ : an array of regular binary registers, each $F C[i]$ is written by reader $p_{i}$ and by read by the other readers.
- $R C[1, \ldots, n]$ : an array of regular binary registers, each $R C[i]$ is written by reader $p_{i}$ and read by the writer and other readers.
- $W C[1, \ldots, n]$ : an array of regular binary registers, written by the writer and read by the readers.

Intuitively, $L E V E L=1$ corresponds to $W F L A G=$ true, and $L E V E L=2$ and $L E V E L=0$ correspond to WFLAG = false in the algorithm in Figure 7.1. But $L E V E L$ is a regular register now. Hence, to handle the possible new-old inversion on LEVEL, the readers exchange information with each other using the array $F C[1, \ldots, n]$ and with the writer using the arrays $R C[1, \ldots, n]$ and $W C[1, \ldots, n]$.

```
operation R.write $(v)$ :
(1) $L E V E L \leftarrow 1$;
(2) $R E G_{1} \leftarrow v$
(3) $L E V E L \leftarrow 2$;
(4) $L E V E L \leftarrow 0$;
(5) $R E G_{2} \leftarrow v$
(6) for $j=1, \ldots, n$ do
(7) $\quad l r \leftarrow R C[j]$
(8) $\quad W C[j] \leftarrow \neg l r$
operation $R$.read () (code for reader $\left.p_{i}\right)$ :
(9) $v a l \leftarrow R E G_{1}$;
(10) $l w \leftarrow W C[i]$
(11) if $l w \neq R C[i]$ then
(12) $\quad F C[i] \leftarrow$ false;
(13) $\quad R C[i] \leftarrow l w$;
(14) case $L E V E L$ do
(15) 0: return (val);
(16) 2: $F C[i] \leftarrow$ true; return (val);
(17) 1 : for $j=1, \ldots, n$ do
(18) $\quad l r \leftarrow R C[j]$;
(19) $\quad l f \leftarrow F C[j]$;
(20) $\quad l w \leftarrow W C[j]$
(21) $\quad$ if $(l r=l w) \wedge l f$ then
(22)
(23)
$(24)$
$F C[i] \leftarrow$ true
(25) $\quad \operatorname{return}(\mathrm{val})$
return $($ val);
```

Figure 7.2.: From bounded regular registers to a bounded atomic register.

Theorem 18 The algorithm in Figure 7.2 implements a IWMR atomic register using 1WMR regular registers.

Proof Consider a history $H$ and the corresponding execution $L$ of the algorithm in Figure 7.2. As in the proof of Theorem 17, we take any reading function $\pi$ acting over read operations on base regular registers, and then extend it to high-level read operations on the implemented register $R$ as follows. For each complete high-level operation $r$ returning the value read by an operation $\rho$ in $R E G_{1}$ (line 9 ) or $R E G_{2}$ (line 24), let $\pi(r)$ be the high-level write operation $w$ that contains $\pi(\rho)$. It is immediate that $\pi$, as a function on high-level reads, is regular.

Now assume, by contradiction, that $\pi$ is not atomic, i.e., there exist two high-level operations $r_{1}$ and $r_{2}$, such that $r_{1} \rightarrow_{H} r_{2}$ and $\pi\left(r_{2}\right) \rightarrow_{H} \pi\left(r_{1}\right)$. For $i=1,2$, let $\rho_{i}$ be the read operation on $R E G_{1}$ or $R E G_{2}$ that was used by $r_{i}$ to evaluate the returned value.

For brevity, we introduce the following notation:

- $w_{1}=\pi\left(\rho_{1}\right)$ and $w_{2}=\pi\left(\rho_{2}\right)$
- $w r_{i, j}$ denotes the write to $R E G_{j}$ performed within $w_{i}(i=1,2, j=1,2)$, if any;
- $r r_{i, j}$ denotes the read of $R E G_{j}$ performed within $r_{i}(i=1,2, j=1,2)$;
- $w l_{i, j}$ denotes $j$-th write to $L E V E L$ performed within $w_{i}(i=1,2, j=1,2,3)$, if any; note that $w l_{i, j}$ writes the value $j \bmod 3$
- $r l_{i}$ denotes the read operations on $L E V E L$, performed within $r_{i}(i=1,2)$.

Since every complete high-level write operation contains writes on both $R E G_{1}$ and $R E G_{2}$, it follows that $w_{2}$ immediately precedes $w_{1}$. Otherwise, regardless of which register $R E G_{i}(i=1,2)$ is read by $\rho_{2}$, we would have a write $w r$ on $R E G_{i}$ such that $\pi\left(\rho_{2}\right) \rightarrow_{L} w r \rightarrow_{L} \pi\left(\rho_{1}\right)$ which, combined with $\rho_{1} \rightarrow_{L} \pi\left(\rho_{1}\right)$ and $\rho_{1} \rightarrow_{L} \rho_{2}$ (our initial assumption), would imply $\pi\left(\rho_{2}\right) \rightarrow_{L}$ wr $\rightarrow_{L} \rho_{2}$-a violation of $A 1$ for $\rho_{2}$.

As in the proof of Theorem 17, we now should consider the four following cases:

(1) $\rho_{1}$ reads $R E G_{2}$ and $\rho_{2}$ reads $R E G_{1}$.

Since $w_{2} \rightarrow_{H} w_{1}$, we have $\pi\left(\rho_{2}\right) \rightarrow_{L} w r_{1,1} \rightarrow_{L} \pi\left(\rho_{1}\right)$. Now, by $A 0, \rho_{1} \rightarrow_{L} \pi\left(\rho_{1}\right)$, which, together with $\rho_{1} \rightarrow_{L} \rho_{2}$, implies $\pi\left(\rho_{2}\right) \rightarrow_{L} w r_{1,1} \rightarrow_{L} \rho_{2}$-a violation of $A 1$ for $\rho_{2}$.

(2) Both $\rho_{1}$ and $\rho_{2}$ read $R E G_{2}$.

Properties $A 0$ and $A 1$ imply that $\pi\left(\rho_{1}\right) \nrightarrow_{L} \rho_{2}$ and $\rho_{1} \nrightarrow_{L} \pi\left(\rho_{1}\right)$, i.e., $\pi\left(\rho_{1}\right)$ is concurrent with both $\rho_{1}$ and $\rho_{2}$. Thus, no write on $L E V E L$ takes place between the response of $\rho_{1}$ and the invocation $\rho_{2}$. By the algorithm, immediately before updating $R E G_{2}, w_{1}$ writes 0 to $L E V E L$. Thus, before reading $R E G_{2}, r_{2}$ must have read 0 in $L E V E L$ and return the value read in $R E G_{1}-$ a contradiction.

(3) $\rho_{1}$ reads $R E G_{1}$ and $\rho_{2}$ reads $R E G_{2}$.

Just before updating $R E G_{1}$ in $\pi\left(\rho_{1}\right)$, $w_{1}$ writes 1 to $L E V E L$ in operation $w l_{1,1}$, thus, $w l_{1,1} \rightarrow_{L}$ $\pi\left(\rho_{1}\right), \rho_{1} \rightarrow_{L} r l_{1}$, and $\rho_{1} \nrightarrow_{L} \pi\left(\rho_{1}\right)$ (property $A 0$ ) imply $w l_{1,1} \rightarrow_{L} r l_{1} \rightarrow_{L} r l_{2}$.

By the algorithm, $r_{2}$ must have read 1 in $L E V E L$. Suppose that $w l_{1,1} \neq \pi\left(r l_{2}\right)$, i.e., $r l_{2}$ reads 1 written to $L E V E L$ by another write operation $w l$. Since $w l_{1,1} \rightarrow_{L} r l_{2}$, property $A 1$ for $r l_{2}$ implies $w l_{1,1} \rightarrow_{L} w l$. By the algorithm, since $w l$ writes 1 , we have $w l_{1,2} \rightarrow_{L} w l$. But $\pi\left(\rho_{2}\right) \rightarrow_{L} w r_{1,2}$ (since $\left.w_{2} \rightarrow_{H} w_{1}\right), r l_{2} \nrightarrow_{L} w l\left(A 0\right.$ for $\left.r l_{2}\right)$, and $r l_{2} \rightarrow_{L} \rho_{2}$ (by the algorithm). Therefore, $\pi\left(\rho_{2}\right) \rightarrow_{L} w r_{1,2} \rightarrow_{L} \rho_{2}$-a violation of $A 1$ for $\rho_{2}$. Thus, $\pi\left(r l_{2}\right)=w l_{1,1}$.

Since $r l_{1} \rightarrow_{L} r l_{2}$ (by the assumption), $w l_{1,2} \nrightarrow_{L} r l_{2}\left(A 1\right.$ for $r l_{2}$ ), and $w l_{1,2} \rightarrow_{L} w l_{1,3}$ (by the algorithm), we have $r l_{1} \rightarrow_{L} w l_{1,3}$. Also, since $w l_{1,1} \rightarrow_{L} w r_{1,1}, \rho_{1} \rightarrow_{L} r l_{1}$ (by the algorithm), and $\rho_{1} \rightarrow_{L} w r_{1,1}\left(A 0\right.$ for $\left.\rho_{1}\right)$, we have $w l_{1,1} \rightarrow_{L} r l_{1}$. Furthermore, $r l_{1} \rightarrow_{L} w l_{1,3}$ : otherwise, $w l_{1,2} \rightarrow_{L} w l_{1,3}$ and $r l_{1} \rightarrow_{L} r l_{2}$ would imply $w l_{1,1} \rightarrow_{L} w l_{1,2} \rightarrow_{L} r l_{2}$-a violation of $A 1$ for $r l_{2}$.

Thus, by the algorithm, $r l_{1}$ reads either 1 written by $w l_{1,1}$ or 2 written by $w l_{1,2}$. In both cases, $r_{1}$ (executed, e.g., by reader $p_{i}$ ) sets $F C[i]$ to true before returning the value read by $\rho_{1}$ (in lines 16 or 22$)$.

Since $\rho_{2}$ reads $R E G_{2}$, we have $\operatorname{wr}_{1,2} \rightarrow_{L} \rho_{2}$, otherwise we would violate $A 1$ by having $\pi\left(\rho_{2}\right) \rightarrow_{L}$ $w r_{1,2} \rightarrow_{L} \rho_{2}$. Thus, $\rho_{1} \nrightarrow_{L} \pi\left(\rho_{1}\right)$ and $w r_{1,2} \nrightarrow_{L} \rho_{2}$ imply that the writer performs no updates on registers $W C[i]$ in the interval between the response of $\rho_{1}$ and before $r_{2}$ finishes reading $W C[i]$. Note that, within this interval, $r_{1}$ makes sure that $R C[i]=W C[i]$ and then sets $F C[i]$ to true.

Any subsequent operation $r w$ performed by $p_{i}$ writing false in $F C[i]$ or modifying $R C[i]$ can only take place if $p_{i}$ previously finds out that $R C[i] \neq W C[i]$ (line 11), which cannot take place before a write on $W C[i]$ performed by the writer which, by the algorithm, must succeed $w r_{1,2}$ : indeed, after $r_{1}$ ensures $R C[i]=W C[i]$ and sets $F C[i]$ to true and before it sets $F C[i]$ to false and modifies $R C[i]$ (lines 12 and 13), the writer must modify $W C[i]$ which can only happen after $w r_{1,2}$.

Thus, reads of $R C[i]$ and $F C[i]$ performed by $r_{2}$ precede $r w$, and the values read by $r_{2}$ satisfy $R C[i]=W C[i]$ and $F C[i]=$ true (Figure 7.3). By the algorithm, $r_{2}$ must then return the value of $R E G_{1}$ - a contradiction.

(4) Both $\rho_{1}$ and $\rho_{2}$ read $R E G_{1}$.

By $A 0, \rho_{1} \nrightarrow_{L} \pi\left(\rho_{1}\right)$ and by $A 1, \pi\left(\rho_{1}\right) \nrightarrow_{L} \rho_{2}$, i.e., $\pi\left(\rho_{1}\right)$ is concurrent with both $\rho_{1}$ and $\rho_{2}$.

Hence, $\pi\left(r l_{1}\right)=w l_{1,1}$, i.e., $r_{1}$ reads 1 in $L E V E L$, and then returns the value of $R E G_{1}$ in line 23 before the response of $\pi\left(\rho_{1}\right)$.

We say that a read operation $r_{k}$ finishes its check-forwarding when it executes the last read operation on some $W C[j]$ in line 20 before exiting the for loop starting in line 17. For any operation $o p$, we write $c f_{k} \rightarrow_{L} o p$ if $r_{k}$ finishes its check-forwarding before the invocation of $o p$.

Consider now any (high-level) read operation $r_{k}$ returning in lines 23 or 25 such that:

(1) $r l_{k} \rightarrow_{L} w l_{1,1}$, and

(2) $c f_{k} \rightarrow_{L} w l_{1,2}$.

Note that $r_{1}$ satisfies these conditions. We establish a contradiction by showing that no such $r_{k}$ can return in line 23 .

For read operations $r_{\ell}$ and $r_{m}$, we say that $r_{\ell}$ finishes check-forwarding before $r_{m}$, and we write $c f_{\ell} \rightarrow_{L} c f_{m}$, if the last read operation of the check-forwarding phase of $r_{\ell}$ precedes the last read operation of the check-forwarding phase of $r_{m}$.

By contradiction, assume that there is a non-empty set $R$ of read operations satisfying conditions (1) and (2) above that return in line 23. Without loss of generality, let $r_{k}$ be any operation in $R$, such that no other operation in $R$ finishes its check-forwarding before $r_{k}$.

By the algorithm, before returning in line $23, r_{k}$ finds out that, for some reader $p_{\ell}, F C[\ell]=$ true and $W C[\ell]=R C[\ell]$. Let $r_{t}$ be the read operation performed by $p_{\ell}$ that, according to the reading function $\pi$, wrote this value in $F C[\ell]$. Let $r f$ denote the read operation on $F C[\ell]$ performed within $r_{k}$ (line 19), and let $w f$ denote the write operation on $F C[\ell]$ performed within $r_{t}$ (lines 16 or 22), i.e., $\pi(r f)=w f$. By the algorithm, before executing $w f, r_{t}$ read 1 or 2 in LEVEL.

First we are going to show that $r_{t}$ reads the value written in $L E V E L$ by a write operation that precedes $w_{1}$. Since $r f \rightarrow_{L} w l_{1,2}\left(r_{k} \in R\right.$ and the check-forwarding phases of reads in $R$ satisfy condition (2) above), $r l_{t} \rightarrow_{L} w f$ (by the algorithm), and $r f A_{L} w f$ ( $A 0$ for $r f$ ), we have $r l_{t} \rightarrow_{L}$ $w l_{1,2}$ that is $r l_{t}$ returns the value written by $w l_{1,1}$ or an earlier write.

Suppose, by contradiction, that $\pi\left(r l_{t}\right)=w l_{1,1}$, i.e., $r l_{t}$ returns 1 written by $w l_{1,1}$. By $A 0$, we have $r l_{t} \rightarrow_{L} w l_{1,1}$. Note that the fact that the last read operation of $c f_{k}$ succeeds $r f, c f_{t} \rightarrow_{L} w f$ (by
the algorithm), and $r f \nrightarrow_{L} w f(A 0$ for $r f)$ imply $c f_{t} \rightarrow_{L} c f_{k}$. But $c f_{t} \rightarrow_{L} w f$ and $r f \rightarrow_{L} w l_{1,2}$ imply $c f_{t} \rightarrow_{L} w l_{1,2}$, i.e., $r_{t}$ satisfies conditions (1) and (2), while $c f_{t} \rightarrow_{L} c f_{k}$ - a contradiction with the definition of $r_{k}$.

Hence, $r l_{t}$ returns a value written by a write operation on $L E V E L$ preceding $w_{1}$. Since $r_{t}$ modified $F C[\ell], r l_{t}$ must have returned 1 or 2 , and $w l_{2,3} \nrightarrow_{L} r l_{t}$ (otherwise, the only value that $r l_{t}$ can return is 0 ). Note that, by the algorithm, any subsequent read operation by $p_{\ell}$ must set $F C[\ell]$ to false (line 12) before modifying $R C[\ell]$ (line 13). Since $r_{k}$ first reads $R C[\ell]$ and then reads true in $F C[\ell]$ written by $w f$, the value of $R C[\ell]$ read by $r_{k}$ must then be the value that $r_{t}$ has "ensured", i.e., written or read in its last operation on $R C[\ell]$. Also, $w_{2}$ reads $R C[\ell]$ after the invocation of $r l_{t}$ and before $r_{k}$ read $R C[\ell]$, therefore it must read the same value of $R C[\ell]$.

Recall that after executing $w l_{2,3}, w_{2}$ ensures that $W C[\ell] \neq R C[\ell]$. Since, no succeeding update on $W C[\ell]$ takes place before $r_{k}$ finishes its check-forwarding, the value of $W C[\ell]$ read by $r_{k}$ must be the value that $w_{2}$ has previously ensured (Figure 7.4).

Thus, $r_{k}$ will find $W C[\ell] \neq R C[\ell]$-a contradiction with the assumption that $r_{k}$ returns line 23 after finding out that $F C[\ell]=$ true and $W C[\ell]=R C[\ell]$.

Thus, the algorithm in Figure 7.2 ensures $A 0, A 1$ and $A 2$, and the algorithm indeed implements an atomic register.

