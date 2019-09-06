


def calculate_twice_profit(A): # returns total profit, buy/sell twice
    
    max_profit = 0

    left_subarray = []
    right_subarray = []

    for i in range(len(A)):
        left, right = A[:i], A[i:]
        curr_profit = calc_max_profit(left) + calc_max_profit(right)
        if curr_profit > max_profit:
            max_profit = curr_profit
    
    return max_profit


def calc_max_profit(A): # returns total profit
    if len(A) == 0: # pythonic syntax for empty array, `[]`
        return 0

    max_profit = 0
    min = A[0]
    max = A[0]
    for i in A:
        if i > max:
            max = i
        if i < min:
            min = i
            max = i
        if (max - min) > max_profit:
            max_profit = max-min
        
    return max_profit




print(calc_max_profit((3,5,1,6,2,7))) # -> 6
print(calc_max_profit([7])) # -> 0
print(calc_max_profit([7,1])) # -> 0
print(calc_max_profit([1,7])) # -> 6

print(problem([3,5,1,6,2,7])) # -> 10