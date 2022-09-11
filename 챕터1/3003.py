king,queen,rook,bishop,knight,pawn=map(int,input().split())
chessboard=[king,queen,rook,bishop,knight,pawn]
chess=[1,1,2,2,2,8]

for i in range(len(chessboard)):
    if chessboard[i] !=chess[i]:
        chessboard[i]=chess[i]-chessboard[i]
    else:
        chessboard[i]=0

result = ' '.join(str(s) for s in chessboard)
print(result)
