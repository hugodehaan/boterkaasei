import random
from bke import MLAgent, is_winner, opponent,  RandomAgent, train_and_plot, load, save, start, train, validate, plot_validation
 
 
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
    

def keuze3():
    naamagent = input("Wat wordt de naam van de computer? \n")
    trainingsaantal = int(input("Hoe vaak wil je je computer laten trainen? \n"))
    my_agent = MyAgent()
    train(my_agent, 500)
    save(my_agent, naamagent)
    print("Je getrainde agent staat opgeslagen onder de naam: " + naamagent)
    
    
def keuze4():
    naamagent = input("Wat wordt de naam van de computer? \n")
    trainingsaantal = int(input("Hoe vaak wil je je computer laten trainen? \n"))
    my_agent = MyAgent()
    train(my_agent, trainingsaantal)
    save(my_agent, naamagent)
    my_agent = load(naamagent)
    my_agent.learning = False
 
    validation_agent = RandomAgent()
 
    validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
 
    plot_validation(validation_result)

    
def keuze5():  
    random.seed(1)
    
    my_agent = MyAgent(alpha=0.2, epsilon=0.6)
    random_agent = RandomAgent()
    aantal = int(input("Hoeveel iteraties wil je voltooien? \n"))
    train_and_plot(
        agent=my_agent,
        validation_agent=random_agent,
        iterations=aantal,
        trainings=100,
        validations=1000)

 
 
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