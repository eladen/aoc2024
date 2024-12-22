from collections import defaultdict, Counter

with open("day22/input.txt") as f:
    init_numbers = [int(line.strip()) for line in f.readlines()]
    
def update_secret(secret):
    res = secret * 64
    secret = secret ^ res
    secret = secret % 16777216

    res = secret // 32
    secret = secret ^ res
    secret = secret % 16777216

    res = secret * 2048
    secret = secret ^ res
    secret = secret % 16777216

    return secret

total_p1 = 0
total_price = Counter()
for init_secret in init_numbers:
    secret = init_secret
    prices = []
    changes = []
    cnt = Counter()

    prices.append(secret % 10)
    seen = set()
    
    for i in range(2000):
        secret = update_secret(secret)
        price = secret % 10
        prices.append(price)
        changes.append(price - prices[-2])

        if i >= 3:
            a = changes[i-3]
            b = changes[i-2]
            c = changes[i-1]
            d = changes[i]
            if (a, b, c, d) not in seen:
                total_price[(a, b, c, d)] += price
            seen.add((a, b, c, d))

    total_p1 += secret

total_p2 = total_price.most_common()[0][1]

print(f"2024 Day 22, Part 1 = {total_p1}") 
print(f"2024 Day 22, Part 2 = {total_p2}")  