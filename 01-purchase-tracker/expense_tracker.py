print("=== Трекер расходов ===")

expenses = {} # Для хранения затрат.
total_expenses = 0

while True:
	print(f"\nТовар №{len(expenses) + 1}:")

	item = input(
		"Введите название товара (или 'стоп'): ").strip().lower()
	if item == 'стоп':
		break

	quantitys = input(
		f"Введите количество {item} (или 'стоп'): ").strip().lower()
	if quantitys == 'стоп':
		break

	prices = input(
		f"Введите цену за единицу товара {item} (или 'стоп'): ").strip().lower()
	if prices == 'стоп':
		break

	try:
		quantity = float(quantitys)
		price = float(prices)
		total = quantity * price

		expenses[item] = {
		'quantity': quantity,
		'price': price,
		'total': total
	    }

	except ValueError:
		print("Ошибка! Пожалуйста, введите числа для количества и цены.")
		continue  # Пропускаем эту итерацию цикла и начинаем заново

if expenses:
	print(f"\nСписок Ваших расходов:")

	for item, details in expenses.items():
		print(f"{item.title()}: {details['quantity']} ед.")
		print(f"  Цена за единицу: {details['price']} руб.")
		print(f"  Итого: {details['total']} руб.")
		print("-" * 30)
		total_expenses += details['total']    
    
print(f"\nОбщая сумма расходов: {total_expenses} руб.")
print(f"Всего товаров: {len(expenses)}")