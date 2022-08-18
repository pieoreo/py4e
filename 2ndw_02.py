### 2번 최종 답안

### monthly_payment = mpay
### after_tax_salary = ats

### 입력 값 체크하기
def input_check():
  while(True):
    try:
      mpay = int(input("Enter your monthly pay(won):"))
      return mpay
    except:
      print("Please Enter number.")
      return input_check()

### 세후 연봉 계산
def ats(year_sal):
  if year_sal <= 12000000:
    tax = 0.06
  elif year_sal <= 46000000:
    tax = 0.15
  elif year_sal <= 88000000:
    tax = 0.24
  elif year_sal <= 150000000:
    tax = 0.35
  elif year_sal <= 300000000:
    tax = 0.38
  elif year_sal <= 500000000:
    tax = 0.4
  else:
    tax = 0.42

  ### ats 결과 값 필터링
  ats = int(year_sal - (year_sal * tax))
  print("yearly salary after tax: " + format(ats, ',') + "won")
  print("yearly salary befor tax: " + format(year_sal, ',') + "won")

### 연봉 계산 시작
mpay = input_check()
year_sal = mpay * 12
ats(year_sal)
