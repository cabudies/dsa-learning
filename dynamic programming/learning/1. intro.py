def fibb(n,dp):
    
    if n==0 or n==1:
        return n
    if dp[n-1]==-1:
        ans1=fibb(n-1,dp)
        dp[n-1]=ans1
    else:
        ans1=dp[n-1]
        
    if dp[n-2]==-1:
        ans2=fibb(n-2,dp)
        dp[n-2]=ans2
    else:
        ans2=dp[n-2]
    
    myAns=ans1+ans2
    return myAns

def fibbI(n):
    dp=[0 for i in range(n+1)]
    dp[0]=0
    dp[1]=1
    i=2
    while i<=n:
        dp[i]=dp[i-1]+dp[i-2]
        i+=1
    return dp[n]

n=int(input("Find fibonacci sum for - "))
ans=fibbI(n)
print(ans)

print()

dp=[-1 for i in range(n+1)]
dp_ans=fibb(n,dp)
print("dynamic programming ans- ", dp_ans)


