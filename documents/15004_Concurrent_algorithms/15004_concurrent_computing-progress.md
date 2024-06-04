# 3. Progress 

### 3.1. Introduction

The previous chapter focused on the property of linearizability, which basically precludes concurrent operations that do not appear as if executed sequentially. Linearizability (when applied to objects with finite non-determinism) is a safety property: it states what should not happen in an execution.

Such a property is in fact easy to satisfy. Think of an implementation (of some shared object) that simply never returns any response. Since no operation would ever complete, the history would basically be empty and would be trivial to linearize: no response, no need for a linearization point. But this implementation would be useless. In fact, to prevent such implementations, we need some progress property stipulating that certain responses should appear in a history, at least eventually and under certain conditions. Ideally, we would like every invoked operation to eventually return a matching response. But this is impossible to guarantee if the process invoking the operation crashes, e.g., the process is paged out by the operating system which could decide not to schedule that process anymore.

Nevertheless, one might require that a response is returned to a process that is scheduled by the operating system to execute enough steps of the algorithm implementing that operation (i.e., implementing the object exporting the operation). As we will see below, a step here is the access to a low-level object (used in the implementation) during the operation's execution.

To express such requirement more precisely, we need to carefully define the notion of object implementation and zoom into the way processes execute the algorithm implementing the object, in particular how their steps are scheduled by the operating system.

In the following, we introduce the notion of implementation history: this is a lower level notion than the history notion presented in the previous chapter and which describes the interaction between the processes and the object being implemented (high-level history) The concept of low-level history will be used to introduce progress properties of shared object implementations.

### 3.2. Implementation

In order to reason about the very notion of implementation, we need to distinguish the very notions of high-level and low-level objects.

### 3.2.1. High-level and low-level objects

To distinguish the shared object to be implemented from the underlying objects used in the implementation, we typically talk about a high-level object and underlying low-level objects. (The latter are sometimes also called base objects and the operations they export are called primitives ). That is, a process invokes operations on a high-level object and the implementation of these operations requires the process to invoke primitives of the underlying low-level (base) objects. When a process invokes such a primitive, we say that the process performs a step.

The very notions of "high-level" and "low-level" are relative and depend on the actual implementation. An object might be considered high-level in a given implementation and low-level in another one. The object to be implemented is the high-level one and the objects used in the implementation
are the low-level ones. The low-level objects might capture basic synchronization constructs provided in hardware and in this case the high-level ones are those we want to emulate in software (the notion of emulation is what we call implement). Such emulations are motivated by the desire to facilitate the programming of concurrent applications, i.e. to provide the programmer with powerful synchronization abstractions encapsulated by high-level objects. Another motivation is to reuse programs initially devised with the high-level object in mind in a system that does not provide such an object in hardware. Indeed, multiprocessor machines do not all provide the same basic synchronization abstractions.

Of course, an object $O$ that is low-level in a given implementation $A$ does not necessarily correspond to a hardware synchronization construct. Sometimes, this object $O$ has itself been obtained from a software implementation $B$ from some other lower objects. So $O$ is indeed low-level in $A$ and highlevel in $B$. Also, sometimes the low-level objects are assumed to be linearizable, and sometimes not. In fact, we will even study implementations of objects that are not linearizable, as an intermediate way to build linearizable ones.

### 3.2.2. Zooming into histories

So far, we represent computations using histories, as sequences of events, each representing an invocation or a response on the object to be implemented, i.e, the high-level object.

Implementation history. In contrast, reasoning about progress properties requires to zoom into the invocations and responses of the lower level objects of the implementations, on top of which the highlevel object is built. Without such zooming we may not be able to distinguish a process that crashes right after invoking a high-level object operation and stops invoking low-level objects, from one that keeps executing the algorithm implementing that operation and invoking primitives on low-level objects. As we pointed out, we might want to require that the latter completes the operation by obtaining a matching response, but we cannot expect any such thing for the former. In this chapter, we will consider as a implementation history, the low-level history involving invocations and responses of low-level objects. This is a refinement of the higher level history involving only the invocations and responses of the high-level object to be implemented.

Consider the example of a fetch-and-increment (counter) high-level-object implementation, as we describe it below in Section 3.4.1. As low-level objects, the implementation uses an infinite array $T[, \ldots, \infty]$ of TAS (test-and-set) objects and a snapshot-memory object my-inc. The high-level history here is a sequence of invocation and response events of fetch-and-increment operations, while the lowlevel history (or implementation history) is a sequence of primitive events read(), update (), snapshot () and test-and-set () (Figure 3.1).

