# Defense Strategies

Defending against software vulnerabilities is possible along four dimensions: (i) formally proving software correct which guarantees that the code is bug free (according to a given specification), (ii) rewriting the software in a safe programming language, (iii) software testing which discovers software flaws before they can do any harm, and (iv) mitigations which protect a system in the presence of unpatched or unknown vulnerabilities.

## 6.1 Software Verification

Software verification proves the correctness of code according to a given specification.

The security constraints (e.g., no memory or type safety violation) are encoded and given as configuration to the verification process. Different forms of formal verification exist such as bounded model checking or abstract interpretation. All of them prove that a given piece of code conforms to the formal specification and guarantee that no violations of the security policy are possible. Some well-known examples of formally verified code are seL4 [14], a formally verified operating system kernel or CompCert [19], a formally verified compiler. For seL4, operating system concepts are encoded as high-level policies on top of a proof system. After proving the correctness of the high level operating system policy, the equivalence between the high-level policy and a low-level implementation is proven in a second step. For CompCert, individual steps and transformations of the compiler are provably correct. This guarantees that verified compiler transformations are always correct and will not introduce any bugs as part of the compilation process.

The main challenge of software verification is scalability. Automatic software verification scales to 100s of lines of code with an exponential increase in verification cost with linear increase of code. As an example, human guided verification of the seL4 kernel verification cost several person years.

## 6.2 Language-Based Security

Language-based security is a rather new area of research that focuses on enforcing security properties as part of the programming language, protecting the programmer from making mistakes. Programming languages have always enforced some form of structure, thereby protecting against certain types of bugs. Language-based security makes reasoning about security aspects explicit and allows languages to be designed in a security specific way. Early examples are functional programming languages that inherently protect against memory safety violations and data races. Functional languages track references to data and prohibit direct pointer manipulation. Orthogonally, variables may only be written once during assignment, protecting against data races as data cannot be modified concurrently. Java is a popular programming language that enforces both type safety and memory safety as part of the programming language and its runtime system.

A modern example of a *secure* imperative programming language is Rust. Rust enforces memory safety and data race freedom through ownership tracking and a strict type system.

The clear ownership in Rust prohibits concurrent modification and allows the compiler to check memory ownership during compilation. The majority of the type checks are executed statically as part of the compilation (and the compiler can give detailed warnings about possible issues) with minimal runtime checks. Rust gives strong memory safety, type safety, and data race freedom guarantees at negligible performance overhead at the cost of a steep learning curve as the programmer must make all ownership assumptions explicit when writing code.

## 6.3 Testing

Software testing allows developers to identify bugs before they can do any harm. This process is orthogonal to software development and, if done correctly, is integrated into the development process to allow for continuous software testing. Testing is the process of executing a program to *find flaws*. An error is a deviation between observed behavior and specified behavior, i.e., a violation of the underlying specification of functional requirements (features a, b, c) or operational requirements
(performance, usability). Both functional and operational requirements are testable. Security requirements are not directly testable as, e.g., the absence of bugs is hard to prove. For applications written in C/C++ we can indirectly test that memory safety and type safety guarantees hold by observing the effects of testing. Instead of checking the correct computation of the result we measure if the program crashes or is terminated through a security exception.

Testing can only show the presence of bugs, never their absence.

(Edsger W. Dijkstra)

## 6.3.1 Manual Testing

Test-driven development flips the process between testing and implementation. Instead of writing test cases for a given implementation, the test cases are written as a first implementation step. This approach allows the programmer to encode details that are specified in the design. The test cases are witnesses for required features. Initially all test cases fail and slowly, as the implementation proceeds, the test cases start to pass as more and more features are implemented. Testing should be integrated with a *continuous integration system* that verifies all test cases (and coding style) whenever new code is checked into the project's source repository. Manual testing involves the development of positive and negative test cases and embedding assertions in the production code. Assertions help test negative test cases and find bugs before they corrupt any state which would make them hard to triage.

Unit tests are small test cases that focus on an individual unit or feature of the program.

The Google testing framework
[7] simplifies the implementation of such tests. To provide necessary application state, unit testing frameworks enable a wide range of mock operations.

Integration tests allow testing of interactions between individual modules. For example, an integration test could measure the interaction between a browser's DOM and the printer daemon that creates a visual representation of the DOM to send it off to a printer.

System testing tests the full application. For example, a browser displaying a web page and a user interacting with that page to accomplish a certain task such as filling out a form and sending it off.

Beta testing leverages a small set of users that thoroughly test the software to find remaining flaws. Any identified bug is triaged and fixed. It is good testing practice to create a test case for each identified flaw to protect against regression. Regression happens if a code change suddenly fails existing test cases. Keeping test cases for each fixed bug allows early detection if a bug is introduced again and may catch similar bugs as well.

An interesting question is what metric is used to evaluate the quality of a test suite. A deterministic metric allows an absolute evaluation of the quality of the suite, i.e., how well a test suite maps to a program. Coverage is a natural metric that suits the aforementioned criteria. Coverage is used as a metric to evaluate the quality of a test suite. The intuition is that a software flaw is only detected if the flawed code is executed. The effectiveness of the test suite therefore depends on the resulting coverage. Different coverage metrics exist with varying tradeoffs. We consider statement coverage, branch coverage, path coverage, and data-flow coverage.

Statement coverage measures, for each statement, if it has been executed. Coverage tracking can be done using a simple array and instrumentation that marks the executed bit for each statement when executed (or basic block without loss of generality). A disadvantage of statement coverage is that not all edges are tracked, e.g., the backward edge of a loop may never be executed in the following example:

```
**int** func(int elem, **int** *inp, **int** len) {
    int ret = -1;
    for (int i = 0; i <= len; ++i) {
        if (inp[i] == elem) { ret = i; **break**; }
    }
    return ret;
}
```
Listing 6.1: Example where statement coverage misses a bug.

The test input elem = 2, inp = [1, 2], len = 2 achieves full statement coverage but the execution never executed the last iteration of the loop which will result in a buffer overflow.

