number = int(input("몇 단?:"))

answer = 0
gugunum = 9
while gugunum>0:
    gugunum=gugunum-1
    if gugunum%2!=0:#홀수일 조건
        def answer():
            return number*gugunum
        if answer()<=40:
            print(number,'X',gugunum,'=',answer())
