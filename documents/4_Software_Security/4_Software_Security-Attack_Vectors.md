# Attack Vectors 

Understanding the intention of an attack helps with assessing the attack surface of a program. Not all attack vectors are feasible for all attacks and not all bugs allow instantiating all attack vectors. Attacker goals can be grouped into three broad classes: Denial of service (DoS); leaking information; and escalation of privileges, with confused deputies a special form of privilege escalation.

## 5.1 Denial Of Service (Dos)

Denial of Service violates the *availability* property. DoS prohibits the legitimate use of a service by either causing abnormal service termination (e.g., through a segmentation fault) or overwhelming the service with a large number of duplicate/unnecessary requests so that legitimate requests can no longer be served. DoS also applies to outside the server setting, e.g., by corrupting a checksum of an image file it will no longer be displayed by an image viewer. This is the easiest attack to achieve as a server simply needs to be overwhelmed with bad requests to drown any legit requests.

## 5.2 Information Leakage

Information leakage violates the *confidentiality* property. Information leaks are abnormal or unintended transfers of sensitive information to the attacker. An information leak abuses an illegal, implicit, or unintended transfer of information to pass sensitive data to the attacker who should not have access to that data.

An attacker can abuse an intended transfer of information and trick the program into sending unintended information (e.g., instead of sending a benign file as intended the server returns a privileged file). Information leaks may be related to memory safety issues or logic errors. If the information leakage is due to a logic error, then the application can be tricked, following a benign path of execution, to leak the information to the attacker. Some information leaks are due to debug statements in the code, e.g., stack trace information that is returned to the user in the case of an exception or crash in a web application or publicly readable log files that record errors and crashes of applications together with auxiliary debug information such as crash addresses.

Memory or type safety violations may be used to leak information. For such leaks, the software flaw corrupts program state to replace or augment benign information with sensitive information. Leaking runtime information of an address space such as pointers, library, stack, or code locations enables bypassing probabilistic defenses such as Stack Canaries or Address Space Layout Randomization as these locations or values are only randomized on a per-process basis and are constant throughout the lifetime of a process.

## 5.3 Confused Deputy

A *confused deputy* is a kind of privilege escalation that tricks a component to execute an unprivileged action with higher privileges. A privileged component is supposed to only use its privileges for a benign action. By carefully setting up its input, an unprivileged attacker can make a privileged component (i.e., the confused deputy) *unintentionally* execute a privileged action
(from the viewpoint of the developer). The confused deputy acts on behalf of the malicious component. The malicious component tricks the confused deputy into abusing its privileges on behalf of the attacker. The name "confused deputy" goes back to Barney Fife, an easily confused deputy who could be tricked into abusing his power in "The Andy Griffith Show" in the 1950s, see Figure 5.1.

The classic example of a confused deputy is a compiler that overwrites its billing file. On old mainframe computing systems customers had to pay for each run of the compiler due to the resources that were used on the mainframe for the compilation process. The compiler had access to a log file that recorded which user invoked the compiler. By specifying the log file as output file, the compiler could be tricked to overwrite the billing file with the executable program. The compiler required access to the log file (to record users) and the user invoking the compiler had the right to specify an output file to specify the new executable. As this compiler did not check if the output file was a special file, it acted as confused deputy. Another, more modern example is Cross-Site Scripting (XSS) which tricks a webpage to execute malicious JavaScript code in the user's browser.

## 5.4 Privilege Escalation

Privilege escalation is an *unintended* increase of privileges (from the viewpoint of the developer).

An example of privilege escalation is gaining arbitrary code execution. Starting from access to the service and constrained to the functions provided by the service, the attacker escalates to arbitrary code execution where she has full access to all files, privileges, and system calls of that service. Another example of privilege escalation is a user without privileges that can modify files owned exclusively by the administrator, e.g., through a misconfiguration of the web interface.

While there are several forms of privilege escalation, we will focus on privilege escalation based on memory or type safety violations. Every such attack starts with a memory or type safety violation. Spatial memory safety is violated if an object is accessed out of bounds. Temporal memory safety is violated if an object is no longer valid. Type safety is violated if an object is cast and used as a different (incompatible) type. Any of these bug types allow a reconfiguration of program state that can trigger a privilege escalation when the legitimate code of the application acts on the corrupted state. In software security, these violations are used to *hijack control-flow*. The control flow is redirected to injected code or existing code that is reused in unintended ways. Alternatively, they can be used to corrupt data. Figure 5.2 shows the different paths an attack can take with the different mitigations that need to be circumvented along the attack flow for code corruption and control-flow hijacking attacks.

## 5.4.1 Control-Flow Hijacking

A successful *Control-Flow Hijacking* attack redirects the application's control-flow to an adversary-controlled location. This attack primitive gives the adversary control over the execution of the program and instruction pointer. Control-flow hijacking is generally achieved by overwriting a code pointer either directly or indirectly. An indirect control-flow transfer such as an indirect call (call rax for x86), indirect jump (jmp rax for x86), or indirect branch (mov pc, r2 for ARM) updates the instruction pointer with a value from a register, continuing control-flow from this new location. The value is often read from writable memory and can therefore be controlled by the attacker. Given code integrity (i.e., benign code cannot be modified), the attacker cannot modify relative control-flow transfers. A direct control-flow transfer is a call or jump to a hard coded location where the target is either in read-only memory or encoded as part of the instruction. For example on x86, function calls are encoded as control-flow transfers relative to the instruction pointers with an offset that is part of the instruction itself. Indirect calls are used to provide flexibility as part of the programming language, e.g., a call through a function pointer in C or a virtual dispatch for C++. Additionally, the return instruction pointer on the stack points back to the location in the calling function. At the programming language level, the target is well defined and given type safety and memory safety, the control-flow of the program is well contained. But given any memory safety or type safety corruption, the value of the target in memory may be overwritten by the attacker.

