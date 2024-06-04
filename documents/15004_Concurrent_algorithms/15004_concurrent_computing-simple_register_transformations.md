# 4. Simple register transformations 

The simplest objects that are usually considered in concurrent computing are registers, namely shared storage objects that provide their users with two basic operations: read and write. For presentation simplicity, and without loss of generality, we focus only consider registers that contain integers.

In the following, we shall describe how to wait-free implement registers ensuring some semantics using registers ensuring weaker semantics. The picture to have in mind here is that where the weak registers are provided in hardware and the stronger ones, implemented on top of the weaker ones, are emulated in software.

### 4.1. Definitions

Different kinds of registers are usually considered, depending on:

(a) Their value range: the range of values the register can store. We typically consider, on the one hand, registers that can contain binary values, i.e., only holding 0 or 1 , also called binary registers, or shared bits, and, on the other hand, registers that contain any value from an an infinite set, also called multi-valued registers. A multi-valued register can be bounded or unbounded. A bounded register is one whose value range contains exactly $b$ distinct values, e.g., the values from 0 until $b-1$ where $b$ is typically a constant integer by the processes. Otherwise the register is said to be unbounded. A register that can contains $b$ distinct values is said to be $b$-valued.

(b) Their access pattern, i.e., the number of processes that can read (resp., write in) the register, which can vary from 1-writer 1-reader to multi-writer multi-reader. It is important to notice here that we do not consider access patterns that change over time. A register is called single-writer, denoted $1 \mathrm{~W}$, (resp., single-reader, denoted 1R) if only one specific process, known in advance, and called the writer (resp., the reader) can invoke a write (resp., read) operation on the register. A register that can be written (resp., read) by multiple processes is called a multi-writer (resp., multi-reader) register. Such a register is denoted MW (resp., MR). For instance, a binary 1WMR register is a register that (a) can contain only 0 or 1 , (b) can be read by all the processes but (c) written by a single process.

(c) Their concurrency behavior, i.e., the correctness guarantees ensured when the register is accessed concurrently. Registers that ensure linearizability are sometimes called atomic or linearizable registers. But as we will discuss below, there are interesting forms of registers that provide weaker correctness guarantees. We will consider two such forms, called safe and regular registers.

The concurrent behavior of a register. When accessed sequentially, the behavior of a register is simple to define: a read invocation returns the last value written. When accessed concurrently, three main variants have been considered. We overview them below.

Safety A read that is not concurrent with a write returns the last written value. This is the only property ensured by a safe register. Such a register supports only a single writer. If this writer is concurrent with a read, this read can return any value in the range domain of the register, including a value
that has never been written. A binary safe register can thus be seen as a bit flickering under concurrency.

Regularity A read that is concurrent with a write returns the value written by that write or the value written by the last preceding write. A regular register ensures this property, in addition to the safety property above. A regular register also only supports a single writer.

It is important to notice that such a register can, if two consecutive (non-overlapping) reads are concurrent with a write, returns the value being written (the new value) and then returns later the previous value written (the old value). This situation is called the new/old inversion. It could occur even if the two reads are issued by the same process, as depicted on Figure 4.1. A read that overlaps several write operations can return the value written by any of these writes as well as the value of the register before these writes.

Atomicity An atomic ( linearizable) register is one that ensures linearizability. Such a register ensures the safety and regularity properties above, but in addition, prevents the situation of read-write inversion. The second read must succeed the first one in any linearization, and thus must return the same or a "newer" value. Basically, considering Figure 4.1, if the first read of $p_{1}$ returns 1, then the second read of $p_{1}$ has to return 1 .

The weakest kind of shared register is one that can only store one bit of information, can be read by a single process $p$ and written by a single process $q$, while not ensuring any guarantee on the value read by $p$ when $p$ and $q$ access the register concurrently. On the other hand, the strongest kind of register is the MWMW multi-valued atomic register.

An algorithm that implements a register of a given kind from a register of a weaker kind is sometimes called register transformation or reduction, the former (high-level) register being "reduced" to the latter one, used as a base object in the implementation. We also say that the high-level register is emulated by, or constructed from, the lower-level one.

Before presenting register transformations, we will highlight first some fundamental techniques that enable to argue about the correctness of a given transformation.

### 4.2. Proving register properties

To prove that a register is safe, it is enough to consider the sequential case and ensure that a read returns the last value written. Proving that a register is regular or atomic is more challenging. The very notion of a reading function is in this context convenient.

