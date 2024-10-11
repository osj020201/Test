import random

number = random.randint(1, 10)

while True:
    user_input = int(input("컴퓨터가 생각한 숫자를 입력해주세요.: "))
    if user_input == number:
        print("축하드립니다, 정답 입니다!")
        break

    if user_input < number:
        print("컴퓨터가 생각한 숫자보다 값이 작습니다, 다시 입력해주세요.")
        continue

    if user_input > number:
        print("컴퓨터가 생각한 숫자보다 값이 큽니다, 다시 입력해주세요.")
    continue


# 처음에 생각에 조건문 ->  GPT한테 정의같은 것만 물어보다가 While, for in <- 반복문 필요할거같아서 생각남, 문법에 관해선 본인의 블로그에 있는 데일리 루틴을 참고하였음. 
# 김대영 튜터님에게 for 와 while 중 무엇을 쓸지 말씀드렸을 때 while 이 낫다는 의견을 듣고 While 문으로 작성함.