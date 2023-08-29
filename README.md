# Stack Based Virtual Machine Simulator

This simple virtual machine simulator is a Python script that demonstrates the basic functioning of a virtual machine by interpreting an assembly-like language and executing a sequence of instructions. This project provides a hands-on exploration of how virtual machines work, how they manage memory, registers, and control flow, and how instructions are processed.

The available instructions include: 

- `START`: Initializes the VM's registers and stack. 
-  `PUSH value`: Pushes a value onto the stack. 
-  `POP`: Pops a value from the stack. 
-  `ADD`: Pops values from the stack, adds them, and pushes the result back onto the stack. 
-  `HLT`: Halts the VM, resetting its registers and stack. 
-  `JMP value`: Jumps to a specified instruction index. 
-  `SUM`: Updates the compare register based on the accumulator. 
-  `CMP value`: Compares the value in the compare register with the specified value.

## How to run

```python
from stack-based-vm import VM
# new
vm = VM()

# add instructions
vm.instructions.append("START")
vm.instructions.append("PUSH 1")
vm.instructions.append("HLT")

# run 
vm.run() # hit <Enter> to proceed
```



