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

In order for the camera to work and take in the user inputs, the first step is to import  the &ensp;__cV2 module__&ensp; from the keras_model. This will allow the capture frame which will take in the user input to pop up during each run. The other required imports for the script are  &ensp;__numpy as np__&ensp; and &ensp;__random__&ensp;.

__get_prediction method__
&nbsp;
The output of the keras model is a list of probabilities for each class (Rock,Paper,Scissors,Nothing). A list labelled choices which contains the four classes was created. in order for the highest probability to be chosen, the prediction is stored in a highest index variable which contained the np.argmax function. The highest probability is then picked and was stored in a user_choice variable. As each class corresponds to the corresponding value (e.g 0 - Rock) and he user_choice variable contains the choices list which is indexed based on the highest_index. This will convert high probability into the corresponding class.
&nbsp;

![](Images/Milestone_4%20-%20get_prediction.PNG)

*Figure 5 - get_prediction method*

&nbsp;

__get_computer_choice method__

the &ensp;__get_computer_choice method__&ensp; returns the random computer choice using the &ensp;__random.choice function__&ensp; and is indexed between [0:3]. This is to ensure the computer choice does not choose "Nothing" in the choices list.

&nbsp;

![](Images/Milestone_4%20-%20get_computer_choice.PNG)

*Figure 6 - get_computer_choice method*

__get_winner method__

the output from the &ensp;__get_prediction method__&ensp; and &ensp;__get_computer_choice method__&ensp; are returned and stored as user_choice and computer_choice variables respectively and are passed as arguments within the parameter of the get_winner method. The get_winner function contains if,elif,else statements which decide the winner based on the classic Rock,Paper,Scissors rules 

__play_game method__

In order to run the main game loop A define play_game function was created amd the main code encapsulated into this methods and the corresponding functions mentioned above are called in the play_game function. Since the main code from the model is within a while loop the script reads the input from the camera and then compares it with the computer's choice without stopping. Therefore the &ensp;__time.time() function__&ensp; was stored within a  start_time variable and placed outside of the __play_game__ while loop. The  __time.time() function__ is to used to calculate the current function and placed in a variable  placed within the while loop. An elapsed time variable was created which is the difference between the start_time and current time. This allows for a countdown before the get_prediction function is called. A series of if,elif statements were created to ensure the the &ensp;__get_prediction method__&ensp; and the &ensp;__get_computer_choice method__&ensp; is called after the countdown of 5 seconds. then between 5 and 7 seconds the &ensp;__get_winner method__&ensp; is called. After  7 seconds the start_variable is called  which resets the countdown. A series of true/false flags are placed within the code of the &ensp;__play_game method__&ensp; to ensure only one user prediction is store per iteration.

&nbsp;

![](Images/Milestone_4%20-%20play_game_1.PNG)
![](Images/Milestone_4%20-%20play_game_2.PNG)
![](Images/Milestone_4%20-%20play_game_3.PNG)

*Figure 7 - play_game method*

&nbsp;

 __Class computer vision__

&nbsp;

In order to repeat the game until the user or computer wins 3 games, each win would need to be stored and iterated within a variable. In order to do this the methods for the game were wrapped in a class called Computer_Vision. The def &ensp;__init__&ensp; method was created in order to initialize the two parameters which are computer_wins and user_wins. The parameters initialise and  iterate the user and computer score. A series of if,elif statements were created in the play_game function which control the user and computer points. If the return variable from the &ensp;__get_winner method__&ensp; is 'Computer wins' then the computer_wins variable is increased by 1 and vise versa for the user wins. An additional set of if,elif statments were created in the &ensp;__play_game method__&ensp; which return a  print statement on who wins the game if the computer_wins or user_wins reaches 3 points. Once 3 points is reach the while loop breaks amd the game ends.

&nbsp;

__Code improvements__

&nbsp;

in order to make the script more readable the methods in the class are encapsulated within the  __game_loop method__ .

To make the script more user friendly a additional lines are written at the start of the code which explains to the user how to play the game. The user score and user score are also displayed throughout the game the so the user is aware. 

