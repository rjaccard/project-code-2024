# 9. Immediate snapshot and iterated immediate snapshot 

In Chapter 8, we discussed the atomic-snapshot abstraction that provides two operations, update, which allows a process to write a value in a dedicated memory location, and snapshot, which atomically returns the "current" state of the memory. Strong and useful, the atomic-snapshot abstraction, however, does not preclude a situation when snapshots taken by different processes are "unbalanced": a snapshot $S_{i}$ taken by $p_{i}$ contains a value written by $p_{j}$ but the snapshot $S_{j}$ taken by $p_{j}$ contains more recent values (and, thus, is more up-to-date) than $S_{i}$. In this chapter, we discuss a restricted version of atomic snapshot, called immediate snapshot, that only exports "balanced" runs: IF $p_{i}$ "sees" $p_{j}$, than $S_{i}$ contains $S_{j}$.

### 9.1. Immediate snapshots

### 9.1.1. Definition

An immediate-snapshot object exports a single operation update_snapshot () that takes a value as a parameter and returns a vector of values (a view) in response. It is required that the executions of these operations appear as executed in "batches". In each batch, a fixed subset of processes execute their update_snapshot () in parallel: the processes in the subset first execute their updates and then take their snapshots. Obviously, the results of the snapshots taken by the processes in the same batch are identical. Intuitively, these snapshots are operations "immediate" in the sense that the snapshot taken by a process does not "lag" too much behind its update. As we shall see, the immediate-snapshot model has a straightforward geometrical representation which, in turn, enables simple and elegant reasoning about the model's computability.

As in the original definition of atomic snapshots (Chapter 8), we assume that each written value is unique. Any history of an immediate-snapshot object satisfies the following properties.

- Self-inclusion. For any operation update_snapshot $\left(v_{i}\right)$ that returns $V_{i}$, we have $\left(i, v_{i}\right) \in V_{i}$.
- Containment. For any two operations update_snapshot $\left(v_{i}\right)$ and update_snapshot $\left(v_{j}\right)$ that return $V_{i}$ and $V_{j}$, respectively, we have $V_{i} \leq V_{j}$ or $V_{j} \leq V_{i}$.
- Immediacy. For any operation update_snapshot $\left(v_{i}\right)$ and update_snapshot $\left(v_{j}\right)$ that return $V_{i}$ and $V_{j}$, respectively, if $\left(i, v_{i}\right) \in V_{j}$ then $V_{j} \leq V_{i}$.

The first two properties will automatically hold if we take an atomic snapshot object and implement update_snapshot $\left(v_{i}\right)$ as update $\left(v_{i}\right)$ followed by snapshot () . However, the immediacy property will not be satisfied here: it is possible that an update operation of a process $p_{i}$ is followed by an update and snapshot operation of another process $p_{j}$, and then multiple updates and snapshots of other processes. The subsequent snapshot by $p_{i}$ would then strictly succeed the snapshot taken by $p_{j}$, as it would contain the updates that occurred after $p_{j}$ performed its snapshot (see Exercise 3).

FIGURE

Notice that the immediacy property implies that the immediate snapshot object has no sequential specification. Indeed, a history in which update_snapshot $\left(v_{i}\right)$ and update_snapshot $\left(v_{j}\right)$ return $V_{i}$ and $V_{j}$, respectively, such that $\left(i, v_{i}\right) \in V_{j}$ and $\left(j, v_{j}\right) \in V_{j}$ does not allow for a legal ordering of these two operations with a sequential semantics that matches the properties above. We leave it to the reader to prove this claim, e.g., along the lines of the proof of Lemma 5 (Exercise 1).

### 9.1.2. Block runs

We can view the immediate-snapshot model as a subset of runs of the conventional atomic-snapshot model in which every process alternates between performing updates (on its distinct location in the shared memory) and taking atomic snapshots. Every run in the immediate-snapshot model is induced by a block sequence:

$$
B_{1}, B_{2}, B_{2}, \ldots
$$

where each $B_{i}$ is a non-empty set of processes. The induced run consists in $B_{1}$ performing updates (in an arbitrary order) and then taking snapshots (in the arbitrary order), followed by all processes in $B_{2}$ performing updates and then taking snapshots, and so on.

It is not hard to see that the snapshots taken by the members of the same $B_{i}$ are identical and for all $i<j$, the snapshot $V_{i}$ taken by $B_{i}$ and the snapshot $V_{j}$ taken by $B_{j}$ satisfy $V_{i} \leq V_{j}$. Moreover, if $V_{i}$ only contains values that processes in $B_{j}, j \leq i$ have written in the induced run. Thus, if $\left(i, v_{i}\right) \in V_{j}$, where $v_{i}$ is the value written by $p_{i}$ just before it obtained immediate snapshot $V_{i}$, then $V_{i} \leq V_{j}$.

### 9.1.3. A one-shot implementation

We begin with an implementation of the immediate-snapshot abstraction, assuming that every process performs at most one update_snapshot () in a run.

The algorithm, presented in Figure 9.1, uses a shared array of 1WMR atomic registers $R E G[1: n]$, where $R E F G[i]$ can be written only by $p_{i}$ and read by all processes. Each $R E F G[i]$ stores a pair $\left(\ell_{i}, v_{i}\right)$, initially $(n+1, \perp)$, where $v_{i}$ is the value written by $p_{i}$ and $\ell_{i}$ is the level reached by $p_{i}$ so far.

## Operation

