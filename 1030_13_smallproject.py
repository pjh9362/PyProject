
arr = [1,2,3,4,5,6,7,8,9]

for i in range(len(arr)//2):
    arr[i], arr[0-(i+1)] = arr[0-(i+1)], arr[i]

print("변환된 arr은", arr, "입니다.")

i=0
while i<(len(arr)//2):
    arr[i], arr[0-(i+1)] = arr[0-(i+1)], arr[i]
    i+=1

print("변환된 arr은", arr, "입니다.")


left, right = 0, len(arr)-1

while left<right: #while left<(len(arr)//2)
    arr[left], arr[right] = arr[right], arr[left]
    left+=1
    right-=1

print("변환된 arr은", arr, "입니다.")

