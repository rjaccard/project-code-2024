# 12. Failure detectors 

As we have seen, only a small set of problems can be solved in an asynchronous fault-prone system. This chapter focuses on failure detectors, a popular abstraction proposed to overcome these impossibilities.

Informally, a failure detector is a distributed oracle that provides processes with hints about failures [20]. The notion of a weakest failure detector [19] captures the exact amount of information about failures needed to solve a given problem: $\mathcal{D}$ is the weakest failure detector for solving $\mathcal{M}$ if (1) $\mathcal{D}$ is sufficient to solve $\mathcal{M}$, i.e., there exists an algorithm that solves $\mathcal{M}$ using $\mathcal{D}$, and (2) any failure detector $\mathcal{D}^{\prime}$ that is sufficient to solve $\mathcal{M}$ provides at least as much information about failures as $\mathcal{D}$ does, i.e., there exists a reduction algorithm that extract the output of $\mathcal{D}$ using the failure information provided by $\mathcal{D}^{\prime}$.

One of the most important results in distributed computing was showing that the "eventual leader" failure detector $\Omega$ is necessary and sufficient to solve consensus. The failure detector $\Omega$ outputs, when queried, a process identifier, such that, eventually, the same correct process identifier is output at all correct processes.

We consider a system of $n$ crash-prone processes that communicate using atomic reads and writes in shared memory. Recall that in the (binary) consensus problem [34], every process starts with a binary input and every correct (never-failing) process is supposed to output one of the inputs such that no two processes output different values. As we know by now, consensus is impossible to solve using reads and writes in the asynchronous system of two or more processes, as long as at least one process may fail by crashing. In particular, it is not possible to solve 2 -process in the wait-free manner.

### 12.1. Solving problems with failure detectors

Until now, we assumed that processes are restricted to apply operations on shared objects. In this chapter, they can also query a failure-detector oracle. But how exactly is this done? An how can we compare failure detectors based on the amount of information about failures they provide?

We first define formally the failure-detector abstraction as a map from a failure pattern (describing the failures that actually took place) to failure-detector histories (describing the hints about failures provided by the failure detector). We then discuss how to solve problems using failure detectors and introduce a partial order on failure detectors that will allow us to define the notion of a weakest failure detector for a given problem.

### 12.1.1. Failure patterns and failure detectors

We assume the existence of a discrete time range $\mathbb{T}=\{0\} \cup \mathbb{N}$. Each event in an execution is supposed to take place in a distinct moment of time. Without loss of generality, and with a little abuse of intuition, we assume that all events in an execution are totally ordered according to the times they occurred.

A failure pattern $F$ is a function from the time range $\mathbb{T}=\{0\} \cup \mathbb{N}$ to $2^{\Pi}$, where $F(t)$ denotes the set of processes that have crashed by time $t$. Once a process crashes, it does not recover, i.e., $\forall t: F(t) \subseteq F(t+1)$. The set of faulty processes in $F, \cup_{t \in \mathbb{T}} F(t)$, is denoted by faulty $\left.F\right)$. Respectively, $\operatorname{correct}(F)=\Pi-$ faulty $(F)$. A process $p \in F(t)$ is said to be crashed at time $t$. An environment is a set of failure patterns. For example, a $t$-resilient environments consists of all failure patterns in which at
most $t$ processes are faulty. Without loss of generality, we assume environments that consists of failure patterns in which at least one process is correct.

A failure detector history $H$ with range $\mathcal{R}$ is a function from $\Pi \times \mathbb{T}$ to $\mathcal{R}$. Here $H\left(p_{i}, t\right)$ is interpreted as the value output by the failure detector module of process $p_{i}$ at time $t$.

Finally, a failure detector $\mathcal{D}$ with range $\mathcal{R}_{\mathcal{D}}$ is a function that maps each failure pattern to a (nonempty) set of failure detector histories with range $\mathcal{R}_{\mathcal{D}} . \mathcal{D}(F)$ denotes the set of possible failure detector histories permitted by $\mathcal{D}$ for failure pattern $F$.

For example, consider the following failure detectors:

- The perfect failure detector $\mathcal{P}$ outputs a set of suspected processes at each process. $\mathcal{P}$ ensures strong completeness: every crashed process is eventually suspected by every correct process, and strong accuracy: no process is suspected before it crashes.

Formally, for each failure pattern $F$, and each history $H \in \mathcal{P}(F) \quad \Leftrightarrow$

$$
\begin{aligned}
& \left(\exists t \in \mathbb{T} \forall p \in \text { faulty }(F) \forall q \in \operatorname{correct}(F) \forall t^{\prime} \geq t: p \in H\left(q, t^{\prime}\right)\right) \wedge \\
& (\forall t \in \mathbb{T} \forall p, q \in \Pi-F(t): p \notin H(q, t))
\end{aligned}
$$

- The eventually perfect failure detector $\diamond \mathcal{P}[20]$ also outputs a set of suspected processes at each process. But the guarantees provided by $\diamond \mathcal{P}$ are weaker than those of $\mathcal{P}$. There is a time after which $\diamond \mathcal{P}$ outputs the set of all faulty processes at every non-faulty process. More precisely, $\diamond \mathcal{P}$ satisfies strong completeness and eventual strong accuracy: there is a time after which no correct process is ever suspected.

Formally, for each failure pattern $F$, and each history $H \in \diamond \mathcal{P}(F) \quad \Leftrightarrow$

$$
\exists t \in \mathbb{T} \forall p \in \operatorname{correct}(F) \forall t^{\prime} \geq t: H\left(p, t^{\prime}\right)=\text { faulty }(F)
$$

- The leader failure detector $\Omega$ [19] outputs the id of a process at each process. There is a time after which it outputs the id of the same non-faulty process at all non-faulty processes.

Formally, for each failure pattern $F$, and each history $H \in \Omega(F) \quad \Leftrightarrow$

$$
\exists t \in \mathbb{T} \exists q \in \operatorname{correct}(F) \forall p \in \operatorname{correct}(F) \forall t^{\prime} \geq t: H\left(p, t^{\prime}\right)=q
$$

- The quorum failure detector $\Sigma$ [27] outputs a set of processes at each process. Any two sets (output at any times and at any processes) intersect, and eventually every set consists of only non-faulty processes.

Formally, for each failure pattern $F$, and each history $H \in \Sigma(F) \quad \Leftrightarrow$

$$
\begin{aligned}
& \left(\forall p, p^{\prime} \in \Pi \forall t, t^{\prime} \in \mathbb{T} H(p, t) \cap H\left(p^{\prime}, t^{\prime}\right) \neq \emptyset\right) \wedge \\
& \left(\forall p \in \operatorname{correct}(F) \exists t \in \mathbb{T} \forall t^{\prime} \geq t H\left(p, t^{\prime}\right) \subseteq \operatorname{correct}(F)\right)
\end{aligned}
$$

### 12.1.2. Algorithms using failure detectors

We now define the notion of an algorithm in systems with failure detectors. Formally, an algorithm $\mathcal{A}$ using a failure detector $\mathcal{D}$ is a collection of deterministic automata, one for each process in the system. Let $\mathcal{A}_{i}$ denote the automaton on which process $p_{i}$ runs the algorithm $\mathcal{A}$. Computation proceeds in atomic steps of $\mathcal{A}$. In each step of $\mathcal{A}$, process $p_{i}$
(i) invokes an atomic operation (read or write) on a shared object and receives a response or queries its failure detector module $\mathcal{D}_{i}$ and receives a value from $\mathcal{D}$, and

