
class Player:

    def __init__(self,name="testDummy"):
        self.name = name


    moveMarker=0

    unknown = 0

    moveLog=  [[ unknown, unknown, unknown],
               [ unknown, unknown, unknown],
               [ unknown, unknown, unknown]]

    enemyMoves =[[ unknown, unknown, unknown],
               [ unknown, unknown, unknown],
               [ unknown, unknown, unknown]]

    gameState= [[ unknown, unknown, unknown],
               [ unknown, unknown, unknown],
               [ unknown, unknown, unknown],]
    


   
    def playerMove(self):
        print(f"Hamle Sırası Sende {self.name} ")
        move=input("sol üst 1 olacak şekilde seçtiğiniz kare numarsını veriniz")
        # input alır almaz maymun mu insan mı diye bakarız 
        acceptableMoves =["1","2","3","4","5","6","7","8","9"]
  
        while move not in acceptableMoves:
            print("1 den 9 kadar olan değerler geçerlidir  lütfen tekrar dene ")
            move=input("sol üst 1 olacak şekilde seçtiğiniz kare numarsını veriniz")


        move=int(move)
        move -=1
        moveA= move//3
        moveB = move%3
        moveTuple=(moveA, moveB)
        return moveTuple




# burdan aşağsı importta çalışma 
if __name__ == "__main__":


    print("test gerçek kod değil")

    testPlayer=Player("testEdiyorum")
    testResult = testPlayer.playerMove()
    print(testResult)