The algorithm operates as follows. Every process $p_{i}$ begins with posting its value $v_{i}$ in $V A L[i]$ and announcing its participating at level $n$ by writing $n$ in $R E G[i]$ and. Then it reads $R E G[1: n]$ to check the levels reached by other processes. If all $n$ processes are at levels $n$ or less, then $p_{i}$ returns the set of $n$ their values (read in $V A L$ ). Otherwise, $p_{i}$ goes down to level $n-1$. If, inductively, after writing $\ell$ $(\ell=n-1, \ldots, 1)$ in $R E G[i]$ and checking $R E G[1: n], p_{i}$ finds out that $\ell$ processes reached levels $\ell$ or lower, it returns the values of these $\ell$ processes. Clearly, the process returns at level 1 at the latest, i.e., the algorithm is bounded wait-free: it takes $O\left(n^{2}\right)$ basic reads and writes to complete an operation.

## Correctness

To get an intuition about the algorithm's correctness, let us consider a run in which a set of $k$ processes proceed in lock step, i.e., the $k$ processes alternate between concurrently writing to $R E G$ and reading $R E G[1: n]$. Notice that in this run, whenever a process reaches a level $\ell$ and reads $R E G[1: n]$, it witnesses exactly $k$ processes at the same level. Thus, all the processes will return the same set of $k$ values as soon as they reach level $k$.

At the other extreme, consider a sequential execution of $n$ processes performing update_snapshot () operations one by one. The first process, as it only sees itself, will be obliged to return at level 1.

```
Shared:
    value array of registers $V A L[1: n]$, initially $\perp$
    integer array of registers $R E G[1: n]$, initially $n+1$
Local:
    value array $\operatorname{val}[1: n]$, initially $\perp$
    integer level, initially $n+1$
operation update_snapshot $\left(v_{i}\right)$ invoked by $p_{i}$ :
    $V A L[i]:=v_{i}$
(1) $\quad$ repeat level $:=$ level -1
(2) $R E G[i]:=$ level
    $V:=\emptyset$
(3)
$|V| \geq$ level
(5) $\quad$ for_each $j \in\{1, \ldots, n\}$ do
if $j \in V$ then
$\operatorname{val}[j]:=\operatorname{VAL}[j]$
(6) return (val)
```

Figure 9.1.: A one-shot IS implementation

Inductively, the $k$-th process in the sequential order $(k=2, \ldots, n)$, will output at level $k$ : it will see itself and $k-1$ processes before it. Thus, the processes will return strictly increasing sets of values, from a singleton containing the value of the first process to the

More generally, the last process $p_{i}$ to reach level $n$, i.e., to write $\left(n, v_{i}\right)$ in $R E G[i]$ will see exactly $n$ processes at levels $n$ or lower. Thus, $p_{i}$ returns the set of $n$ values, and at most $n-1$ processes will reach levels $n-1$ or lower. Inductively, we can show that if $\ell$ processes reach level $\ell(\ell=n, \ldots, 2)$, at least one process will return at this level, and at most $\ell-1$ will proceed to level $\ell-1$.

Formally, what we need to show is that, in every run of the algorithm, the sets of values returned by the processes satisfy the three properties of immediate snapshot: self-inclusion, containment and immediacy.

## Lemma 10 The algorithm in Figure 9.1 is bounded wait-free.

Proof In every round (lines 1-4), a process performs one write and $n$ reads. In the round $n$ (reaching at level 1), the process will see at least one value (its own). Thus, at the latest, the process returns in round $n$ and, thus, every operation performs $O\left(n^{2}\right)$ basic read-write steps.

Consider any run of the algorithm. Let $S_{\ell}$ denote the set of processes that ever reach level $\ell$ in that run. By the algorithm, $S_{1} \subseteq S_{2} \subseteq \ldots \subseteq S_{n}$.

Lemma 11 For all $\ell \in\{1, \ldots, n\},\left|S_{\ell}\right| \leq \ell$.

Proof We proceed by downward induction on $\ell$. The base case $\ell=n$ is trivial, as there are at most $n$ processes taking steps in any run.

Suppose that for some $\ell \in\{2, \ldots, n\},\left|S_{\ell}\right| \leq \ell$, i.e., at most $\ell$ processes reach level $\ell$. If $\left|S_{\ell}\right|<\ell$, then we are done, as $S_{\ell-1} \subseteq S_{\ell}$. Otherwise, suppose that $\left|S_{\ell}\right|=\ell$, and let $p_{j}$ be the last process in this set of $\ell$ processes that reaches level $\ell$, i.e., writes $\ell$ in $R E G$ in line 2 . By the algorithm, $p_{j}$ witnesses exactly $n$ processes at levels $\ell$ and lower and, thus, returns in level $\ell$. Therefore, at most $\ell-1$ process ever reach level $\ell-1$.

Theorem 22 The algorithm in Figure 9.1 is a bounded wait-free implementation of immediate snapshot.

Proof By Lemma 10, the algorithm is bounded wait-free.

Consider any run of the algorithm, and let $V_{i}$ denote the set of values returned by a process $p_{i}$ in that run. Let $\ell_{i}$ denote the level at which $p_{i}$ returns. By the algorithm, $p_{i}$ reached level $\ell_{i}$ by writing $\ell_{i}$ in $R E G[i]$, then read $R E G[1: n]$ and then returned the set of $\ell_{i}$ values written by processes that reached level $\ell_{i}$ or lower.

