arr = input().split()
n = len(arr)

i = j = 0

while(i < n):
    minIndex = i
    j = i+1
    while(j < n):
        if(float(arr[j]) < float(arr[minIndex])):
            minIndex = j
        j += 1
    arr[i], arr[minIndex] = arr[minIndex], arr[i]
    i += 1

print(arr[0]+" "+arr[1]+" "+arr[2])

