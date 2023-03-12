while True:
    print('\t\t********게산기*******\n\t\t********제작자:이온유********\n\n\n\n\n\n\n\t\t버전:알파')
    num1 = input('\t\t숫자 1을 입력하세요: 종료: 0')
    if num1 == 0:
        break
    else:
        num2 = input('\t\t숫자 2를 입력하세요: ')
        try:
            num1 = int(num1)
            num2 = int(num2)
        except:
            try:
                num1 = float(num1)
                num2 = float(num2)
            except:
                print(f'{num1} 은 숫자가 아닙니다.')
        op = input('연산자를 입력하세요(+ - * / ): ')
        if op == '+':
            print(f'{num1} + {num2} = {num1 + num2}입니다.')
        elif op == '-':
            print(f'{num1} - {num2} = {num1 - num2}입니다.')
        elif op == '*':
            print(f'{num1} * {num2} = {num1 * num2}입니다.')
        elif op == '/':
            if num2 == 0:
                print('0으로는 나눌 수 없습니다.')
            else:
                print(f'{num1} / {num2} = {num1 / num2}입니다.')
        else:
            print('연산자가 아닙니다.')
            continue