Thus, $p_{i}$ returned values written by a subset of $S_{\ell_{i}}$ of size $\ell_{i}$ or more, including its own value-the property of self-inclusion is ensured. Furthermore, by Lemma 11, $S_{\ell_{i}} \leq \ell_{i}$ and, thus, $p_{i}$ returned exactly the values of processes in $S_{\ell_{i}}$.

Consider any other process $p_{j}$ that returned in the given run and suppose, without loss of generality, that $p_{j}$ returned at level $\ell_{j}<\ell_{i}$. Recall that $S_{\ell_{j}} \subseteq S_{\ell_{i}}$ and, thus, $V_{j} \subseteq V_{i}$-the property of containment is ensured.

Finally, consider any process $p_{j}$ such that $p_{j} \in S_{\ell_{i}}$ and, thus, $v_{j} \in V_{i}$. Since $p_{j}$ reached level $\ell_{i}$ in that run, it can only return some the values written by some $S_{\ell_{j}}$ such that $\ell_{j} \leq \ell_{i}$. Since, $S_{\ell_{j}} \subseteq S_{\ell_{i}}$, we have $V_{j} \subseteq V_{i}$-the property of immediacy is ensured.

### 9.2. Fast renaming

To illustrate how the IS model can be used, we describe an elegant algorithm solving the classical renaming problem. In the renaming algorithm, processes take, as inputs, with original names from a large range and return, as outputs, new names taken in a smaller range the size of which is proportional to the number of participating processes. More precisely, the following properties must be satisfied in every run of a renaming algorithm:

Termination: Every correct process eventually output a name.

Uniqueness: Now two distinct processes output the same name.

Name-Adaptivity: The output names belong to the range $\{1, \ldots, 2 p-1\}$, where $p$ is the number of participating processes.

To rule out a trivial solution in which process $p_{i}$ outputs name $i$ we add the following requirement:

Anonymity: For all $p_{i}$ and $p_{j}$, the algorithm of $p_{i}$ with input $x$ is the same as the algorithm of $p_{j}$ with input $x$.

We should be careful here. In solving renaming, assuming that a single-writer multi-reader share memory is available somewhat undermines the very motivation behind this problem that, even though there is a bound on the number of participating processes in every run, the participants themselves may come from a very large (unbounded) space. One may ask how the assignment of distinct single-writer registers to participating can be implemented in such a system. The challenge of simulating single-writer multi-reader memory in such a system (also called bootstraping) has been addressed in $[25,26]$. In this chapter, we however rule this out by assuming anonymous algorithms.

### 9.2.1. Snapshot-based renaming

A simple snapshot-based renaming algorithm in Figure 9.2 is based on "arbitration". A process starts with writing its input name in its dedicated register. Then it takes a snapshot of the memory to evaluate the set of participants, selects a name based on its ranking in the set (using the compare operator), writes the chosen name, together with its input, back in its register, and takes a snapshot again. If no other process chose the same name, the process terminates with the chosen output. Otherwise, the process chooses, as its new name, the first name with its ranking in the current set of participants that is not claimed by another process and repeats the procedure.

```
Shared:
    atomic-snapshot object $A S$
operation $\operatorname{rename}\left(v_{i}\right)$ invoked by $p_{i}$ with input $v_{i}$ :
    name $:=1$
    repeat forever
        AS.update $\left(\left[\right.\right.$ name,$\left.\left.v_{i}\right]\right)$
        $S:=$ AS.snapshot ()
        if $S$ contains no $\left[\right.$ name $\left.e^{\prime}, v_{j}\right]$ such that name $e^{\prime}=$ name and $v_{j} \neq v_{i}$ then
            return name
        rank $:=$ the rank of $v_{i}$ in $\left\{v_{j} \mid\left[*, v_{j}\right] \in S\right\}$
        free $:=\{u \mid[u, *] \notin S\}$
        name $:=$ the $r$-th element in free
```

Figure 9.2.: A renaming algorithm using atomic snapshots

When $p$ processes participating, the largest name a process may choose is $2 p-1$. Intuitively, a given process can "block" at most two names at a time: one it has written to the memory and one that it is about to write. As a result, in the worst case, the process may see $p-1$ blocked and have rank $p$ among the participants: thus, the largest name $2 p-1$.

### 9.2.2. IS-based renaming

In the recursive IS-based algorithm described in Figure 9.2, we use one-shot IS instances to evaluate the set of participating processes. Each invocation of the IS instance is associated with a range of names that the processes invoking this instance are allowed to return. The range is determined via a starting point (denoted start) and a direction (denoted dir $\in\{-1,1\}$ ) in which names of the range, starting from start, are allocated. A list of integer values tags contains the sequence of starting points of preceding recursive calls of get_name.

For instance, if $p$ processes invoke get_name(tags, start,dir), then the algorithm guarantees that all names output by these processes fall within the range start + dir, $\ldots$, start $+\operatorname{dir}(2 p-1)$ of $2 p-1$ names.

The property of IS that the number of processes that output a set of values of size $\ell$ is precisely $\ell$ minus the number of processes that output strictly smaller sets of values guarantees that all output names are distinct.

For each sequence $L$ of values in $\{1, \ldots, n\}$, the algorithm uses a distinct one-shot IS object $I S[L]$. A process invokes get_name $(L, f, d)$ where $L$ is the list of sizes of sets obtained in all preceding IS calls. As we will show, all such sequences $L$ are monotonically decreasing.

