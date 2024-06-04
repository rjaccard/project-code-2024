# 5. Unbounded register transformations 

In this chapter we consider a simplistic case when unbounded base objects, i.e., registers of unbounded capacity, can be used. This assumption allows us to use the sequence numbers: each written value is associated with a sequence number that intuitively captures the number of write operations performed up to now. A typical base register consists therefore of two fields: a data field that stores the value of the register and a control field that stores the sequence number associated with it.

Of course, assuming base objects of unbounded capacity is not very realistic. In the coming Chapters 6 and 7 we discuss algorithms that implement bounded (i.e., storing values from a bounded range) atomic registers using bounded safe registers.

### 5.1. 1W1R registers: From unbounded regular to atomic

We show in the following how to implement an 1W1R atomic register using a 1W1R regular register. The use of sequence numbers make such a construction easy and helps in particular prevent the new/old inversion phenomenon. Preventing this, while preserving regularity, means, by Theorem 5, that the constructed register is atomic.

The algorithm is described in Figure 5.1. Exactly one base regular register $R E G$ is used in the implementation of the high-level register $R$. The local variable $s n$ at the writer is used to hold sequence numbers. It is incremented for every new write in $R$. The scope of the local variable aux used by the reader spans a read operation; it is made up of two fields: a sequence number (aux.sn) and a value (aux.val).

Each time it writes a value $v$ in the high-level register, $R$, the writer writes the pair $[s n, v]$ in the base regular register $R E G$. The reader manages two local variables: last_sn stores the greatest sequence number it has even read in $R E G$, and last_val stores the corresponding value. When it wants to read $R$, the reader first reads $R E G$, and then compares last_sn with the sequence number it has just read in $R E G$. The value with the highest sequence number is the one returned by the reader and this prevents new/old inversions.

```
operation R.write $(v)$ :
    $s n \leftarrow s n+1 ;$
    $R E G \leftarrow[s n, v] ;$
    return ()
operation R.read():
    aux $\leftarrow R E G$
    if $($ aux.sn $>$ last_sn $)$ then last_sn $\leftarrow$ aux.sn;
        last_val $\leftarrow$ aux.val;
    return (last_val)
```

Figure 5.1.: From regular to atomic: unbounded construction

Theorem 11 Given an unbounded 1WIR regular register, the algorithm described in Figure 5.1 constructs a 1W1R atomic register.

Proof The proof is similar to the proof of Theorem 5. We associate with each read operation $r$ of the high-level register $R$, the sequence number (denoted $s n(r)$ ) of the value returned by $r$ : this is possible as the base register is regular and consequently a read always returns a value that has been written with its sequence number, that value being the last written value or a value concurrently written (if any). Considering an arbitrary history $H$ of register $R$, we show that $H$ is atomic by building an equivalent sequential history $S$ that is legal and respects the partial order on the operations defined by $\rightarrow_{H}$.

$S$ is built from the sequence numbers associated with the operations. First, we order all the write operations according to their sequence numbers. Then, we order each read operation just after the write operation that has the same sequence number. If two reads operations have the same sequence number, we order first the one whose invocation event is first. (Remember that we consider a 1W1R register.)

The history $S$ is trivially sequential as all the operations are placed one after the other. Moreover, $S$ is equivalent to $H$ as it is made up of the same operations. $S$ is trivially legal as each read follows the corresponding write operation. We now show that $S$ respects $\rightarrow_{H}$.

- For any two write operations $w 1$ and $w 2$ we have either $w 1 \rightarrow_{H} w 2$ or $w 2 \rightarrow_{H} w 1$. This is because there is a single writer and it is sequential: as the variable $s n$ is increased by 1 between two consecutive write operations, no two write operations have the same sequence number, and these numbers agree on the occurrence order of the write operations. As the total order on the write operations in $S$ is determined by their sequence numbers, it consequently follows their total order in $H$.
- Let $o p 1$ be a write or a read operation, and $o p 2$ be a read operation such that $o p 1 \rightarrow_{H} o p 2$. It follows from the algorithm that $\operatorname{sn}(o p 1) \leq \operatorname{sn}(o p 2)$ (where $\operatorname{sn}(o p)$ is the sequence number of the operation $o p)$. The ordering rule guarantees that $o p 1$ is ordered before $o p 2$ in $S$.
- Let $o p 1$ be a read operation, and $o p 2$ a write operation. Similarly to the previous item, we then have $s n(o p 1)<s n(o p 2)$, and consequently $o p 1$ is ordered before $o p 2$ in $S$ (which concludes the proof).

