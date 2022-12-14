import cv2
from keras.models import load_model
import numpy as np
import random
import time

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
choices = ["Rock", "Paper", "Scissors", "nothing"]
print ("Welcome to the computer vision Rock, Paper and Scissors game \
       please display Rock, Paper or Scissors to camera.")

class Computer_Vision:
    '''
        This class represents the process of using keras modelling and python methods to create the classic rock paper scissors game.
        
        Attributes:
            self.computer_wins = initialises and updates the computer score.
            self.user_wins = initialises and updates the user score.

    '''
    def __init__(self, computer_wins=0, user_wins=0):
        '''
        See help(Computer_Vision) for accurate signature.
        
        Parameters:
            self.computer_wins = initialises and updates the computer score.
            self.user_wins = initialises and updates the user score
        
        '''
        self.computer_wins = computer_wins
        self.user_wins = user_wins

    def play_game(self) -> str:
        '''
        This method is the main game loop and will open the capture frame and take in the user input and then call the self.get_computer_choice() method 
        to return the computer choice. Then the self.get_winner(computer_choice,user_choice) method is called to determine the winner between the user
        and computer. The scores are updated accordingly and the loop breaks once the user or computer reaches a score of three.
   
        Returns:
            str: returns the winner of the  game.
        
        '''   
        start_time = time.time()
        print_winner = False
        while True:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time > 4.9 and  elapsed_time < 5:
                print("Please show Rock,Paper, or Scissors at the camera.")
                user_choice = self.get_prediction()
                print (f'You chose {user_choice}')
                computer_choice = self.get_computer_choice()
            elif elapsed_time > 5 and elapsed_time < 7:
                if print_winner is False:
                   winner = self.get_winner(computer_choice,user_choice)
                   print (winner)
                   print ("Get ready for the next round. Please display Rock, Paper or Scissors to the camera.")
                   if winner == 'Computer wins':
                       self.computer_wins += 1
                   elif winner == 'user wins':
                       self.user_wins +=1
                   print_winner = True
                   print ("computer score:",self.computer_wins)
                   print ("user score:", self.user_wins)
                   if self.computer_wins == 3:
                       print ("Computer has won 3 rounds. Computer wins. Game over.")
                       return
                   elif self.user_wins == 3:
                       print ("User has won 3 rounds. User wins. Game over.")
                       return
            elif elapsed_time > 7:
                print_winner = False
                start_time = time.time()

    def get_prediction(self) -> str:
        '''
        This method chooses the highest probability based on the user input captured in the frame.
   
        Returns:
            str: The user choice is returned.
        
        '''   
        prediction = model.predict(data)
        highest_index = np.argmax(prediction[0])
        user_choice = choices[highest_index]
        return user_choice

    def get_computer_choice(self):
        '''
        This method chooses the computer choice.
   
        Returns:
            str: The computer choice is returned.
        
        '''  
        computer_choice = random.choice(choices[0:3])
        return computer_choice

    def get_winner(self,computer_choice,user_choice):
        '''
        This method decides on the winner based on the computer and user choice.
   
        Returns:
            str: The winner between the computer and user or a draw.
        
        '''  
        if user_choice == "nothing":
                return("Please put your hand to the camera.")
        elif user_choice == computer_choice:
                return("Its a draw.")
        elif (computer_choice =='Rock' and user_choice == 'Scissors') or \
            (computer_choice =='Scissors' and user_choice == 'Paper') or \
            (computer_choice =='Paper' and user_choice == 'Rock'):
                return ('Computer wins')
        else:
            return ('user wins')
        
def game_loop():
        '''
        This initiates an instance of the Computer_Vision class and calls the play_game() method.
        
        '''  
        
        game =Computer_Vision(computer_wins=0, user_wins=0)
        game.play_game()

if __name__ == '__main__':
    game_loop()

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()