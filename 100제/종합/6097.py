# 입력
# 첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
# 두 번째 줄에 놓을 수 있는 막대의 개수(n)
# 세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
# 1 <= w, h <= 100
# 1 <= n <= 10
# d = 0 or 1
# 1 <= x <= 100-h
# 1 <= y <= 100-w

# 출력
# 모든 막대를 놓은 격자판의 상태를 출력한다.
# 막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
# 단, 각 숫자는 공백으로 구분하여 출력한다.

h, w = map(int, input().split())                #세로와 가로 값 입력받음
arr = [[0 for j in range(w)] for i in range(h)] #입력받은 값으로 격자판 생성

n = int(input())                                #막대의 개수 입력받음

for i in range(n):                              #막대의 개수만큼
    l, d, x, y = map(int, input().split())      #막대의 길이, 방향, 좌표값 입력받음

    if (d == 0):                                #방향이 가로일때
        for j in range(l):                      #막대 길이만큼
            arr[x - 1][y - 1 + j] = 1           #막대 놓기
    else:                                       #방향이 세로일때
         for j in range(l):                     #막대 길이만큼
            arr[x - 1 + j][y - 1] = 1           #막대 놓기

for i in range(h):                              #격자판 출력
    for j in range(w):
        print(arr[i][j], end = " ")
    print("")
    