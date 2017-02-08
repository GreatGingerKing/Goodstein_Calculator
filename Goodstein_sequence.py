#This function converts a number in base 10 to a new base. Output is a list.
#For example 10 gives you [1,0,1,0]
def base_converter(number,base,answer):
	#These two lines divide the number by the base you want it to be in and get the principle dividend and remainder 
	remainder=number%base
	dividend=number/base
	#This inserts the remainder the the begging of the list.
	answer.insert(0,remainder)
	#This is the principle logic of this function, if the dividend is zero, you return you list, if it's not, 
	#you recall the function with your new number.
	if dividend==0:
		
		return answer
	else:
		return base_converter(dividend,base,answer)
	
	
#x=base_converter(54532,3,[]) These two lines are bebuging lines.
#print x

def base_converter_medium(number,base):
	numb_base=[]
	
	while number>0:
		#print number
		numb_base.insert(0,(number%base))
		#print numb_base
		number=number/base
		#print number
	return numb_base

#This function takes a number in base 10 and creates it's base notation in a new base. Output is a dictionary
def regular_to_base(number,base):
	#Converts the number to the list. 
	base_number=base_converter_medium(number,base)
	#Intializes the output
	base_num={'coeffecient':[],'base':[],'exponents':[]}
	#Coeffecients of the base notation number is equal to the output of the function.
	base_num['coeffecient']=base_number
	#This for loop creaes a list as long as the coeffecient list and gives it a value equal to the 'base'
	#that you're in for each corresponding non-zero coeffecient.
	for item in base_number:
		if item !=0:
			base_num['base'].append(base)
		else:
			base_num['base'].append(0)
	
	#This last part calculates and fills in the 'exponents' list. 
	for numb in range(0,len(base_number)):
		if base_number[numb] !=0:
			base_num['exponents'].append((len(base_number)-1)-numb)
		else:
			base_num['exponents'].append(0)
	#print hered_num['exponents']
	
	return base_num
#This function takes in a base_notation dictionary are returns a normal base 10 notation number.	
def base_to_regular(base_num):
		answer=0
		for number in range(0,len(base_num['base'])):
			answer+=base_num['coeffecient'][number]*(base_num['base'][number])**(base_num['exponents'][number])
		return answer

#These four lines are degugging lines.		
#thing= regular_to_base(23,2)
#print thing
#thing1=base_to_regular(thing)
#print thing1

#This function takes a number in a goodstein_sequence and computes the next.
#The basic alogrith is that is converts a number into base notation, then checks to see if the exponents qualify it 
#for hereditary base notation. If they don't, this function recalls this function on that number until it's in hereditary
#base notation. Then, the most nested itteration adds one to each exponent and base converts the number back to normal 
#notation and outputs it.
def goodstein_number(number,base):
	#Get's the number in base notation
	base_note=regular_to_base(number,base)
	#print base_note
	#This loop  is a doozy. If first checks to see if it's in Hereditary Base notation.
	#If it is then it increments the sequence by one, computes and outputs. If it's not, it recall's this function
	#on the exponents that aren't in the lowers form.
	for item in range(0, len(base_note['base'])):
		if base_note['exponents'][item] > base:
			base_note['exponents'][item]=goodstein_number(base_note['exponents'][item],base)
		elif base_note['exponents'][item]==base:
			base_note['exponents'][item]+=1
		else:
			pass
		if base_note['base'][item] != 0:
			base_note['base'][item]+=1
		else:
			pass
	output=base_to_regular(base_note)
	#print base_note -degugging
	return output

input_number=int(raw_input("What number would you like to start with?\n"))
#prints out a sequence of goodstein numbers
def goodstein_sequence(number):
	iterations=100
	base=2
	goodstein=number
	print number
	for i in range(0,iterations):
		if goodstein <=0:
			break
		goodstein=goodstein_number(goodstein,base)-1
		base+=1
		print goodstein
		
goodstein_sequence(input_number)	
#print (goodstein_number(1279,4)-1)
		
	