Basically, a reading function is associated with a given history and maps every returned read operation $r(x)$ to some $w(x)$ in that history. Without loss of generality, we assume that every history starts with a sequential operation $w\left(x_{0}\right)$ that writes the initial value $x_{0}$.

We say that a reading function $\pi$ associated with a history $H$ is regular if (here $r$ and $w$ with indices denote read and write operations in $H)$ :

$$
A 0: \forall r: \neg\left(r \rightarrow_{H} \pi(r)\right) . \text { (No read returns a value not yet written.) }
$$

$$
\text { A1 }: \forall r, w \text { in } H:\left(w \rightarrow_{H} r\right) \Rightarrow\left(\pi(r)=w \vee w \rightarrow_{H} \pi(r)\right) .(\text { No read returns an overwritten value.) }
$$

We say that a reading function is atomic if it is regular and satisfies the following additional property:

$$
\text { A2 }: \forall r 1, r 2:\left(r 1 \rightarrow_{H} r 2\right) \Rightarrow\left(\pi(r 1)=\pi(r 2) \vee \pi(r 1) \rightarrow_{H} \pi(r 2)\right) . \text { (No new/old inversion.) }
$$

It turns out that determining a regular reading function is exactly what we need to show that a history can be produced by a regular register.

Theorem $4 H$ is a history of a 1WMR regular register if and only if it has a regular reading function $\pi$.

