expenses = []

sum = 0
num_expenses = int(input("Enter # of expenses: "))

for idx in range(num_expenses):
    expenses.append(float(input("Enter an expense: ")))

for expense in expenses:
    sum += expense
    
print('You spent €', sum, sep= '')