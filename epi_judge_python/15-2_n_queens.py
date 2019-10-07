from test_framework import generic_test

def n_queens(n: int):
    def valid(i,j):
        # no need to check for row because we recurse on rows
        # check columns
        if j in queens:
            return False
        return major_diags[i-j] + minor_diags[i+j] == 0 # check diags

    def add(i, j):
        queens.append(j)
        major_diags[i - j] = True
        minor_diags[i + j] = True
    
    def remove(i,j):
        queens.pop()
        major_diags[i-j] = False
        minor_diags[i+j] = False
    
    def backtrack(row):
        if row == n:
            output.append(queens.copy())
            return
        
        for col in range(n):
            if valid(row, col):
                add(row, col)
                backtrack(row + 1)
                remove(row, col)
    
    # jth hill/dale diag is True if queen is on that diag 
    major_diags = [False] * (2*n - 1)
    minor_diags = [False] * (2*n - 1)
    queens = [] # queens[i] is column that the queen is on, on ith row
    output = []
    backtrack(0)
    return output

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