Proof Suppose that $H$ is a history of a regular register. We define $\pi$ as follows. For any $r$, a read operation in $H$ that returns $x$, we define $\pi(r)$ as the last write operation $w(x)$ in $H$ such that $\neg\left(r \rightarrow_{H}\right.$ $w(x)$. Since by the definition of a regular register, $x$ is the argument of the latest preceding write or a concurrent write, it is easy to see that $\pi$ satisfies properties $A 0$ and $A 1$ above.

Now suppose that $H$ allows for a regular reading function. Let $r$ be a complete read operation in $H$ that returns $x$. Then there exists a write $w(x)$ in $H$ that either precedes or is concurrent with $r$ in $H(A 0)$ and is not succeeded by a write that precedes $r$ in $H(A 1)$. Thus, $r$ returns either the last written or a concurrently written value.

Now we show that a history can be produced by an atomic register if and only it can be associated with an atomic reading function.

Theorem $5 H$ is a history of an atomic 1WMR register if and only if it allows for an atomic reading function $\pi$.

Proof Given a linearizable history $H$, we construct an atomic reading function as follows. Take any $S$, a linearization of $H$ and define $\pi(r)$ as the last write that precedes $r$ in $S$. By construction, $\pi(r)$ satisfies properties $A 0, A 1$ and $A 2$.

Now suppose that $H$ allows for an atomic reading function $\pi$. We use $\pi$ to construct $S$, a linearization of $H$, as follows.

We first construct $S$ as the sequence of all writes that took place in $H$ in the order of appearance. Since we have only one writer, the writes are totally ordered. (In case the last write is incomplete, we add to $S$ its complete version.) Then we put every complete operation $r$ immediately after $\pi(r)$, making sure that:

$$
\text { if } \pi(r 1)=\pi(r 2) \text { and } r 1 \rightarrow_{H} r 2, \text { then } r 1 \rightarrow_{S} r 2
$$

Clearly, $S$ is legal: the reading function guarantees that $\pi(r)$ writes the value read by $r$, and thus every read in $S$ returns the last written value.

To show that $\rightarrow_{H} \subseteq \rightarrow_{S}$, we consider the following four possible cases. Here $w 1$ and $w 2$ denote write operations, while $r 1$ and $r 2$ denote read operations.

- $w 1 \rightarrow_{H} w 2$. Since $S$ preserves the real-time occurrence order of writes in $H$, we have $w 1 \rightarrow_{S}$ $w 2$.
- $r 1 \rightarrow_{H} r 2$. By $A 2$, we have $\pi(r 1)=\pi(r 2)$ or $\pi(r 1) \rightarrow_{H} \pi(r 2)$.

If $\pi(r 1)=\pi(r 2)$, as $r 1$ precedes $r 2$ in $H$, the way $S$ is constructed implies that $r 1$ is ordered before $r 2$ in $S$ and, thus, $r 1 \rightarrow_{S} r 2$.

If $\pi(r 1) \rightarrow_{H} \pi(r 2)$, then, since $S$ preserves the real-time occurrence order of writes in $H$ and $r 1$ and $r 2$ are placed just after $\pi(r 1)$ and $\pi(r 2)$, respectively, in $S$, we have $r 1 \rightarrow_{S} r 2$.

- $r 1 \rightarrow_{H} w 2$. By $A 0$, either $\pi(r 1)$ is concurrent with $r 1$ or $\pi(r 1) \rightarrow_{H} r 1$. Since $r 1 \rightarrow_{H} w 2$ and all writes are totally ordered, we have $\pi(r 1) \rightarrow_{H} w 2$. By construction of $S$, since $\pi(r 1)$ is the last write preceding $r 1$ in $S, r 1 \rightarrow_{S} w 2$.
- $w 1 \rightarrow_{H} r 2$. By $A 1$ we have $\pi(r 2)=w 1$ or $w 1 \rightarrow_{H} \pi(r 2)$.

Suppose that $\pi(r 2)=w 1$. As $r 2$ is placed just after $\pi(r 2)$ in $S$, we have $\pi(r 2)=w 1 \rightarrow_{S} r 2$.

Suppose that $w 1 \rightarrow_{H} \pi(r 2)$. Again, by the way $S$ is constructed, we have $w 1 \rightarrow_{H} \pi(r 2) \Rightarrow$ $w 1 \rightarrow_{S} \pi(r 2)$. Further, $\pi(r 2) \rightarrow_{S} r 2(r 2$ is ordered just after $\pi(r 2)$ in $S$ ), we obtain (by transitivity of $\left.\rightarrow_{S}\right) w 1 \rightarrow_{S} r 2$.

Finally, since $S$ contains all complete operations of $H$ and preserves $\rightarrow_{H}, H$ is indistinguishable from $S$ for every process, modulo the last incomplete read operation (if any).

Thus, $S$ is a legal sequential history that is equivalent to a completion of $H$ and preserves $\rightarrow_{H}$.

We say that a history of a regular register commits a new/old inversion if it allows for a non atomic reading function. Notice that a history may allow for multiple reading functions, some of them atomic and some of them only regular. Theorems 4 and 5 imply that an atomic register can be seen as a regular register that never suffers from new/old inversion.

Since linearizability is a local property, a set of 1WMR regular registers behave atomically if each of them independently from the others is written by a single process and never exhibits no new/old inversion.

### 4.3. Register transformations

In the following, we will present several register transformations, namely algorithms that, each, builds a register $R$ with certain properties, called a high-level register, from other registers, called low-level or base registers, providing weaker properties. For example, we will show how to obtain a regular register from safe base registers, 1WMR register from 1W1R registers, or multi-valued register from binary registers.

The transformations we will present vary in their complexity, i.e., the number and size of the underlying base registers. For example, the number of base registers used by a transformation may be proportional to the number of readers and writers. Also, a transformation may assume base registers of bounded capacity or unbounded base registers. Naturally, assuming only bounded registers is more realistic.

In this and the subsequent chapters, we proceed as follows.

1. We first present two simple (bounded) algorithms. The first builds a 1WMR safe register out of a number of 1W1R safe registers. The second builds a binary 1WMR regular register out of a binary 1WMR safe register. Combining the two, we can implement a binary 1WMR regular register using a number of binary 1W1R safe registers.
2. We then show how to transform a binary 1WMR register that provides certain semantics (safe, regular or atomic) into a multi-valued 1WMR register that preserves the same semantics. The three transformations we present here are all bounded. By combining the algorithms obtained so far, we can implement a multi-valued 1WMR regular register using a number of binary 1W1R safe registers.
3. Finally, in Chapter 5, we show how to transform a 1W1R regular register into a MWMR atomic register. We go through three intermediate (unbounded) transformations here: from a 1W1R regular register into a 1W1R atomic register, then to a 1WMR atomic register, and finally to a MWMR register.

### 4.4. Two simple bounded transformations

We first focus on safe and regular registers. Recall that these kinds of registers assume a single writer for each register. First we present an algorithm that uses single-reader registers, being safe or regular, to emulate a multi-reader register. Second we show how a safe multiple-reader bit can be turned into a regular one.

### 4.4.1. Safe/regular registers: from single reader to multiple readers

The idea here is to emulate the multi-reader register using several single-reader registers. We consider a system of $n$ processes and all are potential readers. In the transformation, described in Figure 4.2, the constructed register $R$ is built from $n 1 \mathrm{~W} 1 \mathrm{R}$ base registers, denoted $R E G[1: n]$, one per reader process. A reader $p_{i}$ reads the base register $R E G[i]$ it is associated with, while the single writer writes to every base register, one by one (in any order).

It is important to see that this transformation is bounded: it uses no additional control information beyond the actual value stored, and each base register can be of the same capacity as the multiple-reader register we want to build.

An interesting feature of this algorithm is that replacing the base safe 1W1R registers with regular ones, we obtain an emulation of a regular 1WMR register.

```
operation R.write $(v)$ :
    for_all $j$ in $\{1, \ldots, n\}$ do $R E G[j] \leftarrow v$;
    return ()
operation $R . \operatorname{read}()$ issued by $p_{i}$ :
    return $(R E G[i])$
```

Figure 4.2.: From 1W1R safe/regular to 1WMR safe/regular (bounded transformation)

We show now that the algorithm is correct:

Theorem 6 Given one safe (resp., regular) IWIR base register per reader, the algorithm described in Figure 4.2 implements a 1WMR safe (resp., regular) register.

Proof Assume first that base 1W1R registers are safe. It follows directly from the algorithm that a read of $R$ (i.e., $R$.read ()$)$ that is not concurrent with a $R$.write() operation returns the last value deposited in the register $R$. The obtained register $R$ is consequently safe while being 1WMR.

Let us now suppose that the base registers are regular. We will argue that the high-level register $R$ constructed by the algorithm is a 1WMR regular one. Since a regular register is safe, the argument above implies that $R$ is safe. Hence, we only need to show that a read operation $R . \operatorname{read}()$ that is concurrent with one or more write operations returns a concurrently written value or the last written value.

Let $p_{i}$ be any process that reads some value from $R$. When $p_{i}$ reads the base regular register $R E G[i]$ $p_{i}$ returns (a) the value of a concurrent write on $R E G[i]$ (if any) or (b) the last value written to $R E G[i]$ before such concurrent write operations. In case (a), the value $v$ obtained is from a $R$.write $(v)$ that is
concurrent with the $R . \operatorname{read}()$ of $p_{i}$. In case (b), the value $v$ obtained can either be (b.1) from a $R$.write $(v)$ that is concurrent with the R.read () of $p_{i}$, or (b.2) from the last value written by a R.write() before the R.read () of $p_{i}$. Thus, the constructed register $R$ is regular.

It is important to see that the algorithm of Figure 4.2 does not implement a 1WMR atomic register even when every base register $R E G[i]$ is a $1 \mathrm{~W} 1 \mathrm{R}$ atomic register. This is because the transformation may exhibit new/old inversion, even if the base registers preclude it. To show this, let us consider the history described in Figure 4.3. The example involves one writer $p_{w}$ and two readers $p_{1}$ and $p_{2}$. Assume the register $R$ implemented by the algorithm contains initially value 1 (which means that we initially have $R E G[1]=R E G[2]=1$ ). To write value 2 in $R$, the writer first executes $R E G[1] \leftarrow 2$ and then $R E G[2] \leftarrow 2$. Concurrently, $p_{1}$ reads $R E G[1]$ and returns 2 , and then $p_{2}$ reads $R E G[2]$ and returns 1 . Clearly, there is new/old inversion here: the read by $p_{1}$ returns the new value, and the subsequent read by $p_{2}$ returns the old value.

### 4.4.2. Binary multi-reader registers: from safe to regular

Now we emulate a regular binary register using a single safe binary register, i.e., construct a regular bit out of a safe one. The algorithm is very simple, precisely because we want to implement a register storing only one out of two values (0 or 1 ).

The difference between a safe and a regular register is only visible in the face of concurrency. That is, the value to be returned in the regular case has to be a value concurrently written or the last value written, while a safe register is allowed to return any value in the range ( 0 or 1 in our case). To illustrate the issue, assume that the regular register is directly implemented using a safe base register: every read (resp. write) on the high-level register is directly translated into a read (resp. write) on the base (safe) register. Assume this register has value 0 and there is a write operation that writes the very same value 0 . As the base register is only safe, it is possible that a concurrent read operation returns value 1 , which might have never been written.

The way to fix this problem is to allow the writer to actually write to the base register only if the writer intends to change the value of the high-level register. This way a concurrent read can obtain any value in $\{0,1\}$ (remember that only two values are possible), i.e., either the previously written or a concurrently written value, which complies with the regularity semantics.

The transformation algorithm is presented in Figure 4.4. Besides a safe register $R E G$ shared between the reader and the writer, the algorithm requires that the writer maintains a local variable prev_val that
contains the most recent value that has been written in the base safe register $R E G$. Before writing a value $v$ in the high-level regular register, the writer checks if this value $v$ is different from the value in prev_val and, only in that case, $v$ is written in $R E G$.

```
operation R.write $(v)$ :
    if $\left(p r e v \_v a l \neq v\right)$ then $R E G \leftarrow v$;
    prev_val $\leftarrow v$
    return ()
operation $R \cdot \operatorname{read}()$ issued by $p_{i}:$
    return $(R E G)$
```

Figure 4.4.: From a binary safe to a binary regular register (bounded transformation)

Theorem 7 Given a 1WMR binary safe register, the algorithm described in Figure 4.4 implements a 1WMR binary regular register.

Proof As the underlying base register is safe, a read that is not concurrent with a write returns the last written value. As the underlying base register $R E G$ always alternates between 0 and 1 , a read concurrent with one or more write operations returns the value of the base register before these write operations or one of the values written by such a write operation. Thus, the implemented register is regular.

Notice that the transformation does not work for registers that store 3 or more values. The transformation does not implement an atomic register either as it does not prevent a new/old inversion. Notice also that If the safe base binary register is 1W1R, then the algorithm implements a 1W1R regular binary register.

### 4.5. From binary to $b$-valued registers

This section presents three transformations from binary registers to multi-valued registers. A register is $b$-valued if in the range of values it can store has cardinality $b$; we assume here that $b>2$.

Our transformations preserve the semantics of the base registers in the following sense: if the base bits have semantics $X$ (safe, regular or atomic), then the resulting high-level ( $b$-valued) registers also have semantics $X$. Also, the transformations are bounded. There is a bound on the number of base registers used, as well as on the amount of memory needed within each register.

### 4.5.1. From safe bits to safe $b$-valued registers

Overview. The first algorithm we present here uses a number of safe bits in order to implement a multi-valued register $R$. We assume that the capacity of $R$ is an integer power of 2 , i.e., $2^{B}$ for some integer $B$. It follows that (with a possible pre-encoding if the $b=2^{B}$ distinct values are not the consecutive values from 0 until $b-1$ ) the binary representation of a value stored in $R$ requires exactly $B$ bits. Any combination of $B$ bits thus identifies a value in the range of $R$ (notice that this would not be true if $b$ was not an integer power of 2 ).

The algorithm uses an array $R E G[1: B]$ of 1WMR safe bit registers to store the current value of $R$. Given $\mu_{i}=R E G[i]$, the binary representation of the current value of $R$ is $\mu_{1} \ldots \mu_{B}$. The corresponding transformation algorithm is given in Figure 4.5.

```
operation R.write $(v)$ :
    let $\mu_{1} \ldots \mu_{B}$ be the binary representation of $v$;
    for_all $j$ in $\{1, \ldots, B\}$ do $R E G[j] \leftarrow \mu_{j}$
    return ()
operation $R . \operatorname{read}()$ issued by $p_{i}$ :
    for_all $j$ in $\{1, \ldots, B\}$ do $\mu_{j} \leftarrow R E G[j]$;
    let $v$ be the value whose binary representation is $\mu_{1} \ldots \mu_{B}$;
    return $(v)$
```

Figure 4.5.: Safe register: from bits to $b$-valued register

Space complexity. As $B=\log _{2}(b)$, the memory cost of the algorithm is logarithmic with respect to the size of the value range of the constructed register $R$. This follows from the binary encoding of the values of the high level register $R$.

Theorem 8 Given B 1WMR safe bits, the algorithm described in Figure 4.5 implements a 1WMR $2^{B}$ valued safe register.

Proof A read of $R$ that does not overlap a write of $R$ returns the binary representation of the last value that has been written into $R$ and is consequently safe to return. A read of $R$ that overlaps a write of $R$ can obtain any of $b$ possible values whose binary encoding uses $B$ bits. As every possible combination of the $B$ base bit registers represents one of the the $b$ values that $R$ can potentially contain (this is because $b=2^{B}$ ), it follows that a read concurrent with a write operation returns a value that belongs to the range of $R$. Consequently, $R$ is a $b$-valued safe register, for $b=2^{B}$.

It is interesting to notice that this algorithm does not implement a regular register $R$ even when the base bits are regular. For instance, a read changing the value of $R$ from $0 \ldots 0$ to $1 \ldots 1$ (in binary representation) can return any value, i.e., even one that was never written, if it overlaps a write operation. The reader (the human, not the process) can check that imposing a specific order according to which the array $\operatorname{REG}[1: B]$ is accessed does not overcome this issue.

### 4.5.2. From regular bits to regular $b$-valued registers

Overview. We build a 1WMR regular $b$-valued register $R$ (storing values $1, \ldots, b$ ) from regular bits using "unary encoding". Considering an array $R E G[1: b]$ of 1 WMR regular bits, the value $v \in[1 . . b]$ is represented by 0 s in bits 1 to $v-1$ and 1 in bit $v$.

The algorithm is described in Figure 4.6. The key idea is to write into the array $R E G[1: b]$ in one direction, and to read it in the opposite direction. To write $v$, the writer first sets $R E G[v]$ to 1 , and then "cleans" the array $R E G$, which consists in setting the bits $R E G[v-1]$ to $R E G[1]$ to 0 . To read, a reader traverses the array $R E G[1: b]$ starting from its first entry $(R E G[1])$ and stops as soon as it discovers an index $j$ such that $R E G[j]=1$. The reader then returns $j$ as the result of the read operation. Notice that a read proceeds through the "cleaned" part of the array in the ascending order, while a write updates the array in the opposite direction, from $v-1$ until 1.

It is also important to notice that, even when no write operation is in progress, it may happen that several entries of the array are set to 1 . Intuitively, only the smallest entry of $R E G$ set to 1 encodes the most recently written value. The other entries can be seen as a partial evidence on past values.

The algorithm assumes that the register $R$ has an initial value $v_{0}$ : initially, $R E G[j]=0$ for $1 \leq j<v_{0}$, $R E G\left[v_{0}\right]=1$, and $R E G[j]=0$ or 1 for $v_{0}<j \leq b$.

Two observations are in order:

```
operation R.write $(v)$ :
    $R E G[v] \leftarrow 1$;
    for $j=v-1$ down to 1 do $R E G[j] \leftarrow 0$;
    return ()
operation R.read () issued by $p_{i}$ :
    $j \leftarrow 1$
    while $(R E G[j]=0)$ do $j \leftarrow j+1$
    return $(j)$
```

Figure 4.6.: Regular register: from bits to $b$-valued register

1. The "last" base register $R E G[b]$, once set to 1 will never change. Therefore, a reader once it witnessed 0 in all entries of $R E G$ up to $b-1$, might by default consider $R E G[b]$ to be 1 .
2. The reader's algorithm does not write to base registers. As a result, the algorithm may handle an arbitrary number of readers, assuming that the base registers can maintain sufficiently many readers.

Space complexity. The memory cost of the transformation algorithm is $b$ base bits, i.e., it is linear with respect to the size of the value range of the constructed register $R$. This is a consequence of the unary encoding of these values.

Lemma 2 The algorithm of Figure 4.6 is wait-free. The value $v$ returned by a read belongs to the set $\{1, \ldots, b\}$.

Proof A R.write $(v)$ operation trivially terminates in a finite number of its own steps: the for loop only goes through $v$ iteration.

To see that a R.read () operation terminates in at most $v$ iterations of the while loop, observe that whenever the writer changes sets $R E G[x]$ from 1 to 0 , it has previously set to 1 another entry $R E G[y]$ such hat $x<y \leq b$. Therefore, if a reader reads $R E G[x]$ and returns the new value 0 , then a higher entry of the array is set to 1 .

As the running index of the while loop starts at 1 and is incremented each time the loop body is executed, it follows that the loop always terminates, and the value $j$ it returns is such that $1 \leq j \leq b$.

The previous lemma relies heavily on the fact that the high-level register $R$ can contain up to $b$ distinct values. If the range of $R$ is unbounded, a $R \cdot \operatorname{read}()$ operation might never terminate if the writer continuously updates $R$ with ever-increasing values. More precisely, suppose that the range of $R$ is unbounded and consider the following scenario. Let $R$.write $(x)$ be the last write operation terminated before a $R . \operatorname{read}()$ starts. Let the read operation proceed until it is about to read $R E G[x]$ and then schedule a concurrent $R$.write $(y), y>x)$ to set $R E G[x]$ from 1 to 0 . Then we schedule the read of $R E G[x]$ by the reader. As the register is unbounded, this scenario can repeat indefinitely, forcing the reader to take infinitely many reads of $R E G$.

