employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()
EPF_rate = 0.11
SOSCO_rate = 0.005

# TODO your code here
if tax_status == "Single":
    if base_salary >= 5000:
        tax_rate = 0.22
    else:
        tax_rate = 0.18
elif tax_status == "married":
    if base_salary >= 6000:
        tax_rate = 0.20  
    else: 
        tax_rate = 0.15
elif tax_status == "head":
    if base_salary >= 5500:
        tax_rate = 0.25
    else:
        tax_rate = 0.19 
else: 
    tax_rate = 0.0

# Calculate deductions 
income_tax = base_salary * tax_rate 
epf = base_salary * EPF_rate 
sosco = base_salary * SOSCO_rate 

# total deductions
total_deductions = income_tax + epf + sosco 

# Calculate net_salary
net_salary = base_salary - total_deductions 

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")