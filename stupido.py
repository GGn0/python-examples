import random

n = random.randint(1,1e3)
inStr = ''

for _ in range(n):
    inStr += str(random.randint(1,1e9)) + ' '

inStr = inStr[:-1]
print(inStr)
#n = int(input())
#inStr = input()

tmp = inStr.split(' ')
inArray = [int(a) for a in tmp]

origArray = inArray.copy()
inArray.sort()

cnt = 0
for i in range(len(origArray)):
    if not ((origArray[i] - inArray[i]) == 0):
        cnt += 1

if (cnt == 0):
    print(0)
elif (cnt == 2):
    print(1)
else:
    print(-1)