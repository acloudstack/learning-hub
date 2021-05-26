def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def add(a, b):
    print('Start - function add')
    """This program adds two
       numbers and return the result"""
    result = a + b
    print('End - function add')
    return result

# add(4, 5)
def main():
    add(1,2)

if __name__ == '__main__':
    main()