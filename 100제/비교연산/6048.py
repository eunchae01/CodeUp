# 입력
# 두 정수(a, b)가 공백을 두고 입력된다.
# -2147483648 <= a, b <= +2147483647

# 출력
# a가 b보다 작은 경우 True 를, 그렇지 않은 경우 False 를 출력한다.

a, b = map(int, input().split())

if(a < b):
    print("True")
else:
    print("False")