import heapq

def minimize_cable_cost(cables):
    if len(cables) <= 1:
        return 0
    
    # Тепер на вершині (cables[0]) завжди найменший елемент
    heapq.heapify(cables)
    
    total_cost = 0
    
    # більше 1 кабеля
    while len(cables) > 1:
        # Витягуємо два найменші кабелі
        first_smallest = heapq.heappop(cables)
        second_smallest = heapq.heappop(cables)

        # Витрати на їх з'єднання
        connection_cost = first_smallest + second_smallest
        
        # + в загальні витрати
        total_cost += connection_cost
        
        # об'єднаний кабель назад у купу
        heapq.heappush(cables, connection_cost)
        # debug
        # print(f"З'єднуємо кабелі довжиною {first_smallest} і {second_smallest}")
        # print(f"Поточні витрати: {total_cost}")
        # print(f"Залишилися кабелі: {cables}")
        
    return total_cost


if __name__ == "__main__":
    # Приклад 1
    cables_list = [4, 3, 2, 6]
    # Логіка ручного підрахунку:
    # 1. Беремо 2 і 3 -> сума 5. Витрати: 5. Купа: [4, 6, 5] -> сортується як [4, 5, 6]
    # 2. Беремо 4 і 5 -> сума 9. Витрати: 5 + 9 = 14. Купа: [6, 9]
    # 3. Беремо 6 і 9 -> сума 15. Витрати: 14 + 15 = 29. Купа: [15]
    # Результат має бути 29.
    
    print(f"Вхідні кабелі: {cables_list}")
    result = minimize_cable_cost(cables_list)
    print(f"Мінімальні витрати: {result}")
    
    print("-" * 20)
    
    # Приклад 2
    cables_list_2 = [1, 2, 3, 4, 5]
    print(f"Вхідні кабелі: {cables_list_2}")
    result_2 = minimize_cable_cost(cables_list_2)
    print(f"Мінімальні витрати: {result_2}")
    # Логіка ручного підрахунку:
    # 1. Беремо 1 і 2 -> сума 3. Витрати: 3. Купа: [3, 3, 4, 5] -> сортується як [3, 3, 4, 5]
    # 2. Беремо 3 і 3 -> сума 6. Витрати: 3 + 6 = 9. Купа: [4, 5, 6] -> сортується як [4, 5, 6]
    # 3. Беремо 4 і 5 -> сума 9. Витрати: 9 + 9 = 18. Купа: [6, 9] -> сортується як [6, 9]
    # 4. Беремо 6 і 9 -> сума 15. Витрати: 18 + 15 = 33. Купа: [15]
    # Результат має бути 33.