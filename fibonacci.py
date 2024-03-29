def find_fib(n):
    if n <= 2:
        return 1
    return find_fib(n - 1) + find_fib(n - 2)


n = int(input("Enter a number: "))
for i in range(1, n):
    print(find_fib(i), end=" ")
