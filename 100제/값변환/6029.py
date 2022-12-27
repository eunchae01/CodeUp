# 16진수를 입력받아 8진수(octal)로 출력해보자.

hex = input()

hex = int(hex, 16)

print("%o" % hex)