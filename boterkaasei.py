from bke import MLAgent, is_winner, opponent, train, save, load
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
 
my_agent = MyAgent()
my_agent = load('MyAgent_3000')
 
train(my_agent, 3000)
 
save(my_agent, 'MyAgent_3000')