The get a new name, every process $p_{i}$ invokes get_name $(\epsilon, 0,1)$, where $\epsilon$ is the empty list. Within get_name $\left(L\right.$, start,dir), the process first invokes $I S[L]$.update_snapshot $\left(v_{i}\right)$, where $v_{i}$ is its input name, to get a set $S$ of input names. If $v_{i}$ happens to be the largest name in $S, p_{i}$ returns the "most faraway" name in the range $\operatorname{start}+\operatorname{dir}, \ldots$, start $+\operatorname{dir}(2|S|-1)$, i.e., name $=$ start $+\operatorname{dir}(2|S|-1)$. Otherwise, $p_{i}$ selects name as a new starting point and inverses the direction by recursively calling get_name $(L \cdot|S|$, name - dir $)$ to get its new name.

In Figure 9.3, we describe an execution of the algorithm for seven processes with original names $1, \ldots, 7$. The processes invoke get_name with parameters $(\epsilon, 0,1)$ which means that they compete for names in the range $1, \ldots, 13\}$. Suppose that after accessing $I S[\epsilon]$, processes with names 1,2 and 3 see all 7 processes, processes with names 4,5 see four processes $4,5,6,7$, processwith name 6 sees 6,7 and process with name 7 sees only itself.

As their names are not the maximal in the set, 1,2 and 3 invoke get_name with parameters $(7,13,-1)$, i.e., they compete for names in the range $12,11,10,9,8$ (in the descending order). After accessing $I S[7]$, process with name 3 sees only itself and outputs 12 (the "first" name in the range). Processes with names 1 and 2 see all of the three processes and invoke get_name with parameters $(7 \cdot 3,8,1)$ to compete for names in the range $9,10,11$ (in the ascending order).

After accessing $I S[7 \cdot 3]$, process 2 sees only itself and outputs 9 (the "first" name in the corresponding range). Process with name 1 sees both 1 and 2 and, thus, invokes get_name $(7 \cdot 3 \cdot 2,11,-1)$ to finally output 10.

```
Shared:
    for each $L$, list of values in $\{1, \ldots, n\}$ : one-shot IS instance $I S[L]$
operation get_name( $L$, start, dir) invoked by $p_{i}$ with input $v_{i}$ :
    $S:=I S[L]$. update_snapshot $\left(v_{i}\right)$
    st $:=\operatorname{start}+\operatorname{dir}(2|S|-1)$
    if $v_{i}=\max (S)$ then
        name $:=s t$
    else
        name $:=$ get_name $(L \cdot|S|, s t,-$ dir $)$
    return name
operation $\operatorname{rename}\left(v_{i}\right)$ invoked by $p_{i}$ with input $v_{i}$ :
    return get_name $(\epsilon, 0,1)$
```

Figure 9.4.: A renaming algorithm using one-shot IS instances

Given that an access to one-shot IS object exhibits $O\left(n^{2}\right)$ read-write steps, we get the following result.

Lemma 12 In every run of the renaming algorithm in Figure 9.4, every correct process returns in $O\left(n^{2}\right)$ read-write steps.

Proof By the algorithm, the participating processes start with calling get_name $(\epsilon, 0,1)$. We observe first that the participant with the highest input name will return the value computed in line 9.2 .2 of this call. Indeed, regardless of the set of participating processes, it obtains in line 9.2.2, it will always itself to have the maximal name. The property holds for any recursive call of get_name (line 9.2.2). Thus, the number of processes that reach line 9.2.2 within a call of get_name is at least by one smaller than the number of processes that started this call. When the total number of processes preforming a call of get_name $(L$, start, dir) drops to one, this process will return the value computed in 9.2.2.

Thus, in the worst case, a process returns in the $n$-th recursive calls of get_name. Each recursive call involves a single invocation of a single invocation of update_snapshot on a one-shot IS instance which gives $O\left(n^{2}\right)$ read-write complexity per instance and, thus, $O\left(n^{3}\right)$ total step complexity per call of rename $\left(v_{i}\right)$.

The safety properties of renaming (Uniqueness and Name-Adaptivity) are shown via the following auxiliary lemma:

Lemma 13 Suppose that at most $k>0$ processes call get_name $(L, s, d)$ in a run of the algorithm in Figure 9.4. Then these calls can only return distinct values outside $\{s+d, \ldots, s+d(2 k-1)\}$.

Proof We note first that, since the size of the set returned by a one-shot IS instance unambiguously identifies the set itself, every two processes that call $\operatorname{get\_ name}(L,-,-)$ agree on the remaining two parameters.

Now we proceed by induction on $k$. The claim holds trivially when $k=1$ : the only process to call get_name ( $L$, start, dir) obtains a set of size 1 from $I S[L]$ and returns value start + dir computed in line 9.4.

Now suppose that the claim holds for all values $k^{\prime}<k$ and consider a run in which $k$ processes call get_name( $L$, start, dir).

Suppose that the $k$ processes obtained sets of distinct sizes $1 \leq \ell_{1}<\ldots<\ell_{m}$ from $I S[L]$.

We can show that $\ell_{m}=k$ and if $m \leq 2$, then for all $j=2 \ldots, m$, the number of processes that obtained a set of size $\ell_{j}$ is $\ell_{j}-\ell_{j-1}$. We leave it to the reader to prove this claim (Exercise 2).

