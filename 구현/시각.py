h = int(input())

count = 0
for i in range(h+1):#0시0분0초부터 h시59분59초까지 해야하므로 h+1번만큼 반복해야한다
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+ str(j) + str(k): #"str(i)+ str(j) + str(k)"안에 '3'이 하나라도 포함하면 카운터를 센다
                count += 1

print(count)

#3중for문(O(n^3))을 내가 수학적으로 풀어서 시간복잡도를 O(n)로 만들어 보았다
#수학적으로 계산하면 여기서는 범위를 시간단위로 하기 때문에 분과 초는 일정하다
# 3은 각 단위마다 15번이 나오며, 분에서 3이 나오면 모든 초는 해당 되므로 15(분마다 3이 나오는 횟수) x 60(초) = 900이며, 
# 분에서 3이 안나와도 분마다 초에서 15번이나 나오기 때문에 45(분에서 3이 나오는 횟수를 제외한 분의 수) & 15(초마다 3이 나오는 수) =675
# 즉 시간당 3이 나오는 횟수는 900 + 675 = 1575는 무조건 나온다
# 하지만 시간에도 3이 나오면 분,초의 값과 관계없이 60(분) x 60(초) = 3600만큼 3이 나온다
# 즉 for문으로 count변수에 1575만큼 더하며, i가 3이면 3600을 더한다
count=0

for i in range(h+1):
    if '3' in str(i):
        count+=3600
    else:
        count+=1575

print(count)