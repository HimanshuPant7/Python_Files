def fibonacci_number(n):
    if n <= 1:
        return n
    a=0
    b=1
    for i in range(input_n-1):
        c=b+a
        a=b
        b=c
    return c

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))


