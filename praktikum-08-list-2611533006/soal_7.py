menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

# Write your code below
for day in range(number_of_days):
    daily_sales = []
    for menu in menus:
        qty = int(input(f"Day {day + 1}, {menu}: "))
        daily_sales.append(qty)
    sales.append(daily_sales)

print("Total per day:")
for day in range(number_of_days):
    day_total = 0
    for col in range(len(menus)):
        day_total += sales[day][col]
    print(f"Day {day + 1}: {day_total}")

menu_totals = []
for col in range(len(menus)):
    menu_total = 0
    for day in range(number_of_days):
        menu_total += sales[day][col]
    menu_totals.append((menus[col], menu_total))

print(f"Total per menu: {menu_totals}")

best_name = menu_totals[0][0]
best_total = menu_totals[0][1]

for name, total in menu_totals:
    if total > best_total:
        best_total = total
        best_name = name

print(f"Best seller: {best_name} ({best_total})")