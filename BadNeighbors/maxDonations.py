"""
Suppose v[i] = the value of house i, and totally we have n houses.
f[0] = v[0], f[1] = v[1], f[i] = max{f[i - 1], f[i - 2] + v[i]} for i >= 2

A modified version of this problem is that all houses form a circle, whose
solution is very similar. We need to run DP twice.
1st: f[0] = v[0], f[1] = 0, f[i] = max{f[i - 1], f[i - 2] + v[i]} for i = 2,
3, ..., n - 2 ==> ans1 = f[n - 2]
2nd: f[0] = 0, f[1] = v[1], f[i] = max{f[i - 1], f[i - 2] + v[i]} for i = 2,
3, ..., n - 1 ==> ans2 = f[n - 1]
return max{ans1, ans2}
"""
class BadNeighbors(object):
    def maxDonations(self, donations):
        donation_len = len(donations)
        if donation_len == 1:
            return donations[0]
        if donation_len == 2:
            return max(donations[0],donations[1])

        dp = [[0]*2 for _ in range(donation_len)]
        dp[1][0] = donations[0]
        dp[1][1] = donations[1]
        dp[2][0] = max(donations[0],donations[1])
        dp[2][1] = max(donations[1],donations[2])

        for i in range(3,donation_len):
            dp[i][0] = max(dp[i-1][0],dp[i-2][0]+donations[i-1])
            dp[i][1] = max(dp[i-1][1],dp[i-2][1]+donations[i])

        return max(dp[donation_len-1][0],dp[donation_len-1][1])
