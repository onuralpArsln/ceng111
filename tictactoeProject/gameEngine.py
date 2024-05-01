from player import Player 

# board 
# protokol 
# a= [[1,2,3],[4,5,6],[7,8,9]]

 # boş kare =  


class GameEngine:
    empty = 0 
    player1Move= 1
    player2Move=  2



    def __init__(self, player1=None, player2=None):
        self.player1 = player1
        self.player2 = player2

        if (player1 is None or player2 is None):
            print("Not Enough Players")
            raise Exception("Not Enough Players For Game Engine please provide 2 players")

    gameState=[[ empty, empty, empty],
               [ empty, empty, empty],
               [ empty, empty, empty]]


    
    def display(self)->None:
        # displays current game 
        for i in self.gameState:
            print(i)

 
    def playerMoveRequest(self) -> None:
        moveTuple=self.player1.PlayerMove() #hamle alınıyo, oyuncunun seçtiği kare noyu alıp tuple döndüryo
        self.gameState[int(moveTuple[0])][int(moveTuple[0])]=self.player1Move

    def turnStalker(): 
        pass
        
    def winDetection(self)->None:
        pass




if __name__ == "__main__":

    testEngine=GameEngine()
    testEngine.display() 
