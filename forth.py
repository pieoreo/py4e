import random
computer = random.randint(0,2)
options = ["가위", "바위", "보", "0", "1", "2"]
def get_user_input():
    while True:
        user_input = input("가위 바위 보 ")
        if user_input not in options:
            print("다시 입력해주세요. ")
        else:
            for i in range(3):
                if user_input == options[i + 3]:
                    user_input = int(user_input)
                break
        return user_input
def conversion(case):
    if case == 0: case = "가위"
    elif case == 1: case = "바위"
    elif case == 2: case = "보"
    return case

computer = conversion(computer)

def rcp(my):
    my = conversion(my)

    print("나:", my)
    print("컴퓨터:", computer)
    if my == computer:
        print("무승부")
    elif my == "가위" and computer == "바위":
        print("컴퓨터 승리!")
    elif my == "바위" and computer == "보":
        print("컴퓨터 승리!")
    elif my == "보" and computer == "가위":
        print("컴퓨터 승리!")
    else:
        print("사용자 승리!")
def continue_playing():
    want_to_play = True
    while want_to_play:
        user = input("게임을 다시하시겠습니까? ")
        if user == "예":
            my = get_user_input()
            rcp(my)
        elif user == "아니요":
            want_to_play = False
        else:
            print("예 또는 아니요를 입력하세요.")
my = get_user_input()
rcp(my)
continue_playing()
