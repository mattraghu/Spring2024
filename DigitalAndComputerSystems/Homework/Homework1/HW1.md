# Homework 1 - Digital and Computer Systems Architecture

## Problem 1 - Write characteristics of the six different classes of computers. (15 Points)

### Personal Computers

- General Purpose with a variety of software
- Cost/Performance tradeoff

### Server Computers

- Used for running programs for multiple users
- Network based
- High cap, performance, and reliability
- Ranges from very small to very large

### Supercomputers

- Used for complex scientific and engineering calculations
- High performance but lowest fraction of market

### Embedded Computers

- Hidden inside everyday objects
- Power/Performance/Cost tradeoff is important

## Problem 2 - What are the three levels of program code? Describe each level. (15 Points)

### High-Level Language

Level of abstraction that is closer to human language. It is easier to read and write. Additionally, it is ideal for portability and productivity.

### Assembly Language

Essentially a human-readable version of machine code. It is a low-level language that is specific to a particular computer architecture.

### Hardware Representation

The lowest level. It's the actual binary code that the computer reads and executes. Encoded in the form of 1s and 0s.

## Problem 3 - Discuss five components of a computer? Give at least two examples for each component. (10 Points)

### User Interface

The part of the computer that allows the user to interact with the computer. Examples include the keyboard and mouse.

### Storage

The part of the computer that stores data. Examples include hard drives and SSDs.

### Network

The part of the computer that allows it to communicate with other computers. Examples include Ethernet and Wi-Fi.

## Problem 4 - State Amdahl’s law. (5 Points)

It allows us to calculate the speedup of a program when only a portion of the program is sped up. It is given by the formula:

$$
T_{improved} = \frac{T_{affected}}{\text{Improvement Factor}} + T_{unaffected}
$$

Where:

- $T_{improved}$ is the improved time (The total time it takes to run the program after the improvement)
- $T_{affected}$ is the affected time (The time it takes to run the portion of the program being sped up before the improvement)
- $T_{unaffected}$ is the unaffected time (The time it takes to run the portion of the program not being sped up before the improvement)

## Problem 5 - Consider three different processors P1, P2, and P3 executing the same instruction set. If the processors each execute a program in 10 seconds, find the number of cycles and the number of instructions for each processor? (20 Points)

### Processor 1

- Clock Rate: 3 GHz
- CPI (Cycles per Instruction): 1.5

$$
\begin{align*}
10 \text{ seconds} * 3E9 \text{ cycles/second} = 3E10 \text{ cycles} \\
3E10 \text{ cycles} * \frac{1 \text{ instruction}}{1.5 \text{ cycles}} = 2E10 \text{ instructions}
\end{align*}
$$

### Processor 2

- Clock Rate: 2.5 GHz
- CPI (Cycles per Instruction): 1.0

$$
\begin{align*}
10 \text{ seconds} * 2.5E9 \text{ cycles/second} = 2.5E10 \text{ cycles} \\
2.5E10 \text{ cycles} * \frac{1 \text{ instruction}}{1 \text{ cycle}} = 2.5E10 \text{ instructions}
\end{align*}
$$

### Processor 3

- Clock Rate: 4 GHz
- CPI (Cycles per Instruction): 2.2

$$
\begin{align*}
10 \text{ seconds} * 4E9 \text{ cycles/second} = 4E10 \text{ cycles} \\
4E10 \text{ cycles} * \frac{1 \text{ instruction}}{2.2 \text{ cycles}} = 1.818E10 \text{ instructions}
\end{align*}
$$

## Problem 6 - Consider two different implementations of the same ISA. The instructions can be divided into classes as follows (Classes A, B, C, D): (35 Points)

| Class    | A   | B   | C   | D   |
| -------- | --- | --- | --- | --- |
| CPI (P1) | 1   | 2   | 3   | 3   |
| CPI (P2) | 2   | 2   | 2   | 2   |

P1 and P2 have clock rate of 2.5 GHZ and 3.0 GHZ, respectively. Given a program of
Dynamic Instruction count of 1.0E6 instructions divided into classes as follows: 10% class A, 20% class B, 50% class C and 20% class D.

#### P1

$$
\begin{align*}
\text{CPI}_{\text{avg}} &= (0.1 * 1) + (0.2 * 2) + (0.5 * 3) + (0.2 * 3) \\
&= 2.6 \text{ cycles/instruction} \\ \\
\text{Cycles} &= 2.6 \text{ cycles/instruction} * 1E6 \text{ instructions} \\
&= 2.6E6 \text{ cycles} \\ \\
\text{Time} &= \frac{2.6E6 \text{ cycles}}{2.5E9 \text{ cycles/second}} \\
&= 1.04E{-3} \text{ seconds}
\end{align*}
$$

#### P2

$$
\begin{align*}
\text{CPI}_{\text{avg}} &= (0.1 * 2) + (0.2 * 2) + (0.5 * 2) + (0.2 * 2) \\
&= 2 \text{ cycles/instruction} \\ \\
\text{Cycles} &= 2 \text{ cycles/instruction} * 1E6 \text{ instructions} \\
&= 2E6 \text{ cycles} \\ \\
\text{Time} &= \frac{2E6 \text{ cycles}}{3E9 \text{ cycles/second}} \\
&= 6.67E{-4} \text{ seconds}
\end{align*}
$$

#### Which is faster?

**P2** is faster.

#### What is the average CPI for each implementation?

**P1:** 2.6 cycles/instruction

**P2:** 2 cycles/instruction

#### How many clock cycles for each case?

**P1:** 2.6E6 cycles

**P2:** 2E6 cycles
