cat_A = int(input("Enter the any possition number of the cat_A"))       #9

cat_B = int(input("Enter the any possition number of the cat_B"))       #5

mouse_C = int(input("Enter the any possition number of the mouse_C"))   #7

if cat_A == 0:                                                          #if 9 == 0:
    print("cat_B")                                                          #print(5)
if cat_B == 0:                                                          #if 5 == 0:
    print("Cat_A")                                                          #print(9)
    
differance_1 = cat_A-mouse_C                                            #differance_1=9-7  =  2

differance_2 = cat_B-mouse_C                                            #differance_2=5-7  =  -2

if differance_1 < 0:                                                    #if 2 < 0:
    differance_1 = differance_1*-1                                          # 2 = 2*-1 = -2

if differance_2 < 0:                                                    #-2 < 0:
    differance_2 = differance_2*-1                                          #-2 = -2*-1 = 2

if differance_1 == differance_2:                                        #if -2 == 2:
    print("Mouse_C is the winner of this game")                              #print("mouse_C is the winner of this game")

elif differance_1 > differance_2:                                       #elif -2 > 2:
    print("Cat_B is the winner of this game")                                #print("cat_B is the winner of this game")

else:                                                                   #else:
    print("cat_A is the winner of this game")                                #print("cat_A is the winner of this game")