(ii) applies its current state, the response received from the shared object or the value output by $\mathcal{D}$ to the automaton $\mathcal{A}_{i}$ to obtain a new state.

A step of $\mathcal{A}$ is thus identified by a tuple $\left(p_{i}, d\right)$, where $d$ is the failure detector value output at $p_{i}$ during that step if $\mathcal{D}$ was queried, and $\perp$ otherwise.

If the state transitions of the automata $\mathcal{A}_{i}$ do not depend on the failure detector values, the algorithm $\mathcal{A}$ is called asynchronous. Thus, for an asynchronous algorithm, a step is uniquely identified by the process id.

### 12.1.3. Runs

A state of algorithm $\mathcal{A}$ defines the state of each process and each object in the system. An initial state $I$ of $\mathcal{A}$ specifies an initial state for every automaton $\mathcal{A}_{i}$ and every shared object.

A run of algorithm $\mathcal{A}$ using a failure detector $\mathcal{D}$ in an environment $\mathcal{E}$ is a tuple $R=\langle F, H, I, S, T\rangle$ where $F \in \mathcal{E}$ is a failure pattern, $H \in \mathcal{D}(F)$ is a failure detector history, $I$ is an initial state of $\mathcal{A}, S$ is an infinite sequence of steps of $\mathcal{A}$ respecting the automata $\mathcal{A}$ and the sequential specification of shared objects, and $T$ is an infinite list of increasing time values indicating when each step of $S$ has occurred, such that for all $k \in \mathbb{N}$, if $S[k]=\left(p_{i}, d\right)$ with $d \neq \perp$, then $p_{i} \notin F(T[k])$ and $d=H\left(p_{i}, T[k]\right)$.

A run $\langle F, H, I, S, T\rangle$ is fair if every process in $\operatorname{correct}(F)$ takes infinitely many steps in $S$, and $k$ resilient if at least $n-k$ processes appear in $S$ infinitely often. A partial run of an algorithm $\mathcal{A}$ is a finite prefix of a run of $\mathcal{A}$.

For two steps $s$ and $s^{\prime}$ of processes $p_{i}$ and $p_{j}$, respectively, in a (partial) run $R$ of an algorithm $\mathcal{A}$, we say that $s$ causally precedes $s^{\prime}$ if in $R$, and we write $s \rightarrow s^{\prime}$, if (1) $p_{i}=p_{j}$, and $s$ occurs before $s^{\prime}$ in $R$, or (2) $s$ is a write step, $s^{\prime}$ is a read step, and $s$ occurs before $s^{\prime}$ in $R$, or (3) there exists $s^{\prime \prime}$ in $R$, such that $s \rightarrow s^{\prime \prime}$ and $s^{\prime \prime} \rightarrow s^{\prime}$.

### 12.1.4. Consensus

Recall that in the binary consensus problem, every process starts the computation with an input value in $\{0,1\}$ (we say the process proposes the value), and eventually reaches a distinct state associated with an output value in $\{0,1\}$ (we say the process decides the value). An algorithm $\mathcal{A}$ solves consensus in an environment $\mathcal{E}$ if in every fair run of $\mathcal{A}$ in $\mathcal{E}$, (i) every correct process eventually decides, (ii) every decided value was previously proposed, and (iii) no two processes decide different values.

Given a an algorithm that solves consensus, it is straightforward to implement an abstraction cons that can be accessed with an operation propose $(v)(v \in\{0,1\})$ returning a value in $\{0,1\}$, and guarantees that every propose operation invoked by a correct process eventually returns, every returned value was previously proposed, and no two different values are ever returned.

### 12.1.5. Implementing and comparing failure detectors

The failure detector abstraction intends to capture the minimal information about failures that suffices to solve a given problem. But what does "minimal" actually mean? Intuitively, it should mean that any failure detector that enables solutions to the problem provides at least as much information about failures. But given that failure detectors can give their hints about failures in arbitrary formats, it becomes necessary to introduce a way to compare different failure detectors. Here we define a notion of reduction
between failure detectors in the algorithmic sense: a failure detector $\mathcal{D}$ provides as much information about failures as failure detector $\mathcal{D}^{\prime}$ if there is an algorithm that uses $\mathcal{D}$ to implements $\mathcal{D}^{\prime}$.

More precisely, an implementation of a failure detector $\mathcal{D}$ in an environment $\mathcal{E}$ provides a query operation to every process that, when invoked, returns a value in $\mathcal{R}_{\mathcal{D}}$. It is required that in every run of the implementation with a failure pattern $F \in \mathcal{E}$, there exists a history $H \in \mathcal{D}(F)$ such that, for all times $t_{1}, t_{2} \in \mathbb{N}$, if process $p_{i}$ queries $\mathcal{D}$ at time $t_{1}$ and the query returns response $d$ at time $t_{2}$, then $d=H\left(p_{i}, t\right)$ for some $t \in\left[t_{1}, t_{2}\right]$.

If, for failure detectors $\mathcal{D}$ and $\mathcal{D}^{\prime}$ and an environment $\mathcal{E}$, there is an implementation of $\mathcal{D}$ using $\mathcal{D}^{\prime}$ in $\mathcal{E}$, then we say that $\mathcal{D}$ is weaker than $\mathcal{D}^{\prime}$ in $\mathcal{E}$.

### 12.1.6. Weakest failure detector

Finally, we are ready to define the notion of $a$ weakest failure detector for solving a given problem (in this section this problem is going to be consensus).

$\mathcal{D}$ is a weakest failure detector to solve a problem $\mathcal{M}$ (e.g., consensus) in $\mathcal{E}$ if there is an algorithm that solves $\mathcal{M}$ using $\mathcal{D}$ in $\mathcal{E}$ and $\mathcal{D}$ is weaker than any failure detector that can be used to solve $\mathcal{M}$ in $\mathcal{E}$.

### 12.2. Extracting $\Omega$

Let $\mathcal{A}$ be an algorithm that solves consensus using a failure detector $\mathcal{D}$. The goal is to construct an algorithm that emulates $\Omega$ using $\mathcal{A}$ and $\mathcal{D}$. Recall that to emulate $\Omega$ means to output, at each time and at each process, a process identifiers such that, eventually, the same correct process is always output.

### 12.2.1. Overview of the Reduction Algorithm

Our reduction algorithm uses the given failure detector $\mathcal{D}$ to construct an ever-growing directed acyclic graph (DAG) that contains a sample of the values output by $\mathcal{D}$ in the current run and captures some temporal relations between them. This DAG can be used by an asynchronous algorithm $\mathcal{A}^{\prime}$ to simulate a (possibly finite and "unfair") run of $\mathcal{A}$. In particular, since the original algorithm $\mathcal{A}$ solves consensus, no two processes can decide differently in a run of $\mathcal{A}^{\prime}$.

Recall that, using BG-simulation, 2 processes can simulate a 1-resilient run of $\mathcal{A}^{\prime}$. The fact that waitfree 2-process consensus is impossible implies that the simulation, when used for all possible inputs provided to the two simulatore, must produce at least one "non-deciding" 1 -resilient run of $\mathcal{A}^{\prime}$, i.e., in at least one simulated 1-resilient run of $\mathcal{A}^{\prime}$ some process takes infinitely many steps without deciding.

