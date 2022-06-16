from tictactoe import TicTacToe
a=TicTacToe()
while a.GameEnd()==False:
    for j in a.Board():
        for i in j:
            print(i,end=" ")
        print()
    x,y=map(int,input(f"{a.current_turn()}의 턴, 좌표를 입력:").split())
    if a.current_turn()=="O":
        a.Player_O(x,y)
    else:
        a.Player_X(x,y)
print(f"게임끝 {a.winner()}승")