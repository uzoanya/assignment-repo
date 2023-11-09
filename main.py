# YUSUF AND SONS COMPANY

print('YUSUF AND SONS')
print('provide required data to calculate SI & CI')
p = float(input("Enter initial principal :"))
r = float(input("Enter interest rate :"))
n = float(input("Enter number of time interest applied per time period :"))
t = float(input("Enter number of time period elapsed :"))

SI = p * (1 + r * t)
CI = p * (1 + (r/n))**n * t

print("YUSUF AND SONS COMPANY")
print(f'SI of company is {SI}')
print(f'CI of company is {CI}')



