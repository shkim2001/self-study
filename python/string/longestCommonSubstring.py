def longestCommonSubString(text1, text2):
    n,m=len(text1),len(text2)
    dp=[[0]*(m) for _ in range(n)]
    for i in range(n):
        if text2[0] == text1[i]:
            temp = i
            while temp <= n:
                dp[temp][0] = 1
                temp += 1
            break
        
    
    for i in range(m):
        if text1[0] == text2[i]:
            temp = i
            while temp <= n:
                dp[0][temp] = 1
                temp += 1
            break
        
        
    
    for i in range(1, n):
        for j in range(1, m):
            if text1[i] == text2[j] and dp[i][j-1] == dp[i-1][j] == dp[i - 1][j - 1] == 0:
                dp[i][j]=1
                print(text1[i], text2[j])
            elif text1[i-1] == text2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
                print(text1[i], text2[j])
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    
    for list in dp:
        print(list)
    return dp[-1][-1]

print(longestCommonSubString("HILBERT", "SCHILLER"))
