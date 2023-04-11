# 입력
# 바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
# 십자 뒤집기 횟수(n)가 입력된다.
# 십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.

# 출력
# 십자 뒤집기 결과를 출력한다.

d = [[0 for i in range(19)] for i in range(19)] #바둑판 생성

for i in range(19):                             
        d[i] = list(map(int, input().split()))  #바둑알 깔려있는 상황 입력받기

n = int(input())                                #십자 뒤집기 횟수

for i in range(n) :                             #십자 뒤집기 횟수만큼
    x, y = map(int, input().split())            #십자 뒤집기 좌표 입력받음

    for j in range(19) :                        
        if(d[j][y - 1] == 0):                   #왼쪽에서 오른쪽으로 가면서 깔려있는 돌이 0이면
            d[j][y - 1] = 1                     #1로 바꿔줌
        else:                                   #깔려있는 돌이 1이면
            d[j][y - 1] = 0                     #0으로 바꿔줌

        if(d[x - 1][j] == 0):                   #위에서 아래로 가면서 깔려있는 돌이 0이면
            d[x - 1][j] = 1                     #1로 바꿔줌
        else:                                   #깔려있는 돌이 1이면
            d[x - 1][j] = 0                     #0으로 바꿔줌

for i in range(19):                             #십자 뒤집기 한 바둑판 출력
    for j in range(19):
        print(d[i][j], end = " ")
    print("")