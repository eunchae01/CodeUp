# 6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.

# 입력
# 6자리 숫자로 이루어진 연월일(YYMMDD)이 입력된다.

# 출력
# 년도(YY) 월(MM) 일(DD)을 공백으로 구분해 한 줄로 출력한다.

date = input()

print(date[0:2], date[2:4], date[4:6], sep=" ")
    