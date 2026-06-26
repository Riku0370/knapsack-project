import csv
import random
import time
import matplotlib.pyplot as plt

W = 45


def brute_force(Weight, money):
    start = time.perf_counter()

    max_money = 0
    best_weight = 0
    n = len(Weight)

    for bit in range(2 ** n):
        total_weight = 0
        total_money = 0

        for i in range(n):
            if bit & (1 << i):
                total_weight += Weight[i]
                total_money += money[i]

        if total_weight <= W and total_money > max_money:
            max_money = total_money
            best_weight = total_weight

    end = time.perf_counter()
    return max_money, best_weight, end - start


def dp_method(Weight, money):
    start = time.perf_counter()

    dp = [0] * (W + 1)
    n = len(Weight)

    for i in range(n):
        for w in range(W, Weight[i] - 1, -1):
            no_item = dp[w]
            yes_item = dp[w - Weight[i]] + money[i]

            if yes_item > no_item:
                dp[w] = yes_item

    end = time.perf_counter()
    return dp[W], end - start


def main():
    random.seed(0)

    base_weight = [random.randint(1, 15) for _ in range(25)]
    base_money = [random.randint(1, 20) for _ in range(25)]

    n_list = []
    brute_times = []
    dp_times = []

    with open("result.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "n",
            "bruteforce_money",
            "bruteforce_weight",
            "bruteforce_time",
            "dp_money",
            "dp_time"
        ])

        for n in [5, 10, 15, 20, 21, 23, 24 , 25]:
            Weight = base_weight[:n]
            money = base_money[:n]

            brute_money, brute_weight, brute_time = brute_force(Weight, money)
            dp_money, dp_time = dp_method(Weight, money)

            writer.writerow([
                n,
                brute_money,
                brute_weight,
                brute_time,
                dp_money,
                dp_time
            ])

            n_list.append(n)
            brute_times.append(brute_time)
            dp_times.append(dp_time)

            print("n =", n)
            print("総当たり 最大金額:", brute_money, "重さ:", brute_weight, "時間:", brute_time)
            print("DP 最大金額:", dp_money, "時間:", dp_time)
            print()

    plt.figure(figsize=(8, 5))

    plt.plot(n_list, brute_times,
             marker="o",
             linewidth=2,
             label="Brute Force")

    plt.plot(n_list, dp_times,
             marker="s",
             linewidth=2,
             label="Dynamic Programming")

    plt.xlabel("Number of Items")
    plt.ylabel("Execution Time [s]")
    plt.title("Comparison of Execution Time")
    plt.grid(True)
    plt.legend()

    plt.savefig("time_compare.png", dpi=300)
    plt.show()


main()