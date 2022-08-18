'''make Baskinrobbins31 game'''
import random
print("Baskinrobbins31!")
try:
    my_num = int(input("Say any number start from 1 to 31: "))
    '''start with number what you input between 1 to 31'''

except:
    print("Error, please enter integer type")
    '''if my_num type is not int print this line'''

    my_num = int(input("Say any number start from 1 to 31: "))
    '''try again'''

computer_num = 1
'''computer_num declare and define'''

while 1<=my_num<=31 and 1<=computer_num<=31  :
    '''set my_num range and computer_num range'''

    try:
        count_num = int(input("numbers of consecutive 1 to 3: "))#
        '''set how many numbers what user want to say'''

    except:
        print("Error, please enter integer type")
        '''print Error'''

        count_num = int(input("numbers of consecutive 1 to 3: "))
        '''try again'''

    computer_turn_num = random.randint(1,3)
    '''call function that computer count 1 to 3 numbers '''

    user_num = my_num
    '''define user_num and get number from user'''

    user_num1 = user_num+1
    '''sencond number need to 1 bigger than first number'''

    user_num2 = user_num+2
    '''third number need to 2 bigger than first number'''

    computer_num = user_num+count_num
    computer_num1 = computer_num+1
    '''sencond number need to 1 bigger than first number'''

    computer_num2 = computer_num+2
    '''third number need to 2 bigger than first number'''

    if count_num == 1:
        '''case when user just count one number'''

        user_num = user_num
        user_num1 = ""
        ''' "" is my way to print there is no value'''
        user_num2 = ""
        computer_num = user_num+1
        '''next computer value need to be 1 bigger than user_num'''

        if computer_turn_num == 1:
            ''' case when computer count one number'''

            computer_num = computer_num
            computer_num1 = ""
            computer_num2 = ""
            my_num = user_num+2
        if computer_turn_num == 2:
            ''' case when computer count two numbers'''

            computer_num = computer_num
            computer_num1 = computer_num1
            computer_num2 = ""
            my_num = user_num+3
        if computer_turn_num == 3:
            ''' case when computer count three numbers'''

            computer_num = computer_num
            computer_num1 = computer_num1
            computer_num2 = computer_num2
            my_num = user_num+4
    if count_num == 2:
        '''case when user just count two numbers'''

        user_num = user_num
        user_num1 = user_num1
        user_num2 = ""
        computer_num = user_num+2
        if computer_turn_num == 1:
            computer_num = computer_num
            computer_num1 = ""
            computer_num2 = ""
            my_num = user_num+3
        if computer_turn_num == 2:
            computer_num = computer_num
            computer_num1 = computer_num1
            computer_num2 = ""
            my_num = user_num+4
        if computer_turn_num == 3:
            computer_num = computer_num
            computer_num1 = computer_num1
            computer_num2 = computer_num2
            my_num = user_num+5
    if count_num == 3:
        '''case when user just count three numbers'''

        user_num = user_num
        user_num1 = user_num1
        user_num2 = user_num2
        computer_num = user_num+3
        if computer_turn_num == 1:
            computer_num = computer_num
            computer_num1 = ""
            computer_num2 = ""
            my_num = user_num+4
        if computer_turn_num == 2:
            computer_num = computer_num
            computer_num1 = computer_num1
            computer_num2 = ""
            my_num = user_num+5
        if computer_turn_num == 3:
            computer_num = computer_num
            computer_num1 = computer_num1
            computer_num2 = computer_num2
            my_num = user_num+6
    if count_num > 3:
        print("Please Enter a right integer 1 to 3")
        continue
        '''kind of exception handling when the count num is bigger than 3'''

    if count_num < 1:
        print("Please Enter a right integer 1 to 3")
        continue
        '''kind of exception handling when the count num is less than 1'''

    if type(count_num) != int:
        print("Please Enter a right integer 1 to 3")
        continue
        '''kind of exception handling when the count num type is not int'''

    print("U s e r : ",user_num,user_num1,user_num2)
    print("Computer: ",computer_num,computer_num1,computer_num2)
    continue
    '''iteration '''

if user_num==31 or user_num1==31 or user_num2==31:
    print("You lost")
    '''somebody mention 31 will be a looser'''

if user_num==32 or user_num1==32 or user_num2==32:
    user_num = '', user_num == user_num1 == user_num2
    print("Game over")
    quit()
    ''' game can play upto number 31'''

if computer_num==31 or computer_num1==31 or computer_num2==31:
    print("Computer lost")
if computer_num1 == 32 and computer_num2 ==33:
    computer_num1 = '', computer_num2 = ''
    print("Game over")
    quit()
