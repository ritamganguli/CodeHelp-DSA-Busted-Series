arr=[1,2,4,5,6,10]
k=int(input())
# If we Use Linear Search It Will Be Like
for i in range(len(arr)):
    if arr[i]==k:
        print(i)
#While Using Binary Search Print Index And If Not Return -1
start=0
end=len(arr)
mid=int((start+end)/2)
a=-1
while(start<=end):
    mid=int((start+end)/2)
    if arr[mid]==k:
        a=(mid)
        break
    if arr[mid]<k:
        start+=mid+1
    if arr[mid]>k:
        end=mid-1
print(a)
