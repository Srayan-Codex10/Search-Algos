def binsearch(arr,left,right,val):
	if(left <= right):
		mid = (left+right)//2
		#print(mid)
		if(arr[mid]==val):
			return mid
    
		elif(arr[mid]>=val):
			return binsearch(arr,0,mid-1,val)

		else:
			return binsearch(arr,mid+1,right,val)
	else:
		return -1


# x = [23, 24, 29, 38, 47, 58, 60, 62, 65, 75, 79, 88, 94, 135]
# r = len(x)-1
#n = int(input("Enter number to search: "))
#binsearch(x,0,r,n)