The branch edge from the check in the loop to the end of the loop is never followed.

Branch coverage measures, for each branch, if it has been followed. Again, coverage tracking can be done using a simple array and instrumentation that marks executed branches. Branch coverage marks both the execution of the basic block and the branch to a given basic block and is therefore a super set of simple statement coverage. Full branch coverage implies full statement coverage. Unfortunately, branch coverage may not be precise enough:

```
**int** arr[5] = { 0, 1, 2, 3, 4 };
**int** func(int a, **int** b) {
    int idx = 4;
    if (a < 5) idx -= 4; **else** idx -= 1;
    if (b < 5) idx -= 1; **else** idx += 1;
    return arr[idx];
}
```
Listing 6.2: Limitation Of Branch Coverage.

The test inputs a = 5, b = 1 and a = 1, b = 5 achieve full branch coverage (and full statement coverage), yet, not all possible paths through the program will be executed. The input a = 1, b = 1 results in a bug when both statements are true at the same time. Full path coverage evaluates all possible paths. Evaluating all possible paths quickly becomes expensive as each branch doubles the number of evaluated paths or even impossible for loops where the bounds are not known. This exponential increase in the amount of paths is called *path explosion*. Loop coverage (execute each loop 0, 1, n times), combined with branch coverage probabilistically covers state space.

Implementing path coverage requires runtime tracing of the paths as, programs with more than roughly 40 branches cannot be mapped into a flat array and enumerating all paths becomes impossible given current (and future) memory constraints.

Data-flow coverage extends beyond path coverage and tracks full data flow through the program at even higher overhead. In addition to path constraints (a boolean for each path decision), the values of all program values have to be tracked as well.

This is the most precise way to track coverage but involves high overheads.

Therefore, in practice, branch coverage is the most efficient tool and several mechanisms exist that allow branch coverage tracking for software. Two examples are gcov and Sanitizer- Coverage. Branch coverage keeps track of edges in the CFG, marking each executed edge with the advantage that only a bit of information is required for each edge (and no dynamic information that depends on the number of executed paths).

## 6.3.2 Sanitizers

Test cases detect bugs through miscompared results, assertion failures, segmentation faults, division by zero, uncaught exceptions, or mitigations that trigger process termination.

Sanitizers are compilation frameworks that instrument a program with additional checks. When executed with the test cases, unit tests, or under fuzz testing, the sanitizers can detect violations at the source of the flaw and not just when the process traps. Sanitizers detect low level violations of, e.g., memory safety or type safety, not high-level functional properties. Recently several new sanitizers were added to the LLVM compiler framework to target different kinds of vulnerabilities:
AddressSanitizer, LeakSanitizer, MemorySanitizer, Undefined-
BehaviorSanitizer, ThreadSanitizer, and HexType.

AddressSanitizer (ASan) [30] detects memory errors. It places red zones around objects and checks those objects on trigger events. The typical slowdown introduced by ASan is 2x. The tool can detect the following types of bugs:

- Out-of-bounds accesses to heap, stack and globals 
- Use-after-free 
- Use-after-return (configurable) 
- Use-after-scope (configurable) 
- Double-free, invalid free 
- Memory leaks (experimental)

Note that the ASan memory safety guarantees are probabilistic.

ASan leverages so called red zones around objects which are marked with a special value. Checks ensure that the special value remains intact. Similarly for use-after-free, instrumentation ensures that the values remain correct. This obviously does not protect against memory areas that are reallocated to different objects. ASan is therefore not a mitigation but a sanitizer that helps to probabilistically detect flaws.

LeakSanitizer detects run-time memory leaks. It can be combined with AddressSanitizer to get both memory error and leak detection, or used in a stand-alone mode. LSan adds almost no performance overhead until process termination, when the extra leak detection phase runs.

MemorySanitizer (MSan) detects uninitialized reads. MSan uses heavy-weight program transformation to keep state of allocated objects. Memory allocations are tagged and uninitialized reads are flagged. The typical slowdown of MSan is 3x. Note: do not confuse MemorySanitizer (detects uninitialized reads) and AddressSanitizer (detects spatial memory safety violations and probabilistic memory reuse).

UndefinedBehaviorSanitizer (UBSan) detects undefined behavior. It instruments code to trap on typical undefined behavior in C/C++ programs. Slowdown depends on the amount and frequency of checks. This is the only sanitizer that can be used in production. For production use, a special minimal runtime library is used with minimal attack surface. Detectable errors are:

- Unsigned/misaligned pointers 
- Signed integer overflow 
- Conversion between floating point types leading to overflow
- Illegal use of NULL pointers 
- Illegal pointer arithmetic 
- and many more (check the documentation)

ThreadSanitizer (TSan) detects data races between threads. It instruments writes to global and heap variables and records which thread wrote the value last, allowing detecting of Write-
After-Write, Read-After-Write, Write-After-Read data races.

The typical slowdown of TSan is 5-15x with 5-15x memory overhead.

HexType [11] detects type safety violations (type confusion). It records the true type of allocated objects and makes all type casts explicit. HexType implements type safety for C++. The typical slowdown of HexType is 1.5x.

Alternatively, Valgrind [24] implements a sanitization framework for binaries. Binaries are lifted into a high-level representation that is instrumented. During execution, metadata is kept depending on the selected instrumentation of the sanitizer.

Valgrind implements different memory safety and thread safety sanitizers.

## 6.3.3 Fuzzing

Dynamic analysis techniques leverage a concrete execution through the program to test a given policy. *Fuzz testing* is a simple approach that creates program input to generate different traces through the program with the intention to trigger a crash. Crashing inputs are then collected and triaged to fix bugs. Different approaches for fuzz testing exist with different levels of program cooperation. Fuzzing can leverage information about the input structure or the program structure to improve over blind random input mutation.

While fuzzing, the process of providing random input to a program to trigger unintended crashes, has been around for decades, we have recently seen a revival of techniques with several papers improving fuzzing effectiveness at each top tier security conference.