One might think of a naïve extension of the previous algorithm to construct a 1WMR atomic register from base 1W1R regular registers. Indeed, we could, at first glance, consider an algorithm associating one 1W1R regular register per reader, and have the writer writes in all of them, each reader reading its dedicated register. Unfortunately, a fast reader might see a new concurrently written value, whereas a reader that comes later sees the old value. This is because the second reader does not know about the sequence number and the value returned by the first reader. The latter stores them locally. In fact, this can happen even if the base 1W1R registers are atomic. The construction of a 1WMR atomic register from base 1W1R atomic registers is addressed in the next section.

### 5.2. Atomic registers: from unbounded 1W1R to 1WMR

In Section 4.4.1, we presented an algorithm that builds a 1WMR safe/regular register from similar 1W1R base registers. We also pointed out that the corresponding construction does not build a 1WMR atomic register even when the base registers are 1W1R atomic (see the counter-example presented in Figure 4.3).

This section describes such an algorithm: assuming 1W1R atomic registers, it shows how to go from single reader registers to a multi-reader register. This algorithm uses sequence numbers, and requires unbounded base registers.

Overview. As there are now several possible readers, actually $n$, we make use of several $(n)$ base 1W1R atomic registers: one per reader. The writer writes in all of them. It writes the value as well as a sequence number. The algorithm is depicted in Figure 5.2.

We prevent new/old inversions (Figure 4.3) by having the readers "help" each other. The helping is achieved using an array $\operatorname{HELP}[1: n, 1: n]$ of $1 \mathrm{~W} 1 \mathrm{R}$ atomic registers. Each register contains a pair (sequence number, value) created and written by the writer in the base registers. More specifically, $\operatorname{HELP}[i, j]$ is a $1 \mathrm{~W} 1 \mathrm{R}$ atomic register written only by $p_{i}$ and read only by $p_{j}$. It is used as follows to ensure the atomicity of the high-level 1WMR register $R$ that is constructed by the algorithm.

- Help the others. Just before returning the value $v$ it has determined (we discuss how this is achieved in the second bullet below), reader $p_{i}$ helps every other process (reader) $p_{j}$ by indicating to $p_{j}$ the last value $p_{i}$ has read (namely $v$ ) and its sequence number $s n$. This is achieved by having $p_{i}$ update $H E L P[i, j]$ with the pair $[s n, v]$. This, in turn, prevents $p_{j}$ from returning in the future a value older than $v$, i.e., a value whose sequence number would be smaller than $s n$.
- Helped by the others. To determine the value returned by a read operation, a reader $p_{i}$ first computes the greatest sequence number that it has ever seen in a base register. This computation involves all 1W1R atomic registers that $p_{i}$ can read, i.e., $R E G[i]$ and $H E L P[j, i]$ for any $j . p_{i}$. Reader $p_{i}$ then returns the value that has the greatest sequence number $p_{i}$ has computed.

The corresponding algorithm is described in Figure 5.2. Variable $a u x$ is a local array used by a reader; its $j$ th entry is used to contain the (sequence number, value) pair that $p_{j}$ has written in $H E L P[j, i]$ in order to help $p_{i}$; aux $[j] . s n$ and $a u x[j] . v a l$ denote the corresponding sequence number and the associated value, respectively. Similarly, reg is a local variable used by a reader $p_{i}$ to contain the last (sequence number, value) pair that $p_{i}$ has read from $R E G[i]$ (reg.sn and reg.val denote the corresponding fields).

Register HELP $[i, i]$ is used only by $p_{i}$, which can consequently keep its value in a local variable. This means that the 1W1R atomic register $H E L P[i, i]$ can be used to contain the 1W1R atomic register $R E G[i]$. It follows that the protocol requires exactly $n^{2}$ base $1 \mathrm{~W} 1 \mathrm{R}$ atomic registers.

