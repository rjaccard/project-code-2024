# 11. Consensus number and the consensus hierarchy 

In the previous chapter, we introduced a notion of a universal object type. Using read-write registers and objects of a universal type and, one can implement an object of any total type in the wait-free manner. As we have shown, one example of a universal type is consensus. Therefore, the power of an object type can be measured by the ability of its objects to implement consensus.

We show in this section that atomic registers cannot implement a consensus object shared by two processes, thus, the register type is not universal even in a system of two processes. If, however, in addition to registers, we may use queue objects, then we can implement 2 -processe consensus, but not 3 -process consensus.

More generally, we introduce the notion of consensus number of an object type $T$, the largest number of processes for which $T$ is universal. Consensus numbers are fundamental in capturing the relative power of object types, and we show how to evaluate the consensus power of various object types.

### 11.1. Consensus number

The consensus number of an object type $T$, denoted by cons $(T)$, is the highest number $n$ such that it is possible to wait-free implement a consensus object from atomic registers and objects of type $T$, in a system of $n$ processes. If there is no such largest $n$, i.e., consensus can be implemented in a system of arbitrary number of processes, the consensus number of $T$ is said to be infinite.

Note that if there exists a wait-free implementation of an object in a system of $n$ process implies a wait-free implementation in a system of any $n^{\prime}<n$ processes. Thus, the notion of consensus number is well-defined. By the definition, if $\operatorname{cons}(T)<\operatorname{cons}\left(T^{\prime}\right)$, then there is no wait-free implementation of an object of type $T^{\prime}$ from objects of type $T$ and registers in a system of $\operatorname{cons}(T)+1$ or more processes.

If atomic registers are strong enough to wait-free implement consensus for any number of processes, i.e., cons $($ regiter $)=\infty$, then all object types would have the same consensus number, and the very notion of consensus number would be useless. We show below that this is not the case. Moreover, we show that for each $n$, there exists object types $T$, such that $\operatorname{cons}(T)=n$, i.e., the consensus hierarchy is populated for each level $n$.

### 11.2. Preliminary definitions

In this section, we introduce some machinery that is going to be used to compute consensus numbers of object types. Let us consider an algorithm $A$ that implements a wait-free consensus object assuming that processes only propose values 0 and 1 , we call it a binary consensus object.

### 11.2.1. Schedule, configuration and valence

We consider a system in which $n$ sequential processes communicate by invoking operations on "base" atomic (linearizable) objects of types $T_{1}, \ldots, T_{x}$. As the base objects are atomic, an execution in this system can be modeled by a sequential history that (1) includes all the operations on base objects issued
by the processes (except possibly the last operation of a process if that process crashes), (2) is legal with respect to the type of each base object, and (3) respects the real time occurrence order on the operations. Recall that this sequential history is called a linearization.

Schedules and configurations A schedule is a sequence of base-object operations. In the following, we assume that the base object types are deterministic and the processes are running deterministic wait-free consensus algorithms. Thus, we can represent an operation in a schedule only by the identifier of the process that issues that operation.

A configuration $C$ is a global state of the system execution at a given point in time. It includes the state of each base object plus the local state of each process. The configuration $p(C)$ denotes the configuration obtained from $C$ by applying an operation issued by the process $p$. More generally, given a schedule $S$ and a configuration $C, S(C)$ denotes the configuration obtained by applying to $C$ the sequence of operations defining $S$.

In an input configuration of algorithm $A$, base objects and processes are in their initial states. In particular, for binary consensus, the initial state of a process can be 0 or 1 , depending on the value the process is about to propose.

Valence The notion of valence is fundamental in proving consensus impossibility results. Let $C$ be a configuration resulting after a finite execution of algorithm $A$.

We say that configuration $C$ is $v$-valent if every schedule applied to $C$ leads to $v$ as the decided value. We say that $v$ is the valence of that configuration $C$. A 0 -valent or 1 -valent configuration is said to be monovalent. A configuration that is not monovalent is said to be bivalent.

By the definition, every descendant $S(C)$ of a monovalent configuration $C$ must be monovalent. Similarly, if a configuration $C$ has a bivalent descendant $S(C)$, then $C$ is bivalent.

Lemma 19 Every configuration of a wait-free consensus implementation $A$ is monovalent or bivalent.

