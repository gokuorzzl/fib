def fib(n):
    if n == 1:
        return 1
    else:
        if n == 0:
            return 0
        else:
            return fib(n-2) + fib(n-1)

def main():
    n = input('피보나치 수열 n번째 값은?')
    n = int(n)
    print(fib(n))

if __name__ == '__main__':
    main()

