#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear - O(n)
    The number of additional operations the algorithm needs to perform grows in direct proportion to the increace in input size(n) 

b) Exponential - O(n!)
    The number of operations being performed as an exponential function of the input size n. The number of nested loops increases as a function of the input size

c) Constant - O(1)
    The runtime or space used is not affected by the size of the input

## Exercise II

# Understand
# -- Eggs get broken if n >= f, ! if n < f
# -- Find the value of f while dropping/breaking as few eggs as possible

# Plan
# -- Recursive or iterative sort? 
# -- Create an empty list to hold the floors:
#   -- floors = []
# -- Add floors to it if > 0
#   -- if cur_floor > 0:
#       -- floors.append(cur_floor) 
# -- Write f() with floors, cur_floor, eggs parameters
# -- Find base case:
#   -- if n == 0:
#       -- return value of eggs 
# -- As n increases, # of broken eggs increases
# -- Split floors list // 2 & use quicksort to find lhs/rhs of f

# Runtime complexity would probably be O(n log n)