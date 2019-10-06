'''
Given a list of distinct ints, return all possible permutations

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

def permute(nums):
    N = len(nums)
    # store all results
    results = []
    # used[i] True if ith num used in curr
    used = [False for _ in range(N)]

    def recursive_backtrack(curr):
        if len(curr) == N: # end condition 
            results.append(curr.copy()) # use curr.copy() since curr tracks all solutions, it eventually becomes []
            return

        for i in range(N):
            if not used[i]:
                curr.append(nums[i])
                used[i] = True

                # move to next solution
                recursive_backtrack(curr)

                # backtrack to previous partial state
                curr.pop()
                used[i] = False

    # start with curr=[]
    recursive_backtrack([])
    return results

permute((1,2,3))