The idea behind fuzzing is incredibly simple: execute a program in a test environment with random input and detect if it crashes. The fuzzing process is inherently sound but incomplete. By producing test cases and observing if the program under test crashes, fuzzing produces a witness for each discovered crash. As a dynamic testing technique, fuzzing is incomplete as it will likely neither cover all possible program paths nor data-flow paths except when run for an infinite amount of time. Fuzzing has seen a massive amount of attention in recent years both from industry where fuzzing is used to discover bugs to academia where new fuzzing techniques are developed. Fuzzing strategies are inherently an optimization problem where the available resources are used to discover as many bugs as possible, covering as much of the program functionality as possible through a probabilistic exploration process. Due to its nature as a dynamic testing technique, fuzzing faces several unique challenges:

- Input generation: fuzzers generate inputs based on a
mutation strategy to explore new state. The underlying strategy determines how effectively the fuzzer explores a given state space. A challenge for input generation is the balance between exploring new control flow and data flow.
- Detecting flaws: to discover flaws, fuzzers must distinguish between benign and buggy executions. Not every bug results in an immediate segmentation fault and detecting state violation is a challenging task, especially as code generally does not come with a formal model.
- Preparing programs: fuzzing struggles with some aspects
of code such as fuzzing a complex API, checksums in file formats, or hard comparisons such as password checks. Preparing the fuzzing environment is a crucial step to increase the efficiency of fuzzing.
- Evaluating fuzzing effectiveness: defining metrics to evaluate the effectiveness for a fuzzing campaign is challenging. For most programs the state space is (close to) infinite and fuzzing is a brute force search in this state space. Deciding when to, e.g., move to another target, path, or input is a crucial aspect of fuzzing. Comparing different fuzzing techniques requires understanding of the strengths of a fuzzer and the underlying statistics to enable fair comparison.

AFL [36] is the state-of-the art fuzzer that uses mutational input generation. AFL uses grey-box instrumentation to track branch coverage and mutate fuzzing seeds based on previous branch coverage. Branch coverage tracks the last two executed basic blocks (resulting in a crude approximation of path coverage). New coverage is detected on the history of the last two branches.

## 6.3.3.1 Input Generation

Input generation is the first of two essential parts of the fuzzing process. Every fuzzer must automatically generate test cases to be run on the execution engine. The cost for generating a single input should be low, following the underlying philosophy of fuzzing where iterations are cheap. There are two fundamental forms of input generation: *model-based input generation* and mutation-based input generation. The first is aware of the input format while the latter is not. 

Knowledge of the input structure given through a grammar enables *model-based input generation* to produce (mostly) valid test cases. The grammar specifies the input format and implicitly the explorable state space. Based on the input specification, the fuzzer can produce valid test cases that satisfy many checks in the program such as valid state checks, dependencies between fields, or checksums such as a CRC32. For example, without an input specification the majority of randomly generated test cases will fail the check for a correct checksum and quickly error out without triggering any complex behavior. The input specification allows input generation to balance the generated test inputs according to the underlying input grammar. The disadvantage of grammar-based input generation is the need for a concrete input specification. Most input formats are not formally described and will require an analyst to define the intricate dependencies.

Mutation-based input generation requires a set of seed inputs that trigger valid functionality in the program and then leverages random mutation to modify these seeds. Providing a set of valid inputs is significantly easier than formally specifying an input format. The input mutation process then constantly modifies these input seeds to trigger interesting behavior. Orthogonally to the awareness of the input format, a fuzzer can be aware of the program structure. Whitebox fuzzing infers knowledge of the program structure through program analysis or relies on an analyst to custom-tailor fuzzing for each tested program, resulting in untenable cost. Blackbox fuzzing blindly generates new input without reflection, severely limiting progress of the fuzzer.

Greybox fuzzing leverages program instrumentation instead of program analysis to infer coverage during the fuzzing campaign itself, merging analysis and testing.

Coverage-guided greybox fuzzing combines mutation-based input generation with program instrumentation to detect whenever a mutated input reaches new coverage. Program instrumentation tracks which areas of the code are executed and the coverage profile is tied to specific inputs. Whenever an input mutation generates new coverage, it is added to the set of inputs for mutation.

This approach is incredibly efficient due to the low cost instrumentation but still results in broad program coverage. Modern fuzzing is heavily optimized and focuses on efficiency, measured by the number of bugs found per time. Sometimes, fuzzing efficiency is generalized as the number of crashes found per time, but this may lead to problems as crashes may not be unique and many crashes point to the same bug.

## 6.3.3.2 Execution Engine

After generating the test cases, they must be executed in a controlled environment to observe when a bug is triggered. The execution engine takes the produced input, executes the program under test, extracts runtime information such as coverage, and detects crashes. Ideally a program would terminate whenever a flaw is triggered. For example, an illegal pointer dereference on an unmapped memory page results in a segmentation fault which terminates the program, allowing the executing engine to detect the flaw. Unfortunately, only a small subset of security violations will result in program crashes. Buffer overflows into adjacent memory locations for example, may only be detected later if the overwritten data should be used or may never be detected at all. The challenge for this component of the fuzzing process is to efficiently enable the detection of policy violations. For example, without instrumentation only illegal pointer dereferences to unmapped memory, control-flow transfers to non-executable memory, division by zero, or similar exceptions will trigger a fault.

To make security policies tractable, the program under test may be instrumented with additional checks that detect violations early. Safety violations through undefined behavior for code written in systems languages are particularly tricky. Sanitization analyzes and instruments the program during the compilation process to enforce selected properties. Address Sanitizer [30], the most commonly used sanitizer, probabilistically detects spatial and temporal memory safety violations by placing red-zones around allocated memory objects, keeping track of allocated memory, and carefully checking memory accesses. Other sanitizers cover undefined behavior, uninitialized memory, or type safety violations [11]. Each sanitizer requires certain instrumentation that increases the performance cost.

The usability of sanitizers for fuzzing therefore has to be carefully evaluated as, on one hand, it makes error detection more likely but, on the other hand, reduces fuzzing throughput.

