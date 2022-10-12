import cv2
from keras.models import load_model
import numpy as np
import time
import random

class RPS:

    def __init__(self,rounds = 5):
        self.rounds = rounds
        self.user_choice = None
        self.computer_choice = None
        self.user_wins = 0
        self.computer_wins = 0
        self.round_winner = None
        
        
    def get_computer_choice(self):
        return random.choice(['rock','paper','scissor'])
    
    def get_winner(self,computer_choice, user_choice):
        if (self.computer_choice == 'rock' and self.user_choice =='scissor') or (self.computer_choice == 'scissor' and self.user_choice == 'paper') or (self.computer_choice == 'paper' and self.user_choice == 'rock'):
            return 'computer'
        elif (self.computer_choice == 'rock' and self.user_choice =='paper') or (self.computer_choice == 'paper' and self.user_choice == 'scissor') or (self.computer_choice == 'scissor' and self.user_choice == 'rock') :
            return 'user'
        else:
            return 'Draw'

    def game_winner(self):
        if self.computer_wins > self.user_wins:
            print(f'Computer Wins. Computer: {self.computer_wins} User: {self.user_wins}')
        elif self.computer_wins < self.user_wins:
            print(f'User Wins. Computer: {self.computer_wins} User: {self.user_wins}')
        else:
            print(f'Draw. Computer: {self.computer_wins} User: {self.user_wins}')

        
    def play(self,mdel):
        model = load_model(mdel)
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        init_time = time.time()

        while self.rounds!= 0: 
            
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image

            if time.time() >= init_time + 3: 
                self.rounds = self.rounds -1
                init_time = time.time()
                prediction = model.predict(data)
                if prediction[0][0] > 0.5:
                    self.user_choice =  'rock'
                elif prediction[0][1] > 0.5:
                    self.user_choice = 'paper'
                elif prediction[0][2] > 0.5:
                    self.user_choice = 'scissors'
                else:
                    self.user_choice = 'Nothing'
                self.computer_choice = self.get_computer_choice()
                print('Computer Played:{} , You Chose:{}'.format(self.computer_choice, self.user_choice))
                self.winner = self.get_winner(self.computer_choice, self.user_choice)
               
                if self.winner == 'computer':
                    self.computer_wins = self.computer_wins  + 1
                elif self.winner == 'user':
                    self.user_wins = self.user_wins + 1
                else :
                    continue  
               
                
            cv2.imshow('frame', frame)
            # Press q to close the window
            #print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        print(self.user_wins, self.computer_wins)

game = RPS()
game.play('keras_model.h5')
game.game_winner()
