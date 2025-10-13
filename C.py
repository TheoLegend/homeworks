def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return ~a & 1  # Ensure result is 0 or 1

def XOR(a, b):
    return a ^ b

def simulate_circuit(A, B, C, D):
    part1 = AND(A, B)
    part2 = XOR(NOT(C), D)
    output = OR(part1, part2)
    return output

# Example usage
if __name__ == "__main__":
    print("Enter inputs (0 or 1) for A, B, C, D:")
    try:
        A = int(input("A: "))
        B = int(input("B: "))
        C = int(input("C: "))
        D = int(input("D: "))
        
        if all(x in [0, 1] for x in [A, B, C, D]):
            result = simulate_circuit(A, B, C, D)
            print(f"Output of the circuit: {result}")
        else:
            print("Inputs must be 0 or 1.")
    except ValueError:
        print("Please enter valid binary inputs (0 or 1).")