In the reduction algorithm, every correct process locally simulates all executions of BG-simulation on two processes $q_{1}$ and $q_{2}$ that simulate a 1-resilient run of $\mathcal{A}^{\prime}$ of the whole system $\Pi$. Eventually, every correct process locates a never-deciding run of $\mathcal{A}^{\prime}$ and uses the run to extract the output of $\Omega$ : it is sufficient to output the process that takes the least number of steps in the "smallest" non-deciding simulated run of $\mathcal{A}^{\prime}$. Indeed, exactly one correct process takes finitely many steps in the non-deciding 1-resilient run of $\mathcal{A}^{\prime}$ : otherwise, the run would simulate a fair and thus deciding run of $\mathcal{A}$.

The reduction algorithm extracting $\Omega$ from $\mathcal{A}$ and $\mathcal{D}$ consists of two components that are running in parallel: the communication component and the computation component. In the communication component, every process $p_{i}$ maintains the ever-growing directed acyclic graph (DAG) $G_{i}$ by periodically querying its failure detector module and exchanging the results with the others through the shared memory. In the computation component, every process simulates a set of runs of $\mathcal{A}$ using the DAGs and maintains the extracted output of $\Omega$.

```
Shared variables:
    for all $p_{i} \in \Pi: G_{i}$, initially empty graph
$k_{i}:=0$
while true do
    for all $p_{j} \in \Pi$ do $G_{i} \leftarrow G_{i} \cup G_{j}$
    $d_{i}:=$ query failure detector $\mathcal{D}$
    $k_{i}:=k_{i}+1$
    add $\left[p_{i}, d_{i}, k_{i}\right]$ and edges from all other vertices
        of $G_{i}$ to $\left[p_{i}, d_{i}, k_{i}\right]$, to $G_{i}$
```

Figure 12.1.: Building a DAG: the code for each process $p_{i}$

### 12.2.2. DAGs

The communication component is presented in Figure 12.1. This task maintains an ever-growing DAG that contains a finite sample of the current failure detector history. The DAG is stored in a register $G_{i}$ which can be updated by $p_{i}$ and read by all processes.

DAG $G_{i}$ has some special properties which follow from its construction [19]. Let $F$ be the current failure pattern, and $H \in \mathcal{D}(F)$ be the current failure detector history. Then a fair run of the algorithm in Figure 12.1 guarantees that there exists a map $\tau: \Pi \times \mathcal{R}_{\mathcal{D}} \times \mathbb{N} \mapsto \mathbb{T}$, such that, for every correct process $p_{i}$ and every time $t(x(t)$ denotes here the value of variable $x$ at time $t)$ :

(1) The vertices of $G_{i}(t)$ are of the form $\left[p_{j}, d, \ell\right]$ where $p_{j} \in \Pi, d \in \mathcal{R}_{\mathcal{D}}$ and $\ell \in \mathbb{N}$.

(a) For each vertex $v=\left[p_{j}, d, \ell\right], p_{j} \notin F(\tau(v))$ and $d=H\left(p_{j}, \tau(v)\right)$. That is, $d$ is the value output by $p_{j}$ 's failure detector module at time $\tau(v)$.

(b) For each edge $\left(v, v^{\prime}\right), \tau(v)<\tau\left(v^{\prime}\right)$. That is, any edge in $G_{i}$ reflects the temporal order in which the failure detector values are output.

(2) If $v=\left[p_{j}, d, \ell\right]$ and $v^{\prime}=\left[p_{j}, d^{\prime}, \ell^{\prime}\right]$ are vertices of $G_{i}(t)$ and $\ell<\ell^{\prime}$ then $\left(v, v^{\prime}\right)$ is an edge of $G_{i}(t)$

(3) $G_{i}(t)$ is transitively closed: if $\left(v, v^{\prime}\right)$ and $\left(v^{\prime}, v^{\prime \prime}\right)$ are edges of $G_{i}(t)$, then $\left(v, v^{\prime \prime}\right)$ is also an edge of $G_{i}(t)$.

(4) For all correct processes $p_{j}$, there is a time $t^{\prime} \geq t$, a $d \in \mathcal{R}_{\mathcal{D}}$ and a $\ell \in \mathbb{N}$ such that, for every vertex $v$ of $G_{i}(t),\left(v,\left[p_{j}, d, \ell\right]\right)$ is an edge of $G_{i}\left(t^{\prime}\right)$.

(5) For all correct processes $p_{j}$, there is a time $t^{\prime} \geq t$ such that $G_{i}(t)$ is a subgraph of $G_{j}\left(t^{\prime}\right)$.

The properties imply that ever-growing DAGs at correct processes tend to the same infinite DAG $G$ : $\lim _{t \rightarrow \infty} G_{i}(t)=G$. In a fair run of the algorithm in Figure 12.1, the set of processes that obtain infinitely many vertices in $G$ is the set of correct processes [19].

### 12.2.3. Asynchronous simulation

It is shown below that any infinite DAG $G$ constructed as shown in Figure 12.1 can be used to simulate partial runs of $\mathcal{A}$ in the asynchronous manner: instead of querying $\mathcal{D}$, the simulation algorithm $\mathcal{A}^{\prime}$ uses the samples of the failure detector output captured in the DAG. The pseudo-code of this simulation is presented in Figure 12.2. The algorithm is hypothetical in the sense that it uses an infinite input, but this requirement is relaxed later.

```
Shared variables:
    $V_{1}, \ldots, V_{n}:=\perp, \ldots, \perp$
        $\left\{\right.$ for each $p_{j}, V_{j}$ is the vertex of $G$
        corresponding to the latest simulated step of $\left.p_{j}\right\}$
    Shared variables of $\mathcal{A}$
initialize the simulated state of $p_{i}$ in $\mathcal{A}$, based on $I^{\prime}$
$\ell:=0$
while true do
    $\left\{\right.$ Simulating the next $p_{i}$ 's step of $\left.\mathcal{A}\right\}$
    $U:=\left[V_{1}, \ldots, V_{n}\right]$
    repeat
        $\ell:=\ell+1$
        wait until $G$ includes $\left[p_{i}, d, \ell\right]$ for some $d$
    until $\forall j, U[j] \neq \perp:\left(U[j],\left[p_{i}, d, \ell\right]\right) \in G$
    $V_{i}:=\left[p_{i}, d, \ell\right]$
    take the next $p_{i}$ 's step of $\mathcal{A}$ using $d$ as the output of $\mathcal{D}$
```

Figure 12.2.: DAG-based asynchronous algorithm $\mathcal{A}^{\prime}$ : code for each $p_{i}$

In the algorithm, each process $p_{i}$ is initially associated with an initial state of $\mathcal{A}$ and performs a sequence of simulated steps of $\mathcal{A}$. Every process $p_{i}$ maintains a shared register $V_{i}$ that stores the vertex of $G$ used for the most recent step of $\mathcal{A}$ simulated by $p_{i}$. Each time $p_{i}$ is about to perform a step of $\mathcal{A}$ it first reads registers $V_{1}, \ldots, V_{n}$ to obtain the vertexes of $G$ used by processes $p_{1}, \ldots, p_{n}$ for simulating the most recent causally preceding steps of $\mathcal{A}$ (line 37 in Figure 12.2). Then $p_{i}$ selects the next vertex of $G$ that succeeds all vertices (lines 82-91). If no such vertex is found, $p_{i}$ blocks forever (line 40).