Theorem 9 Given b 1WMR regular bits, the algorithm described in Figure 4.6 implements a IWMR $b$-valued regular register.

Proof Consider first a read operation that is not concurrent with any write, and let $v$ be the last written value. By the write algorithm, when the corresponding R.write $(v)$ terminates, the first entry of the array that equals 1 is $R E G[v]$ (i.e., $R E G[x]=0$ for $1 \leq x \leq v-1$ ). Because a read traverses the array starting from $R E G[1]$, then $R E G[2]$, etc., it necessarily reads until $R E G[v]$ and returns the value $v$.

Let us now consider a read operation R.read () that is concurrent with one or more write operations $R$.write $\left(v_{1}\right), \ldots, R$. write ( $v_{m}$ ) (as depicted in Figure 4.7 ). Let $v_{0}$ be the value written by the last write operation that terminated before the operation R.read () starts. For simplicity we assume that each execution begins with a write operation that sets the value of $R$ to an initial value. As a read operation always terminates (Lemma 2), the number of writes concurrent with the R.read () operation is finite.

By the algorithm, the read operation finds 0 in $R E G[1]$ up to $R E G[v-1], 1$ in $R E G[v]$, and then returns $v$. We are going to show by induction that each of these base-object reads returns a value previously or concurrently written by a write operation in $R$.write $\left(v_{0}\right), R$.write $\left(v_{1}\right), \ldots, R$.write $\left(v_{m}\right)$.

