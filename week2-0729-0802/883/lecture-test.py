
# calculate npv
# def calculate_npv(rate, cash_flows):
#     npv = 0
#     for t, cash_flow in enumerate(cash_flows):
#         npv += cash_flow / (1 + rate) ** t
#     return npv

# cash_flows = [-1000, 0, 2000, 2000, 2000]  # 包括初始投资和未来现金流
# rate = 0.10  # 折现率

# npv = calculate_npv(rate, cash_flows)
# print(f"The NPV of the project is: {npv}")


# calculate ROI

def calculate_cumulative(values, discount):
    total = 0
    each_discount = 1
    for value in values:
        each_discount *= (1 - discount)
        total += value * each_discount
    return total

netProfit = calculate_cumulative([0, 200000, 200000, 200000], 0.08)
costs = calculate_cumulative([140000, 40000, 40000, 40000], 0.08)

print(f"The ROI of the project is: {(netProfit - costs) / costs * 100}%")