## 6.3.3.3 Preparing Programs

The key advantage of fuzzing is its incredible simplicity (and massive parallelism). Due to this simplicity, fuzzing can get stuck in local minima where continuous input generation will not result in additional crashes or new coverage - the fuzzer is stuck in front of a coverage wall. A common approach to circumvent the coverage wall is to extract seed values used for comparisons. These seed values are then used during the input generation process. Orthogonally, a developer can comment out hard checks such as CRC comparisons or checks for magic values. Removing these non-critical checks from the program requires that the developer is aware of what are critical safety checks and what can be safely commented out. Several recent extensions [31:@sanjay17ndss, @peng18sp, @insu18sec] try to bypass the coverage wall by detecting when the fuzzer gets stuck and then leveraging an auxiliary analysis to either produce new inputs or to modify the program. It is essential that this (sometimes heavy-weight) analysis is only executed infrequently as alternating between analysis and fuzzing is costly and reduces fuzzing throughput.

The concept of fuzzing libraries also faces the challenge of experiencing low coverage during unguided fuzzing campaigns. Programs often call exported library functions in sequence, building up complex state in the process. The library functions execute sanity checks and quickly detect illegal or missing state.

These checks make library fuzzing challenging as the fuzzer is not aware of the dependencies between library functions. Existing approaches such as libFuzzer [32]] require an analyst to prepare a test program that calls the library functions in a valid sequence to build up the necessary state to fuzz complex functions.

## 6.3.3.4 Evaluating Fuzzing

At a high-level, evaluating fuzzing is straightforward: if technique A finds more bugs than technique B, then technique A is superior to technique B. In practice, there are challenging questions that must be answered such as for how long the techniques are evaluated, how bugs are identified, or what the fuzzing environment is. A recent study [13] evaluated the common practices of recently published fuzzing techniques (and therefore also serves as overview of the current state of the art). The study identified common benchmarking crimes and condensed their findings into five recommendations:

- A single execution is not enough due to the randomness
in the fuzzing process. To evaluate different mechanisms,
we require multiple trials and statistical tests to measure
noise.
- A single target is not enough to evaluate a fuzzer. Instead,
fuzzers should be evaluated across a broad set of target programs to highlight advantages and disadvantages of a given configuration.
- Heuristics cannot be used as the only way to measure
performance. For example, collecting crashing inputs or even stack bucketing does not uniquely identify bugs. Ground truth is needed to disambiguate crashing inputs and to correctly count the number of discovered bugs. A benchmark suite with ground truth will help.
- The choice of seeds must be documented as different
seeds provide vastly different starting configurations and not all techniques cope with different seed characteristics equally well.
- Fuzzing campaigns are generally executed for multiple
days to weeks. Comparing different mechanisms based on a few hours of execution time is not enough. Fuzzing must be evaluated for at least 24 hours, maybe even longer.

## 6.3.3.5 Future Fuzzing Work

Fuzzing is currently an extremely hot research area in software security with several new techniques being presented at each top tier security conference. The research directions can be grouped into improving input generation, reducing the performance impact for each execution, better detection of security violations, or pushing fuzzing to new domains such as kernel fuzzing or hardware fuzzing. All these areas are exciting new dimensions and it will be interesting to see how fuzzing can be improved further.

## 6.3.3.6 Fuzzing Summary

With the advent of coverage-guided greybox fuzzing, dynamic testing has seen a renaissance with many new techniques that improve security testing. While incomplete, the advantage of fuzzing is that each reported bug comes with a witness that allows the deterministic reproduction of the bug. Sanitization, the process of instrumenting code with additional software guards helps to discover bugs closer to their source. Overall, security testing remains challenging, especially for libraries or complex code such as kernels or large software systems. Given the massive recent improvements of fuzzing, there will be exciting new results in the future. Fuzzing will help make our systems more secure by finding bugs during the development of code before they can cause any harm during deployment.

## 6.3.4 Symbolic Execution

Static analysis techniques analyze the source code (or binary)
for violations of a given policy. Static analysis frameworks usually combine a wide set of techniques to discover different types of vulnerabilities based on abstract interpretation of the code combined with control-flow and data-flow analysis. Abstract interpretation transforms the semantics of the programming language to simplify source code, translating it into a form that allows reasoning over an abstract grammar. The advantage of static analysis techniques is their ubiquity and simple application to large code bases. A disadvantage is that they may lead to large amounts of false positives.

Symbolic execution is an analysis technique that is somewhat between static and dynamic analysis with many different flavors.

A symbolic execution engine reasons about program behavior through "execution" with symbolic values. Concrete values
(input) are replaced with symbolic values. Symbolic values can have any value, i.e, variable x instead of value 0x15. Symbolic values capture all possible values. The symbolic state of the application is tracked through a set of collected constraints. Operations (read, write, arithmetic) become constraint collection/modification operations as they add new constraints to the collection, possibly summarizing existing constraints. Symbolic execution allows *unknown* symbolic variables in the evaluation.

Through this abstract interpretation, the program is turned into a set of constraints. Instead of executing the program with concrete input, all memory becomes symbolic and computation updates the symbolic values. This allows a large amount of traces through the program to be evaluated at the same time. Symbolic execution is limited through the complexity of the constraints. For each branch in the program, the amount of state doubles as either the true or the false branch can be taken which leads to a state explosion.

```
**void** func(int a, int b, **int** c) {
    int x = 0, y = 0, z = 0;
    if (a) x = -2;
    if (b < 5) {
        if (!a && c) y = 1;
        z = 2;
    }
    assert(x + y + z != 3);
}
```
Listing 6.3: Symbolic execution example. The parameters a, b, and c are symbolic.

A path condition is a quantifier-free formula over symbolic inputs that encodes all branch decisions (so far). To determine whether a path is feasible, the symbolic execution engine checks if the path condition is satisfiable. Given the set of constraints, an SMT solver provides satisfying assignment, counter example, or timeout.