```
operation R.write (v):
    $s n \leftarrow s n+1 ;$
    for_all $j$ in $\{1, \ldots, n\}$ do $R E G[i] \leftarrow[s n, v]$;
    return ()
operation $R$.read () issued by $p_{i}$ :
    reg $\leftarrow R E G[i]$
    for_all $j$ in $\{1, \ldots, n\}$ do aux $[j] \leftarrow H E L P[j, i]$;
    let $s n \_m a x$ be $\max (r e g . s n, a u x[1] . s n, \ldots$, aux $[n] . s n)$;
    let $v a l$ be reg.val or aux $[k] . v a l$ such that the associated seq number is sn_max;
    for_all $j$ in $\{1, \ldots, n\}$ do $H E L P[i, j] \leftarrow\left[s n \_m a x, v a l\right]$;
    return (val)
```

Figure 5.2.: Atomic register: from one reader to multiple readers (unbounded construction)

Theorem 12 Given $n^{2}$ unbounded 1W1R atomic registers, the algorithm described in Figure 5.2 implements a 1WMR atomic register, where $n$ is the number of readers.

Proof As for Theorem 5, the proof consists in showing that the sequence numbers determine a linearization of any history $H$.

Considering an history $H$ of the constructed register $R$, we first build an equivalent sequential history $S$ by ordering all the write operations according to their sequence numbers, and then inserting the read
operations as in the proof of Theorem 5. This history is trivially legal as each read operation is ordered just after the write operation that wrote the value that is read. A reasoning similar to the one used in Theorem 5, but based on the sequence numbers provided by the arrays $R E G[1: n]$ and $H E L P[1: n, 1$ : $n]$, shows that $S$ respects $\rightarrow_{H}$.

### 5.3. Atomic registers: from unbounded 1WMR to MWMR

In this section, we show how to use sequence numbers to build a MWMR atomic register from $n$ 1WMR atomic registers (where $n$ is the number of writers). The algorithm is simpler than the previous one. An array $\operatorname{REG}[1: n]$ of $n 1$ WMR atomic registers is used in such a way that $p_{i}$ is the only process that can write in $R E G[i]$, while any process can read it. Each register $R E G[i]$ stores a (sequence number, value) pair. Variables $X . s n$ and $X . v a l$ are again used to denote the sequence number field and the value field of the register $X$, respectively. Each $R E G[i]$ is initialized to the same pair, namely, $\left[0, v_{0}\right]$ where $v_{0}$ is the initial value of $R$.

The problem we solve here consists in allowing the writers to totally order their write operations. To that end, a write operation first computes the highest sequence number that has been used, and defines the next value as the sequence number of its write. Unfortunately, this does not prevent two distinct concurrent write operations from associating the same sequence number with their respective values. A simple way to cope with this problem consists in associating a timestamp with each value, where a timestamp is a pair of a sequence number and the identity of the process that issues the corresponding write operation.

The timestamping mechanism can be used to define a total order on all the timestamps as follows. Let $t s 1=[s n 1, i]$ and $t s 2=[s n 2, j]$ be any two timestamps. We have:

$$
t s 1<t s 2 \stackrel{\text { def }}{=}((s n 1<s n 2) \vee(s n 1=s n 2 \wedge i<j))
$$

The corresponding construction is described in Figure 5.3. The meaning of the additional local variables that are used is, we believe, clear from the context.

```
operation R.write $(v)$ issued by $p_{i}$ :
    for_all $j$ in $\{1, \ldots, n\}$ do $\operatorname{reg}[j] \leftarrow R E G[j]$
    let $s n \_m a x$ be $\max (\operatorname{reg}[1] . s n, \ldots, \operatorname{reg}[n] . s n)+1$
    $R E G[i] \leftarrow\left[s n \_m a x, v\right]$
    return ()
operation $R \cdot \operatorname{read}()$ issued by $p_{i}$ :
    for_all $j$ in $\{1, \ldots, n\}$ do $\operatorname{reg}[j] \leftarrow R E G[j]$;
    let $k$ be the process identity such that $[s n, k]$ is the greatest timestamp
        among the $n$ timestamps $[\operatorname{reg}[1] . s n, 1], \ldots$ and $[\operatorname{reg}[n] . s n, n]$;
    return $(r e g[k] . v a l)$
```

Figure 5.3.: Atomic register: from one writer to multiple writers (unbounded construction)

Theorem 13 Given n unbounded 1WMR atomic registers, the algorithm described in Figure 5.3 implements a MWMR atomic register.

Proof Again, we show that the timestamps define a linearization of any history $H$.

Considering an history $H$ of the constructed register $R$, we first build an equivalent sequential history $S$ by ordering all the write operations according to their timestamps, then inserting the read operations

