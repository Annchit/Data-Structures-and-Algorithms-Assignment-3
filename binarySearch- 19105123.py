def binarySearch(arr, l, r, x):

	if r >= l:
		mid = l + (r - l) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binarySearch(arr, l, mid-1, x)
		else:
			return binarySearch(arr, mid + 1, r, x)
	else:
		return -1


n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(0, n):
    element = input("Enter " + str(i) + " index element\n")
    arr.append(int(element))

x = int(input("Number to search: "))

result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index % d" % result)
else:
	print("Element is not present in array")