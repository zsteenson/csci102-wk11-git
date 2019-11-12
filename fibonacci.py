def fib():
    fibs = [1, 2]

    for i in range(1,9):
        fibs.append(fibs[i] + fibs[i - 1])
    
    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
