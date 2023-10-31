def get_last_fibonacci_digit_huge(n):
    if n <= 1:
        return n

    fib_array = [0, 1]
    for i in range(2, n + 1):
        fib_array.append((fib_array[i - 1] + fib_array[i - 2]) % 10)

    return fib_array[n]


if __name__ == "__main__":
    input_n = int(input())
    print(get_last_fibonacci_digit_huge(input_n))