While symbolic execution gives a precise evaluation of all paths in the program, it has a hard time with loops and recursions which result in infinite execution traces. Path explosion is another challenge as each branch doubles the number of paths and state that is tracked. Environment modeling, e.g., through system calls is also complex due to the amount of operating system state that must be modeled. Lastly, symbolic data where both the array data and the index are symbolic is challenging as arbitrary data increases the number of possible solutions. Constraint tracking along the different paths for the symbolic execution example.

All these problems have in common that the complexity makes the constraints explode, reducing the chances that the SMT solver will find a solution before a timeout. Concolic testing addresses the problems of symbolic execution by leveraging a concrete execution trace to "base" the symbolic execution to places nearby. Only constraints close to and along the recorded trace are evaluated. KLEE [6] is an example of a symbolic/concolic execution engine based on the LLVM compiler.

LLVM compiles the target program with instrumentation for symbolic/concolic execution. KLEE then models the environment and provides a selection of many different search strategies and heuristics to constrain symbolic execution.

## 6.4 Mitigations

Mitigations are the last line of defense against software flaws that violate low level security policies such as memory safety, type safety, or integer overflows. Logic flaws are out of scope for mitigations as they are dependent on the requirements and specification of an application which is (generally) not expressed in a machine-readable way. Given that code was neither verified nor tested for a bug, mitigations can check for policy violations at runtime. Mitigations against flaws generally result in some performance overhead due to these additional checks. The majority of mitigations are therefore designed to incur negligible performance or memory overhead, at the tradeoff of lower security guarantees. The reason why overhead is not tolerated is the abstract risk of bugs. Mitigations protect against unpatched and unknown bugs and, therefore, against an abstract risk. The cost of running the mitigation is real.

The set of deployed mitigations is Data Execution Prevention (DEP) to protect against code injection, Address Space Layout Randomization (ASLR) to probabilistically protect against information leaks, stack canaries to protect backward edge control-flow, safe exception handling to protect against injected C++ exception frames, and fortify source to protect against format string attacks. Some stronger mitigations such as Control-Flow Integrity (CFI), sandboxing, stack integrity, and software-based fault isolation are being deployed on highly exposed software with broad dissemination likely happening soon.

## 6.4.1 Data Execution Prevention (Dep)/WˆX

Most widespread hardware did initially not distinguish between code and data. Any readable data in a process' address space could be executed by simply transferring control-flow to that data location. The memory management unit allowes pages to be unmapped, readable, or writable. These three different configurations are handled through a single bit in the page table that marks if a page is writable or only readable. If a page is not mapped then it is neither writable nor readable.

Any mapped page is always readable.

Data Execution Prevention (DEP) or WˆX (writable xor executable) enforces that any location in memory is either executable or writable but never both. DEP enforces code integrity, i.e., code cannot be modified or injected by an adversary. In the absence of a just-in-time compiler or self-modifying code in the process, code remains static and limited to the initial set of executable code as loaded when the process started.

The assumption for designing this mitigation was that enabling the CPU to distinguish between code and data would stop code execution attacks. Modern architectures extended the page table layout with an additional No-eXecute bit (Intel calls this bit eXecute Disable, AMD calls it Enhanced Virus Protection, and ARM calls it eXecute Never). This bit allows the MMU to decide, on a per-page basis, if it is executable or not. If the bit is set, then data on that page cannot be interpreted as code and the processor will trap if control flow reaches that page. Not all hardware supports the necessary extensions and several software-only extensions were designed to give similar guarantees, often at higher performance cost. Figure 6.1 shows the changes to a process' address space under DEP/WˆX.

This mitigation is a prime example of a successful mitigation that results in negligible overhead due to a hardware extension.

The hardware-enabled mitigation is now used generally and widely. DEP and WˆX stop an attacker from injecting new executable code in the address space of the application. However, without any other mitigation, an application is still prone to code reuse. See Section 5.4.2 and 5.4.3 for more details.

## 6.4.2 Address Space Layout Randomization (Aslr)

Any successful control-flow hijack attack depends on the attacker overwriting a code pointer with a known alternate target.

Address space randomization changes (randomizes) the process memory layout. If the attacker does not know where a piece of code (or data) is, then it cannot be reused in an attack. Under address space randomization, an attacker must first *learn* and recover the address layout. Alternatively, an attacker may cleverly reuse existing pointers at well-known relative offsets. Challenges for address space randomization are information leakage through side channels or other leaks, low entropy that enables brute forcing of the relocation strategy, and rerandomization as long running processes will have their layout fixed after the start of the process (due to performance trade-offs as rerandomization would be costly). The security improvement of address space randomization depends on (i) the entropy available for each randomized location, (ii) the completeness of randomization (i.e., are all objects randomized), and (iii) the lack of any information leaks.

Address space randomization features several candidates that can be placed at random locations in the address space:

- Randomize start of heap; - Randomize start of stack; - Randomize start of code (PIE for executable, PIC for
libraries);
- Randomize code at the instruction level (resulting in
prohibitive overhead);
- Randomize mmap allocated regions; - Randomize individual allocations (malloc);
- Randomize the code itself, e.g., gap between functions,
order of functions, basic blocks;
- Randomize members of structs, e.g., padding, order.
There are different forms of fine-grained randomization with different performance, complexity, and security trade-offs. Address Space Layout Randomization (ASLR) is a form of address space randomization that leverages virtual memory to randomize parts of an address space. ASLR shuffles the start addresses of the heap, the stack, all libraries, the executable, and mmapped regions. ASLR is inherently page based (to limit overhead) and the main cost is due to position independent code [26].

ASLR requires virtual memory and support from the operating system, linker/loader, and compiler. The implementation of ASLR is straightforward and fits well into the virtual address space provided by operating systems. When loading a library, allocating a stack, or mmapping a region it has to be placed somewhere in memory. Randomizing the low bits of the page base address implements address space randomization at the page level. Virtual memory is required to allow reshuffling of addresses. The operating system must allow randomization for random address for the initial binary and mmapped regions.

The linker/loader must prepare the process at a random location in memory. The compiler must ensure that code references other code locations relatively as each code block may be at a different location every time the process starts. Figure 6.2 shows the change to the address space under ASLR.

