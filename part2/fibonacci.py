import time

def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number -2 )

import random
number = random.randint(15, 35)

start_time = time.time()
result = fibonacci(number)
end_time = time.time()

print("The {number}-th term: {result}")
print("Took {end_time - start_time} seconds")