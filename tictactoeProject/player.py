
class Player:

    def __init__(self,name):
        self.name = name

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
        
        move=input("sol üst 1 olacak şekilde seçtiğiniz kare numarsını veriniz ")
        move=int(move)
        move -=1
        moveA= move/3
        moveB = move%3
        moveTuple=(moveA, moveB)
        return moveTuple




# burdan aşağsı importta çalışma 
if __name__ == "__main__":


    print("test gerçek kod değil")