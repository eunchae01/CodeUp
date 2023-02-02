# 입력
# 3개의 정수가 공백으로 구분되어 입력된다.
# -2147483648 ~ +2147483648

# 출력
# 가장 작은 값을 출력한다.

num1, num2, num3 = map(int, input().split())

print((num1 if(num1 < num2) else num2) if((num1 if(num1 < num2) else num2) < num3) else num3)