The entropy of each section is key to security (if all sections are randomized). For example, Figure 6.2 uses 8 bit of entropy for each section. An attacker follows path of least resistance, i.e., targets the object with the lowest entropy. Early ASLR implementations had low entropy on the stack and no entropy on x86 for the main executable (non-PIE executables). Linux
(through Exec Shield) uses 19 bits of entropy for the stack (16
byte aligned) and 8 bits of mmap entropy (4096 byte/page aligned).

## 6.4.3 Stack Integrity

Early code execution attacks often targeted stack-based buffer overflows to inject code. An early defense targeted precisely these buffer overflows. While memory safety would mitigate this problem, adding full safety checks is not feasible due to high performance overhead. Instead of checking each dereference to detect arbitrary buffer overflows we can add a check for the integrity of a certain variable. The goal for this mitigation is to protect an application against stack-based overflows that change the stored return instruction pointer or saved stack base pointer. Stack integrity as a property ensures that both the return instruction pointer and the stack pointer cannot be modified illegally. Legal modifications of the return instruction pointers include, e.g., a trampoline that redirects control flow to an alternate location (overwriting the stored return instruction pointer from a call instruction) or so-called thunks that pop the return instruction pointer into a general purpose register (allowing code to infer the current value of the instruction pointer through a call nextInstruction; pop generalPurposeRegister sequence for ISAs such as x86 that do not allow explicit access to the instruction pointer). A stack pivot changes the stack pointer and shifts the current stack frame to an alternate location under the attacker's control, e.g., by overwriting a spilled stack pointer value. Different mitigations implement some form of stack integrity.

The most common forms are stack canaries that place guards around sensitive values, shadow stacks that store a copy of sensitive data in an alternate location, and safe stacks which split the stacks into sensitive, protected data and unprotected data. Interesting challenges for mitigations are, next to security guarantees, the support for exceptions in C++, setjmp/longjmp for C programs, and tail call optimizations which replace the call to a leaf function to reuse the same stack frame. These features allow abnormal control flow on the return edge and transfer code to stack frames higher up on the stack, potentially skipping several frames in the chain.

## 6.4.3.1 Stack Canaries

The key insight for stack canaries is that, in order to overwrite the return instruction pointer or base stack pointer, all other data on the way to those pointers must be overwritten as well.

This mitigation places a canary before the critical data and adds instrumentation to (i) store the canary when the function is entered and (ii) check its integrity right before the function returns. The compiler may place all buffers at the end of the stack frame and the canary just before the first buffer. This way, all non-buffer local variables are protected against sequential overwrites as well. Stack canaries are a purely compiler-based defense.

The term stack canaries comes from mine workers who brought canary birds along when they went into coal mines.

The birds would pass out from the lack of oxygen and alert the mine workers, similar to how stack canaries signal a buffer overflow when data adjacent to the return instruction pointer is overwritten.

The weakness of this defense is that the stack canary only protects against continuous overwrites as long as the attacker does not know the canary. If the attacker knows the secret or the attacker uses a direct overwrite then this mitigation is not effective. An alternative to protect the return instruction pointer through a canary is to encrypt the return instruction pointer, e.g., by xoring it with a secret. The stack canary instrumentation is surprisingly simple (note that, to support a per-thread unique canary, this implementation uses thread local storage that is relative to the %fs segment register):
```
; Prologue:
mov     %fs:0x28,%rax
mov     %rax,-0x8(%rbp)
xor     %eax,%eax
; Epilogue:
mov     -0x8(%rbp),%rcx
xor     %fs:0x28,%rcx
je      <safe_return>
callq   <__stack_chk_fail@plt>
safe_return:
    leaveq
    ret 
```
Listing 6.4: Prologue and epilogue for stack canaries.

## 6.4.3.2 Shadow Stack

Shadow stacks are a strong form of stack integrity. The core idea is that sensitive data such as the return instruction pointer and any spilled stack pointers is moved to a second, protected stack. Any flaws in the program can therefore no longer corrupt the protected information. Code is instrumented to allocate two stack frames for each function invocation: the regular stack frame and the shadow stack frame. The two stack frames can be of different size, i.e., the frame with the sensitive data may be much smaller than the regular stack frame. Figure 6.4 shows the shadow stack layout.

A key question is how the shadow stack is protected from arbitrary writes.

Simply moving it to another memory location stops continuous buffer overflows (similarly to stack canaries) but cannot stop an adversary with arbitrary memory modification capabilities. Shadow stacks result in about 5% performance overhead due to the allocation of additional stack frames and checks when returning from a function.

## 6.4.3.3 Safe Stack

Safe stacks are a form of stack integrity that reduce the performance penalty compared to shadow stacks. A shadow stack always keeps two allocated stack frames for each function invocation, resulting in overhead. Stack canaries are only added if unsafe buffers are in a stack frame. The goal of safe stacks is to achieve security guarantees of shadow stacks with low performance overhead by only executing checks for unsafe objects.

All variables that are accessed in a safe way are allocated on the safe stack. An optional unsafe stack frame contains all variables that *may* be accessed in an unsafe way. A compiler-based analysis infers if unsafe pointer arithmetic is used on objects or if references to local variables escape the current function. Any objects that are only accessed in safe ways (i.e., no odd pointer arithmetic and no reference to the object escapes the analysis scope) remain on the safe stack frame. Unsafe stack frames are only allocated when entering a function that contains unsafe objects. This reduces the amount of unsafe stack frame allocations, achieving low performance overhead while providing equal security to a safe shadow stack implementation. Figure 6.5 shows the safe stack layout.

## 6.4.4 Safe Exception Handling (Seh)

Programs often handle irregular control-flow, e.g., when error conditions are passed across several function call frames to where they are handled.

While C allows setjmp/longjmp and goto for irregular control-flow, C++ provides a more elegant and structured variant to handle irregular control-flow: exceptions.

