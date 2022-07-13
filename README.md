# Computer-Vision-Rock-Paper-Scissors23
This project will simulate the classic game of Rock-Paper-Scissor with the computer using webcam. It relies on computer vision technology.

# Milestone 1

The image model for four different classes-Rock, Paper, Scissors and Nothing was created using teachable machine web application. It uses webcam to capture image of different objects or in this case hand signs for rock, paper and scissor to generate a tensorflow model of each individual image classes.

# Milestone 2 

An environment called rps_env was created using conda and necessary modules - opencv-python, tensorflow and ipykernel was installed using pip.

# Milestone 3

A file called 'manual_rps.py' is created to simulate game without computer vision. In this file, three functions have been created:
1. get_computer_choice(choices) : gets a random sign from the list of rock, paper or scissor
1. get_user_choice(choices): asks user to choose a sign
2. get_winner(user_choice, computer_choice) : takes input from both players(user and computer) and return winner
3. play() : simulates the game

