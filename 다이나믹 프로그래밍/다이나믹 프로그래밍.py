# 동태적 최적화 문제를 수학적으로 푸는 방식을  dynamic programming 이라고 합니다.
# 핵심 아이디어는 벨만 최적성 원리이고 그 아이디어에 따라서 optimal substructure가 나오게 됐습니다. 
# 간단하게 말하면 부분적으로 순간순간 매 time step step마다 최적의 결정을 내린다면 
# 그 결정들의 set (policy)은 최적의 결정이 된다는 것이  벨만의 최적성 원리에 대한 아이디어입니다.
# 그래서 dp로 그래프 문제를  풀면 계속 구조를 잘잡으면서 푸니까  가중치때문에  
# 꼬여서, 했던 계산을 또 하는  문제를   해결할 수 있습니다.
# 다이나믹 프로그래밍을 풀때 작은 팁은 일단 dp테이블를 점진적으로 생각해보고 잘 안되면 트리구조로 풀어본다

#예시문제 피보나치 수열

n = int(input())

#하양식(탑 다운, 메모리제이션)을 이용한 다이나믹프로그래밍
#탑 다운보다 보텀 업을 가능한 이용하는 것이 좋다
#이유는 탑 다운방식은 재귀함수를 이용하는데 재귀함수를 너무 많이 호출하면 오버헤드가 발생할 수 있기 때문이다

dp = [0] * 2999

def dpd(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    if dp[i] == 0:
        dp[i] = dpd(i-1) + dpd(i-2)
    return dp[i]

print(dpd(n))

#상향식(보텀 업, 점화식)을 이용한 다이나믹프로그래밍

dp = [0] * 2999

dp[0] = 0
dp[1] = 1

def dpdx(i):
    
    for j in range(2,i+1):
        dp[j] += dp[j-1] + dp[j-2]

    return dp[i]

print( dpdx(n))