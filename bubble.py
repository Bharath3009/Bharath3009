def bubble(arr):
    n = len(arr)
    print("length of :",n)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

                
li = ["apple","cat","ball"]

bubble(li)
print(li)