Proof Let $S(C)$ a configuration of $A$ reachable from an initial configuration $C$ by a finite schedule $S$. Since the algorithm is wait-free, for any sufficiently long $S^{\prime}$, some process must decide in $S^{\prime}(S(C))$. Since only 0 and 1 can be proposed and, thus, decided, the set of values that can be decided in extensions of $S(C)$ is a non-empty subset of $\{0,1\}$.

Lemma 20 A configuration in which a process decides is monovalent.

Proof By Lemma 19, if a configuration Suppose, by contradiction, that a process $p$ decides $v \in\{0,1\}$ in a bivalent configuration $S(C)$. Since $C$ is bivalent, there exists a schedule $S^{\prime}(S(C))$ in which value $1-v$ is decided, contradicting the agreement property of consensus.

The corollary of Lemmas 19 and 20 is that no process can decide in a bivalent configuration.

### 11.2.2. Bivalent initial configuration

Our next observation is that any wait-free consensus algorithm must have a bilent initial configuration $C$. In other words, for some distribution of input values, the decided value may depend on the schedule: in some $S(C), 0$ is decided and in some $S^{\prime}(C), 1$ is decided.

Lemma 21 Any wait-free consensus implementation for 2 or more processes has a bivalent initial configuration.

Proof Let $C_{0}$ be the initial configuration in which all the processes propose 0 , and $C_{i}, 1 \leq i \leq n$, the initial configuration in which the processes from $p_{1}$ to $p_{i}$ propose the value 1 , while all the other processes propose 0 . So, all the processes propose 1 in $C_{n}$. Thus, any two adjacent configurations $C_{i-1}$ and $C_{i}, 1 \leq i \leq n$, differ only in $p_{i}$ 's proposed value: $p_{i}$ proposes 0 in $C_{i-1}$ and 1 in $C_{i}$. Moreover, it follows from the validity property of consensus and Lemma 19 , that $C_{0}$ is 0 -valent and $C_{n}$ is 1-valent.

Let us assume that all configurations $C_{0}, \ldots, C_{n}$ are monovalent. As $n \geq 2$, there are two consecutive configurations $C_{i-1}$ and $C_{i}$, such that $C_{i-1}$ is 0 -valent and $C_{i}$ is 1 -valent.

Since the algorithm is wait-free, for any sufficiently long schedule $S$, some process $p_{j}$ decides in $S\left(C_{i-1}\right)$, and, since $C_{i-1}$ is 0 -valent, the decided value must be 0 . Let us suppose that $p_{i}$ takes no steps in $S$.

But as every process besides $p_{i}$ has the same inputs in $C_{i-1}$ and $C_{i}$ and the states of base objects in the two initial configurations are identical, no process besides $p_{i}$ can distinguish $S\left(C_{i-1}\right)$ and $S\left(C_{i}\right)$. Thus, $p_{j}$ must also decide 0 in $S\left(C_{i}\right)$, contradicting the assumption that $C_{i}$ is 1-valent. $\quad \square_{\text {Lemma } 21}$

Note that the proof above would work even if we assume that at most one process may initially crash. In particular, if $p_{i}$ crashes before taking any step, then no other process can distinguish an execution starting from $C_{i-1}$ from an execution starting from $C_{i}$.

### 11.2.3. Critical configurations

We now show that every wait-free consensus algorithm for two or more processes has a critical configuration $D$ with the following properties:

- $D$ is bivalent;
- for every process $p_{i}, p_{i}(D)$ is monovalent;
- there exists an object $X$, such that every process $p_{i}$ is about to access $X$ in its next step in $D$.

In other words, one step of any given process applied to a critical configuration determines the decision value.

Lemma 22 Any wait-free consensus implementation A for 2 or more processes has a critical configuration.

Proof By Lemma 21, $A$ has a bivalent initial configuration $C$. We are going to prove that $C$ has a critical descendant $S(C)$.

Suppose not, i.e., for every schedule $S$, there exists $p_{i}$ such that $p_{i}(S(C))$ is bivalent. Therefore, starting from $C$, we inductively construct an infinite schedule $\tilde{S}$ that, when applied to $C$, only goes through bivalent configurations: for every its prefix $S, S(C)$ is bivalent. Indeed, let $q_{1}$ be any process such that $q_{1}(C)$ is bivalent, $q_{2}$ be any process such that $q_{2}\left(q_{1}(C)\right)$, etc. Then, by Lemma 20, starting from $C$, the resulting infinite schedule $\tilde{S}=q_{1}, q_{2}, \ldots$ can never reach a configuration in which a process decides-a contradiction with the assumption that $A$ is a wait-free consensus algorithm.

