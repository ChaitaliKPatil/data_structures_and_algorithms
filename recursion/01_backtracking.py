# printing or performing the actions the opposite way as that of the loop is running or in the back order of the track. -- backtracking


def reverse_order_print(i, N):
    if i > N: return
    reverse_order_print(i +1, N)
    print(i)

def same_order_backtrack(i, N):
    if i < 1: return
    same_order_backtrack(i-1, N)
    print(i)

N = 10
reverse_order_print(1, N)
same_order_backtrack(N, N)