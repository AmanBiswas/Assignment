def find_leader(arr):
    leader = arr[n - 1]
    leaders = [leader]

    for i in range(n - 2, -1, -1):
        if arr[i] > leader:
            leader = arr[i]
            leaders.append(leader)

    return leaders


arr = [7, 10, 4, 10, 6, 5, 2]
n=7
leaders = find_leader(arr)
print(leaders[::-1])
