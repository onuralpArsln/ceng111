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

        if type(player1) != Player or  type(player2) != Player :
          raise Exception("Game Engine needs player class parameter to initialize")
        
        if (player1 is None or player2 is None):
            print("Not Enough Players")
            raise Exception("Not Enough Players For Game Engine please provide 2 players")
        
        self.player1 = player1
        self.player1.moveMarker=self.player1Move
        self.player2 = player2
        self.player2.moveMarker=self.player2Move

       

    gameState=[[ empty, empty, empty],
               [ empty, empty, empty],
               [ empty, empty, empty]]


    
    def display(self)->None:
        # displays current game 
        for i in self.gameState:
            print(i)

 
    # bu playerdan hamle isteme şablonumuz
    def playerMoveRequest(self, activePlayer:Player) -> None:

        # verilen parametre gerçekten player classı mı kontrol et
        if type(activePlayer) != Player:
            raise Exception("Player isterim")
        
        # hamle alnıyor
        moveTuple=activePlayer.playerMove() #hamle alınıyo, oyuncunun seçtiği kare noyu alıp tuple döndüryo
        
        # hamle uygun mu kontrol ediliyor
        while  self.gameState[int(moveTuple[0])][int(moveTuple[1])] != 0:
            # uyarı
            print("burası dolu başka yer seç")
            # hamle yaptır
            moveTuple=activePlayer.playerMove()

        self.gameState[int(moveTuple[0])][int(moveTuple[1])]=activePlayer.moveMarker #oyuncunun hamlesini alıyoz boardda göstercez.İlk line satırı, ikinci sütunu belirtiyo,


    # şablonu kullanarak player1den move istiyor 
    def player1MoveRequest(self):
        self.playerMoveRequest(self.player1)

    # şablonu kullanarak player2den move istiyor 
    def player2MoveRequest(self):
        self.playerMoveRequest(self.player2)

    def turnStalker(): 
        pass
        
    def winDetection(self)->None:
        pass

    def startEngine(self):
        ## oyunu oynatan döngü
            # boş display gelsin
            # oyuncudan hamle istensin
            # güncel display gelsin

            pass




if __name__ == "__main__":

    testPlayer1 = Player("testPlayer1")
    testPlayer2 = Player("testPlayer2")
    testEngine=GameEngine( player1=testPlayer1, player2=testPlayer2 )
    testEngine.display() 
    testEngine.player1MoveRequest()
    testEngine.display()
    testEngine.player2MoveRequest()
    testEngine.display()
