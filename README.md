# computer-vision-rock-paper-scissors

This file contains a project called computer vision rock paper scissors where the aim is create a rock-paper scissors games which will compare the user input with the computers choice. The computers choice was developed by creating a computer vision system model on teachable-machines.

Milstone 1 - Create the computer vision system

Teachable-Machine was used to creat the model. This consisted of creating four classes which represent Rock,Paper,Scissors and Nothing. for each class I took roughly 1000 images to build the model.

Once all the images were taken the model was trained and downloaded from the "Tensorflow" tab. the model is labbeled as "keras_model.h5" and contains a "labels.txt" file which contains the classes with the corresponding index.

![](Images/Milestone_1.PNG)

Milstone 2 -Setting up the virtual environment

In order to run the model a virtual environment with the correct installed libaries needed to be set up. The required libaries were opencv-python, tensorflow and ipykernel.

The conda create -n command was inputted into the bash terminal on VSCode to create the virtual environment and , conda pip install(pip install) commands were inputted to install the required libraries and its depedencies in the virtual environment.

pip list > requirments.txt and conda env export > env.yaml commands were inputted into the bash terminal to copy over the required libaries and dependencies. These file enables any other user that wants to use your computer to easily install these exact dependencies.

Milestone 3 - Create a Rock


