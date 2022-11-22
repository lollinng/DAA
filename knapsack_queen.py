# Fractional

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractionalKnapsack(W, arr):
    
    arr.sort(key=lambda x: (x.value/x.weight), reverse=True) # sorting Item on basis of weight ratio
    finalvalue = 0.0
    for item in arr:
        # If adding item in knapsack won't overflow, add it completely
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value
        else:
            finalvalue += item.value * W / item.weight
            break
    return finalvalue

if __name__ == "__main__":
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    max_val = fractionalKnapsack(W, arr)
    print("Knapsack Capacity:", W)
    print ('Maximum value we can obtain = {}'.format(max_val))


# 0/1 knapsack
# choice when reached the weight level-
# 1) Either accept the previous value or 
# 2) add the new value [weigth index-current_wieght_value]
def knapsack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # Build table K[][] in bottom up manner
    for i in range(n + 1):  # ranging over weights and column
        for w in range(W + 1):  
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] > w: # if smaller than minimum weight how row go up and take its value
                K[i][w] = K[i-1][w]
            else:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
                
    for i in K:
        print(i)
    return K[n][W]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print("Values:", val)
print("Weights:", wt)
print("Knapsack Capacity:", W)
print("Maximum Weight:", knapsack(W, wt, val, n))


# NQueen
print ("Enter the number of queens (N): ")
N = int(input())

# creating the chessboard
board = [[0]*N for _ in range(N)]

def is_attack(i, j):
    
    # checking if there is a queen in row or column
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    
    # checking diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def N_queen(n):
    # if n is 0, solution found
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                if N_queen(n-1)==True:
                    return True
                board[i][j] = 0
    return False
N_queen(N)
for i in board:
    print (i)