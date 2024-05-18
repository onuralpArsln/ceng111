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
        
    def winDetection(self)->int:  #birisi üçlü yapınca kazanmayı görcez 
        for i in range(3): #bu yatay kazanan için olucak 
            if self.gameState[i][0]==self.gameState[i][1]==self.gameState[i][2]!=0:
                print(f"player{self.gameState[i][0]} won")
                return self.gameState[i][0]
                
        for i in range(3): #dikey için olucak
            if self.gameState[0][i]==self.gameState[1][i]==self.gameState[2][i]!=0:
                 print(f"player{self.gameState[0][i]} won")
                 return self.gameState[0][i]
       
        if self.gameState[0][0]==self.gameState[1][1]==self.gameState[2][2]!=0:  #sol üstten başlayan çapraz win
             print(f"player{self.gameState[0][0]} won")
             return self.gameState[0][0]
         
        if self.gameState[0][2]==self.gameState[1][1]==self.gameState[2][0]!=0: #sağ üst çapraz 
             print(f"player{self.gameState[0][2]} won")
             return self.gameState[0][2]
        return 0 #eğer kimse kazanmazsa bu çalışır 

    counter=0
    def isBoardFull(self)->bool:
        self.counter+=1 
        if self.counter>=8:
            print("tahta doldu")
            self.counter=0 
            return True 
        else:
            return False
    
    who_won=0
    def isGameActive(self)->bool:
        self.who_won=self.winDetection()
        if self.who_won==0 and self.isBoardFull()== False:
            return True
        else:
            return False
        
    def celebrate(self)->int:
        if not self.who_won==0:
            print("yippiiiee")
        else:
            print(f"yipiie for player {self.who_won}!") 
    
        
        




    
    
                       

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
     
    while testEngine:     
        testEngine.display()          
        testEngine.player1MoveRequest()
        testEngine.display()          
        if not testEngine:
            break
    
        testEngine.display()          
        testEngine.player2MoveRequest()
        testEngine.display()




