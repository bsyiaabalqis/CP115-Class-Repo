employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here
if base_salary >= 5000 and "Single" 
    if tax_status == "single":
        tax_rate = 0.22
    else:
        tax_rate = 0.18
elif base_salary >= 6000:
    if tax_status == "married":
        tax_rate = 0.20  
    else: 
        tax_rate = 0.15

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")