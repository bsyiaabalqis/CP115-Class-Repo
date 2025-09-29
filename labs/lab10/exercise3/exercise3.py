monthly_income = int(input())
credit_score = int(input())
loan_amount = int(input())

# Determine credit score tiers and interest rates
if credit_score >= 700:
    interest_rate = 0.035
    max_loan_amount = monthly_income * 5
elif credit_score >= 600 and credit_score <= 699:
    interest_rate = 0.055
    max_loan_amount = monthly_income * 5
else: 
    interest_rate = 0
    max_loan_amount = 0
    
#Determine loan approval status
if monthly_income >= 4000 and credit_score >= 600 and loan_amount <= monthly_income * 5: 
    approval_status = "Approved"
else: 
    approval_status = "Denied"

print(interest_rate)
print(max_loan_amount)
print(approval_status)