Note that the process with the highest input name that obtained the set of size $\ell_{1}$ will output a value. Thus, at most $\ell_{1}-1<k$ processes can recursively call get_name $\left(L \cdot \ell_{1}, s+d\left(2 \ell_{1}-1\right),-d\right)$. If $\ell_{1}>1$, by the induction hypothesis, these at most $\ell_{1}-1$ processes can only get names in the range $\left\{s+d\left(2 \ell_{1}-1\right)-d, \ldots, s+d\left(2 \ell_{1}-1\right)-d\left(2\left(\ell_{1}-1\right)-1\right)\right\}=\left\{s+2 d, \ldots, s+d\left(2 \ell_{1}-2\right)\right\} \subseteq$ $\{s+d, \ldots, s+d(2 k-1)\}$.

Now suppose that $m \geq 2$ and consider $j=2, \ldots, m$. By the algorithm, at most $\ell_{j}-\ell_{j-1}<k$ can recursively call get_name $\left(L \cdot \ell_{j}, s+d\left(2 \ell_{j}-1\right),-d\right)$ which, by the induction hypothesis, can only return names in the range $\left\{s+d\left(2 \ell_{j}-1\right)-d, \ldots, s+d\left(2 \ell_{j}-1\right)-d\left(2\left(\ell_{j}-\ell_{j-1}\right)-1\right)\right\}=\{s+$ $\left.2 \ell_{j-1} d, \ldots, s+d\left(2 \ell_{j}-2\right)\right\}$ which, as $1 \leq \ell_{j-1}<\ell_{j} \leq k$, is a subset of $\{s+d, \ldots, s+d(2 k-1)\}$.

Thus, all outputs are distinct subsets of non-overlapping ranges $\left.\left\{s+2 d, \ldots, s+2 \ell_{1} d-2 d\right)\right\},\{s+$ $\left.2 \ell_{1} d, \ldots, s+2 \ell_{2} d-2 d\right\}, \ldots,\left\{s+2 \ell_{m-1} d, \ldots, s+2 \ell_{m} d-2 d\right\}$, all of which are subsets of $\{s+$ $d, \ldots, s+d(2 k-1)\}$. Hence, all outputs values are distinct and belong to $\{s+d, \ldots, s+d(2 k-1)\}$.

We are finally ready to prove that our algorithm is correct.

Theorem 23 The algorithm in Figure 9.4 solves renaming with $O\left(n^{3}\right)$ read-write step complexity.

Proof Consider any run of the algorithm. By Lemma 12, every correct process returns in $O\left(n^{3}\right)$ stepsthe Termination property holds.

Suppose that $p$ processes participate. Since every process obtains a new name by calling get_name $(\epsilon, 0,1)$, Lemma 13 implies that all output names are distinct and belong to $\{1, \ldots, 2 p-1\}$-the Uniqueness and Name-Adaptivity properties are satisfied. Finally, the algorithm only uses input names and not process identifiers, ensuring the Anonymity property.

### 9.3. Long-lived immediate snapshot

The immediate-snapshot (IS) model is at least as powerful as the classical read-write one. Assuming the full-information protocol (every written value contains the outcome of the most recent update_snapshot () operation), a run the IS model can be represented as a run of the full-information Atomic-Snapshot model. Thus, anything that can be solved in the AS model, can also be solved in the IS one.

In this section, we show that the inverse is also true. We present an algorithm that, in the AS model, simulates a run of IS model.

### 9.3.1. Overview of the algorithm

The idea behind our simulation is to use the one-shot implementation in Figure 9.1 on an unbounded number of floors. Intuitively, each floor corresponds to the total number of write operations a process completed at a given point of a run. For simplicity, we assume that every process maintains a local counter (initially 0 ) that is incremented and used as an argument each time the update_snapshot operation is invoked. The operation returns a view: an array of counter values of all the processes. Every process $p_{i}$ maintains an array $A[i]$ of views, one for each process that can be written by $p_{i}$ and read by all other processes.

In the update_snapshot operation, every process $p_{i}$ first updates a snapshot memory with its current counter valus, takes a snapshot $V$, and for each $p_{j}$, if $V$ contains a more recent value for $p_{j}$, updates the view of $p_{j}$ as seen by $p_{i}, A[i][j]$ with $V$. Then $p_{i}$ computes $V$, the minimal view in $\{A[1], \ldots, A[n]\}$ that stores its most recent value. The starting floor for $p_{i}$ is then computed as the sum of counter values in $V: \sum_{j} V[j]$.

The process then registers its view at level $f$ (line 9.3.1) and, starting from floor $f-1$ downwards, accesses IS instances until it finds a registered view with a previous value of $p_{i}$ that was "seen" by some process in the view obtained from the IS instance at that floor. At this moment, $p_{i}$ returns a view constructed as a "maximum" of the registered view and the result of the IS instance.

### 9.3.2. Proof of correctness

### 9.4. Iterated immediate snapshot

We now consider iterated shared-memory models. In such models, processes communicate via a series of shared memories $M_{1}, M_{2}, \ldots$. A process proceeds in consecutive rounds $1,2, \ldots$, and in each round $i$ it accesses memory $M_{i}$. In this section, we assume that every memory $M_{i}$ is an instance of immediate snapshot, and a process simply applies the update_snapshot() operation to access it.

Iterated immediate snapshot memory (IIS) is of particular interest for us for two reasons. First, IIS is equivalent to the conventional (non-iterated) read-write shared-memory model, as long as we are concerned with solving distributed tasks or designing non-blocking algorithms (Section 9.4.1). Second, it has a very simple geometric representation, enabling a straightforward characterization of computability (Section 9.4.2).