Thus, $C$ has a bivalent descendant configuration $D$ such that for every $p_{i}, p_{i}(D)$ is monovalent.

Now suppose, by contradiction, that there exist two processes $p$ and $q$ that access different objects in their next steps enabled in $D$. We can safely assume that $p(D)$ is 0 -valent and $q(D)$ is 1 -valent. We encourage the reader to see why this is the case.

Then the steps of $p$ and $q$ applied to $D$ commute, i.e., $q(p(D))$ and $p(q(D))$ are identical: in the two configurations, base-objects states and process states are the same (Figure 11.1).

Since $p(D)$ is 0 -valent, $q(p(D))$ is 0 -valent, and since $q(D)$ is 1 -valent, $p(q(D))$ is 1 -valent-a contradiction.

Thus, $D$ is indeed a critical configuration of algorithm $A$.

Note that Lemma 22 holds for any wait-free consensus algorithm. By analyzing steps that processes can apply to a critical configuration and using the number of available processes, we can deduce the consensus number of any given object type.

### 11.3. Consensus number of atomic registers

Atomic registers are fundamental objects in concurrent shared-memory systems. In this section, we show that they are however too weak to solve wait-free consensus even for two processes. Put differently, the consensus number of object type atomic register is 1.

Theorem 27 There does not exist a wait-free consensus implementation for two processes from atomic registers.

Proof By contradiction, suppose that there exists a wait-free consensus algorithm $A$ for two processes, $p$ and $q$, using atomic registers. By Lemma 22, $A$ has a critical configuration $D$, i.e., $D$ is bivalent, $p(D)$ and $q(D)$ are monovalent, and the two processes are about to access the same register $R$ in their next steps enabled in $D$. Since $p(D)$ and $q(D)$ are the only two one-step descendants of $D$, it must hold that $p(D)$ and $q(D)$ have different valences. Without loss of generality, assume that $p(D)$ is 0 -valent and $q(D)$ is 1 -valent.

Let $\mathrm{OP}_{1}$ and $\mathrm{OP}_{2}$ be base-object operations performed by, respectively, processes $p$ and $q$ in their next steps enabled in configuration $D$.

The following cases are then possible:

- $\mathrm{OP}_{1}$ and $\mathrm{OP}_{2}$ are read operations

As a read operation on an atomic register does not modify its value, this case is the same as the previous one where $p$ and $q$ access distinct registers.

- One of the two operations $\mathrm{OP}_{1}$ and $\mathrm{OP}_{2}$ is a write. Without loss of generality, suppose that $q$ is about to write in $R$ in $D$ (Figure 11.2).

