from matrix_op import matrix_right_turn
from matrix_op import matrix_left_turn

m1 = [["w","g","g"],["y","b","o"],["r","o","o"]]

stop = 0
while stop == 0:
    lre =input("enter left, right or exit(l,r,e): ")
    if lre == "e":
        stop += 1
        print("file stoped")
    elif lre == "r":
        m1= matrix_right_turn(m1)
        print('',m1[0],'\n',m1[1],'\n',m1[2])
    elif lre == "l":
        m1 = matrix_left_turn(m1)
        print('',m1[0],'\n',m1[1],'\n',m1[2])
    else:
        print("invalid")