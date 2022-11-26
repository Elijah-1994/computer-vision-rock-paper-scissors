## Computer Vision Rock-Paper-Scissors
&nbsp;

The aim of this project is to use keras modelling and python methods
to create the classic rock paper scissors game. Keras modelling is used to define the user input.

&nbsp;

## Milestone 1 - Create the computer vision system 
&nbsp;

The first step is to go onto [Teachable-Machine](https://teachablemachine.withgoogle.com/) to create the model. This consisted of creating four classes which represent Rock,Paper,Scissors and Nothing. I placed my hand to the camera to represent the first three classes and for nothing the camera was placed to the wall. For each class roughly 1000 images were taken to build the model.

Once all the images were taken the model was trained and downloaded from the "Tensorflow" tab. the model is labeled as "keras_model.h5" and contains a "labels.txt" file which contains the classes with the corresponding index. The model is used to take in the user input.

![](Images/Milestone_1.PNG)
*Figure 1 - Training model*

&nbsp;
## Milestone 2 - Setting up the virtual environment
&nbsp;

In order to run the model a virtual environment with the correct installed libaries needs to be set up. The required libraries installed are opencv-python, tensorflow and ipykernel.

The conda create -n command is inputted into the bash terminal on VSCode to create the virtual environment and , conda pip install(pip install) commands are inputted to install the required libraries and its dependencies in the virtual environment.

pip list > requirements.txt and conda env export > env.yaml commands are inputted into the bash terminal to copy over the required libraries and dependencies. These file enables any other user to run the script on there computer but installing the dependencies.

In order to check if the virtual environment is correctly installed the script which contains the  main code for the model was run and worked fine.

&nbsp;

## Milestone 3 - Create a Rock-Paper-Scissors game

&nbsp;

The object of this Milestone is to create a python script that will simulate a Rock-Paper-Scissors game that will ask for a user input and then compare the user input against the computers choice to show the winner.

__ask_user_input function__
&nbsp;

The first step is to create a list which contains the options between rock,paper and scissors and the use the import random module to pick a random option in the list.

A get_user choice functions is written which will take in the users choice. The user choice input is placed in a while loop which asks the user to enter either Rock,Paper or Scissors. If the user enters one of these options the users choice will be returned and stored as a string variable. The while loop will continue to run until the user input is correct.

![](Images/Milestone_3%20-%20User_Input.PNG)
*Figure 2 - get_user_choice function*

&nbsp;

__ask_computer_input function__

&nbsp;
A get_computer_choice function was written which will pick a random option from a list which contains strings labelled Rock,Paper,Scissors and return a choice and store as a string variable.

![](Images/Milestone_3%20-%20computer_choice.PNG)

*Figure 3 - get_computer_choice function*

&nbsp;

__get winner function__

A get_winner function was written which will contain if-elif-else statements to decide the winner between the user and winner based on the classic rules of rock,paper,scissors. The arguments passed through the parameters of the get_winner function are the variables stored from the get_user_choice function and get_computer_choice function.

&nbsp;
![](Images/Milestone_3%20-%20Get_winner.PNG)
*Figure 4 - get_winner function*

&nbsp;

__play function__

In order to make the script more streamlined and efficient the &ensp; __play function__&ensp;  is coded and encapsulates the &ensp; __get_user_choice function__&ensp;  ,&ensp; __get_computer_choice function__&ensp;  and &ensp;__get_winner function__&ensp;.


## Milestone 4 - Use the camera to play  Rock - Paper Scissors

&nbsp;

The first step was to code import  the cV2 module from the keras_model. This will allow the capture frame which will take in the user input to pop up during each run. The import numpy as np and random were also written in order for the code to run.

get_prediction!
The output of the model is a list of probabilities for each class (Rock,Papper,Scissors,Nothing). A list labelled choices which contained the four classes was created. in order to choose the highest probability the prediction was stored in a highest index varible which contained the np.argmax function. The will pick the highest probability and was stored in in a user_choice variable. As each class corresponds to the corresponding value (e.g 0 - Rock) the user_choice variable contains the choices list which is indexed based on the highest_index. This will convert high probablity into the corresponding class.
![](Images/Milestone_4%20-%20get_prediction.PNG)


get_computer_choice!

the get_computer_choice function was created to return the random computer choice using the choices variable. The computer choice variable is cantains the random.choice function with an index between [0:3]. This is to ensure the computer choice does not choose "Nothing" in the choices list.
![](Images/Milestone_4%20-%20get_computer_choice.PNG)

get_winner!

the output from the get_prediction and get_computer_choice were returned and stored as user_choice and computer_choice variebles respectively and are passed as arguments within the parameter of the get_winner function. The get_winner function contains if,elif,else statements which descides the winner based classic Rock,Papper,Scissors. 

play_game!

A define play_game function was created to which will contain the main game loop. The main code from the model  was wrapped into this function and the corresponding functions mentioned above are called in the play_game function. Since the main code from the model is within a while loop the script reads the input from the camera and then compares it with the computer's choice without stopping. Therefore the time.time() function was stored within a  start_time variable which placed outside of the game while loop. a current time variable  which also  the time.time() function was placed within the game loop below the main code from the model. An elapsed time variable was created which is the difference between the start_time and current time. This allows for a countdown before the get_prediction function is called. A series of if,elif statements were created to ensure the the get_prediction and get_computer choise function is called after the countdown of 5 seconds. then between 5 and 7 seconds the get_winner function is called. After  7 seconds the start_variable is called again which resets the countdown. A series of true/false flages are placed within the code of the play_game function to ensure only one prediction is  sotred per itteration.
![](Images/Milestone_4%20-%20play_game_1.PNG)
![](Images/Milestone_4%20-%20play_game_2.PNG)
![](Images/Milestone_4%20-%20play_game_3.PNG)


Class Computer_Vision!

In order to repeat the game until the user or computer wins 3 games, each win would need to be stored and itterated within a variable. In order to do this the functions for the game were wrapped in a class Computer_Vision. The def __init__ method was created in order to initialize the two parameters which are computer_wins and user_wins. The parameters store and itterate the user and computer score. A series of if,elif statments were created in the play_game function which control the user and computer points. If the return variable from the get_winner function is 'Computer wins' then the computer_wins variable is increased by 1 and vise versa for the user wins. An additional set of if,elif statments were created in the play_game function which return a statement on who wins the game if the computer_wins or user_wins reaches 3 points. This stops the while loop in the play_game function and ends the game.

Code improvements

in order to make the code readibility the class to initialize the class and function play_game call are wrapped in a def game loop function.

To make the script more usear friendly a additonal lines are written at the start of the code which explains to the user how to play the game. The user score and user score are also displayed throughout the game the so the user is aware. hello

