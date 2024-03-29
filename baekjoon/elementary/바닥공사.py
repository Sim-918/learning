# 2*n인 직사각형에서 1x2,2x1,2x2 인 타일들을 이용해 바닥을 덮을 때 몇가지 방법이 있나

n=int(input())
dp=[0]*(n+1)

dp[0]=1     #n의 길이가 1일때 무조건 1가지 (2x1)타일
dp[1]=3     #n의 길이가 2일때 무조건 3가지 (2x2)->한가지 (2x1모두)->한가지 (1x2모두)->한가지 총3가지

for i in range(2,n):
    # 즉 반복문에서 dp[0]과 dp[1]을 더하면서 n길이의 타일방법을 찾음
    # dp[i-2]*2는 2x2 1개와 2x1 2개를 덮는 경우이다. 같은 경우이므로 *2
    dp[i]=(dp[i-1]+dp[i-2]*2)
print(dp[n-1])
