country = input('What is your nationality:')
age = int(input('Enter your age:'))
if country == 'malaysia':  # if the country isn't malaysia it won't execute 
	if age >= 18:
		print('You can apply driving license')
	else:
		print('You cannot apply driving license')
elif country == 'united state':
     if age >= 16:
     	print('You can apply driving license')
     else:
     	print('You cannot apply driving license') 
     		