The two faces of a process. To better understand the very notion of a low-level history, it is important to distinguish the two roles of a process. On the one hand, a process has the role of a client
that sequentially invokes operations on the high-level object and receives responses. On the other hand, the process also acts as a server implementing the operations. While doing so, the process invokes primitives on lower level objects in order to obtain a response to the high-level invocation.

It might be convenient to think of the two roles of a process as executed by different entities and written by two different programmers. As a client, a process invokes object operations but does not control the way the low-level primitives implementing these operations are executed. The programmer writing this part does typically not know how an object operation is implemented. As a server, a process executes the implementation algorithm made up of invocations of low-level object primitives. This algorithm is typically written by a different programmer who does not need to know what client applications will be using this object. Similarly, the client application does not need to know how the objects used are implemented, except that they ensure linearizability and some progress property as discuss below.

Scheduling and asynchrony. The execution of a low-level object operation is called a step. The interleaving of steps in an implementation is specified by a scheduler (itself part of an operating system). This is outside of the control of processes and, in our context, it is convenient to think of a scheduler as an adversary. This is because, when devising an algorithm to implement some high-level object, one has to cope with worst-case strategies the scheduler may choose to defeat the algorithm. This is then viewed as an adversarial behavior.

A process is said to be correct in a low-level history if it executes an infinite number of steps, i.e., when the scheduler allocates infinitely many steps of that process. This "infinity" notion models the fact that the process executes as many steps as needed by the implementation until all responses are returned. Otherwise, if the process only takes finitely many steps, it is said to be faulty. In this book, we only assume that faulty processes crash, i.e., permanently stop performing steps, otherwise they never deviate from the algorithm assigned to them. In other words, they are not malicious (we also say they are not Byzantine).

Unless explicitly stated otherwise, the system is assumed to be asynchronous , i.e., the relative speeds of the processes are unbounded: for all $\Phi \in \mathbb{N}$ and processes $p$ and $q$, there is an execution in which $p$ takes $\Phi$ steps while process $q$ takes only one step. Basically, an asynchronous system is controlled by a very weak scheduler, i.e., a scheduler that may prevent a correct process from taking steps for an arbitrary (but finite) periods of time.

### 3.3. Progress properties

As pointed out above, a trivial way to ensure linearizability would be to do nothing, i.e., return no response to any operation invocation. This would preclude any history that violates linearizability by simply precluding any history with a response.

Besides this (clearly, meaningless) approach, a popular way to ensure linearizability is to use critical sections (say using locks), preventing concurrent accesses to the same high-level shared object. In the simplest case, every operation on a shared object is executed as a critical section. When a process invokes an operation on an object, it first requests the corresponding lock, and the algorithm of the operation is executed by the process only when the lock is acquired. If the lock is not available, the process waits until the lock is released. After a process obtains the response to an operation, it releases the corresponding lock. This approach also trivially ensures linearizability because the linearization points of the operations of a history correspond to the moment at which the lock is acquired for the operation.

As we discussed in Chapter 1, such an implementation of a shared object has an inherent drawback: the crash of a process holding the lock on an object prevents any other process from completing its
operation. In practice, the process holding the lock might be preempted for a long period of time, while all processes contending on the same object remain blocked. When processes are asynchronous (i.e., the scheduler can arbitrarily preempt processes) which is the default assumption we consider, there is no way for a process to know whether another process has crashed (or was preempted for a long while) or is only very slow. In a system with a couple of processors, this might not be considered a big deal. But in a modern architecture with a very large number of processors, having a single point of blocking might be considered unacceptable.

This book focuses on robust shared object implementations with progress properties precluding situations where the crash of some strict subset of processes prevents every other process from making progress. This models the requirement that processes that are delayed by the operating system should not block all other processes from progressing. Hence, we preclude the use of critical sections or locks.

- Informally, we say that an implementation is lock-based if it allows for a situation in which some process running in isolation after some finite execution is never able to complete its operation.
- Taking a negation of this property, we state that an implementation does-not-employ-locks if starting after any finite execution, every process can complete its operation in a finite number of its own steps.

Intuitively, this property, called obstruction-freedom (or solo termination), must be satisfied by any implementation where the crash of any process does not prevent other processes from making progress. Below we discuss this property in more details together with some of its variants.

### 3.3.1. Variations

Several progress properties preclude the usage of locks:

- Obstruction-freedom (also called solo termination). An implementation (of a shared object) is obstruction-free, if any of its operations returns a response if it is eventually executed without concurrency by a correct process.

The operation is said to be eventually executed without concurrency if there is a time after which the only process to take step involving the object is the process that invoked that operation. ${ }^{1}$
- Non-blockingness (partial termination). This property, strictly stronger than obstruction-freedom, states that at least one of several correct processes executing operations on the same object, terminates its operation. Intuitively, non-blockingness can be interpreted as deadlock-freedom (despite asynchrony and crashes).
- Wait-freedom (also called global termination). This property is even stronger. It states that any correct process that executes an operation eventually returns a response. Wait-freedom can be viewed as starvation-freedom (despite asynchrony and crashes).[^0]

### 3.3.2. Bounded termination

Wait-freedom, the strongest of the properties above, does not stipulate any bound on the number of steps that a process needs to execute before obtaining a matching response for the high-level object operation it invoked. Typically, this number of steps can depend on the behavior of the other processes. It could be small if no other process performs any step, and gets bigger when all processes perform steps (or the opposite), while remaining always finite, regardless of the number and timing of crashes.

- An implementation is bounded wait-free if there exists a bound $B \in \mathbb{N}$ such that every process $p$ that invokes an operation receives a matching response within $B$ of its own (not necessarily consecutive in the execution) steps.

In other words, there is no prefix of a low-level history in which a process invokes an operation and executes $B$ steps without obtaining a matching response.

Showing that an implementation is bounded wait-free consists in exhibiting an upper bound on the number of steps needed to return from any operation. That upper bound is usually defined by a function of the number $n$ of processes (e.g., $O\left(n^{2}\right)$ ). One can similarly define notions like bounded solo termination or bounded partial termination.

### 3.3.3. Liveness

Recall that safety properties (Section 2.5) are used to declare what it means for an implementation to reach an undesired state. To show that an implementation satisfies a safety property $P$, it is sufficient to check if each of its finite executions satisfies $P$.

In contrast, a liveness property ensures that the implementation eventually reaches some desired state. More specifically, we say that $P$ is a liveness property if any finite execution has an extension in $P$. Hence, no matter what state our implementation is in, there is always a chance to reach a desired state in some extension of the current execution. To show that an implementation satisfies a liveness property $P$, we should thus show that all its infinite executions are in $P$.

Interestingly, every property can be represented as an intersection of a safety property and a liveness property [78]. Linearizability is a safety property (Section 2.5). Wait-freedom, as we can easily see, is a liveness property. Indeed, we can only violate wait-freedom in an infinite execution: every finite execution in which an operation invoked by a given process has an extension in which the operation returns. Similarly, non-blockingness and obstruction-freedom are also liveness properties. For example, the only way to violate obstruction-freedom is to exhibit an execution in which a process takes infinitely many steps without completing an invoked operation.

It is interesting to notice that bounded wait-freedom is, in fact, a safety property. Indeed, $B$-bounded wait-freedom is violated in a finite execution where an operation does not return after $B$ steps of the process that invoked it. It is not difficult to see that $B$-bounded wait-freedom is prefix-closed and limitclosed. Therefore, to prove that an implementation is, e.g., linearizable and $B$-bounded wait-free, it is enough to consider its finite executions.

### 3.4. Linearizability and wait-freedom

### 3.4.1. A simple example

