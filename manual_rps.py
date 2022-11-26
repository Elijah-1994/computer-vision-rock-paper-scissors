import random

def play():
	computer = get_computer_choice(['Rock','Paper','Scissors'])
	user = get_user_choice()
	get_winner(computer,user)

def get_computer_choice(computer):
	return random.choice(computer)

def get_user_choice ():
	while True:
		choice = input('please enter Rock, Paper or Scissors')
		if choice == 'Rock':
			return choice
		elif choice  == 'Paper':
			return choice
		elif choice == 'Scissors':
			return choice
			print('please enter Rock, Paper or Scissors')

def get_winner(computer_choice,user_choice):
    if computer_choice == user_choice:
        print ('Its a draw')
    elif (computer_choice =='Rock' and user_choice == 'Scissors') or \
            (computer_choice =='Scissors' and user_choice == 'Paper') or \
            (computer_choice =='Paper' and user_choice == 'Rock'):
                print ('Computer wins')
    else:
        print ('user wins')
play()