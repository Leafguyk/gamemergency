import random
class RSPsqure : 
    def __init__(self):
        self.AI_choice=random.choice(["R","S","P"])
        self.P_choice=None
        self.ahead=None
        self.turn=0
    def P_turn(self,rsp):
        if rsp==self.AI_choice and self.turn==0:
            self.AI_choice=random.choice(["R","S","P"])
        if rsp==self.AI_choice and self.ahead=="P":
            return "Win"
        elif rsp==self.AI_choice and self.ahead=="AI":
            return "Lose"
        else:
            self.P_choice=rsp
            if self.AI_choice=='R':
                if rsp=='S':
                    self.ahead="AI"
                    self.AI_choice=random.choice(["R","S","P"])
                elif rsp=='P':
                    self.ahead="P"
                    return "Win"
            if self.AI_choice=='S':
                if rsp=='R':
                    self.ahead="P"
                    self.AI_choice=random.choice(["R","S","P"])
                elif rsp=='P':
                    return "Lose"
            if self.AI_choice=='P':
                if rsp=='R':
                    return "Lose"
                elif rsp=='S':
                    return "Win"
    def RSPs(player, com) :

        if player == 1:
            if com == 2:
                win = 1
            else :
                win = 0
        elif player == 2:
            if com == 1:
                win = 0
            else :
                win = 1
        else :
            if com == 1:
                win = 1
            else :
                win = 0
        
        print("다시 가위, 바위, 보 중에 하나를 입력하세요.")
        player = int(input())
        com = random.choice(1,3)
        print(com)

        if win == 1:
            if player == com:
                print("Player win!!!")
                return 0
        elif win == 0:
            if player == com:
                print("Computer win!!!")
                return 0
        
        RSPs(player,com)

    print("묵찌빠 게임에 오신 것을 환영합니다!")
    print("--------RULES--------")
    print("묵 : 1\n찌 : 2\n빠 : 3")

    print("가위, 바위, 보 중에 하나를 입력하세요.")
    player = int(input())
    com = random.choice(1,3)
    print(com)

#player이 이기면 result = 1
#player이 이기고 있는 중이면 win = 1

    while player == com:
        player = int(input())
        com = random.choice(1,3)
        print(com)
    
    RSPs(player, com)           