Since $R$.write $\left(v_{0}\right)$ sets $R E G\left[v_{0}\right]$ to 1 and $R E G\left[v_{0}-1\right]$ down to $R E G[1]$ to 0 , the first base-object read performed by the $R$.read () operation returns the value written by $R$.write $\left(v_{0}\right)$ or a concurrent write. Now suppose that the read on $\operatorname{REG}[j]$, for some $j=1, \ldots, v-1$, returned 0 written by the latest preceding or a concurrent write operation $R . w$ write $\left(v_{k}\right)(k=1, \ldots, m)$. Notice that $v_{k}>j$ : otherwise, $R$.write $\left(v_{k}\right)$ would not touch $R E G[j]$. By the algorithm, $R$.write $\left(v_{k}\right)$ has previously set $R E G\left[v_{k}\right]$ to 1 and $R E G\left[v_{k}-1\right]$ down to $R E G[j+1]$ to 0 . Thus, since the base registers are regular, the subsequent read of $R E G[j+1]$ performed within the $R . r e a d()$ operation can only return the value written by $R$. write $\left(v_{k}\right)$ or a subsequent write operation that is concurrent with R.read () .

By induction, we derive that the read of $R E G[v]$ performed within $R . r e a d()$ returns a value written by the latest preceding or a concurrent write.

