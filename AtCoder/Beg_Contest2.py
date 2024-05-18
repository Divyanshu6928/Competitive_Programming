def attraction(n,k,a):
    empty_seats = k
    attraction_starts = 0

    for group in a:
        if empty_seats < group:
            attraction_starts += 1
            empty_seats = k - group
        else:
            empty_seats -= group

    if empty_seats < k:
        attraction_starts += 1

    return attraction_starts


n,k = map(int,input().split())
a=list(map(int,input().split()))

print(attraction(n,k,a)) 