### 9.4.1. An equivalence between IIS and read-write

It is straightforward to implement IIS in the read-write shared memory model using the construction in Section 9.1 for each $M_{i}$ independently.

For the other direction, it is hopeless to look for wait-free implementations of the read-write memory in the IIS model in which every correct process is able to complete each of its operations. Consider a run in which a correct process $p_{i}$ is "left behind" in every IIS iteration and, as a result, it never appears in the view of any other process. No write operation performed by $p_{i}$ in any read-write implementation, based on IIS, will be able to affect read operations performed other processes. Thus, no correct read-write implementation can guarantee that $p_{i}$ completes any of its writes in that run.

However, as we will show now, IIS can simulate read-write memory in a non-blocking way. Recall that a non-blocking implementation guarantees that in an infinite execution at least one process makes progress. We focus on algorithms in which a process may complete its computation and terminate or perform infinitely many reads and writes. Thus, our simulation will guarantee that every correct process either terminates or performs infinitely many (simulated) reads and writes.

We use IIS to implement the read-write model in which memory is organized as a vector of singlewriter multiple-reader registers, and every process alternates updates of its dedicated register with atomic snapshots of the memory. Again, we assume that every process runs the full-information protocol: first
it writes its input value and every subsequent update includes the outcome of the preceding snapshot.

The implementation maintains, at every process $p_{i}$, a local array $c_{i}[1, \ldots, n]$, called a vector clock. Each $c_{i}[j]$ has two components:

- $c_{i}[j]$.clock that contains the number of update operations of $p_{j}$ "witnessed" by $p_{i}$ so far, and
- $c_{i}[j] . v a l$ that contains the most recent value of $p_{j}$ 's vector clock "witnessed" by $p_{i}$ so far.

The simulation, presented in Figure 9.6, works as follows. To perform an update, $p_{i}$ increments $c_{i}[i]$. clock and sets $c_{i}[i]$. clock to be the "most recent" vector clock observed so far. To take a memory snapshot, $p_{i}$ goes through multiple iterations of IIS until the "size" of the currently observed vector clock, $\left|c_{i}\right|=\sum_{j} c_{i}[j] . c l o c k$, gets "large enough". We explain what we mean by "most recent" and "large enough" below.

In every round of our implementation, $p_{i}$ writes its current view of the memory and stores an update of it in a local variable view $=$ view $[1], \ldots$, view $[n]$ (line 3 ). Then for every process $p_{j}, p_{i}$ computes the position

$$
k=\operatorname{argmax}_{\ell} \text { view }[\ell][j] . \text { clock }
$$

and fetches view $[k][j] . v a l$. The resulting vector of the "most recent" values written by the processes is denoted by top (view).

Then $p_{i}$ checks if $|c|=\sum_{j} c[j]$. clock, the sum of clock values of all the processes equals the current round number. Intuitively, the condition that the currently simulated snapshot of $p_{i}$ contains all the most recent written values and relates by containment to the results of all other simulated snapshot operations. Indeed, as the clock values grow monotonically, snapshots $S$ and $S^{\prime}$ produced in IIS rounds $r$ and $r^{\prime}$, $r \leq r^{\prime}$, satisfy $S \leq S^{\prime}$.

Formally, every process $p_{i}$ goes through a number of phases, where phase $k=1,2, \ldots$ starts when $p_{i}$ 's local variable $c_{i}[i]$. clock is assigned value $k$ (line 1 for $k=1$ or line 11 for $k>1$ ). Phase $k$ ends when $p_{i}$ departs after executing line 8 or starts phase $k+1$. The argument of the write operation of phase $k$ is the value of $c[i] . v a l$ initialized at the end of phase $k-1$ in line 10 if $k>1$ and the input value of $p_{i}$ otherwise. The outcome of the $k$-th simulated snapshot operation is chosen to be the last value of $c . v a l$ computed in line 5 of the phase.

```
Shared variables: IS memories $I S_{1}, I S_{2}, \ldots$
Local variables at each $p_{i}: c_{i}[1, \ldots, n]$, initially $[\perp, \ldots, \perp]$
Code for process $p_{i}$ :
(1) $r:=0 ; c[i]$. clock $:=1 ; c_{i}[i]$.val $:=$ input of $p_{i} ; \quad\left\{\right.$ memorize $p_{i}$ 's input $\}$
(2) repeat forever
(3) $\quad r:=r+1$
(4) view $:=I S_{r}$.update_snapshot $(c) \quad\left\{\right.$ update the view using $\left.I S_{r}\right\}$
(5) $\quad c:=$ top $($ view $) \quad\{$ update the clock vector with the most recent information $\}$
(6) $\quad$ if $|c|=r$ then $\quad\{$ if the current snapshot is complete $\}$
(7) if decided (c.val) then $\quad\{$ if ready to decide $\}$
(8) return decision(c.val)
(9) endif
(10) $\quad c_{i}[i]$. val $:=c \quad\{$ compute the next value to write $\}$
(11) $\quad c_{i}[i]$. clock $:=c_{i}[i]$. clock $+1 \quad$ \{update the local clock $\}$
(12) endif
(13) end repeat
```

Figure 9.6.: Implementing AS using IIS

