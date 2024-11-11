def rounding_error():
    # Demonstrates common rounding error (due to the binary representation of decimal numbers, some values cannot be represented exactly)
    a = 0.1 + 0.2
    print("Rounding error example:", a)

def addition_of_large_and_small_numbers():
    # Demonstrates that adding very large and very small numbers can result in the small number being ignored due to the limited precision 
    a = 1e10
    b = 1e-10
    result = a + b
    print("Addition of large and small numbers result:", result)

def infinite_loop_example():
    # Demonstrates an infinite loop due to floating-point inaccuracy (`b` never exactly equals `a`)
    a = 1
    b = 0.1
    while b != a:
        print(b)
        b += 0.1

def infinite_loop_solution():
    # Solution to avoid infinite loop using epsilon (very small tolerance)
    a = 1
    b = 0.1
    epsilon = 1e-9
    while abs(b - a) > epsilon:
        print(b)
        b += 0.1

def fixed_point_operations():
    # Demonstrates simple fixed-point arithmetic example which allows for consistent precision without the rounding errors
    SCALE = 1000
    a = 10123
    b = 5679
    result = a + b
    print("Fixed-point operation result:", result / SCALE)

def main():
    rounding_error()
    addition_of_large_and_small_numbers()
    # infinite_loop_example()
    infinite_loop_solution()
    fixed_point_operations()

if __name__ == "__main__":
    main()
