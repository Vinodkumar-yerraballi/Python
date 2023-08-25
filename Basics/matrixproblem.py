matrix=[[0,0,0],
        [0,0,0],
        [0,0,0],]

matrix[0][0]=1
matrix[1][1]=1
matrix[2][2]=1
def get_game(player=0,row=0,columns=0,just_display=False):
    print("  a  b  c")
    if not  just_display:
        matrix[row][columns]=player
    for col,row in enumerate(matrix):
        print(col,row)
get_game(just_display=True)
get_game(player=3,row=2,columns=2)