To justify that our simulation is correct, we first prove a few auxiliary lemmas. Let view $w_{i}^{r}$ and $c_{i}^{r}$ denote, respectively, the view and the clock vector evaluated by process $p_{i}$ in round $r$, i.e., in lines 4 and 5, respectively, of the $r$ th iteration of the algorithm. We say that $c_{i}^{r} \leq c_{j}^{r}$ if $\forall k: c_{i}^{r}[k] . c l o c k \leq$ $c_{j}^{r}[k] . c l o c k$, i.e., $c_{i}^{r}$ contains at least as recent perspective on the simulated state as $c_{j}^{r}$. Recall that $\left|c_{i}^{r}\right|=\sum_{j} c_{i}^{r}[k]$. clock

Lemma 14 For all $r \in \mathbb{N}, p_{i}, p_{j} \in \Pi,\left|c_{i}^{r}\right| \leq\left|c_{j}^{r}\right|$ implies $c_{i}^{r} \leq c_{j}^{r}$.

Proof By the Set Inclusion property of IS (see Section 9.1), the views evaluated by $p_{i}$ and $p_{j}$ in line 4 of round $r$ are related by containment, i.e., view ${ }_{i}^{r} \subseteq v i e w_{j}^{r}$ or view ${ }_{j}^{r} \subseteq v i e w_{i}^{r}$. Since $c_{i}^{r}$ and $c_{j}^{r}$ are computed as the vector of the most up-to-date values gathered from the views (line 5), we have $c_{i}^{r} \leq c_{j}^{r}$ or $c_{j}^{r} \leq c_{i}^{r}$.

Suppose, by contradiction that $\left|c_{i}^{r}\right| \leq\left|c_{j}^{r}\right|$ but $c_{i}^{r} \not \leq c_{j}^{r}$, i.e., $c_{j}^{r} \leq c_{i}^{r}$ but $c_{j}^{r} \neq c_{i}^{r}$. Since the operation $|c|$ sums up the values of $c[i]$.clock, we get $\left|c_{j}^{r}\right|>\left|c_{i}^{r}\right|$ —a contradiction. Thus, $\left|c_{i}^{r}\right| \leq\left|c_{j}^{r}\right|$ indeed implies $c_{i}^{r} \leq c_{j}^{r}$.

Since, by Lemma 14, $\left|c_{i}^{r}\right|=\left|c_{j}^{r}\right|$ implies $c_{i}^{r}=c_{j}^{r}$, we have:

Corollary 2 All processes that complete a snapshot operation in round $r$, evaluate the same clock vector $c,|c|=r$.

Lemma 15 For all $r \in \mathbb{N}, p_{i} \in \Pi,\left|c_{i}^{r}\right| \geq r$.

Proof By the Self-Inclusion property of IS, $c_{1}^{1}[i]$. clock $=1$, and, thus, $\left|c_{1}^{1}\right| \geq 1$. Suppose, inductively, that for all $p_{i},\left|c_{i}^{r}\right| \geq r$ for some $r \geq 1$.

Since the view computed by $p_{i}$ in round $r$ is written afterward to $I S_{r+1}$, the values of $\left|c_{i}^{r}\right|$ do not decrease with $r$. Thus, if $\left|c_{i}^{r}\right|>r$, then $\left|c_{i}^{r+1}\right| \geq\left|c_{i}^{r}\right| \geq r+1$. On the other hand, if $\left|c_{i}^{r}\right|=r$, i.e., $p_{i}$ completes its snapshot operation in round $r$, then $p_{i}$ increments $c_{i}[i]$.clock and we have $\left|c_{i}^{r+1}\right|>$ $\left|c_{i}^{r}\right|+1 \geq r+1$. In both cases, $\left|c_{r+1}^{r}\right| \geq r+1$ and the claim follows by induction. $\quad \square_{\text {Lemma } 15}$

The values of $c_{i}^{r}$.clock can only increase with $r$. Thus, by Lemmas 14 and 15 , we have:

Corollary 3 If $\left|c_{i}^{r}\right|=r$ (i.e., $p_{i}$ completes a snapshot operation in round $r$ ), then for all $p_{j}$ and $r^{\prime}>r$, we have $c_{i}^{r} \leq c_{j}^{r^{\prime}}$.

Now we show that some correct process always makes progress in the simulated run. We say that a process terminates once it reaches line 8 . Note that if a process terminates in round $r$, it does not access any $I S_{r^{\prime}}$, for $r^{\prime}>r$.

Lemma 16 For all $r \in \mathbb{N}$, if there is a correct process reaches round $r$, eventually some correct nonterminating process its current phase in round $r^{\prime} \geq r$.

Proof By contradiction, assume that there is an execution in which some correct non-terminated process is in round $r$ and no correct non-terminated process ever completes its current phase, i.e., no process $p_{i}$ ever increases the value of $c_{i}[i]$. clock. Thus, there exists a clock vector $c$ such that $\forall r^{\prime} \geq r, p_{i} \in \Pi$ : $c_{i}^{r^{\prime}}=c$.

By Lemma 15, for all $p_{i}$ and $r^{\prime} \geq r,|c|=\left|c_{i}^{r}\right| \geq r$. Consider round $r^{\prime}=|c| \geq r$. By the assumption, every correct non-terminated process $p_{i}$ evaluates $c_{i}^{r^{\prime}}=c$ and, by the algorithm, terminates in round $r^{\prime}-\mathrm{a}$ contradiction.

Now we are ready to prove correctness of our simulation.

