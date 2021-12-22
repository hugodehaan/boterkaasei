import random
from bke import MLAgent, is_winner, opponent,  RandomAgent, train_and_plot, load, save, start
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
    

def keuze2():
    my_agent = MyAgent()
    my_agent = load('MyAgent_3000')
 
    my_agent.learning = False
 
    start(player_x=my_agent)

    
    
random.seed(1)
#0.2 0.6
 
my_agent = MyAgent(alpha=0.2, epsilon=0.6)
random_agent = RandomAgent()

train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=100,
    validations=1000)

 
 
save(my_agent, 'MyAgent_3000')





while True:
  choice = input("\n 1: tegen elkaar spelen \n 2: tegen de computer spelen \n 3: Train de computer \n 4: hoe goed is de computer \n 5: welke parameters werken het best \n Kies wat je wilt spelen: \n")

  if choice == '1':
    start()

  if choice == '2':
    keuze2()

  if choice == '3':
    keuze3()

  if choice == '4':
    keuze4()

  if choice == "5":
    keuze5()