def fizzbuzz(x):
    if x % 15 == 0:
        return 'FizzBuzz'
    if x % 5 == 0:
        return 'Buzz'
    if x % 3 == 0:
        return 'Fizz'
    return x

def umACem():
    map(fizzbuzz, range(1, 101))