Note that a correct process $p_{i}$ may block forever if $G$ contains only finitely many vertices of $p_{i}$. As a result an infinite run of $\mathcal{A}^{\prime}$ may simulate an unfair run of $\mathcal{A}$ : a run in which some correct process takes only finitely many steps. But every finite run simulated by $\mathcal{A}^{\prime}$ is a partial run of $\mathcal{A}$.

Theorem 34 Let $G$ be the DAG produced in a fair run $R=\langle F, H, I, S, T\rangle$ of the communication component in Figure 12.1. Let $R^{\prime}=\left\langle F^{\prime}, H^{\prime}, I^{\prime}, S^{\prime}, T^{\prime}\right\rangle$ be any fair run of $\mathcal{A}^{\prime}$ using $G$. Then the sequence of steps simulated by $\mathcal{A}^{\prime}$ in $R^{\prime}$ belongs to a (possibly unfair) run of $\mathcal{A}, R_{\mathcal{A}}$, with input vector of $I^{\prime}$ and failure pattern $F$. Moreover, the set of processes that take infinitely many steps in $\mathcal{R}_{\mathcal{A}}$ is $\operatorname{correct}(F) \cap \operatorname{correct}\left(F^{\prime}\right)$, and if $\operatorname{correct}(F) \subseteq \operatorname{correct}\left(F^{\prime}\right)$, then $R_{\mathcal{A}}$ is fair.

Proof Recall that a step of a process $p_{i}$ can be either a memory step in which $p_{i}$ accesses shared memory or a query step in which $p_{i}$ queries the failure detector. Since memory steps simulated in $\mathcal{A}^{\prime}$ are performed as in $\mathcal{A}$, to show that algorithm $\mathcal{A}^{\prime}$ indeed simulates a run of $\mathcal{A}$ with failure pattern $F$, it is enough to make sure that the sequence of simulated query steps in the simulated run (using vertices of $G$ ) could have been observed in a run $R_{\mathcal{A}}$ of $\mathcal{A}$ with failure pattern $F$ and the input vector based on $I^{\prime}$.

Let $\tau$ be a map associated with $G$ that carries each vertex of $G$ to an element in $\mathbb{T}$ such that (a) for any vertex $v=[p, d, \ell]$ of $G, p \notin F(\tau(v))$ and $d=H\left(p_{j}, \tau(v)\right)$, and (b) for every edge $\left(v, v^{\prime}\right)$ of $G$, $\tau(v)<\tau\left(v^{\prime}\right)$ (the existence of $\tau$ is established by property (5) of DAGs in Section 12.2.2). For each step $s$ simulated by $\mathcal{A}^{\prime}$ in $\mathcal{R}^{\prime}$, let $\tau^{\prime}(s)$ denote time when step $s$ occurred in $\mathcal{R}^{\prime}$, i.e., when the corresponding line 43 in Figure 12.2 was executed, and $v(s)$ be the vertex of $G$ used for simulating $s$, i.e., the value of $V_{i}$ when $p_{i}$ simulates $s$ in line 43 of Figure 12.2.

Consider query steps $s_{i}$ and $s_{j}$ simulated by processes $p_{i}$ and $p_{j}$, respectively. Let $v\left(s_{i}\right)=\left[p_{i}, d_{i}, \ell\right]$ and $v\left(s_{j}\right)=\left[p_{j}, d_{j}, m\right]$. WLOG, suppose that $\tau\left(\left[p_{i}, d_{i}, \ell\right]\right)<\tau\left(\left[p_{j}, d_{j}, m\right]\right)$, i.e., $\mathcal{D}$ outputs $d_{i}$ at $p_{i}$ before outputting $d_{j}$ at $p_{j}$.

If $\tau^{\prime}\left(s_{i}\right)<\tau^{\prime}\left(s_{j}\right)$, i.e., $s_{i}$ is simulated by $p_{i}$ before $s_{j}$ is simulated by $p_{j}$, then the order in which $s_{i}$ and $s_{j}$ see value $d_{i}$ and $d_{j}$ is the run produced by $\mathcal{A}^{\prime}$ is consistent with the output of $\mathcal{D}$, i.e., the values $d_{i}$ and $d_{j}$ indeed could have been observed in that order.

Suppose now that $\tau^{\prime}\left(s_{i}\right)>\tau^{\prime}\left(s_{j}\right)$. If $s_{i}$ and $s_{j}$ are not causally related in the simulated run, then $R^{\prime}$ is indistinguishable from a run in which $s_{i}$ is simulated by $p_{i}$ before $s_{j}$ is simulated by $p_{j}$. Thus, $s_{i}$ and $s_{j}$ can still be observed in a run of $A$.

Now suppose, by contradiction that $\tau^{\prime}\left(s_{i}\right)>\tau^{\prime}\left(s_{j}\right)$ and $s_{j}$ causally precedes $s_{i}$ in the simulated run, i.e., $p_{j}$ simulated at least one write step $s_{j}^{\prime}$ after $s_{j}$, and $p_{i}$ simulated at least one read step $s_{i}^{\prime}$ before $s_{i}$, such that $s_{j}^{\prime}$ took place before $s_{i}^{\prime}$ in $R^{\prime}$. Since before performing the memory access of $s_{j}^{\prime}, p_{j}$ updated $V_{j}$ with a vertex $v\left(s_{j}^{\prime}\right)$ that succeeds $v\left(s_{j}\right)$ in $G$ (line 42), and $s_{i}^{\prime}$ occurs in $R^{\prime}$ after $s_{j}^{\prime}, p_{i}$ must have found $v\left(s_{j}^{\prime}\right)$ or a later vertex of $p_{j}$ in $V_{j}$ before simulating step $s_{i}$ (line 37) and, thus, the vertex of $G$ used for simulating $s_{i}$ must be a descendant of $\left[p_{j}, d_{j}, m\right]$, and, by properties (1) and (3) of DAGs (Section 12.2.2), $\tau\left(\left[p_{i}, d_{i}, \ell\right]\right)>\tau\left(\left[p_{j}, d_{j}, m\right]\right)$ — a contradiction. Hence, the sequence of steps of $\mathcal{A}$ simulated in $R^{\prime}$ could have been observed in a run $R_{\mathcal{A}}$ of $\mathcal{A}$ with failure pattern $F$.

Since in $\mathcal{A}^{\prime}$, a process simulates only its own steps of $\mathcal{A}$, every process that appears infinitely often in $R_{\mathcal{A}}$ is in $\operatorname{correct}\left(F^{\prime}\right)$. Also, since each faulty in $F$ process contains only finitely many vertices in $G$, eventually, each process in $\operatorname{correct}\left(F^{\prime}\right)-\operatorname{correct}(F)$ is blocked in line 40 in Figure 12.2, and, thus, every process that appears infinitely often in $R_{\mathcal{A}}$ is also in $\operatorname{correct}(F)$. Now consider a process $p_{i} \in \operatorname{correct}\left(F^{\prime}\right) \cap \operatorname{correct}(F)$. Property (4) of DAGs implies that for every set $V$ of vertices of $G$, there exists a vertex of $p_{i}$ in $G$ such that for all $v^{\prime} \in V,\left(v^{\prime}, v\right)$ is an edge in $G$. Thus, the wait statement in line 40 cannot block $p_{i}$ forever, and $p_{i}$ takes infinitely many steps in $R_{\mathcal{A}}$.

Hence, the set of processes that appear infinitely often in $R_{\mathcal{A}}$ is exactly $\operatorname{correct}\left(F^{\prime}\right) \cap \operatorname{correct}(F)$. Specifically, if $\operatorname{correct}(F) \subseteq \operatorname{correct}\left(F^{\prime}\right)$, then the set of processes that appear infinitely often in $R_{\mathcal{A}}$ is $\operatorname{correct}(F)$, and the run is fair.