Consider configurations $q\left(p(D)\right.$ and $q(D)$. Since $p$ accessed $R$ in $\mathrm{OP}_{1}$ and $q$ writes in $R$ in $\mathrm{OP}_{2}$, the state of $D$ is the same in the two configurations. Thus, the only difference between the two is the local state of $p$ : $p$ took one more step after $D$ in $q(p(D)$, but not in $q(D)$.

Recall that $q(p(D)$ is 0 -valent and $q(D)$ is 1 -valent. Take any sufficiently long schedule $S$ only containing steps of $q$, such that some process $q$ decides in $S(q(p(D)))$. Since $q$ cannot distinguish $S(q(p(D)))$ from $S(q(D))$, it should decide the same value in $S(q(D))$.

But $q(p(D))$ is 0 -valent and $p(D)$ is 1 -valent-a contradiction.

The case when $p$ writes in its next step in $D$ is symmetric.

As solving consensus for one process is trivial, the following result is immediate from Theorem 27.

Corollary 5 cons(atomic-register) $=1$

### 11.4. Objects with consensus numbers 2

In this section, we show that the hierarchy of object types based on consensus numbers is "populated": for ever $n$, there exists an object type $T$, such that $\operatorname{cons}(T)=n$. We begin with showing that objects types test\&set and queue have consensus number 2.

### 11.4.1. Consensus from test\&set objects

A test\&set object stores a binary value, initially 0 , and exports a single (atomic) test \&set operation that writes 1 to it and returns the old value. Its sequential specification is defined as follows:

```
operation X.test\&set ( )
    $l o c:=X$
    $X:=1$;
    return (prev).
```

Thus, the first process to access a (non-initialized) test\&set object hets 0 (we call it a winner) and all subsequent processes get 1.

The consensus algorithm described in Figure 11.3 uses one test\&set object $T S$ and two 1W1R atomic registers $R E G[0]$ and $R E G[1]$.

When the process $p_{i}$ (for convenience, we assume that $i \in\{0,1\}$ ) invokes propose $(v)$ on the consensus object, it "publishers" its input value $v$ in $R E G[i]$ (line 1).

Then $p_{i}$ accesses $T S$ (line 2). If it wins, it decides its own input value (line 3). Otherwise, it decides the value proposed by the other process $p_{1-i}$ (line 4). Intuitively, as exactly one process wins $T S$, only the value proposed by the winner can be decided.

```
operation propose $(v)$ issued by $p_{i}$ :
(1) $R E G[i]:=v$;
(2) $\quad$ aux $:=$ TS.test\&set ()
(3) if $(a u x=0)$ then return $(v)$
(4) $\quad(a u x=1)$ else return $(R E G[1-i])$
```

Figure 11.3.: From test\&set to consensus

Theorem 28 The algorithm in Figure 11.3 is a wait-free consensus implementation for two processes using test\&set objects and atomic registers.

Proof As every process performs at most three shared-memory steps before deciding, the algorithm is clearly wait-free.

Let $p_{i}$ be the process that, in a given execution of the algorithm, accesses $T S$ first and decides its own input value $v$. By the algorithm, $p_{i}$ previously wrote $v$ in atomic register $R E G[i]$. Thus, $p_{1-i}$ that accesses $T S$ after $p_{i}$, will after that find $v$ in $R E G[i]$ and return it.

Thus, the two processes can only return that inout value of the winner, and the agreement and validity properties of consensus are satisfied..

### 11.4.2. Consensus from queue objects

Recall that a queue object exports two operations enqueue and dequeue, where enqueue(v) adds element $v$ to the end of the queue and dequeue() removes the element at the head of the queue and returns it; if the queue is empty, the default value $\perp$ is returned.

A wait-free consensus algorithm for two processes that uses two registers and a queue is presented in Figure 11.4. The algorithm assume that the queue is initialized with the sequence of items $<w, \ell>$. The first process first to perform a dequeue operation on this queue gets $w$ and considers itself a winner. As in the previous algorithm, the value proposed by the winner will be decided.

```
operation propose $(v)$ issued by $p_{i}$ :

(1) $R E G[i]:=v$

(2) $\quad$ aux $:=Q$.dequeue ();

(3) if $(a u x=w)$ then return $(R E G[i])$

(4) $\quad(a u x=\ell)$ else return $(R E G[1-i])$
```

Figure 11.4.: From queue to consensus

Using the arguments of the proof of Theorem 28, we obtain:

Theorem 29 The algorithm in Figure 11.4 is a wait-free consensus implementation for two processes using queue objects and atomic registers.

### 11.4.3. Consensus numbers of test\&set and queue

As we have shown, test\&set and queue objects, combined with atomic registers, can be used to waitfree implement consensus in a system of two processes. We show below that the objects have consensus number 2 , i.e., they cannot be used to solve consensus for three or more processes.

Theorem 30 There does not exist a wait-free consensus implementation for three processes from objects of types in $\{$ test\&set, queue, atomic-registers $\}$.

Proof By contradiction, suppose that there exists a wait-free consensus algorithm $A$ for two processes, $p, q$, and $r$ using atomic registers, test\&set objects and queues.

By Lemma 22, $A$ has a critical configuration $D$, i.e., $D$ is bivalent, $p(D), q(D)$, and $r(D)$ are monovalent, and all the three processes are about to access the same object $X$. Without loss of generality, assume that $p(D)$ is 0 -valent, while $q(D)$ and $r(D)$ are 1 -valent.

It is immediate from the proof of Theorem 27 that $X$ must be a test\&set object or a queue.

1. $X$ is a test\&set object.

The two test\&set operations on $X$ performed by $p$ and $q$ result in two configurations $q(p(D))$ and $p(q(D))$ that only $p$ and $q$ can distinguish: the state of $r$ and the states of all objects (including $X)$ are identical in the two configurations.

Consider a schedule $S$ in which $r$ runs solo (neither $p$ nor $q$ appear in $S$ ) starting from $q(p(D))$ and $r$ decides in $S(q(p(D)))$. Since $p(D)$ is 0 -valent, $r$ must decide 0 in $S(q(p(D)))$. But $S(q(p(D))$ is indistinguishable to $r$ from $S(p(q(D)))$-a contradiction with the assumption that $q(D)$ is 1valent.
2. $X$ is a queue.

Let $\mathrm{OP}_{p}$ the operation issued by $p$ that leads from $D$ to $p(D), \mathrm{OP}_{q}$ the operation issued by $q$ that leads from $D$ to $q(D)$, and $\mathrm{OP}_{r}$ the operation issued by $r$ that leads from $D$ to $r(D)$.

Here we consider the following possible subcases:

- $\mathrm{OP}_{p}$ and $\mathrm{OP}_{q}$ are dequeue operations.

Then, regardless of the state of $X$ in $D, q(p(D))$ and $p(q(D))$ are identical, except for the local states of $P$ and $q$. Thus, in a solo schedule, $r$ can never distinguish two configurations of opposite valences-a contradiction.

- $\mathrm{OP}_{p}$ is an enqueue operation and $\mathrm{OP}_{q}$ is a dequeue operation.

If, in configuration $D, X$ is empty, then $q(p(D))$ and $q(D)$ only differ in the local states of $p$ and $q$, and $X$ is left empty in both configurations.

If $X$ is non-empty in $D$, then $q(p(D))$ and $p(q(D))$ are identical.

In both cases, in solo extensions, $r$ cannot distinguish two configurations of opposite valencesa contradiction.

- Now we are left with the most interesting case: $\mathrm{OP}_{p}$ and $\mathrm{OP}_{q}$ are enqueue operations, let $a$ and $b$ be, respectively, the arguments of the two operations.

Configurations $q(p(D))$ and $p(q(D))$ differ only in the state of $X$ : in $q(p(D))$, the element enqueued by $p$ precedes the element enqueued by $q$, and in $q(p(D))$-vice versa.

Consider a solo schedule of $p$ applied to $q(p(D))$. To decide, $p$ must be able to distinguish the run from a run starting applied $q(p(D)), p$ should eventually access $X$.

Let $S_{p}$ be the solo schedule of $p$ such that in $S_{p}(q(p(D))), p$ is about to dequeue element $a$ it previously enqueued (in operation $\mathrm{OP}_{p}$ ).

Note that in $S_{p}(q(p(D)))$ and $S_{p}(p(q(D)))$ differ only in the state of $X$ and, thus, to decide in a solo schedule applied to $S_{p}(q(p(D))), q$ must eventually access $X$ to dequeue its own element in $X$ enqueued by operation $\mathrm{OP}_{q}$.

Similarly, Let $S_{q}$ be the solo schedule of $p$ such that in $S_{q}\left(S_{p}(q(p(D)))\right), q$ is about to dequeue element $b$ it previously enqueued (in operation $\mathrm{OP}_{p}$ ).

Finally, we observe that $S_{q}\left(S_{p}(q(p(D)))\right)$ and $S_{q}\left(S_{p}(p(q(D)))\right)$ still differ only in the state of $X$ (Figure 11.5): in the first configuration, $X$ begins with $a ; b$ and in the second configurationwith $a ; b$. Thus, by the dequeue operations of $p$ and $q$ in reversed orders, we obtain two identical configurations, $q\left(p\left(S_{q}\left(S_{p}(q(p(D)))\right)\right)\right)$ and $p\left(q\left(S_{q}\left(S_{p}(p(q(D)))\right)\right)\right)$, of opposite valences-a contradiction.

Corollary $6 \operatorname{cons}($ test\&set $)=\operatorname{cons}($ queue $)=2$.

### 11.5. Objects of $n$-consensus type

In this section, we show that for each $n \in \mathbb{N}$, there exists object types $T$, such that $\operatorname{cons}(T)=n$, i.e., the hierarchy of object types implied by their consensus numbers is populated for each level $n$.

The sequential specification of the $n$-consensus object type is given in Figure 11.7. The state of an $n$-consensus object is defined by two variables: $x$ (initially $\perp$ ) —the value to be decided and $\ell$ (initially $0)$ - the number of propose operations perfomed on the object so far. As with the consensus type,
the argument of the first propose operation fixes $x$. However, only first $n$ propose operation return a decided value. All subsequent operations return $\perp$.

```
operation propose $(v)$ :
    $\ell:=\ell+1$
    if $(x=\perp)$ then $x:=v$
    if $(\ell \leq n)$ then
        return $(x)$
    else
        return $(\perp)$
```

Figure 11.7.: Consensus specification: sequential execution of popose $(v)$

We suggest the reader to compute the consensus number of the type, following the lines of the proofs above:

Theorem 31 For all $n \in \mathbb{N}$, cons $(n$-consensus $)=n$.

### 11.6. Objects whose consensus number is $+\infty$

We now complete the picture by showing that some object types have an infinite consensus number: atomic objects of these types, combined with atomic registers can be used to solve consensus among any number of processes. We discuss two such object types: compare\&swap objects and augmented queue.

### 11.6.1. Consensus from compare\&swap objects

A compare\&swap object that stores a value $x$ exports a single compare\&swap () operation that takes two values as arguments, old and new, with the following sequential specification:

```
operation compare\&swap $($ old, new $)$
prev $:=x$
if $(x=$ old $)$ then $x:=$ new;
return $($ prev $)$
```

From compare\&swap objects to consensus Implementing consensus from a single compare\&swap object in a system of any number $n$ of processes is straightforward (Figure 11.8) The base compare\&swap object $C S$ is initialized to $\perp$, a default value that cannot be proposed to the consensus object. When a process proposes a value $v$, it invokes CS.compare\&swap $(\perp, v)$ (line 1 ). If $\perp$ is returned, the process decides its value (line 2). Otherwise, it decides the value returned by the compare\&swap object (line $3)$.

Theorem 32 cons $($ compare\&swap $)=\infty$.

Proof The algorithm in Figure 11.8 is clearly wait-free. Let $p_{i}$ be the first process to execute CS.compare\&swap () operation in a given execution. (Recall that "the first" is defined based on the linearization order on operations on CS.) Clearly, any subsequent call of CS.compare\&swap () returns the input value of $p_{i}$ and, thus, only this value can be decided.

```
operation propose $(v)$ issued by $p_{i}$ :
(1) $\quad$ aux $:=$ CS.compare\&swap $(\perp, v)$;
(2) if aux $=\perp$ then return $(v)$
(3) else return $(a u x)$
```

Figure 11.8.: From compare\&swap to consensus

### 11.6.2. Consensus from augmented queue objects

An augmented-queue object is a previously considered queue with an additional peek () operation that returns the first item of the queue without removing it. Intuitively, the object type has infinite consensus power, as the first element to be enqueued can then be "peeked" and returned as a decision value (assuming that the queue is initially empty).

```
operation propose $(v)$ issued by $p_{i}$ :
    Q.enqueue $(v)$
    $\operatorname{return}(Q \cdot p e e k())$
```

Figure 11.9.: From an augmented queue to consensus

Figure 11.9 gives a simple wait-free implementation of a consensus object from an augmented queue. The construction is pretty simple. The augmented queue $Q$ is initially empty. A process first enqueues its input value and then invokes the $p e e k()$ operation to obtain the first value that has been enqueued. It is easy to see that the construction works for any number of processes, and we have the following theorem:

Theorem 33 cons(augmented-queue) $=\infty$.

### 11.7. Consensus hierarchy

Consensus numbers establish a hierarchy on the power of object types to wait-free implement a consensus object, i.e., to wait-free implement any object defined by a sequential specification on total operations. As we have shown, the lowest level object types (of consensus number 1) include atomicregisters, the second weakest class of object types (of consensus number 2) includes test\&set and queue, and the strongest class (of consensus number $\infty$ ) includes compare\&swap and augmentedqueue. We also showed that for all $n \in \mathbb{N}$, there are object types, e.g., $n$-consensus, that have consensus number exactly $n$, i.e., every level in the hierarchy is "populated."

Consensus numbers also allow ranking the power of classical synchronization primitives (provided by shared memory parallel machines) in presence of process crashes: compare\&swap is stronger than test\&set that is, in turn, stronger than atomic read/write operations. Interestingly, they also show that classical objects encountered in sequential computing such as stacks and queues are as powerful as the test\&set or fetch\&add synchronization primitives when one is interested in providing upper layer application processes with wait-free objects.

Fault-tolerance can be impossible to achieve when the designer is not provided with powerful enough atomic synchronization operations. As an example, a FIFO queue that has to tolerate the crash of a single process, cannot be built from atomic registers. This follows from the fact that the consensus number of a queue is 2 , while the he consensus number of atomic registers is 1 .