### 4.5.3. From atomic bits to atomic $b$-valued registers

In Chapter 6, we give a direct construction of an atomic bit from three regular ones. However, if we use this construction to replace regular bits with atomic ones in the algorithm in Figure 4.6 we do not get an atomic $b$-valued register. Interestingly, a relatively simple modification of its read algorithm makes that possible by preventing the new/old inversion phenomenon.

The idea is to equip the R.read () algorithm in Figure 4.6 with a "counter-inversion" mechanism. Instead of returning position $j$ where the first 1 was located in $R E G$, the read operation traverses the array again in the opposite direction (from $j$ to 1 ) and returns the smallest entry containing value 1 . The resulting algorithm is presented in Figure 4.8.

Theorem 10 The algorithm in Figure 4.8 implements a IWMR atomic b-valued register using bIWMR atomic bits.

Proof For every history of the algorithm, we define the reading function $\pi$ as follows. Let $r$ be a read operation that returned $v$. Then $\pi(r)$ is the latest write operation that updated $R E G[v]$ before the last read of $R E G[v]$ performed by $r$, or the initializing write operation $w_{0}$ if no such operation exists. Since $r$ returns the index of $R E G$ containing $1, \pi(r)$ writes 1 to $R E G[v]$. Note that $\pi$ is well-defined, as it can be derived from the atomic reading function of the elements of $R E G$.