Theorem 24 Every run $R$ simulated by the algorithm in Figure 9.6 is indistinguishable from a run $R_{s}$ of the full information protocol in the AS model in which either every correct (in $R$ ) process terminates or some correct process takes infinitely many steps.

Proof Given $R$, we construct $R_{s}$ as follows. Assuming that $p_{i}$ completes its $k$ th phase in $r$, let $W_{i}^{k}$ and $S_{i}^{k}$ denote, respectively, the corresponding simulated update and snapshot operations. First we order all resulting $S_{i}^{k}$ according to the round numbers in which they were completed. Then we place each $W_{i}^{k}$ just before the first snapshot that contains the $k$ th simulated view of $p_{i}$.

By Corollary 2, all snapshot outcomes produced in the same round are identical. By Corollary 3, snapshot outcomes grow with the round numbers. Thus, in $R_{s}$, every two snapshots are related by containment, and every next snapshot is a copy or a superset of the previous one. Furthermore, the SelfInclusion property of one-shot IS instances used in the algorithm implies that every $S_{i}^{k}$ contains the $k$ th simulated view of $p_{i}$. Thus, in $R_{s}$, every $p_{i}$ executes the operations appear in the order they take place in $R: W_{i}^{1}, S_{i}^{1}, W_{i}^{2}, S_{i}^{2}, \ldots$

By construction, the outcome of every $S_{i}^{r}$ contains the most recent written value for each process.

Now suppose that a given distributed task is solvable in the AS model: in every run, every process eventually reaches a decided state, captured in line 7 of our algorithm.

Assuming, without loss of generality, that a decided process simply stops taking steps, our nonblocking solution brings the next correct process to the output, then the next one, etc., until every correct process outputs. Note that there is no loss of generality in assuming that a process stops after producing an output, since it juts corresponds to the execution in which the process crashes just after deciding.

Therefore, Theorem 24 implies that IIS is equivalent to AS (or, more generally the read-write model) in terms of task solving:

Corollary 4 A task is solvable in IIS if and only if it is solvable in the read-write asynchronous model.

Note that in the above prove is that we do not use the Immediacy property of IS. Thus, the simulation would still be correct even if we replace view $:=I S_{r}$.update_snapshot $(c)$ in line 4 with $A S_{r}$.update (c) followed by view $:=A S_{r} \cdot$ snapshot $(c)$.

### 9.4.2. Geometric representation of IIS

The IIS model allows for a simple geometric representation. All possible runs of one round of IIS can be represented as a standard chromatic subdivision of the $(n-1)$-dimensional simplex.

The example depicted in Figure 9.7 describes the views obtained by three processes, $p_{1}, p_{2}$, and $p_{3}$, after each executes For example, the blue corner of the triangle models the view of $p_{1}$ in a run where it only sees itself. The internal points on the blue-green face model the views of $p_{1}$ and $p_{2}$ in runs where they see each other but miss $p_{3}$. Finally, the internal points of the triangle model the views of the processes in which they see all three. A triangle in the subdivision models the set of views that can be obtained in the same run.

As we can see, the resulting views and runs result in a nice simplicial complex that is simply a subdivision of the triangle corresponding to the initial state of the system. Multiple rounds of the IIS model can thus be represented as an iterated standard chromatic subdivision, where each of the triangles is subdivided, then each of the resulting triangles is subdivided, etc.

Notice that one round of the (full-information) AS model produces runs that do not fit the subdivision depicted in Figure 9.7. For example, the AS model allows a run in which $p_{1}$ only sees itself and $p_{2}$, but both $p_{2}$ and $p_{3}$ see all three processes. In Figure 9.7 this runs corresponds to the triangle formed
by the blue vertex on the face $\left(p_{1}, p_{2}\right)$ and the green and read vertices in the interior that overlaps with other triangles in the subdivision. But since this run does not satisfy the Immediacy property of IS, it is excluded by the IS model.

The fact that one round of the IS model is captured by the subdivision depicted in Figure 9.7 is obvious for three processes. More generally, to model runs of the IIS model in a system of $n$ processes, consider the initial system state $\mathbf{s}$ represented as $(n-1)$-dimensional chromatic simplex $\mathbf{s}$, i.e., a set of $n$ vertices, each vertex corresponding to a distinct process. Chrs is now defined inductively on the dimension of s.

If $\mathbf{s}$ is zero dimensional, which corresponds to a system of only one process, we let $C h r \mathbf{s}=\mathbf{s}$. Suppose now, inductively, that $\mathbf{s}$ has dimension $n-1$, and that we already took the chromatic subdivision of its $(n-2)$-skeleton, i.e., all subsets of size at most $n-1$. Take a new $(n-1)$-simplex $\mathbf{s}^{\prime}$. For each face $\mathbf{t}$ of $\mathbf{s}$, let $\overline{\mathbf{t}}^{\prime}$ be the complementary face of $\mathbf{s}^{\prime}$, that is, the face of $\mathbf{s}^{\prime}$ corresponding to the processes that do not appear in $\mathbf{t}$. Then every simplex consisting of the vertices $\overline{\mathbf{t}}^{\prime}$ and the vertices of any simplex in the chromatic subdivision of $\mathbf{t}$ is added to the resulting simplicial complex Chrs. If we iterate this construction $k$ times we obtain the $k$ th chromatic subdivision, $C h r^{k} C$.

The fact that Chrs is indeed a subdivided simplex was independently shown by Linial [73] and Kozlov $[65]$.

