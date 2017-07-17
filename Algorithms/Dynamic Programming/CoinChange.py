coins = [1, 2, 5]
value = 12

dp_list = range(value + 2)
for i in dp_list:
	dp_list[i] = 0
dp_list[1] = 1

for coin in coins:
	for i in range(coin, len(dp_list)):
		if i >= coin:
			dp_list[i] = dp_list[i] + dp_list[i-coin]

print (dp_list[value + 1])