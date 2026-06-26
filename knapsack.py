import time

start = time.perf_counter()

Weight = [4,8,3,5,9,2,3,1,5,2,4,2,7,10,3,13,11,8]
money = [6,12,4,3,7,1,3,2,7,3,4,2,10,13,5,16,14,9]
max_money = 0
best_weight = 0
best_items = []

n = len(Weight)
for bit in range(2 ** n):
    total_weight = 0
    total_money = 0
    items = []
    for i in range(n):
        if bit & (1 << i):
            total_weight += Weight[i]
            total_money += money[i]
            items.append(i)
    if total_weight <= 45 and total_money > max_money:
        max_money = total_money
        best_weight = total_weight
        best_items = items
end = time.perf_counter()

print("最大金額",max_money)
print("最大容量",best_weight)
print("品物",best_items)
print("time = ", end-start)