# Midterm Study Guide

## Exam Problems

### 1. Convert C++ code snippet to LEGv8 assembly code. The following variables x, y, and z are associated with registers X19, X20, and X21, respectively, and base address of the array d is in X22. Comment on the code.

```cpp
for (i=0; i<x; i++)
{
    y = d[i] + z;
}
```

```assembly
// Create a temporary register to store the size of a double word
SUBS X3, X3, X3
ADDI X3, X3, #8

// Initialize i to 0
SUBS X4, X4, X4

// Loop
Loop:
    // Check if i < x
    SUBS XZR, X4, X19
    B.GE End

    // Get the address of d[i] (X1)
    MUL X1, X4, X3
    ADD X1, X22, X1

    // Get the value of d[i] (X2) and add z to it and store it in y
    LDUR X2, [X1, #0]
    ADD X20, X2, X21

    // Increment i
    ADDI X4, X4, #1

    // Jump to the beginning of the loop
    B Loop

End:




```