The algorithm described in Figure 3.2 is a simple wait-free linearizable implementation of a fetch-andincrement (FAI object using an infinite array of test-and-set TAS objects $T[1, \ldots, \infty]$ and a snapshot memory object My_inc.

- The high-level object is the FAI. This object stores an integer value and exports one operation fetch-and-increment () . The sequential specification of this operation basically increments the value of the integer value and returns the previous value.
- The low-level objects used in the implementation include TAS objects. Each of these exports one (primitive) operation test-and-set() that returns 0 or 1 . The sequential specification of this operation guarantees that the first invocation of test-and-set () on the object returns 1 and all subsequent invocations return 0 . Intuitively, a TAS object allows a single process to distinguish itself from the rest of the processes. Such objects are typically provided by many multi-core machines.
- The snapshot memory is also a low-level object used in the implementation. It can be seen as an array of $n$ registers, one for each process, such that each process $p_{i}$ can atomically write a value $v$ to its dedicated register with an operation update $(i, v)$ and atomically read the content of the array using an operation snapshot ()$.^{2}$

```
Shared
    $T[1, \ldots, \infty]: n$-process TAS objects
    My_inc $[1, \ldots, \infty]$ : snapshot memory, initialized to 0
Local
    entry, $c$ (initially 0$), S$
operation fetch-and-increment () :
    $c \leftarrow c+1$
    My_inc.update $(i, c)$
    $S \leftarrow$ My_inc.snapshot ()
    entry $\leftarrow \operatorname{sum}(S)$;
    while $T[$ entry].test-and-set ()$\neq 0$ do
        entry $\leftarrow$ entry -1
    return $($ entry -1$)$
```

Figure 3.2.: Fetch-and-increment implementation: code for process $p_{i}$

The algorithm in Figure 3.2 depicts the code executed by every process $p_{i}$ of the system. It works as follows. To increment the value of the FAI object (i.e., to execute a fetch-and-increment () operation), $p_{i}$ first increments its dedicated register in the snapshot memory My_inc. Then $p_{i}$ takes a snapshot of the memory and evaluates entry as the sum of all its elements. Then, starting from the $T[$ entry] down to $1, p_{i}$ invokes operations test-and-set () until some TAS object returns 1 . The index of this TAS object minus 1 is then returned by fetch-and-increment() operation.

Intuitively, when $p_{i}$ evaluates its local variable entry to $\ell$, at most $\ell$ processes have previously incremented their positions and, thus, at least one TAS object in the array $T[1, \ldots, \ell]$ is "reserved" for $p_{i}$ ( $p_{i}$ is one of these $\ell$ processes). Every process that increments its position in $M y$ _inc later will obtain a strictly higher value of entry. Thus, eventually, every operation obtains 1 from one of the TAS objects and returns. Moreover, since a TAS object returns 1 to exactly one process, every returned value is unique.

Notice that the number of steps performed by a fetch-and-increment() operation is finite but in general unbounded (the implementation is not bounded wait-free). This is because an unbounded number of increments can be performed by other processes in the time lag between a process $p_{i}$ increments it[^1]position in My_inc and the moment $p_{i}$ takes a snapshot of My_inc. It is however not difficult to modify the algorithm so that every operation performs $O\left(n^{2}\right)$ steps.

### 3.4.2. A more sophisticated example

Proving that a given implementation satisfies linearizability and wait-freedom can be extremely tricky sometimes. To illustrate this, consider now the algorithm of Figure 3.3 that intends to implement an unbounded FIFO queue. The sequential specification of this object has been given in Section 2.1 of Chapter 2.

The algorithm is quite simple. The system we consider here is made up of producers (clients) and consumers (servers) that cooperate through an unbounded FIFO queue. A producer process repeats forever the following two statements:

1. Prepare a new item $v$
2. Invoke the operation $\operatorname{Enq}(v)$ to deposits $v$ in the queue.

Similarly, a consumer process repeats forever the following two statements:

1. Withdraw an item from the queue by invoking the operation $\operatorname{Deq}()$
2. Consume that item.

If the queue is empty, then the default value nil is returned to the invoking process. (This default value that cannot be deposited by a producer process.) We assume that no processing by the consumer is associated with the nil value.

The algorithm depicted in Figure 3.3 relies on an unbounded array $Q[0, \ldots, \infty]$, where entry of the array is initialized to nil and is used to store the items of the queue. Also, the implementation uses a shared variable NEXT (initialized to 1 ) as a pointer to the next available slot of the array $Q$ for a new value to be deposited.

To enqueue an item to the queue, the producer first locates the index of the next empty slot in the array $Q$, reserves it, and then stores the item in that slot. To dequeue a value, the consumer first determines the last entry of the array $Q$ that has been reserved by a producer. Then, it reads the elements of the array $Q$ in ascending order until it finds an item different from the default value nil. If it finds one, it returns it. Otherwise, the default value is returned.

The variable NEXT is provided with two primitives denoted read() and fetch\&add(). The invocation NEXT.fetch\&add $(x)$ returns the value of NEXT before the invocation and adds $x$ to NEXT. Similarly, each entry $Q[i]$ of the the array is provided with two primitives denoted write() and swap(). The invocation $Q[i] . \operatorname{swap}(v)$ writes $v$ in $Q[i]$ and returns the value of $Q[i]$ before the invocation.

The execution of the read(), write(), fetch\&add() and swap() primitives on the shared base objects (NEXT and each variable $Q[i])$ are assumed to be linearizable. The primitives read() and write() are implicit in the code of Figure 3.3 (they are in the assignment statements denoted " $\leftarrow$ ").

The algorithm does not use locks: no process can block other processes forever. Furthermore, each value deposited in the array by a producer will be withdrawn by a swap () operation issued by a consumer (assuming that at least one consumer is correct).

It is easy to see that the implementation is wait-free: every process completes each of its operations in a finite number of its own steps: the number of steps performed by $\operatorname{En} q()$ is two, and the number of steps performed by $\operatorname{Deq}()$ is proportional to the queue size as evaluated in the first line of its pseudocode.

```
operation $\operatorname{Enq}(v)$ :
    in $\leftarrow N E X T$.fetch\&add (1);
    $Q[i n] \leftarrow v$
    return ()
operation $\operatorname{Deq}()$ :
    last $\leftarrow N E X T-1$
    for $i$ from 0 until last do
        aux $\leftarrow Q[i]$.swap (nil);
        if $(a u x \neq \perp)$ then return $(a u x)$
    return (
```

Figure 3.3.: Enqueue and dequeue implementations

But is the implementation linearizable? Superficially, yes: if no dequeue operation returns nil, we can order operations based on the times when the corresponding updates of $Q[]$ (a write performed by $\operatorname{Enq}($ ) or a successful swap performed by $\operatorname{Deq}())$ takes place.

However, if a dequeue operation returns nil it is not always possible to find the right place for it in a legal linearization. Consider for instance the following scenario:

1. Process $p_{1}$ performs $\operatorname{En} q(x)$. As a result, the value of NEXT is 1 , and $Q[0]$ stores $x$.
2. Process $p_{2}$ starts executing $\operatorname{Deq}()$ and reads 1 in NEXT.
3. Process $p_{1}$ performs $\operatorname{En} q(y)$. The value of $N E X T$ is now $2, Q[0]$ stores $x$, and $Q[1]$ stores $y$.
4. Process $p_{3}$ performs $\operatorname{Deq}()$, reads 2 in NEXT, finds $x$ in $Q[0]$ and returns $x$. The value of $Q[0]$ is nil now.
5. Finally, $p_{2}$ reads $\perp$ in $Q[0]$ and completes $\operatorname{Deq}()$ by returning nil.

In this execution: we have the following partial order on operations: $p_{1} \cdot \operatorname{En} q(x) \rightarrow p_{1} \cdot \operatorname{En} q(y) \rightarrow$ $p_{3} \cdot \operatorname{Deq}(x)$, and $p_{1} \cdot \operatorname{En} q(x) \rightarrow p_{2} \cdot \operatorname{Deq}\left(\right.$ nil). Thus, there are only three possible ways to linearize $p_{2} \cdot \operatorname{Deq}($ nil)(: right after $p_{1} \cdot \operatorname{En} q(x)$, right after $p_{1} \cdot \operatorname{En} q(y)$ or right after $p_{3} \cdot \operatorname{Deq}()$. In all three possible linearizations, the queue is not empty when $p_{2}$ invokes $\operatorname{Deq}()$, and thus nil cannot be returned.

How to fix this problem? One solution is to sacrifice linearizability and not consider operations returning nil in a linearization.

Another solution is to sacrifice wait-freedom and instead of returning nil in the last line of the Deq(), repeat the same procedure (evaluating NEXT and going through the first NEXT elements in $Q[]$ ) over and over until a non- $\perp$ value is found in $Q[]$. As long as a producer keeps adding items to the queue, every Deq () operation is guaranteed to eventually return.

### 3.5. Summary

To reason about correctness of an object implementation, it is common to consider linearizability, as well as some companion progress property. In this chapter, we studied three progress properties: solotermination (obstruction-freedom), partial-termination (non-blockingness) and global termination (waitfreedom). All of these are liveness properties, precluding the usage of locks. The first of these properties says that a process that eventually accesses an object alone (with no contention) will get responses when invoking the object's operation. The second property requires a response to be returned to at least one of the correct processes even if there is contention. The last property, wait-freedom, is the


[^0]:    ${ }^{1}$ There is an alternative, weaker notion of contention, called interval contention. An operation encounters interval contention if it overlaps with another operation (this does not need to take steps). Step contention implies interval contention, but not vice versa. However, an alternative definition of obstruction-freedom requiring that an operation returns if it runs in the absence of interval contention does not preclude the usage of locks. An operation grabs the lock on the shared object, executes the operation on the object, and releases the lock before returning the response.

[^1]:    ${ }^{2}$ In Chapter 8, we show how snapshot memory can be implemented in a wait-free and linearizable manner using only readwrite registers.

