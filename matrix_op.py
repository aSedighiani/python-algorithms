def matrix_right_turn(color:list[list[str]]) -> list[list[str]]:      
    color2 = [["0","0","0"],["0","0","0"],["0","0","0"]]
    for i in range(0,3):
        color2[0][i] = color[2-i][0]
    for i in range(0,3):
        color2[1][i] = color[2-i][1]
    for i in range(0,3):
        color2[2][i] = color[2-i][2]
    return color2

def matrix_left_turn(color:list[list[str]]) -> list[list[str]]:      
    color2 = [["0","0","0"],["0","0","0"],["0","0","0"]]
    for i in range(0,3):
        color2[0][i] = color[i][2]
    for i in range(0,3):
        color2[1][i] = color[i][1]
    for i in range(0,3):
        color2[2][i] = color[i][0]
    return color2