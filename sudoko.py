import numpy as np

class sudoku:
    grid = np.array([
    (0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0)
    ])
    
    @staticmethod
    def reader(address):
        x=0
        print ("reading strted ...")
        f = open(address, "r")
        for i in range(9): 
            temp = f.readline().replace("\n","").split(",")
            for o in temp: 
                sudoku.grid[sudoku.grid_ref(x)] = int(o)
                x+=1 
            f.readline()
        sudoku.grid_original = np.array(sudoku.grid, copy=True)    
                            
                
    grid_original = np.array(grid, copy=True)
    @staticmethod
    def grid_ref(number):
        grid_ref = (number//9, number%9)
        return grid_ref
    @staticmethod
    def value(grid, number):
        g_r = sudoku.grid_ref(number)
        value = grid[g_r]
        return value
    @staticmethod
    def cell(grid, number):
        g_r = sudoku.grid_ref(number)
        cell_ref = (g_r[0]//3, g_r[1]//3)
        cell = grid[((cell_ref[0])*3):((cell_ref[0])*3)+3, ((cell_ref[1])*3):((cell_ref[1])*3)+3]
        return cell
    @staticmethod
    def row(grid, number):
        g_r = sudoku.grid_ref(number)
        row_ref = g_r[0]
        row = grid[(row_ref):(row_ref+1), 0:9]
        return row
    @staticmethod
    def column(grid, number):
        g_r = sudoku.grid_ref(number)
        column_ref = g_r[1]
        column = grid[0:9, (column_ref):(column_ref+1)]
        return column

    @staticmethod
    def solve():
        print("\n Processing... \n")

        forwards = True
        i = 0

        while i <9*9:
            if sudoku.value(sudoku.grid_original, i) == 0 and forwards:
                for a in range(1, 10):
                    if a not in sudoku.cell(sudoku.grid, i) and a not in sudoku.row(sudoku.grid, i) and a not in sudoku.column(sudoku.grid, i):
                        sudoku.grid[sudoku.grid_ref(i)] = a
                        i += 1
                        break
                    else:
                        if a == 9:
                            forwards = False
                            i -= 1 
                            break
            elif sudoku.value(sudoku.grid_original, i) != 0 and forwards:
                i += 1

            elif sudoku.value(sudoku.grid_original, i) == 0 and not forwards:
                if sudoku.grid[sudoku.grid_ref(i)] == 9:
                    sudoku.grid[sudoku.grid_ref(i)] = 0
                    i -= 1
                else:
                    for a in range(sudoku.grid[sudoku.grid_ref(i)]+1, 10):
                        if a not in sudoku.cell(sudoku.grid, i) and a not in sudoku.row(sudoku.grid, i) and a not in sudoku.column(sudoku.grid, i):
                            sudoku.grid[sudoku.grid_ref(i)] = a
                            forwards = True
                            i += 1
                            break
                        else:
                            if a == 9:
                                sudoku.grid[sudoku.grid_ref(i)] = 0
                                i -= 1
                                break

            elif sudoku.value(sudoku.grid_original, i) != 0 and not forwards:
                i -= 1
      
   
    @staticmethod
    def show_board(board):
        print(bcolors.OKBLUE+("-"*37)+bcolors.ENDC)
        for i, row in enumerate(board):
            print(((bcolors.OKBLUE+("|")+bcolors.ENDC) + (" {}   {}   {} "+(bcolors.OKBLUE+("|")+bcolors.ENDC) )*3).format(*[str(bcolors.OKGREEN+(str(int(x/10))+bcolors.ENDC)) if x>=10  else x if x != 0 else " " for x in row]))
            if i == 8:
                print("-"*37)
            elif i % 3 == 2:
                print( bcolors.OKBLUE  +"|" + "---+"*8 + "---|"+bcolors.ENDC)
            else:
                print(bcolors.OKBLUE  +"|" + "   +"*8 + "   |"+bcolors.ENDC)
    
    @staticmethod
    def check_board ():
        canrun = True
        i = 0
        while i <81:
            
            if sudoku.value(sudoku.grid_original, i) != 0 :
                tmp =sudoku.value(sudoku.grid_original, i)
                sudoku.grid[sudoku.grid_ref(i)]=100
                if tmp in  sudoku.column(sudoku.grid, i):
                    sudoku.grid[sudoku.grid_ref(i)] =  (tmp *10)
                    i += 1
                    canrun= False
                elif tmp in  sudoku.column(sudoku.grid, i):
                    sudoku.grid[sudoku.grid_ref(i)] =  (tmp *10)
                    i+=1
                    canrun= False
                elif tmp in  sudoku.row(sudoku.grid, i):
                    sudoku.grid[sudoku.grid_ref(i)] =  (tmp *10)
                    i+=1
                    canrun= False
                elif tmp in  sudoku.cell(sudoku.grid, i):
                    sudoku.grid[sudoku.grid_ref(i)] =  (tmp *10)
                    i+=1
                    canrun= False
                else:
                    sudoku.grid[sudoku.grid_ref(i)] =  (tmp)
                    i+=1                
            else:
                i += 1
        return canrun 
               
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'   
sudoku.reader("a.txt")
print ("reading completed.")
sudoku.show_board(sudoku.grid)
if (sudoku.check_board ()):
    print (sudoku.solve())
    sudoku.show_board(sudoku.grid)
else:
    print ("is not solvable")


