#include <iostream>
#include <vector>

const std::string RESET = "\033[0m";
const std::string GREEN = "\033[92m";
const std::string BLUE = "\033[94m";
const std::string MAGENTA = "\033[95m";
const std::string YELLOW = "\033[93m";
const std::string RED = "\033[91m";

class VM {
public:
    VM() : sp(0), ip(0), acc(0), cmp(0), halt(false) {
        stack = std::vector<int>(5, 0);
        instructions = std::vector<std::string>();
    }

    void append(std::string instruction){
        instructions.push_back(instruction);
    }

    void step() {
        ip += 1;
    }

    void START() {
        stack = std::vector<int>(5, 0);
        sp = 0;
        acc = 0;
        step();
    }

    int PUSH(int value) {
        stack[sp] = value;
        sp += 1;
        step();
        return 0;
    }

    int POP() {
        if (sp == 0) {
            std::cout << "Last stack reached. Couldn't pop." << std::endl;
            std::exit(64);
        }
        sp -= 1;
        step();
        return 0;
    }

    int ADD() {
        acc = 0;
        sp -= 1;
        while (true) {
            acc += stack[sp];
            sp -= 1;
            if (sp == 0) {
                acc += stack[sp];
                stack[sp] = acc;
                break;
            }
        }
        sp += 1;
        step();
        return 0;
    }

    int HLT() {
        halt = true;
        stack = std::vector<int>(5, 0);
        sp = 0;
        step();
        return 0;
    }

    void JMP(int value) {
        ip = value - 1;
    }

    void SUM() {
        cmp += acc;
        step();
    }

    int CMP(int value) {
        if (cmp >= value) {
            halt = true;
        } else {
            step();
        }
        return 0;
    }

    void print_stack(const std::string& instruction) {
        std::cout << "==============REGISTERS==============" << std::endl;
        std::cout << BLUE << "SP: " << RESET << sp << " | ";
        std::cout << RED << "IP: " << RESET << ip << " | ";
        std::cout << YELLOW << "ACC: " << RESET << acc << " | ";
        std::cout << MAGENTA << "CMP: " << RESET << cmp << std::endl;
        std::cout << "================STACK================" << std::endl;
        for (size_t add = 0; add < stack.size(); ++add) {
            std::cout << "#" << add << ":";
            std::cout << "\t";
            std::cout << "0x" << std::hex << stack[add];
            std::cout << "\t\t";
            std::cout << std::dec << stack[add] << " ";
            if (add == sp) {
                std::cout << GREEN << "<- sp" << RESET;
            }
            std::cout << std::endl;
        }
        std::cout << "--------------------------------------" << std::endl;
        std::cout << GREEN << "Current instruction:   " << RESET << instruction << std::endl;
        if (halt) {
            std::cout << GREEN << "Next instruction:      " << RESET << std::endl;
        } else {
            std::cout << GREEN << "Next instruction:      " << RESET << instructions[ip] << std::endl;
        }
        std::cout << std::endl;
        std::cout << std::endl;
    }

    void assembler() {
        std::string instruction = instructions[ip];
        size_t spacePos = instruction.find(' ');
        std::string Operator, Operand;
        if (spacePos != std::string::npos) {
            Operator = instruction.substr(0, spacePos);
            Operand = instruction.substr(spacePos + 1);
        } else {
            Operator = instruction;
        }
        if (Operator == "START") START();
        if (Operator == "HLT") HLT();
        if (Operator == "PUSH") PUSH(std::stoi(Operand));
        if (Operator == "ADD") ADD();
        if (Operator == "POP") POP();
        if (Operator == "JMP") JMP(std::stoi(Operand));
        if (Operator == "SUM") SUM();
        if (Operator == "CMP") CMP(std::stoi(Operand));
    }

    void run() {
        while (!halt) {
            std::string instruction = instructions[ip];
            assembler();
            print_stack(instruction);
            std::cin.ignore();
        }
    }

private:
    int sp; // stack pointer register
    int ip; // program counter register
    int acc; // accumulator register
    int cmp; // compare register
    bool halt;
    std::vector<int> stack;
    std::vector<std::string> instructions;
};

int main() {
    VM stack;

    stack.append("START");
    stack.append("PUSH 1");
    stack.append("PUSH 2");
    stack.append("ADD");
    stack.append("SUM");
    stack.append("POP");
    stack.append("CMP 20");
    stack.append("JMP 2");
    stack.append("HLT");

    stack.run();

    return 0;
}
