from multi_sided_die import *

class  DicePoker:
    
    amount = 100
    double = False
    triple = False
    a = '0'

    
    def __init__(self):
        pass
        

    def roll_dice(self):
        value = []
        ms  = MultiSidedDie(6)
        for num in range(5):
            ms.roll()
            a = str(ms.get_value()) 
            value.append(a)
        print('Position numbers for dices ["0", "1", "2", "3", "4"]')
        print('Dice results               {}'.format(value))
        g = input("Do you want to roll again, y or n? " ) 
        if g == 'y':
            x = input("Which dice do you want to roll again? Type in position of dices each separated by a space " )
            x = x.split()
            #print(x)
            for dice in x:
                ms.roll()
                value[int(dice)] = str(ms.get_value())
            print('Dice results               {}'.format(value))    
            g = input("Do you want to roll again, y or n? " ) 
            if g == 'y':
                x = input("Which dice do you want to roll again? Type in position of dices each separated by a space  " )
                x = x.split()
                #print(x)
                for dice in x:
                    ms.roll()
                    value[int(dice)] = str(ms.get_value())
                print('Dice results               {}'.format(value))    
        print(value)            
        return value




    def count_numbers(self,mystr,z):

        #global amount
        # #global double 
        # self.double = False
        # #global triple 
        # self.triple = False
        counter = 0
        z = set(z)
        for i in z:
            if mystr.count(i) == 2:
                self.double = True
                global a 
                self.a = i
                counter +=1
            if (mystr.count(self.a)!=2 and mystr.count(i)==3):
                self.amount +=  8
            if mystr.count(i)== 3:
                self.triple =True
            if self.double and self.triple:
                self.amount +=  12
            if mystr.count(i)== 4:
                self.amount +=  15
            if mystr.count(i)== 5:
                self.amount +=  30
            if (mystr=='12345' or mystr=='23456'):
                self.amount +=  20
            if counter ==2:
                self.amount += 5
            else:
                pass


    def playgame(self):
    
        g = input("Hello, welcome to the dice game! \n Would you like to play y or n? " ) 
        if g == 'y':
            while self.amount>10 and g =='y':
                print("Your score is %s ." % (self.amount))
                r = input("Press 1 to roll dice " )
                if r == '1':
                    self.amount-=10
                    z = self.roll_dice()
                    mystr = ''.join(z)
                    for i in z:
                        if mystr.count(i)== 2:
                            a = i
                    self.count_numbers(mystr,z)
                    g = input("Would you like to continue playing y or n?" )
    
        print("Game Over! \n Your final score is %s ." % (self.amount)) 
        
dp = DicePoker()
dp.playgame()