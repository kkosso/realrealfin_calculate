# 계산기(+,-,*,/,** 계산 가능)
def Doetsem(a, b):  # 덧셈 함수
    return a + b
def Bbellsem(a, b): # 뺄셈 함수
    return a - b
def Gobsem(a, b):   # 곱셈 함수
    return a * b
def Nanutsem(a, b): # 나눗셈 함수
    return a / b
def Jegob(a, b):    # 제곱 함수
    result = 1
    count = 0
    while count < int(b):
        result = result * a
        count = count + 1
    return result

C = []  # 입력 기록 저장
result = 0

one = input("(:q를 입력 시 종료)\n숫자 입력: ")
if one == ":q" or one == "":
    print("프로그램 종료")
else:
    i = 0
    dot_count = 0
    if one[0] == "-":  # 음수 처리
        i = 1
    isitnumber = True  # 숫자인지 확인할 변수 is it number?
    while i < len(one):
        if one[i] == ".":
            dot_count = dot_count + 1
            if dot_count > 1:
                isitnumber = False
                break
        elif one[i] < "0" or one[i] > "9":  # 아스키 문자 코드로 판별
            isitnumber = False
            break
        i = i + 1

    if isitnumber == True:
        result = float(one)
        C.append(one)
    else:
        print("숫자 아님. 프로그램 종료")
        exit()

# 연산 반복
while True:
    simbol = input("연산자 입력 (+, -, *, /, ^, root, =): ")

    if simbol == ":q" or simbol == "":
        print("프로그램 종료")
        break
    elif simbol == "=":
        print("계산 결과:", result)
        print("입력 수식:", ' '.join(C))
        break
    elif simbol not in ["+", "-", "*", "/", "^", "root"]:
        print("잘못된 연산자. 재입력: ")
        continue

    C.append(simbol)

    if simbol == "root":
        result = result ** 0.5
        continue

    # 다음 숫자 입력
    other = input("다음 숫자 입력: ")
    if other == ":q" or other == "":
        break

    i = 0
    dot_count = 0
    if other[0] == "-":
        i = 1
    isitnumber = True
    while i < len(other):
        if other[i] == ".":
            dot_count = dot_count + 1
            if dot_count > 1:
                isitnumber = False
                break
        elif other[i] < "0" or other[i] > "9":
            isitnumber = False
            break
        i = i + 1

    if isitnumber == True:
        other_num = float(other)
        C.append(other)
    else:
        print("숫자가 아닙니다. 다시 입력하세요.")
        break

    # 연산 수행
    if simbol == "+":
        result = Doetsem(result, other_num)
    elif simbol == "-":
        result = Bbellsem(result, other_num)
    elif simbol == "*":
        result = Gobsem(result, other_num)
    elif simbol == "/":
        if other_num == 0:
            print("0으로 나눌 수 없음")
            break
        result = Nanutsem(result, other_num)
    elif simbol == "^":
        result = Jegob(result, other_num)

# 최종 결과 출력
print("입력한 수식:", ' '.join(C))
print("최종 결과:", result)