```
operation R.write $(v)$ :
    $R E G[v] \leftarrow 1$;
    for $j$ from $v-1$ step -1 until 1 do $R E G[j] \leftarrow 0$;
    return ()
operation R.read () issued by $p_{i}$ :
    j_ир $\leftarrow 1$
(1) while $\left(R E G\left[j \_u p\right]=0\right)$ do $j \_u p \leftarrow j \_u p+1$;
(2) $j \leftarrow j \_u p$
(3) for $j \_d o w n$ from $j \_u p-1$ step -1 until 1 do
if $\left(R E G\left[j \_d o w n\right]=1\right)$ then $j \leftarrow j \_$down
    return $(j)$
```

Figure 4.8.: Atomic register: from bits to $b$-valued register

We now show that $\pi$ is indeed an atomic reading function, i.e., it satisfies properties $A 0, A 1$ and $A 2$ in Section 4.2. By the definition, $\pi(r)$ is a preceding or concurrent write operation, therefore $A 0$ is satisfied.

To see that $A 1$ is also satisfied, suppose, by contradiction, that $\pi(r) \rightarrow w\left(v^{\prime}\right) \rightarrow r(v)$ for some write $w\left(v^{\prime}\right)$. By the algorithm, $w\left(v^{\prime}\right)$ sets $R E G[v]$ to 1 and then writes 0 to all $R E G[v-1]$ down to $R E G[1]$. Thus, $v^{\prime}<v$, otherwise $w\left(v^{\prime}\right)$ would also write to $R E G[v]$ and $\pi(r)$ would not be the latest write updating $R E G[v]$ before $r$ reads $R E G[v]$. Since $r$ reached $R E G[v]$, there exists a write $w\left(v^{\prime \prime}\right)$ that set $R E G\left[v^{\prime}\right]$ to 0 after $w\left(v^{\prime}\right)$ set it to 1 but before $r$ read it. By the algorithm, before setting $R E G\left[v^{\prime}\right]$ to 0 this write has set a $R E G\left[v^{\prime \prime}\right]$ to 1 and, by the assumption, $v^{\prime \prime}<v$. Assuming that $w\left(v^{\prime \prime}\right)$ is the latest such write, before reacing $R E G[v], r$ must have found $R E G\left[v^{\prime \prime}\right]=1$ - a contradiction.

