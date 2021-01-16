
def is_prime(n):
    if(n <= 1):
        return False

    for i in range(2,n):
        if (n % i == 0):
            return False

    return True

def sum_primes(M):
    sum = 0

    for i in range(2, M+1):
        if(is_prime(i)):
            sum = sum + i

    return sum

def getinput():
    print("Check if number is prime.")
    print("Use -1 to exit. \n")
    try:
        val = int(input("Please enter an integer >= 2: "))
        if(val < 2 and val != -1):
            print("Integer must be >= 2! Please try again.\n")
            getinput()
    except ValueError:
        print("No valid integer! Please try again.\n")
        getinput()
    if(val == -1):
        exit()
    if(is_prime(val)):
        print(str(val) + " is prime!")
    else:
        print(str(val) + " is not prime!")

    sum = sum_primes(val)
    print("Sum of primes from 2 to "+str(val)+ " is "+str(sum)+"!\n")
    getinput()

getinput()
