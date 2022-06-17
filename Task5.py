
revenue = float(input("введите выручку фирмы: "))
costs = float(input("введите выручку издержки: "))
if revenue > costs:
    print(f"фирма получила прибыль - {revenue - costs:.2f}")
    print(f"рентабельность фирмы = {(revenue - costs)/revenue*100:.2f} %")
elif revenue == costs:
    print(f"прибыль фирмы равна нулю")
elif revenue < costs:
    print(f"фирма получила убыток - {costs - revenue:.2f}")