To show that $\pi$ satisfies $A 2$, let us consider two read operations $r 1$ and $r 2, r 1 \rightarrow r 2$, and suppose, by contradiction, that $\pi(r 2) \rightarrow \pi(r 1)$.

Let $r 1$ return $v$ and $r 2$ return $v^{\prime}$. Since $\pi(r 1) \neq \pi(r 1)$, the definition of $\pi$ implies that $v \neq v^{\prime}$. Thus, we should only consider the following cases:

(1) $v^{\prime}>v$.

In this case, $r 2$ must have found 0 in $R E G[v]$ before finding 1 in $R E G\left[v^{\prime}\right]$ and returning $v^{\prime}>v$. Thus, a write $w\left(v^{\prime \prime}\right)$ such that $v<v^{\prime \prime}<v^{\prime}$ and $\pi(r 2) \rightarrow w\left(v^{\prime \prime}\right) \rightarrow(r 1)$, has set $R E G[v]$ to 0 after $\pi(v)$ set $R E G[v]$ to 1 but before $r 2$ read it. Assume, without loss of generality, that $v^{\prime \prime}$ is the smallest such value. Since $w\left(v^{\prime \prime}\right)$ has set $R E G\left[v^{\prime \prime}\right]$ to 1 before writing 0 to $R E G[v], r 2$ must have returned $v^{\prime \prime}<v^{\prime}-$ a contradiction.

(2) $v^{\prime}<v$.

In this case, $r 1$ reads 1 in $R E G[v], v>v^{\prime}$, and then reads 0 in all $R E G[v-1]$ down to $R E G[1]$, including $R E G\left[v^{\prime}\right]$. Since $\pi(r 2)$ has previously set $R E G\left[v^{\prime}\right]$ to 1 , another write operation must have set $R E G\left[v^{\prime}\right]$ to 0 after $\pi(r 2)$ set it to 1 but before $r 1$ read it. Thus, when $r 2$ subsequently reads 1 in $R E G\left[v^{\prime}\right], \pi(r 2)$ is not the last preceding write operation to write to $R E G\left[v^{\prime}\right]$-a contradiction with the definition of $\pi$.

Hence, $\pi$ is an atomic reading function and, by Theorem 5, the algorithm indeed implements a 1WMR atomic register.

