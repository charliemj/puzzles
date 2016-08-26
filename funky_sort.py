# https://www.hackerrank.com/challenges/almost-sorted


def is_sorted(n, a, s, b):
	for i in range(1,n):
		if a[i] > a[i-1]:
			if i+1 == len(a) and b==False and s == False:	
				print "sorted"
				return
				
		else:
			x = i-1
			if s == False:
				s = True
				swap(n,a,s,b,x)
			
			else:
				return "sorry nope"

def swap(n,a,s,b,x):
	for j in range(0,len(a)):
		for i in range(j,len(a)):
			tmp = a[:]
			tmp[i],tmp[j] = tmp[j],tmp[i]

			for k in range(1,len(tmp)):

				if tmp[k]<tmp[k-1]:
					break
			else:
				print "swapped and sorted", i, j
				return		
					
	reverse(n,a,s,b,x)
	return
			
	

def reverse(n,a,s,b,x):
	b = True
	rev_list = []
	end_index = x
	for i in range(x+1,len(a)): 
		if a[i] < a[i-1]:
			end_index = i
		else:
			break
	rev_list = a[x:end_index+1]
	rev_list2 = rev_list[::-1]
	new_list = a[0:x]+rev_list2+a[end_index+1:]
	for i in range(1,len(new_list)):
		if new_list[i]>new_list[i-1]:
			pass
		else:
			print "sorry, nope, reversing doesn't help either"
			return 
	print "reversed and sorted"









a = [0,1,2,7,6,5,4,3,8,9]
n = len(a)
#reverse(n,a,True,True,2)
is_sorted(n,a, False, False)




