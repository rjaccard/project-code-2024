The Appendix contains sections on reverse engineering, construction of shell code and ROP chains as well as details on some attack primitives. Currently, the appendix is only a stub but will be extended in the future.

## 8.1 Shellcode

Writing shellcode is an art that focuses on designing useful code that runs under tight constraints. Shellcode executes outside of a program context. Due to the missing context, shellcode can only use variables that are currently in registers, relative to the registers at the time of the exploit, at absolute addresses in the process, or leaked through a prior information leak.

The construction of shellcode often follows constraints of the vulnerability, e.g., only printable ASCII characters or no NULL
bytes. To initialise state for the exploit, shellcode often uses tricks to recover state from the stack or relative addresses such as calling/popping into a register to recover the instruction pointer on x86 32-bit where the EIP register is not directly addressable.

## 8.2 Rop Chains

- Gadgets are a sequence of instructions ending in an indirect control-flow transfer (e.g., return, indirect call, indirect jump)
- Prepare data and environment so that, e.g., pop instructions load data into registers
- A gadget invocation frame consists of a sequence of 0
to n data values and a pointer to the next gadget. The gadget uses the data values and transfers control to the next gadget
Simple ROP tutorial

## 8.2.1 Going Past Rop: Control-Flow Bending

- Data-only attack: Overwriting arguments to exec()
- Non-control data attack: Overwriting is admin flag
- Control-Flow Bending (CFB): Modify function pointer
to valid alternate target
- Attacker-controlled execution along valid CFG - Generalization of non-control-data attacks - Each individual control-flow transfer is valid - Execution trace may not match non-exploit case
Control-Flow Bending research paper

## 8.2.2 Format String Vulnerabilities

Functions that handle format strings (e.g., the printf family)
allow a flexible configuration of the printed data through the first argument (the format string). If an attacker can control the format string then they can often achieve full arbitrary read and write primitives.