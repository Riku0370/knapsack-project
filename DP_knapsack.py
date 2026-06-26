import time

start = time.perf_counter()

Weight = [4,8,3,5,9,2,3,1,5,2,4,2,7,10,3,13,11,8,5,2,4,5,6]
money = [6,12,4,3,7,1,3,2,7,3,4,2,10,13,5,16,14,9,1,4,6,2,4]

W = 45
dp = [0] * (W + 1)
n = len(Weight)
for i in range(n):

    for w in range(W, Weight[i]-1, -1):

        # 品物を入れない
        no_item = dp[w]

        # 品物を入れる
        yes_item = dp[w - Weight[i]] + money[i]

        # 良い方を採用
        if yes_item > no_item:
            dp[w] = yes_item
end = time.perf_counter()


print("最大金額:", dp[W])
print("実行時間:", end - start)