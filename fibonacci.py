try:
    num_terms = int(input("Enter the number of terms to generate in the Fibonacci sequence: "))

    if num_terms <= 0:
        raise ValueError("Number of terms should be a positive integer.")

    fib_sequence = [0,1] if num_terms >= 2 else [0] 

    for _ in range(2, num_terms):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    print(f"Fibonacci sequence for {num_terms} terms: {fib_sequence}")

except ValueError as e:
    print(f"Error: {e}")