C-style error handling is a crude tool to force control-flow to alternate locations. The high irregularity and immense flexibility (basically it is an unconditional jump across several contexts and stack frames completely under the control of the programmer) makes it impossible for the compiler to reason about its semantics and opens up opportunities for bugs. Exceptions are highly structured and allow the compiler to encode the necessary conditions when and how control-flow is transferred. Exception-safe code can safely recover from thrown conditions. Compared to C, the control-flow semantics are explicit in the programming language.
```
**double** div(double a, **double** b) {
    if (b == 0)
        throw "Division by zero!";
        return (a/b);
    } 
...
**try** {
    result = div(foo, bar);
} catch (**const char*** msg) {
...
}
```
Listing 6.5: Exception handling in C++

Exception handling requires support from the code generator (compiler) and the runtime system (libc or libc++). The implementation for exceptions is compiler-specific (libunwind for LLVM). When implementing exceptions, two different approaches exist: (a) inline exception information in stack frame or (b) generate exception tables that are used when an exception is thrown. For *inline exception handling*, the compiler generates code that registers exceptions whenever a function is entered. Individual exception frames are linked (similar to a linked list) across stack frames. When an exception is thrown, the runtime system traces the chain of exception frames to find the corresponding handler. This approach is compact but results in overhead for each function call (as metadata about exceptions has to be allocated).

Exception tables trade-off per-function call costs to cost for each thrown exception. During code generation, the compiler emits per-function or per-object tables that link instruction pointers to program state with respect to exception handling.

Throwing an exception is translated into a range query in the corresponding table, locating the correct handler for the exception. These tables are encoded very efficiently. For both approaches, the encoding of the metadata may lead to security problems. Given a memory corruption vulnerability, an attacker can force throw an exception and may modify the way exceptions are handled by changing the exception data structures. Microsoft Windows uses a combination of tables and inlined exception handling. Each stack frame records (i) unwinding information, (ii) the set of destructors that need to run, and
(iii) the exception handlers if a specific exception is thrown.

Unwinding information includes details on how the stack frame needs to be adjusted when an exception is thrown, e.g., what variables need to be stored from registers to memory or how the stack frame needs to be adjusted. An exception may close several scopes, resulting in objects going out of scope and therefore their destructors have to be run. When entering a function, a structured exception handling (SEH) record is generated, pointing to a table with address ranges for try-catch blocks and destructors. Handlers are kept in a linked list. To attack a Windows C++ program, an attacker may overwrite the first SEH record on the stack and point the handler to the first gadget. In response to this attack vector, Microsoft Visual Studio added two defenses: SafeSEH and SeHOP. SafeSEH generates a compiler-backed list of allowed targets. If a record points to an unknown target it is rejected. SeHOP initializes the chain of registration records with a sentinel, i.e., the sentinel is the first element inserted on the linked list and therefore at the end of any exception list when an exception is thrown. If no sentinel is present, the handler is not executed. The two defenses guarantee that a set of benign targets is chained together ending with the sentinel but they do not guarantee that the right order of exceptions is executed nor the right number of exception handlers. GCC encodes all exception information in external tables.

When an exception is thrown, the tables are consulted to learn which destructors need to run and what handlers are registered for the current location of the instruction pointer. This results in less overhead in the non-exception case (as additional code is only executed *on-demand* but otherwise jumped over).

The information tables can become large and heavyweight compression is used, namely an interpreter that allows on-the-fly construction of the necessary data. The efficient encoding has a downside: the interpreter of the encoding can be abused for Turing-complete computation [25].

## 6.4.5 Fortify Source

Format string vulnerabilities allow an attacker to read or write arbitrary memory locations.

A format string vulnerability allows the adversary to control the first argument to a printf function. See Section 8.2.2 for more details on format string vulnerabilities.

To counter format string vulnerabilities, Microsoft simply deprecated the %n modifier. This stops the arbitrary write primitive but still allows the adversary to leak memory contents under format string vulnerabilities.

For Linux, an extra check is added for format strings:
(i) check for buffer overflows (i.e., only benign elements are accessed), (ii) check that the first argument is in a read-only area, and (iii) check if all arguments are used. Linux checks the following functions: mem{cpy,pcpy,move,set}, str{n}cpy, stp{n}cpy, str{,n}cat, {,v}s{,n}printf. The GCC/glibc fortify source patch distinguishes between four different cases: (i) known correct - do not check; (ii) not known if correct but checkable, i.e., compiler knows the length of the target - do check; (iii) known incorrect - compiler warning and do check; and (iv) not known if correct and not checkable - no check, overflows may remain undetected.

## 6.4.6 Control-Flow Integrity

Control-Flow Integrity (CFI) [1,4] is a defense mechanism that protects applications against control-flow hijack attacks. A successful CFI mechanism ensures that the control-flow of the application never leaves the predetermined, valid control-flow that is defined at the source code/application level. This means that an attacker cannot redirect control-flow to alternate or new locations. CFI relies on a static, often compile-time analysis that infers the control-flow graph of the application. This analysis constructs a set of valid targets for each indirect, forward edge, controlflow transfer. For example, a function pointer of type void
(*funcPtr)(int, int) may only point to the functions in the program that match the prototype and are address taken. At runtime, CFI uses instrumentation to check if the observed value of the function pointer is in the set of statically determined valid targets. Figure 6.6 shows a CFI check and the target set
(and target reduction).

Given indirect forward control-flow transfers (calls through function pointers in C/C++ or virtual dispatch in C++), what are valid targets of these control-flow transfers? A precise control-flow graph of the application lists all these valid targets but creating a precise control-flow graph is challenging due to aliasing, i.e., it is hard to infer the possible valid values of a code pointer through a static analysis. The best static CFI analysis would infer the precise set of targets for each location based on context and flow sensitive alias analysis, potentially with dynamic path tracking [4].

Due to the complexity of the analysis, existing CFI mechanisms focus on alternate schemes to detect the sets of valid targets on a per-location basis. The simplest CFI analysis scheme simply uses the set of valid functions where any valid function can be called from any indirect control-flow transfer location.

