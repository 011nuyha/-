print("202302574_안재현")
import random

com = random.randrange(0,3)

user = int(input("가위 0, 바위 1, 보 2 선택: "))

print("user = %d, com = %d" %(user, com))

if user == com:
    print("비겼음")
elif (user+1)%3 == com:
    print("com 승")
else:
    print("user 승")
