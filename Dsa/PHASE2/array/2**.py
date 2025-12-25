#two pointer approchs

def find_min_max(arr):
    l = 0
    r = len(arr) - 1

    mini = arr[0]
    maxi = arr[0]

    while l <= r:
        if arr[l] < mini:
            mini = arr[l]
        if arr[l] > maxi:
            maxi = arr[l]

        if arr[r] < mini:
            mini = arr[r]
        if arr[r] > maxi:
            maxi = arr[r]

        l += 1
        r -= 1

    print("Min:", mini)
    print("Max:", maxi)



arr=[1,4,4434,2,45,3,23,3]
find_min_max(arr)








