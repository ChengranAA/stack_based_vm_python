"""
This script defines a simple virtual machine (VM) and an assembly-like language to execute instructions on it.
The VM has several registers, including a stack pointer (sp), program counter (ip), accumulator (acc), and compare (cmp) register.
The script implements various operations like pushing and popping values from a stack, arithmetic addition, conditional branching, and comparison checks.

The `VM` class contains methods for each instruction supported by the VM. Notable methods include:
- `START()`: Initializes the VM's registers and stack.
- `PUSH(value)`: Pushes a value onto the stack.
- `POP()`: Pops a value from the stack.
- `ADD()`: Pops values from the stack, adds them, and pushes the result back onto the stack.
- `HLT()`: Halts the VM, resetting its registers and stack.
- `JMP(value)`: Jumps to a specified instruction index.
- `SUM()`: Updates the compare register based on the accumulator.
- `CMP(value)`: Compares the value in the compare register with the specified value.

The script then creates an instance of the `VM` class and adds a series of assembly-like instructions to its instruction list.
These instructions perform a basic computation: pushing two values onto the stack, adding them, accumulating the result, popping the stack,
comparing the accumulated value to 20, and jumping back two instructions if the comparison condition is met.

During execution, the script displays the state of the VM's registers and stack after each instruction is executed.
The user is prompted to press Enter to step through the instructions.

This script provides a simplified example of how virtual machines can interpret instructions and manage state using registers and a stack.
The assembly-like language showcases the fundamental concepts of instruction sets, memory operations, and control flow.
"""

import sys

RESET = "\033[0m"
GREEN = "\033[92m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
RED = "\033[91m"


class VM:
    def __init__(self):
        self.sp = 0 # stack pointer register
        self.ip = 0 # program counter register
        self.acc = 0 # accumulator register
        self.cmp = 0 # compare register
        self.halt = False
        self.stack = [0,0,0,0,0]
        self.instructions = []
        
    def step(self):
        self.ip += 1
    
    # Instruction sets
    def START(self):
        self.stack = [0,0,0,0,0]
        self.sp = 0
        self.acc = 0
        self.step()
        
    
    def PUSH(self, value):
        self.stack[self.sp] = value
        self.sp += 1
        self.step()
        return 0 
    
    def POP(self):
        if self.sp == 0:
            print("Last stack reached. Couldn't pop.")
            sys.exit(64)
        self.sp -= 1
        self.step()
        return 0
    
    def ADD(self):
        self.acc = 0
        self.sp -= 1
        while True:
            self.acc += int(self.stack[self.sp])
            self.sp -= 1
            if self.sp == 0:
                self.acc += int(self.stack[self.sp])
                self.stack[self.sp] = self.acc
                break
        self.sp += 1
        self.step()
        return 0 
    
    def HLT(self):
        self.halt = True
        self.stack = [0,0,0,0,0]
        self.sp = 0
        self.step()
        return 0
    
    def JMP(self, value):
        self.ip = int(value) -1
        return 
    
    def SUM(self):
        self.cmp += self.acc
        self.step()
    
    def CMP(self, value):
        if self.cmp >= int(value):
            self.halt = True
        else:
            self.step()
        return 0
    
    def print_stack(self, instruction):
        print("==============REGISTERS==============")
        print(BLUE+ "SP: "+RESET, self.sp, end=" | ")
        print(RED+ "IP: "+RESET, self.ip, end=" | ")
        print(YELLOW+"ACC: "+RESET, self.acc, end=" | ")
        print(MAGENTA+"CMP: "+RESET, self.cmp)
        print("================STACK================")
        for add, value in enumerate(self.stack):
            print("#{}:".format(add), end="\t")
            print("0x{:04X}".format((int(value))), end= "\t\t")
            print(value, end="    ")
            if add == self.sp:
                print(GREEN + "<- sp" + RESET)
            else:
                print()
        print("--------------------------------------")
        print(GREEN+"Current instruction:   "+RESET, instruction)
        if self.halt is True:
            print(GREEN+"Next instruction:      "+RESET)
        else:
            print(GREEN+"Next instruction:      "+RESET,  self.instructions[self.ip])
        print()
        print()
        
    def assembler(self):
        instruction = self.instructions[self.ip]
        try:
            operator, operand = instruction.split(' ')
        except ValueError:
            try:
                operator = instruction
            except:
                print("Wrong Instruction")
        if operator == "START": self.START()
        if operator == "HLT": self.HLT()
        if operator == "PUSH": self.PUSH(operand)
        if operator == "ADD": self.ADD()
        if operator == "POP": self.POP()
        if operator == "JMP": self.JMP(operand)
        if operator == "ACC": self.SUM()
        if operator == "CMP": self.CMP(operand)
        return instruction # this is for the print_stack() method
    
    def run(self):
        while not self.halt:
            instruction = self.assembler()
            self.print_stack(instruction)
            input()
                

if __name__ == "__main__":
    # initilize VM
    stack = VM()
    
    # Add assembly instructions
    stack.instructions.append("START")
    stack.instructions.append("PUSH 1")
    stack.instructions.append("PUSH 2")
    stack.instructions.append("ADD")
    stack.instructions.append("SUM")
    stack.instructions.append("POP")
    stack.instructions.append("CMP 20")
    stack.instructions.append("JMP 2")
    stack.instructions.append("HLT")
    
    # run 
    stack.run()
    