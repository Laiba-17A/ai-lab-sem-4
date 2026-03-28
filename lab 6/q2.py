
'''Task 2 Implement the Hill Climbing algorithm to maximize the function

f(x)=−x*2+10x+5 where 0 ≤ x ≤ 100

Start from a random value of x, check neighbors (x–1 and x+1), and move
to a better neighbor until no improvement is possible. Run it multiple times.'''

import random

# Objective function
def f(x):
    return -x*x + 10*x + 5

# Hill Climbing
def hill_climbing():
    x = random.randint(0, 100)

    while True:
        current_value = f(x)

        # neighbors
        left = x - 1 if x > 0 else x
        right = x + 1 if x < 100 else x

        left_value = f(left)
        right_value = f(right)

        # choose best neighbor
        if left_value > current_value:
            x = left
        elif right_value > current_value:
            x = right
        else:
            break  # no improvement

    return x, f(x)


# Run multiple times
for i in range(5):
    x, value = hill_climbing()
    print(f"Run {i+1}: x = {x}, f(x) = {value}")
