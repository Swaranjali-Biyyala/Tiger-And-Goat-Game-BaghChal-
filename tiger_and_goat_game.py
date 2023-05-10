# -*- coding: utf-8 -*-
"""TIGER_AND_GOAT_GAME.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11bK_PFSyXgN23ZoHwSivSA5Oo4gn2t-I
"""

import sys
from math import *
import operator
class GoatAndTiger:
    neighbours = {(0,0):[3,4,5,6],(1,0):[3,8],(1,1):[2,4,9,1],(1,2):[1,3,5,10],(1,3):[1,4,6,11],(1,4):[1,5,7,12],(1,5):[6,13],(2,0):[2,9,14],(2,1):[3,8,10,15],(2,2):[4,9,11,16],(2,3):[5,10,12,17],(2,4):[6,11,13,18],(2,5):[7,12,19],(3,0):[8,15],(3,1):[9,14,16,20],(3,2):[10,15,17,21],(3,3):[11,16,18,22],(3,4):[12,17,19,23],(3,5):[13,18],(4,0):[15,21],(4,1):[16,20,22],(4,2):[17,21,23],(4,3):[18,22]}

    tiger_jumps = {(0,0):[9,10,11,12],(1,0):[4,14],(1,1):[5,15],(1,2):[2,6,16],(1,3):[3,17,7],(1,4):[4,18],(1,5):[5,19],(2,0):[10],(2,1):[1,11,20],(2,2):[8,1,12,21],(2,3):[1,9,13,22],(2,4):[1,10,23],(2,5):[11],(3,0):[2,16],(3,1):[3,17],(3,2):[4,14,18],(3,3):[5,15,19],(3,4):[6,16],(3,5):[7,17],(4,0):[9,22],(4,1):[10,23],(4,2):[11,20],(4,3):[12,21]}

    positions = {1:(0,0),2:(1,0),3:(1,1),4:(1,2),5:(1,3),6:(1,4),7:(1,5),8:(2,0),9:(2,1),10:(2,2),11:(2,3),12:(2,4),13:(2,5),14:(3,0),15:(3,1),16:(3,2),17:(3,3),18:(3,4),19:(3,5),20:(4,0),21:(4,1),22:(4,2),23:(4,3)}
    reversed_positions = {}
    for i in range(1,24):
        reversed_positions[positions[i]] = i
    default = [[1],[2,3,4,5,6,7],[8,9,10,11,12,13],[14,15,16,17,18,19],[20,21,22,23]]
    board_matrix = [['*'],['*','*','*','*','*','*'],['*','*','*','*','*','*'],['*','*','*','*','*','*'],['*','*','*','*']]
    dead_goats = []
    goat_counter=1
    
    def __init__(self):
        self.print_board()
    
    def print_board(self):
        print  (f'''                            {GoatAndTiger.board_matrix[0][0]}  



{GoatAndTiger.board_matrix[1][0]}            {GoatAndTiger.board_matrix[1][1]}        {GoatAndTiger.board_matrix[1][2]}        {GoatAndTiger.board_matrix[1][3]}        {GoatAndTiger.board_matrix[1][4]}            {GoatAndTiger.board_matrix[1][5]}    


{GoatAndTiger.board_matrix[2][0]}         {GoatAndTiger.board_matrix[2][1]}        {GoatAndTiger.board_matrix[2][2]}                 {GoatAndTiger.board_matrix[2][3]}        {GoatAndTiger.board_matrix[2][4]}        {GoatAndTiger.board_matrix[2][5]}                


{GoatAndTiger.board_matrix[3][0]}      {GoatAndTiger.board_matrix[3][1]}      {GoatAndTiger.board_matrix[3][2]}                         {GoatAndTiger.board_matrix[3][3]}        {GoatAndTiger.board_matrix[3][4]}     {GoatAndTiger.board_matrix[3][5]}    
 

    {GoatAndTiger.board_matrix[4][0]}      {GoatAndTiger.board_matrix[4][1]}                                {GoatAndTiger.board_matrix[4][2]}       {GoatAndTiger.board_matrix[4][3]}''')



    def position_placer(self):
        GoatAndTiger.goat_counter
        if GoatAndTiger.goat_counter > 16:
            self.move_goat()
        else:
            print ("please enter the position to place a goat")
            choose_goat_position=input()
            if choose_goat_position.isdigit():
                choose_goat_position = int(choose_goat_position)
                if choose_goat_position <= 24:
                    int_to_tuples = GoatAndTiger.positions[choose_goat_position]
                    if (GoatAndTiger.board_matrix[int_to_tuples[0]][int_to_tuples[1]] == '*'):
                        GoatAndTiger.board_matrix[int_to_tuples[0]][int_to_tuples[1]] = 'G'+str(GoatAndTiger.goat_counter)
                        GoatAndTiger.goat_counter+=1
                    else:
                        print("the position is occupied!!! Please choose another")
                        self.position_placer()
                else:
                    print("INVALID ENTRY")
                    self.position_placer()
            else:
                print("INVALID ENTRY")
                self.position_placer()

    def move_tiger(self):
        dead_tigers = self.check_blocked_tigers()
        goat_list = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16']
        goat_pos = []
        for element in goat_list:
            e = self.get_goat_position(element)
            if e!=None:
                goat_pos.append(e)
        if(dead_tigers==1):
            self.end_tiger_game()
        else:
            s = input("choose which tiger to move:")
            if s=='T1' or s=='T2' or s=='T3':
                initial = []
                for i in range(len(GoatAndTiger.board_matrix)):
                    if s in GoatAndTiger.board_matrix[i]:
                        k = GoatAndTiger.board_matrix[i].index(s)
                        initial.append((i,k))
                a = input("choose destination:")
                if(a.isdigit()):
                    a=int(a)
                    destination = GoatAndTiger.positions[a]
                    if (a in GoatAndTiger.tiger_jumps[initial[0]]) and (GoatAndTiger.board_matrix[destination[0]][destination[1]]=='*'):
                        common = list(set(GoatAndTiger.neighbours[initial[0]]) & set(GoatAndTiger.neighbours[destination]))
                        if len(common)>0:
                            common_element = common[0]
                            common_position = GoatAndTiger.positions[common_element]
                            if common_position in goat_pos:
                                GoatAndTiger.board_matrix[destination[0]][destination[1]] = GoatAndTiger.board_matrix[initial[0][0]][initial[0][1]]
                                GoatAndTiger.dead_goats.append(GoatAndTiger.board_matrix[common_position[0]][common_position[1]])
                                GoatAndTiger.board_matrix[common_position[0]][common_position[1]] = GoatAndTiger.board_matrix[initial[0][0]][initial[0][1]] = '*'
                                
                                self.check_end()
                            else:
                                print ("YOU CANNOT JUMP THERE!!!")
                                self.move_tiger()
                    elif(GoatAndTiger.board_matrix[destination[0]][destination[1]]=='*' and a in GoatAndTiger.neighbours[initial[0]]):
                            GoatAndTiger.board_matrix[destination[0]][destination[1]],GoatAndTiger.board_matrix[initial[0][0]][initial[0][1]] = GoatAndTiger.board_matrix[initial[0][0]][initial[0][1]],'*'
                    else:
                        print ("YOU CANNOT JUMP THERE!!!")
                        self.move_tiger()
                else:
                    print ("INVALID ENTRY")
                    self.move_tiger()
            else:
                print ("INVALID ENTRY")
                self.move_tiger()
    
    def move_goat(self):
        goat_list = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16']
        s = input("choose which goat to move")
        if s in goat_list:
           
        
            a = input("choose destination")
            if a.isdigit():
                a = int(a)
                destination = GoatAndTiger.positions[a]
                initial = self.get_goat_position(s)

                if(a in GoatAndTiger.neighbours[initial] and GoatAndTiger.board_matrix[destination[0]][destination[1]]=='*'):
                    GoatAndTiger.board_matrix[destination[0]][destination[1]] = GoatAndTiger.board_matrix[initial[0]][initial[1]]
                    GoatAndTiger.board_matrix[initial[0]][initial[1]] = '*'
                else:
                    print ("YOU CANNOT MOVE THERE!!!!")
                    self.move_goat()
            else:
                print ("INVALID ENTRY")
                self.move_goat()
        else:
            print("INVALID ENTRY")
            self.move_goat()

    def check_end(self):
        if len(GoatAndTiger.dead_goats)==6:
            print ("Tigers Won")
            sys.exit()

    def get_tiger_position(self,tiger):
        for i in range(len(GoatAndTiger.board_matrix)):
            if tiger in GoatAndTiger.board_matrix[i]:
                k = GoatAndTiger.board_matrix[i].index(tiger)
                return (i,k)

    def check_tiger_neighbours(self,neigh):
        count=0
        for i in neigh:
            pos = GoatAndTiger.positions[i]
            if(GoatAndTiger.board_matrix[pos[0]][pos[1]]!='*'):
                count+=1
        if(len(neigh)==count):
            return 1
        else:
            return 0
        
    def check_tiger_jumps(self,jumps):
        count=0
        for i in jumps:
            pos = GoatAndTiger.positions[i]
            if(GoatAndTiger.board_matrix[pos[0]][pos[1]]!='*'):
                count+=1
        if(len(jumps)==count):
            return 1
        else:
            return 0

    def check_blocked_tigers(self):
        count = 0
        tiger_list = ['T1','T2','T3']
        for i in tiger_list:
            tiger_pos = self.get_tiger_position(i)
            tiger_neighbours = self.check_tiger_neighbours(GoatAndTiger.neighbours[tiger_pos])
            tiger_j = self.check_tiger_jumps(GoatAndTiger.tiger_jumps[tiger_pos])
            if(tiger_neighbours==1 and tiger_j==1):
                count+=1
        if(count==3):
            return 1
        else:
            return 0
    def get_goat_position(self,goat):
        for i in range(len(GoatAndTiger.board_matrix)):
            if goat in GoatAndTiger.board_matrix[i]:
                k = GoatAndTiger.board_matrix[i].index(goat)
                return (i,k)

    def check_goat_in_neighbours(self,tiger_pos):
        goat_list = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16']
        neigh = GoatAndTiger.neighbours[tiger_pos]
        for i in neigh:
            neigh_pos = GoatAndTiger.positions[i]
            if GoatAndTiger.board_matrix[neigh_pos[0]][neigh_pos[1]] in goat_list and neigh_pos!=(0,0):
                c = list(set(GoatAndTiger.neighbours[neigh_pos]) & set(GoatAndTiger.tiger_jumps[tiger_pos]))
                if(len(c)>0):
                    c_element = GoatAndTiger.positions[int(c[0])]
                    if(GoatAndTiger.board_matrix[c_element[0]][c_element[1]]=='*'):
                        GoatAndTiger.board_matrix[c_element[0]][c_element[1]] = GoatAndTiger.board_matrix[tiger_pos[0]][tiger_pos[1]]
                        GoatAndTiger.dead_goats.append(GoatAndTiger.board_matrix[neigh_pos[0]][neigh_pos[1]])
                        GoatAndTiger.board_matrix[neigh_pos[0]][neigh_pos[1]] = GoatAndTiger.board_matrix[tiger_pos[0]][tiger_pos[1]] = '*'

                        return 1
    def get_distance(self,element_pos,j):
        return round(sqrt(pow(j[0]-element_pos[0],2)+pow(j[1]-element_pos[1],2)),2)

    def check_tigers_in_neighbours(self):
        goat_list = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16']
        for element in GoatAndTiger.tigers_list:
            tiger_pos = self.get_tiger_position(element)
            tiger_neigh = GoatAndTiger.neighbours[tiger_pos]
            for i in tiger_neigh:
                pos = GoatAndTiger.positions[i]
                if(GoatAndTiger.board_matrix[pos[0]][pos[1]] in goat_list):
                    next_element = list(set(GoatAndTiger.neighbours[pos]) & set(GoatAndTiger.tiger_jumps[tiger_pos]))
                    if(len(next_element)>0):
                        next_element = int(next_element[0])
                        next_element_pos = GoatAndTiger.positions[next_element]
                        if(GoatAndTiger.board_matrix[next_element_pos[0]][next_element_pos[1]]=='*'):
                            return next_element

    def end_tiger_game(self):
        print ("Goats won!!!!")
        sys.exit()

    def two_player(self):
        player1 = input("Player1 choose Goat or Tiger:")
        #if player1 == 'Goat' or player1=='Tiger':
        if player1 == 'Goat':
            print('player2 is Tiger')
        if player1 == 'Tiger':
            print("player2 is Goat")
        
            for i in range(1,16):
                dead = self.check_blocked_tigers()
                if(dead==1):
                    
                    self.end_tiger_game()
                self.position_placer()
                self.print_board()
                self.move_tiger()
                self.print_board()
                self.check_end()
                
            while(True):
                dead = self.check_blocked_tigers()
                if(dead==1):
                    
                    self.end_tiger_game()
                self.move_goat()
                self.print_board()
                self.move_tiger()
                self.print_board()
                self.check_end()
        else:
            print ("INVALID ENTRY!!!")
            self.two_player()
	

    def start_game(self):
        game = input("enter 2P :")
        if(game=="2P"):
            self.two_player()
        else:
            print ("INVALID ENTRY!!!")
            self.start_game()	

GoatAndTiger.board_matrix[0][0]='T1'
GoatAndTiger.board_matrix[1][2]='T2'
GoatAndTiger.board_matrix[1][3]='T3'
goat_list = []

g = GoatAndTiger()
g.start_game()