'''
Basic python stuff
(continued)
'''

'''
# 1: Elements are unique?
'''
def all_elements_unique(input_list):
	dictionary={}
	for element in input_list:
		dictionary[element]=0 #initialize
	for element in input_list:
		dictionary[element]+=1 #count each time that element occurs
	unique=0
	for element in dictionary:
		if dictionary[element] > 1: #if dictionary has more than one occurrence
			unique+=1 #add to counter
		else:
			unique+=0
	if unique > 0:
		return "False" #return conclusion based on count of non unique dictionary items
	else:
		return "True"
			

'''
# 2: Second largest element in a list
'''
def second_largest(input_list):
	max=input_list[0]
	for number in input_list:
		if number > max:
			max=number #determine initial maximum number
	newlist=[]
	for number in input_list:
		if number is not max:
			newlist.append(number) #re-append every number BUT the maximums to new list
	newmax=newlist[0]
	for number in newlist:
		if number > newmax:
			newmax=number #determine new maximum number (second to largest in original list)
	return newmax

'''
# 3: Average of Positives
'''

def avg_of_positives(input_list):
	positives=[]
	total=0
	for number in input_list:
		if number >= 0:
			positives.append(number) #append to new list
			total+=number #sum over positive numbers
	return(total / len(positives) )
	
if __name__ == '__main__' :
	print(all_elements_unique(['banana','python','forest',1000,'1+1','elephant','banana']))
	print(second_largest([2,10,7,10,5,7,4]))
	print(avg_of_positives([1,-4,4,-7,10,6,4,-3]))