Note that in a fair run, the properties of the algorithm in Figure 12.2 remain the same if the infinite DAG $G$ is replaced with a finite ever-growing DAG $\bar{G}$ constructed in parallel (Figure 12.1) such that $\lim _{t \rightarrow \infty} \bar{G}=G$. This is because such a replacement only affects the wait statement in line 40 which blocks $p_{i}$ until the first vertex of $p_{i}$ that causally succeeds every simulated step recently "witnessed" by $p_{i}$ is found in $G$, but this cannot take forever if $p_{i}$ is correct (properties (4) and (5) of DAGs in Section 12.2.2). The wait blocks forever if the vertex is absent in $G$, which may happen only if $p_{i}$ is faulty.

### 12.2.4. BG-simulation

Borowsky and Gafni proposed in $[13,15]$, a simulation technique by which $k+1$ simulators $q_{1}, \ldots, q_{k+1}$ can wait-free simulate a $k$-resilient execution of any asynchronous $n$-process protocol. Informally, the simulation works as follows. Every process $q_{i}$ tries to simulate steps of all $n$ processes $p_{1}, \ldots, p_{n}$ in a round-robin fashion. Simulators run an agreement protocol to make sure that every step is simulated at most once. Simulating a step of a given process may block forever if and only if some simulator has crashed in the middle of the corresponding agreement protocol. Thus, even if $k$ out of $k+1$ simulators crash, at least $n-k$ simulated processes can still make progress. The simulation thus guarantees at least $n-k$ processes in $\left\{p_{1}, \ldots, p_{n}\right\}$ accept infinitely many simulated steps.

In the computational component of the reduction algorithm, the BG-simulation technique is used as follows. Let $B G\left(\mathcal{A}^{\prime}\right)$ denote the simulation protocol for 2 processes $q_{1}$ and $q_{2}$ which allows them to
simulate, in a wait-free manner, a 1-resilient execution of algorithm $\mathcal{A}^{\prime}$ for $n$ processes $p_{1}, \ldots, p_{n}$. The complete reduction algorithm thus employs a triple simulation: every process $p_{i}$ simulates multiple runs of two processes $q_{1}$ and $q_{2}$ that use $\mathrm{BG}$-simulation to produce a 1-resilient run of $\mathcal{A}^{\prime}$ on processes $p_{1}^{\prime}, \ldots, p_{n}^{\prime}$ in which steps of the original algorithm $\mathcal{A}$ are periodically simulated using (ever-growing) DAGs $G_{1}, \ldots, G_{n}$. (To avoid confusion, we use $p_{j}^{\prime}$ to denote the process that models $p_{j}$ in a run of $\mathcal{A}^{\prime}$ simulated by a "real" process $p_{i}$.)

```
$r:=0$
repeat
    $r:=r+1$
    if $G$ contains $\left[p_{i}, d, \ell\right]$ for some $d$ then $u:=1$
    else $u:=0$
    $v:=$ cons $_{r}^{i, \ell} \cdot$ propose $(u)$
until $v=1$
```

Figure 12.3.: Expanded line 40 of Figure 12.2: waiting until $G$ includes a vertex $\left[p_{i}, d, \ell\right]$ for some $d$. Here $G$ is any DAG generated by the algorithm in Figure 12.1.

We are going to use the following property which is trivially satified by BG-simulation:

(BG0) A run of BG-simulation in which every simulator take infinitely many steps simulates a run in which every simulated process takes infinitely many steps.

### 12.2.5. Using consensus

The triple simulation we are going to employ faces one complication though. The simulated runs of the asynchronous algorithm $\mathcal{A}^{\prime}$ may vary depending on which process the simulation is running. This is because $G_{1}, \ldots, G_{n}$ are maintained by a parallel computation component (Figure 12.1), and a process simulating a step of $\mathcal{A}^{\prime}$ may perform a different number of cycles reading the current version of its DAG before a vertex with desired properties is located (line 40 in Figure 12.2). Thus, the same sequence of steps of $q_{1}$ and $q_{2}$ simulated at different processes may result in different 1-resilient runs of $\mathcal{A}^{\prime}$ : waiting until a vertex $\left[p_{i}, d, \ell\right]$ appears in $G_{j}$ at process $p_{j}$ may take different number of local steps checking $G_{j}$, depending on the time when $p_{j}$ executes the wait statement in line 40 of Figure 12.2.

To resolve this issue, the wait statement is implemented using a series of consensus instances cons ${ }_{1}^{i, \ell}$, cons $_{2}^{i, \ell}, \ldots$ (Figure 12.3). If $p_{i}$ is correct, then eventually each correct process will have a vertex $\left[p_{i}, d, \ell\right]$ in its DAG and, thus, the code in Figure 12.3 is non-blocking, and Theorem 34 still holds. Furthermore, the use of consensus ensures that if a process, while simulating a step of $\mathcal{A}^{\prime}$ at process $p_{i}$, went through $r$ steps before reaching line 91 in Figure 12.2, then every process simulating this very step does the same. Thus, a given sequence of steps of $q_{1}$ and $q_{2}$ will result in the same simulated 1-resilient run of $\mathcal{A}^{\prime}$, regardless of when and where the simulation is taking place.

### 12.2.6. Extracting $\Omega$

The computational component of the reduction algorithm is presented in Figure 12.4. In the component, every process $p_{i}$ locally simulates multiple runs of a system of 2 processes $q_{1}$ and $q_{2}$ that run algorithm $B G\left(\mathcal{A}^{\prime}\right)$, to produce a 1-resilient run of $\mathcal{A}^{\prime}$ (Figures 12.2 and 12.3). Recall that $\mathcal{A}^{\prime}$, in its turn, simulates a run of the original algorithm $\mathcal{A}$, using, instead of $\mathcal{D}$, the values provided by an ever-growing DAG $G$. In simulating the part of $\mathcal{A}^{\prime}$ of process $p_{i}^{\prime}$ presented in Figure 12.3, $q_{1}$ and $q_{2}$ count each access of a consensus instance cons $r_{r}^{i, \ell}$ as one local step of $p_{i}^{\prime}$ that need to be simulated. Also, in $B G\left(\mathcal{A}^{\prime}\right)$, when $q_{j}$ is about to simulate the first step of $p_{i}^{\prime}, q_{j}$ uses its own input value as an input value of $p_{i}^{\prime}$.

```
for all binary 2 -vectors $J_{0}$ do
            $\left\{\right.$ For all possible consensus inputs for $q_{1}$ and $\left.q_{2}\right\}$
        $\sigma_{0}:=$ the empty string
        explore $\left(J_{0}, \sigma_{0}\right)$
    function $\operatorname{explore}(J, \sigma)$
        for all $q_{j}=q_{1}, q_{2}$ do
            $\rho:=$ empty string
            repeat
                    $\rho:=\rho \cdot q_{j}$
                    let $p_{\ell}^{\prime}$ be the process that appears the least in $S C H_{\mathcal{A}^{\prime}}(J, \sigma \cdot \rho)$
                    $\Omega$-output $:=p_{\ell}$
            until $S T_{\mathcal{A}}(J, \sigma \cdot \rho)$ is decided
        explore $\left(J, \sigma \cdot q_{1}\right)$
        explore $\left(J, \sigma \cdot q_{2}\right)$
```