```
**int** benign();

**void** vuln(**char** *attacker) {
    int (*func)();
    char buf[16];

    // Function pointer is set to benign function
    func = &benign;

    // Buffer overflow may compromise memory safety
    strcpy(buf, attacker);

    // Attacker may hijack control-flow here.
    func();
}
```
Listing 5.1: Buffer overflow into function pointer.

In the code example above, an attacker may supply a buffer that is larger than the local stack buffer. When copying data into the buffer buf, a stack-based buffer overflow may overwrite the function pointer on the stack. This memory safety violation allows the adversary to compromise the stored code pointer func. When func is later dereferenced, the attacker-controlled value is used instead of the original value.

To orchestrate a control-flow hijack attack, an adversary must know the location of the code pointer that will be overwritten and the location of the target address, i.e., where to redirect control-flow to. Additionally, there must be a path from the vulnerability to the location where the attacker-controlled code pointer is dereferenced.

## 5.4.2 Code Injection

Code injection assumes that the attacker can write to a location in the process that is executable.

The attacker can either overwrite or modify existing code in the process, rewriting instructions either partially or completely. Corrupting existing code may allow an attacker to gain code execution without hijacking control flow as a benign control-flow transfer may direct execution to attacker-controlled code. Alternatively, the attacker can hijack control-flow to the injected code. Modern architectures support the separation of code and data, therefore this attack vector is no longer as prevalent as it was. A modern variant of this attack vector targets Just-In- Time compilers that generate new code dynamically. In such environments some pages may be writable and executable at the same time. Code injection requires the existence of a writable and executable memory area, the knowledge of the location of this memory area, and, if the location is not reached through a benign control-flow transfer, a control-flow hijack primitive.

The injected code conforms to shellcode that, depending on the vulnerability, must follow certain guidelines. See Section 8.1 for a discussion of shellcode and its construction. Given the vulnerable code in the example below, an attacker can provide input to overflow the cookie buffer, continuously overwriting information that is higher up on the stack as the strcpy function does not check the bounds of cookie. Assume that this program is compiled without code execution prevention and the program runs without ASLR.

There are several methods to exploit this vulnerability. Controlflow hijacking is achieved by overwriting the return instruction pointer on the stack.

Code may be injected in three locations: (i) the buffer itself, (ii) higher up on the stack frame
"above" the return instruction pointer, or (iii) in an environment variable (the example conveniently reports the location of the EGG environment variable. We therefore prepare the shellcode in the environment variable EGG and overwrite the return instruction pointer to point to the beginning of EGG.

Upon return, instead of returning control flow to the calling function, the shellcode in EGG will be executed, giving the attacker control.

The full input to exploit the vulnerability is: [AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA], [the address of the EGG environment variable], and a [0x0] byte. The first 32 bytes fill the buffer with As, the next 4 bytes overwrite some padding inserted by the compiler, the next 4 bytes overwrite the frame pointer, and the remaining 4 bytes overwrite the return instruction pointer. The exact layout of the stack frame depends on the compiler and may be inferred by analyzing the assembly code.

```
**#include** <stdio.h>
**#include** <stdlib.h>
**#include** <string.h>

**int** main(int argc, **char*** argv[]) {
    char cookie[32];
    printf("Give me a cookie (%p, %p)\n",
        cookie, getenv("EGG"));
    strcpy(cookie, argv[1]);
    printf("Thanks for the %s\n", cookie);
    return 0;
}
```
Listing 5.2: Stack based code injection.

## 5.4.3 Code Reuse

Instead of injecting code, *reuse* existing code of the program.

The main idea is to stitch together existing code snippets to execute new arbitrary behavior. This is also called Return- Oriented Programming (ROP), Jump-Oriented Programming
(JOP), Call-Oriented Programming (COP), Counterfeit-Object Oriented Programming (COOP) for different aspects of code reuse.

Any executable code of the application may be used by the attacker in an alternate way under the constraints of any active mitigation mechanism. Through indirect control-flow transfers, adversaries can chain together small code sequences (called gadgets) that end in another indirect control-flow transfer.

A successful code reuse attack requires (i) knowledge of a writable memory area that contains *invocation frames* (gadget address and state such as register values), (ii) knowledge of executable code snippets (*gadgets*), (iii) control-flow must be hijacked/redirected to prepared invocation frames, and (iv) construction of ROP payload. See Section 8.2 for a discussion on the construction of ROP payloads.

## 5.5 Summary

This chapter presented a broad overview of different attack vectors. We discussed attack vectors from a simple Denial of Service (DoS) that prohibits a legit user from using a service over information leakage that allows an adversary to extract secrets to privilege escalation and confused deputies which both give the adversary additional computation privileges that they would otherwise not have. The goals of adversaries vary and weaknesses in software may be used to achieve different goals. The craft of an attacker is to leverage an exposed bug to trick the underlying program into doing something on the attacker's behalf.