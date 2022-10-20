import random

def play():
	Computer = get_computer_choice(['Rock','Papper','Scissors'])
	User = get_user_choice()
	get_winner(Computer,User)
	

def get_computer_choice(computer):
	return random.choice(computer)
	

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

def get_winner(Computer_choice,User_choice):
	if Computer_choice =='Rock' and User_choice == 'Scissors':
		print ('Computer wins')
	elif Computer_choice=='Rock' and User_choice == 'Papper':
		print ('User wins')
	elif Computer_choice =='Scissors' and User_choice == 'Rock':
		print ('User wins')
	elif Computer_choice =='Scissors' and User_choice == 'Papper':
		print ('Computer wins')
	elif Computer_choice =='Papper' and User_choice == 'Rock':
		print ('Computer wins')
	elif Computer_choice =='Papper' and User_choice == 'Scissors':
		print ('User wins')
	else:
		print (' It is a draw!')

play()