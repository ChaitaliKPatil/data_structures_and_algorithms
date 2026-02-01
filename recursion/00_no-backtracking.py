# printing or performing the actions the same way as the loop is running or in the order of the track.

def order_print(i, N):
    if i > N: return
    print(i)
    order_print(i + 1, N)

N = 10
order_print(1, N)