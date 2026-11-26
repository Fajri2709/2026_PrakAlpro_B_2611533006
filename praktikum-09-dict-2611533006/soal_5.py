n = int(input())
cash = {}

for _ in range(n):
    parts = input().split()
    name = parts[0]
    amount = int(parts[1])
    
    if name in cash:
        cash[name] += amount
    else:
        cash[name] = amount

total_cash = 0
top_name = ""
top_amount = 0

for name, total in cash.items():
    print(f"{name}: {total}")
    total_cash += total
    if total > top_amount:
        top_name = name
        top_amount = total

print("Total cash:", total_cash)
print(f"Top contributor: {top_name} ({top_amount})")