Figure 12.4.: Computational component of the reduction algorithm: code for each process $p_{i}$. Here $S T_{\mathcal{A}}(J, \sigma)$ denotes the state of $\mathcal{A}$ reached by the partial run of $\mathcal{A}^{\prime}$ simulated in the partial run of $B G\left(\mathcal{A}^{\prime}\right)$ with schedule $\sigma$ and input state $J$, and $S C H_{\mathcal{A}^{\prime}}(J, \sigma)$ denotes the corresponding schedule of $\mathcal{A}^{\prime}$.

For each simulated state $S$ of $B G\left(\mathcal{A}^{\prime}\right), p_{i}$ periodically checks whether the state of $\mathcal{A}$ in $S$ is deciding, i.e., whether some process has decided in the state of $\mathcal{A}$ in $S$. As we show, eventually, the same infinite non-deciding 1 -resilient run of $\mathcal{A}^{\prime}$ will be simulated by all processes, which allows for extracting the output of $\Omega$.

The algorithm in Figure 12.4 explores solo extensions of $q_{1}$ and $q_{2}$ starting from growing prefixes. Since, by property (BG0) of BG-simulation (Section 12.2.4), a run of $B G\left(\mathcal{A}^{\prime}\right)$ in which both $q_{1}$ and $q_{2}$ participate infinitely often simulates a run of $\mathcal{A}^{\prime}$ in which every $p_{j} \in\left\{p_{1}^{\prime}, \ldots, p_{n}^{\prime}\right.$ participates infinitely often, and, by Theorem 34, such a run will produce a fair and thus deciding run of $\mathcal{A}$. Thus, if there is an infinite non-deciding run simulated by the algorithm in Figure 12.2, it must be a run produced by a solo extension of $q_{1}$ or $q_{2}$ starting from some finite prefix.

Lemma 23 The algorithm in Figure 12.4 eventually forever executes lines 50-54.

Proof Consider any run of the algorithm in Figures 12.1, 12.3 and 12.4. Let $F$ be the failure pattern of that run. Let $G$ be the infinite limit DAG approximated by the algorithm in Figure 12.1. By contradiction, suppose that lines 50-54 in Figure 12.4 never block $p_{i}$.

Suppose that for some initial $J_{0}$, the call of $\operatorname{explore}\left(J_{0}, \sigma_{0}\right)$ performed by $p_{i}$ in line 46 never returns. Since the cycle in lines 50-54 in Figure 12.4 always terminates, there is an infinite sequence of recursive calls explore $\left(J_{0}, \sigma_{0}\right)$, explore $\left(J_{0}, \sigma_{1}\right)$, explore $\left(J_{0}, \sigma_{2}\right), \ldots$, where each $\sigma_{\ell}$ is a one-step extension of $\sigma_{\ell-1}$. Thus, there exists an infinite never deciding schedule $\tilde{\sigma}$ such that the run of $B G\left(\mathcal{A}^{\prime}\right)$ based on $\tilde{\sigma}$ and $J_{0}$ produces a never-deciding run of $\mathcal{A}^{\prime}$. Suppose that both $q_{1}$ and $q_{2}$ appear in $\tilde{\sigma}$ infinitely often. By property (BG0) of BG-simulation (Section 12.2.4), a run of $B G\left(\mathcal{A}^{\prime}\right)$ in which both $q_{1}$ and $q_{2}$ participate infinitely often simulates a run of $\mathcal{A}^{\prime}$ in which every $p_{j} \in\left\{p_{1}^{\prime}, \ldots, p_{n}^{\prime}\right\}$ participates infinitely often, and, by Theorem 34, such a run will produce a fair and thus deciding run of $\mathcal{A}$ - a contradiction.

Thus, if there is an infinite non-deciding run simulated by the algorithm in Figure 12.2, it must be a run produced by a solo extension of $q_{1}$ or $q_{2}$ starting from some finite prefix. Let $\bar{\sigma}$ be the first such prefix in the order defined by the algorithm in Figure 12.2 and $q_{\ell}$ be the first process whose solo extension of
$\sigma$ is never deciding. Since the cycle in lines 50-54 always terminates, the recursive exploration of finite prefixes $\sigma$ in lines 55 and 56 eventually reaches $\bar{\sigma}$, the algorithm reaches line 49 with $\sigma=\bar{\sigma}$ and $q_{j}=q_{\ell}$. Then the succeeding cycle in lines 50-54 never terminates - a contradiction.

Thus, for all inputs $J_{0}$, the call of $\operatorname{explore}\left(J_{0}, \sigma_{0}\right)$ performed by $p_{i}$ in line 46 returns. Hence, for every finite prefix $\sigma$, any solo extension of $\sigma$ produces a finite deciding run of $\mathcal{A}$. We establish a contradiction, by deriving a wait-free algorithm that solves consensus among $q_{1}$ and $q_{2}$.

Let $\tilde{G}$ be the infinite limit DAG constructed in Figure 12.1. Let $\beta$ be a map from vertices of $\tilde{G}$ to $\mathbb{N}$ defined as follows: for each vertex $\left[p_{i}, d, \ell\right]$ in $G, \beta\left(\left[p_{i}, d, \ell\right]\right)$ is the value of variable $r$ at the moment when any run of $\mathcal{A}^{\prime}$ (produced by the algorithm in Figure 12.2) exits the cycle in Figure 12.3, while waiting until $\left[p_{i}, d, \ell\right]$ appears in $G$. If there is no such run, $\beta\left(\left[p_{i}, d, \ell\right]\right)$ is set to 0 . Note that the use of consensus implies that if in any simulated run of $\mathcal{A}^{\prime},\left[p_{i}, d, \ell\right]$ has been found after $r$ iterations, then $\beta\left(\left[p_{i}, d, \ell\right]\right)=r$, i.e., $\beta$ is well-defined.

Now we consider an asynchronous read-write algorithm $\mathcal{A}_{\beta}^{\prime}$ that is defined exactly like $\mathcal{A}^{\prime}$, but instead of going through the consensus invocations in Figure 12.3, $\mathcal{A}_{\beta}^{\prime}$ performs $\beta\left(\left[p_{i}, d, \ell\right]\right)$ local steps. Now consider the algorithm $B G\left(\mathcal{A}_{\beta}^{\prime}\right)$ that is defined exactly as $B G\left(\mathcal{A}^{\prime}\right)$ except that in $B G\left(\mathcal{A}_{\beta}^{\prime}\right), q_{1}$ and $q_{2}$ BG-simulate runs of $\mathcal{A}_{\beta}^{\prime}$. For every sequence $\sigma$ of steps of $q_{1}$ and $q_{2}$, the runs of $B G\left(\mathcal{A}^{\prime}\right)$ and $B G\left(\mathcal{A}_{\beta}^{\prime}\right)$ agree on the sequence of steps of $p_{1}^{\prime}, \ldots, p_{n}^{\prime}$ in the corresponding runs of $\mathcal{A}^{\prime}$ and $\mathcal{A}_{\beta}^{\prime}$, respectively. Moreover, they agree on the runs of $\mathcal{A}$ resulting from these runs of $\mathcal{A}^{\prime}$ and $\mathcal{A}_{\beta}^{\prime}$. This is because the difference between $\mathcal{A}^{\prime}$ and $\mathcal{A}_{\beta}^{\prime}$ consist only in the local steps and does not affect the simulated state of $\mathcal{A}$.

We say that a sequence $\sigma$ of steps of $q_{1}$ and $q_{2}$ is deciding with $J_{0}$, if, when started with $J_{0}$, the run of $B G\left(\mathcal{A}_{\beta}^{\prime}\right)$ produces a deciding run of $\mathcal{A}$. By our hypothesis, every eventually solo schedule $\sigma$ is deciding for each input $J_{0}$. As we showed above, every schedule in which both $q_{1}$ and $q_{2}$ appear sufficiently often is deciding by property (BG0) of BG-simulation. Thus, every schedule of $B G\left(\mathcal{A}_{\beta}^{\prime}\right)$ is deciding for all inputs.

Consider the trees of all deciding schedules of $B G\left(\mathcal{A}_{\beta}^{\prime}\right)$ for all possible inputs $J_{0}$. All these trees have finite branching (each vertex has at most 2 descendants) and finite paths. By König's lemma, the trees are finite. Thus, the set of vertices of $\tilde{G}$ used by the runs of $\mathcal{A}^{\prime}$ simulated by deciding schedules of $B G\left(\mathcal{A}_{\beta}^{\prime}\right)$ is also finite. Let $\bar{G}$ be a finite subgraph of $\tilde{G}$ that includes all vertices of $\tilde{G}$ used by these runs.

Finally, we obtain a wait-free consensus algorithm for $q_{1}$ and $q_{2}$ that works as follows. Each $q_{j}$ runs $B G\left(\mathcal{A}_{\beta}^{\prime}\right)$ (using a finite graph $\left.\bar{G}\right)$ until a decision is obtained in the simulated run of $\mathcal{A}$. At this point, $q_{j}$ returns the decided value. But $B G\left(\mathcal{A}_{\beta}^{\prime}\right)$ produces only deciding runs of $\mathcal{A}$, and each deciding run of $\mathcal{A}$ solves consensus for inputs provided by $q_{1}$ and $q_{2}$ - a contradiction.

Theorem 35 In all environments $\mathcal{E}$, if a failure detector $\mathcal{D}$ can be used to solve consensus in $\mathcal{E}$, then $\Omega$ is weaker than $\mathcal{D}$ in $\mathcal{E}$.

Proof Consider any run of the algorithm in Figures 12.1, 12.3 and 12.4 with failure pattern $F$.

By Lemma 23, at some point, every correct process $p_{i}$ gets stuck in lines 50-54 simulating longer and longer $q_{j}$-solo extension of some finite schedule $\sigma$ with input $J_{0}$. Since, processes $p_{1}, \ldots, p_{n}$ use a series of consensus instances to simulate runs of $\mathcal{A}^{\prime}$ in exactly the same way, the correct processes eventually agree on $\sigma$ and $q_{j}$.

Let $e$ be the sequence of process identifiers in the 1 -resilient execution of $\mathcal{A}^{\prime}$ simulated by $q_{1}$ and $q_{2}$ in schedule $\sigma \cdot\left(q_{j}\right)$ with input $J_{0}$. Since a 2 -process BG-simulation produces a 1 -resilient run of $\mathcal{A}^{\prime}$, at least $n-1$ simulated processes in $p_{1}^{\prime}, \ldots, p_{n}^{\prime}$ appear in $e$ infinitely often. Let $U(|U| \geq n-1)$ be the set of such processes.

Now we show that exactly one correct (in $F$ ) process appears in $e$ only finitely often. Suppose not, i.e., $\operatorname{correct}(F) \subseteq U$. By Theorem 34, the run of $\mathcal{A}^{\prime}$ simulated a far run of $\mathcal{A}$, and, thus, the run must
be deciding - a contradiction. Since $|U| \geq n-1$, exactly one process appears in the run of $\mathcal{A}^{\prime}$ only finitely often. Moreover, the process is correct.

Thus, eventually, the correct processes in $F$ stabilize at simulating longer and longer prefixes of the same infinite non-deciding 1-resilient run of $\mathcal{A}^{\prime}$. Eventually, the same correct process will be observed to take the least number of steps in the run and output in line 53 - the output of $\Omega$ is extracted.

### 12.3. Implementing $\Omega$ in an eventually synchronous shared memory system

### 12.3.1. Introduction

This chapter presents a simple algorithm that constructs an omega object in a system of $n$ asynchronous processes that cooperate by reading and writing 1WMR regular registers.

An impossibility Let us first observe that, differently from the alpha objects, an omega object cannot be implemented from atomic registers in a pure asynchronous system.

Theorem 36 There is no algorithm that constructs an omega object in a system of $n$ asynchronous processes that communicate by reading and writing atomic registers.

Proof The proof is by contradiction. Let us assume that there is an algorithm $A$ that implements omega in a system of $n$ asynchronous processes that communicate by reading and writing atomic registers. We have seen in the previous chapter that regular registers allows constructing an alpha object. As atomic registers are stronger than regular registers, it follows that atomic registers allows building an alpha object. Moreover, the algorithm presented in chapter ??(9) constructs a consensus object for any number $n$ of processes from an alpha object and an omega object. It follows that a $n$ process consensus object can be built from atomic registers. This contradicts the fact that atomic registers have consensus number 1.

An additional assumption The previous theorem indicates that additional assumptions on the system are necessary in order to build an omega object. This chapter considers the following assumption and shows that it is sufficient to build omega from 1WMR regular registers.

[Eventually synchronous shared memory system] There is a time after which there are a positive lower bound and an upper bound for a process to execute a local step, a read or a write of a shared register.

It is important to notice that the values of the lower and upper bounds, and the time after which these values become the actual lower and upper bounds are not known. The (finite but unknown) time after which the previous property is satisfied is called global stabilization time (GST).

### 12.3.2. An omega construction

Underlying principle. The algorithm that, based on the previous assumption on the system behavior, build an eventual leader oracle is described in Figure 12.5. Its underlying design principles is the following: each process $p_{i}$ strives to elect as the leader the process with the smallest identity that it
considers as being alive. As a process $p_{i}$ never considers itself as crashed, at any time, the process it elects as its current leader has necessarily an identity $j$ such that $j \leq i$. The identity of the process that $p_{i}$ considers leader is stored in a local variable leader $_{i}$.

Shared memory. The shared memory is composed of an array of $n$ reliable 1WMR regular registers containing integer values. This array, denoted $P R O G R E S S[1 . . n]$, is initialized to $[0, \ldots, 0]$. Only $p_{i}$ can write PROGRESS[i]. Any process can read any register PROGRESS[j]. The register $P R O G R E S S[i]$ is used by $p_{i}$ to inform the other processes about its status.

Process behavior. First, when a process $p_{i}$ considers it is leader, it repeatedly increments its register PROGRESS $[i]$ in order to let the other processes know that it has not crashed (while loop and line 2).

Whether it is or not a leader, a process $p_{i}$ increments a local variable $l_{-} c l o c k_{i}$ (initialized to 0 ) at each step of the infinite while loop (line 3). This variable can be seen as a local clock that $p_{i}$ uses to measure its local progress.

It is possible that $p_{i}$ be very rapid and increments very often $l_{-} c l o c k_{i}$, while its current leader $p_{j}$ is slow and two of its consecutive increments of $P R O G R E S S[j]$ are separated by a long period of time. This can direct $p_{i}$ to suspect $p_{j}$ to have crashed, and consequently to select another leader with a possibly greater id. To prevent such a bad scenario from occurring, each process $p_{i}$ handles another local variable denoted $n e x t \_c h e c k_{i}$ (initialized to an arbitrary positive value, e.g., 1). This variable is used by $p_{i}$ to compensate the possible drift between $l_{-} c l o c k_{i}$ and PROGRESS[j]. More precisely, $p_{i}$ tests if its leader has changed only when $l_{\_} c l o c k_{i}=$ next_check $k_{i}$. Moreover, $p_{i}$ increases the duration (denoted delay $_{i}$ and initialized to any positive value) between two consecutive checks (lines 9) when it discovers that its leader has changed. In all cases, it schedules the the logical date next_check $k_{i}$ at which it will check again for leadership (line 10).

So, the core of its algorithm (lines 6-??), that consists for $p_{i}$ in checking if its leader has changed and a new leader has to be defined, is executed only when $l_{-} c l o c k_{i}=$ next_check $k_{i}$. For doing this check, each $p_{i}$ maintains a local array $l_{a s t}[1 . .(i-1)]$ such that last $[j]$ stores the last value of $P R O G R E S S[j]$ it has previously read (line 8). Moreover, when it tries to define its leader, $p_{i}$ checks the processes always
starting from $p_{1}$ until $p_{i-1}$ (line 6). It stops at the first process $p_{j}$ that did some progress since the last time $p_{i}$ read $P R O G R E S S[j]$ (line 7). If there is such a process $p_{j}, p_{i}$ considers it as its (possibly) new leader (line 11). If $p_{j}$ was not its previous leader, $p_{i}$ considers that it previously did a mistake and consequently increases the delay separating two checks for leadership (line 9). In all cases, it then updates the logical date at which it will test again for leadership (increase of next_check $k_{i}$ at line 10). If, $p_{i}$ sees no progress from any $p_{j}$ such that $j<i$, it considers itself as the leader (line 14).

A property. This algorithm enjoys a very nice property: it is timer-free. No process is required to use a physical local clock. This means that, while the correctness of the algorithm rests on a behavioral property of the underlying shared memory system (eventual synchrony), benefiting from that property does not require a special equipment (such as local physical clocks).

### 12.3.3. Proof of correctness

The validity and termination properties defining the eventual leader service are easy and left to the reader. We focus here only on the proof of the eventual leadership property.

Theorem 37 Let us assume that there is a time after which there are a lower bound and an upper bound for any process to execute a local step, a read or a write of a shared register. The algorithm described in Figure 12.5 eventually elects a single leader that is a correct process.

Proof Let $t 1$ be the time after with there are a lower bound and an upper bound on the time it take for a process to execute a local step, a read or a write of a shared register (global stabilization time). Moreover, let $t 2$ be the time after which no more process crashes. Finally let $t=\max (t 1, t 2)$, and $p_{\ell}$ be the correct process with the smallest id. We show that, from some time after $t, p_{\ell}$ is elected by any process $p_{i}$.

Let us first observe that there is a time $t^{\prime}>t$ after which no process $p_{k}$, such that $k<\ell$, competes with the other processes to be elected as a leader. This follows from the following observations:

- After $t, p_{k}$ has crashed and consequently $P R O G R E S S[k]$ is no longer increased.
- After $t$, for each process $p_{i}$, there is a time after which the predicate last $t_{i}[k]=P R O G R E S S[k]$ remains permanently satisfied, and consequently, $p_{i}$ never executes the lines $8-13$ with $j=k$, from which we conclude that $p_{k}$ can no longer be elected as a leader by any process $p_{i}$.

It follows that after some time $t^{\prime}>t$, as no process $p_{k}(k<\ell)$ increases its clock $P R O G R E S S[k]$, $p_{\ell}$ always exits the for loop (lines 6-??) with $h a s_{-} l d_{\ell}=$ false, and considers itself as the permanent and definitive leader (line 14). Consequently, from $t^{\prime}, p_{\ell}$ increases $P R O G R E S S[\ell]$ each time it executes the while loop (lines 1-??).

We claim that there is a time after which, each time a process $p_{i}$ executes the for loop (lines 6-??), we have $P R O G R E S S[\ell]>$ last $_{i}[\ell]$ (i.e., $p_{i}$ does not miss increases of $P R O G R E S S[\ell]$ ). It directly follows from this claim, line 11 (where leader $i_{i}$ is now always set to $\ell$ ), and the fact that all processes $p_{k}$ such that $k<\ell$ have crashed, that $p_{i}$ always considers $p_{\ell}$ as its leader, which proves the theorem.

Proof of the claim. To prove the claim, let us define two critical values. Both definitions consider durations after $t^{\prime}$, i.e., after the global stabilization time (so, both values are bounded).

- Let $\Delta_{w}(\ell)$ be the longest duration, after $t^{\prime}$, separating two increases of PROGRESS $[\ell]$.
- Let $\Delta_{r}(i, \ell)$ be the shortest duration, after $t^{\prime}$, separating two consecutive reading by $p_{i}$ of $P R O G R E S S[\ell]$.

We have to show that, after some time and for any $p_{i}, \Delta_{r}(i, \ell)>\Delta_{w}(\ell)$ remains permanently true, i.e., we have to show that after some time the predicate last $_{i}[\ell]<P R O G R E S S[\ell]$ is true each time it is evaluated by $p_{i}$.

Let us first observe that, as $p_{\ell}$ continuously increases $P R O G R E S S[\ell]$, the locally evaluated predicate last $t_{i}[\ell]<P R O G R E S S[\ell]$ is true infinitely often. If last ${ }_{i}[\ell]<P R O G R E S S[\ell]$ is true while leader $_{i} \neq \ell, p_{i}$ doubles the duration delay dine $_{i}$ ) before which it will again check for a leader (line 4). This ensures that eventually we will have a time after which $\Delta_{r}(i, \ell)>\Delta_{w}(\ell)$ remains true forever. End of the proof of the claim.

