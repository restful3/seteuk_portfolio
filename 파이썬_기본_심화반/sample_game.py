import random

def guess_number():
    # 1부터 100까지의 임의의 숫자 선택
    secret_number = random.randint(1, 100)
    
    # 사용자에게 안내 메시지 출력
    print("1부터 100 사이의 숫자를 맞춰보세요.")
    
    # 사용자가 숫자를 맞출 때까지 반복
    while True:
        # 사용자로부터 숫자 입력 받기
        user_guess = int(input("추측한 숫자를 입력하세요: "))
        
        # 입력한 숫자와 비교하여 결과 출력
        if user_guess < secret_number:
            print("더 큰 숫자를 입력하세요.")
        elif user_guess > secret_number:
            print("더 작은 숫자를 입력하세요.")
        else:
            print("정답입니다! 축하합니다!")
            break

# 게임 실행
guess_number()