Another, more involved scheme counts the number of arguments and creates one set for each count, i.e., all functions without arguments, functions with 1 argument, functions with two arguments, and so on. The current state of the art for C CFI analysis leverages the function prototype and creates one set of targets per function prototype. For C, the scheme can be improved by measuring which functions are address taken. Only functions that are address taken and somewhere assigned to a function pointer can be used at runtime as pointer arithmetic on function pointers is undefined. For C++, this scheme is improved through class hierarchy analysis. The call site uses a certain type and, given a class hierarchy which must be available, only this type and subtypes in the inheritance chain are allowed for this call location.
```
0xf000b400
**int** bar1(int b, int c, **int** d);

**int** bar2(**char** *str);

**void** bar3(**char** *str);

**void** B::foo(**char** *str);

**class** Greeter :: Base {... }; 
**void** Base::bar5(**char** *str);

**void** Greeter::sayHi(**char** *str);

**class** Related :: Greeter {... }; 
**void** Related::sayHi(**char** *str);

Greeter *o = **new** Greeter(); 
o->sayHi(**char** *str);
```
Listing 6.6: Example of precision trade-offs for different CFI
policies.

In the example above, let us look at the sayHi call in the last line. The valid function policy would allow all functions except the raw address 0xf000b400 which points somewhere into the code area (but not to a valid function). The arity policy would allow the set of bar2, bar3, foo, Base::bar5, Greater::sayHi , Related::sayHi. The function prototype policy removes bar2 from the previous set, resulting in bar3, foo, Base::bar5, Greater::sayHi , Related::sayHi.

Note that for C, this is the most precise prototype-based analysis possible. For the class hierarchy analysis, only the two functions Greater::sayHi , Related::sayHi are in the set, producing the smallest set of targets.

The different CFI analysis schemes provide a trade-off between security (precision) and compatibility. Given imprecise (unsafe) C code, the prototype-based check may fail for benign code.

While this is an actual bug that should be fixed, some people argue that a mitigation should never prohibit benign code.

Therefore, Microsoft uses the valid function policy for their Control-Flow Guard implementation of the CFI policy while Google uses the function prototype for C and the class hierarchy analysis for C++ code in the LLVM-CFI implementation. CFI is an efficient mitigation to stop control-flow hijack attacks but is no panacea. CFI allows the underlying bug to fire and the memory corruption can be controlled by the attacker. The defense only detects the deviation after the fact, i.e., when a corrupted pointer is used in the program. Attackers are free to modify arbitrary data and can leverage complex programs to execute arbitrary computation without hijacking control flow. Alternatively, imprecision in the analysis allows attackers to choose arbitrary targets *in the set of valid targets* for each control-flow location.

## 6.4.7 Code Pointer Integrity

Code Pointer Integrity (CPI) [16] is a defense mechanism that protects applications against control-flow hijacking attacks.

While memory safety and type safety would protect against all control-flow hijack attacks it results in a prohibitive overhead when enforced on top of low-level languages. Conceptually, memory safety protects code pointers against compromise. Memory safety and type safety protect the integrity of all pointers in a program. Unfortunately, memory safety and type safety result in prohibitive overhead.

The core idea of CPI is to restrict memory safety to sensitive pointers. Sensitive pointers are code pointers and pointers that, directly or indirectly, point to code pointers. Enforcing integrity
(memory safety) for these pointers guarantees that a bug in the program cannot modify these pointers and thereby cannot hijack the control-flow. CPI is implemented as a compiler pass that moves sensitive pointers to a safe (sandboxed) memory area that is protected from adversarial access. Note that CPI does not enforce type safety for sensitive pointers.

## 6.4.8 Sandboxing And Software-Based Fault Isolation

In various contexts both trusted and untrusted code must run in the same address space. The untrusted code must be sandboxed so that it cannot access any of the code or data of the trusted code while the trusted code may generally access code and data of the untrusted code. The untrusted code may only read/write its own data segment (and stack). Such a compartmentalization primitive allows powerful use-cases, e.g., running a binary plugin in the address space of a browser without giving it access to the browser's sensitive data or mitigations (with potentially verified code) that keep sensitive values protected from the remaining large code base that may contain bugs. On the 32-bit version of x86 segment registers allowed a separation of address spaces with segment registers enforcing a hard separation. Unfortunately, in the x86_64 extension, segment boundaries are no longer enforced. Software-based Fault Isolation is a way to implement such a separation of the address space between trusted and untrusted parties. The memory access restriction can be implemented through masking each memory access with a constant: and rax, 0x00ffffff; mov [rax], 0xc0fe0000.

The mask in the example restricts the write to the low 24 bit/16 MB of the address space.

Assuming that SFI is implemented by adding additional checks before a memory write then SFI could be bypassed by using an indirect jump to transfer control flow past the check but before the write. On CISC architectures, a jump may even transfer control into an instruction to execute an unintended instruction (e.g., on x86, mov $0x80cd01b0, (%rax) contains mov $1, %al; int $0x80). All indirect jumps therefore have to be aligned to valid instruction beginnings and for write instructions to before the check.

## 6.5 Summary

Several mitigations stop exploitation of unpatched or unknown memory and type safety vulnerabilities. Mitigations have low or negligible performance or runtime overhead due to the unquantified risk of bugs. Data Execution Prevention stops code injection attacks, but does not stop code reuse attacks. Address Space Layout Randomization is probabilistic, shuffles memory space and is prone to information leaks. Stack Canaries are probabilistic, do not protect against direct overwrites and are prone to information leaks. Safe Exception Handling protects exception handlers, reuse of handlers remains possible. Fortify source protects static buffers and format strings. These defenses fully mitigate code injection and probabilistically or partially mitigate code reuse and control-flow hijack attacks. Novel defenses further increase the cost for an attacker to build a working exploit and reduce the chances of success. Shadow stacks enforce stack integrity and protect against return oriented programming. Control-Flow Integrity restricts forward-edge control-flow transfers to a small set. Sandboxing and Software-based Fault Isolation limit unsafe modules to a small area of code and/or data.