import random

def get_computer_choice(computer):
	return random.choice(computer)
	
Computer = get_computer_choice(['Rock','Papper','Scissors'])


def get_user_choice ():
	while True:
		choice = input('please enter Rock, Papper or Scissors')
		if choice == 'Rock':
			return choice
		elif choice  == 'Papper':
			return choice 
		elif choice == 'Scissors':
			return choice		
		else:
			print('please enter Rock, Papper or Scissiors')
     
User = get_user_choice()
		
if Computer =='Rock' and User == 'Scissors':
	print ('Computer wins')
elif Computer =='Rock' and User == 'Papper':
	print ('User wins')
if Computer =='Scissors' and User == 'Rock':
	print ('User wins')
elif Computer =='Papper' and User == 'Rock':
	print ('Computer wins')
else:
	print (' It is a draw!')	