### 12.3.4. Discussion

Write optimality. In addition to its design simplicity, and its timer-free property, the proposed algorithm has another noteworthy property related to efficiency, namely, it is write-optimal. This means that there is a finite time after which only one process keeps on writing the shared memory. Let us observe that this is the best that can be done as at least one process has to write forever the shared memory (if after some time no process writes the shared memory, there is no way for the processes to know whether the current leader has crashed or is still alive).

Theorem 38 The algorithm described in Figure 12.5 is write-optimal.

Proof During the "anarchy" period before the global stabilization time, it is possible that different processes have different leaders, and that each process has different leaders at different times. Theorem 37 has shown that such an anarchy period always terminates when the underlying shared memory system satisfies the "eventually synchronous" property.

To show that the algorithm is write-optimal, let us first observe that, each time a process $p_{j}$ considers it is a leader, it increments its global clock $P R O G R E S S[j]$. It follows that when several processes consider they are leaders, several shared registers $P R O G R E S S[-]$ are increased. Interestingly, after the common correct leader has been elected, a single 1WMR register keeps on being increased. This means that a single shared register keeps growing, while the $(n-1)$ other shared registers stop growing. Consequently, the algorithm is communication-efficient. It follows that it is optimal with respect to this criterion (as at least one process has to continuously inform the others that it is alive).

Another synchrony assumption. The reader can also check that the "eventual synchrony" assumption can be replaced by the following assumption: there is a time after which there is an upper bound $\tau$ on the ratio of the relative speed of any two non-crashed processes. Such a bound-based assumption can be seen as another way to place a limitation on the uncertainty created by the combined effect of asynchrony and failures that allows building an omega object.

