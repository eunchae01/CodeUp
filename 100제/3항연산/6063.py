# 입력
# 두 정수가 공백을 두고 입력된다.
# -2147483648 ~ +2147483647

# 출력
# 두 정수 중 큰 값을 10진수로 출력한다.

num1, num2 = map(int, input().split())

print(num1 if(num1 > num2) else num2)