# STUDENTS PERFORMANCE SYSTEM

students = [
    {"id": 1, "name": "Ali", "marks": (85, 90, 88)},
    {"id": 2, "name": "Sara", "marks": (92, 95, 91)},
    {"id": 3, "name": "Ahmed", "marks": (78, 84, 80)}
]
avg1 = sum(students[0]["marks"]) / len(students[0]["marks"])
avg2 = sum(students[1]["marks"]) / len(students[1]["marks"])
avg3 = sum(students[2]["marks"]) / len(students[2]["marks"])
averages = (avg1, avg2, avg3)
top_index = averages.index(max(averages))
top_student = students[top_index]["name"]
names = (
    students[0]["name"],
    students[1]["name"],
    students[2]["name"]
)
unique_marks = (
    set(students[0]["marks"]) |
    set(students[1]["marks"]) |
    set(students[2]["marks"])
)
print("Averages:", averages)
print("Top Student:", top_student)
print("Names:", names)
print("Unique Marks:", unique_marks)

# EMPLOYEE SKILLS

employees = {
    "Ali": {"Python", "SQL", "AWS"},
    "Sara": {"Python", "Databricks", "SQL"},
    "Ahmed": {"AWS", "Snowflake", "SQL"}
}
common = (
    employees["Ali"] &
    employees["Sara"] &
    employees["Ahmed"]
)
ali_only = employees["Ali"] - (
    employees["Sara"] | employees["Ahmed"]
)
all_skills = (
    employees["Ali"] |
    employees["Sara"] |
    employees["Ahmed"]
)
required = {"Python", "SQL"}
eligible = set()
if required.issubset(employees["Ali"]):
    eligible.add("Ali")
if required.issubset(employees["Sara"]):
    eligible.add("Sara")
if required.issubset(employees["Ahmed"]):
    eligible.add("Ahmed")
print("Common Skills:", common)
print("Ali Only Skills:", ali_only)
print("All Team Skills:", all_skills)
print("Eligible Employees:", eligible)

# SALES DATA

sales = [
    ("Laptop", 120000, 2),
    ("Mouse", 1500, 5),
    ("Keyboard", 3500, 3)
]
r1 = sales[0][1] * sales[0][2]
r2 = sales[1][1] * sales[1][2]
r3 = sales[2][1] * sales[2][2]
revenues = (r1, r2, r3)
total_revenue = sum(revenues)
top_index = revenues.index(max(revenues))
top_product = sales[top_index][0]
revenue_dict = dict(zip(
    (sales[0][0], sales[1][0], sales[2][0]),
    revenues
))
prices = {
    sales[0][1],
    sales[1][1],
    sales[2][1]
}
print("Revenues:", revenues)
print("Total Revenue:", total_revenue)
print("Top Product:", top_product)
print("Revenue Dictionary:", revenue_dict)
print("Unique Prices:", prices)

# CUSTOMER ORDERS

customers = {
    "C101": {"name": "Ali", "orders": [1200, 2500, 1800]},
    "C102": {"name": "Sara", "orders": [3000, 4500]},
    "C103": {"name": "Ahmed", "orders": [1500, 2000, 1000]}
}
total1 = sum(customers["C101"]["orders"])
total2 = sum(customers["C102"]["orders"])
total3 = sum(customers["C103"]["orders"])
totals = (total1, total2, total3)
customer_ids = tuple(customers.keys())
top_index = totals.index(max(totals))
top_id = customer_ids[top_index]
top_customer = customers[top_id]["name"]
spending = dict(zip(customer_ids, totals))
print("Customer Spending:", spending)
print("Top Customer:", top_customer)
print("Totals:", totals)

# COURSE ENROLLMENT

courses = {
    "Python": {"Ali", "Sara", "Ahmed"},
    "SQL": {"Sara", "Ahmed", "Zain"},
    "AWS": {"Ali", "Ahmed", "Zain"}
}
p = courses["Python"]
s = courses["SQL"]
a = courses["AWS"]
all_three = p & s & a
exactly_two = (
    ((p & s) - a) |
    ((p & a) - s) |
    ((s & a) - p)
)
exactly_one = (
    (p - s - a) |
    (s - p - a) |
    (a - p - s)
)
unique_students = p | s | a
print("Exactly Two:", exactly_two)
print("All Three:", all_three)
print("Exactly One:", exactly_one)
print("Unique Count:", len(unique_students))

# E-COMMERCE TRANSACTION

transactions = [
    {"id": 101, "customer": "Ali", "items": [("Laptop", 120000, 1), ("Mouse", 1500, 2)]},
    {"id": 102, "customer": "Sara", "items": [("Keyboard", 3500, 2), ("Mouse", 1500, 1)]},
    {"id": 103, "customer": "Ali", "items": [("Monitor", 45000, 1)]}
]
t1 = transactions[0]["items"]
t2 = transactions[1]["items"]
t3 = transactions[2]["items"]
total1 = t1[0][1] * t1[0][2] + t1[1][1] * t1[1][2]
total2 = t2[0][1] * t2[0][2] + t2[1][1] * t2[1][2]
total3 = t3[0][1] * t3[0][2]
totals = (total1, total2, total3)
total_revenue = sum(totals)
ali_spending = 0
if transactions[0]["customer"] == "Ali":
    ali_spending += total1
if transactions[1]["customer"] == "Ali":
    ali_spending += total2
if transactions[2]["customer"] == "Ali":
    ali_spending += total3
largest_index = totals.index(max(totals))
largest_transaction = transactions[largest_index]["id"]
unique_products = {
    t1[0][0], t1[1][0],
    t2[0][0], t2[1][0],
    t3[0][0]
}
print("Total Revenue:", total_revenue)
print("Ali Spending:", ali_spending)
print("Largest Transaction ID:", largest_transaction)
print("Unique Products:", unique_products)

# PIPELINE MONITORING

pipelines = {
    "pipeline_1": {"status": "success", "records": (1000, 1200, 1100)},
    "pipeline_2": {"status": "failed", "records": (800, 0, 0)},
    "pipeline_3": {"status": "success", "records": (1500, 1600, 1700)}
}
p1 = sum(pipelines["pipeline_1"]["records"])
p2 = sum(pipelines["pipeline_2"]["records"])
p3 = sum(pipelines["pipeline_3"]["records"])
totals = (p1, p2, p3)
names = tuple(pipelines.keys())
total_processed = sum(totals)
failed = set()
if pipelines["pipeline_1"]["status"] == "failed":
    failed.add("pipeline_1")
if pipelines["pipeline_2"]["status"] == "failed":
    failed.add("pipeline_2")
if pipelines["pipeline_3"]["status"] == "failed":
    failed.add("pipeline_3")
largest_index = totals.index(max(totals))
largest_pipeline = names[largest_index]
averages = {
    "pipeline_1": p1 / len(pipelines["pipeline_1"]["records"]),
    "pipeline_2": p2 / len(pipelines["pipeline_2"]["records"]),
    "pipeline_3": p3 / len(pipelines["pipeline_3"]["records"])
}
print("Total Processed:", total_processed)
print("Failed Pipelines:", failed)
print("Largest Pipeline:", largest_pipeline)
print("Average Records:", averages)

# BANKING TRANSACTION

accounts = {
    "A101": {"holder": "Ali", "transactions": [5000, -2000, 3000, -1000]},
    "A102": {"holder": "Sara", "transactions": [10000, -3000, -2000]},
    "A103": {"holder": "Ahmed", "transactions": [7000, -1500, 2500]}
}
t1 = accounts["A101"]["transactions"]
t2 = accounts["A102"]["transactions"]
t3 = accounts["A103"]["transactions"]
balance1 = sum(t1)
balance2 = sum(t2)
balance3 = sum(t3)
balances = {
    "A101": balance1,
    "A102": balance2,
    "A103": balance3
}
highest_balance = max(balances.values())
highest_id = tuple(balances.keys())[
    tuple(balances.values()).index(highest_balance)
]
all_transactions = t1 + t2 + t3
withdrawals = (
    min(t1[0], 0) + min(t1[1], 0) +
    min(t1[2], 0) + min(t1[3], 0) +
    min(t2[0], 0) + min(t2[1], 0) +
    min(t2[2], 0) +
    min(t3[0], 0) + min(t3[1], 0) +
    min(t3[2], 0)
)
total_withdrawals = abs(withdrawals)
largest_deposit = max(all_transactions)
print("Final Balances:", balances)
print("Highest Balance Account:", highest_id)
print("Total Withdrawals:", total_withdrawals)
print("Largest Deposit:", largest_deposit)

# PRODUCT RECOMMENDATION

users = {
    "Ali": {"purchased": {"Laptop", "Mouse"}, "wishlist": {"Keyboard", "Monitor", "Mouse"}},
    "Sara": {"purchased": {"Keyboard", "Monitor"}, "wishlist": {"Laptop", "Mouse"}},
    "Ahmed": {"purchased": {"Laptop", "Keyboard"}, "wishlist": {"Monitor", "Headphones"}}
}
a = users["Ali"]["purchased"]
s = users["Sara"]["purchased"]
h = users["Ahmed"]["purchased"]
at_least_two = (a & s) | (a & h) | (s & h)
ali_recommendations = users["Ali"]["wishlist"] - a
w1 = users["Ali"]["wishlist"]
w2 = users["Sara"]["wishlist"]
w3 = users["Ahmed"]["wishlist"]
shared_wishlist = (w1 & w2) | (w1 & w3) | (w2 & w3)
all_products = a | s | h | w1 | w2 | w3
print("Bought By At Least Two:", at_least_two)
print("Ali Recommendations:", ali_recommendations)
print("Shared Wishlist:", shared_wishlist)
print("All Products:", all_products)

# FINAL COMPANY ANALYSIS

company = {
    "departments": {
        "Engineering": {
            "employees": [
                ("Ali", 120000, {"Python", "AWS", "SQL"}),
                ("Sara", 150000, {"Python", "Databricks", "SQL"})
            ],
            "budget": 500000
        },
        "Analytics": {
            "employees": [
                ("Ahmed", 100000, {"SQL", "Power BI"}),
                ("Zain", 130000, {"Python", "SQL", "Tableau"})
            ],
            "budget": 400000
        }
    }
}

eng = company["departments"]["Engineering"]
ana = company["departments"]["Analytics"]

e1 = eng["employees"][0]
e2 = eng["employees"][1]
a1 = ana["employees"][0]
a2 = ana["employees"][1]

# 1. Payroll per department
eng_payroll = e1[1] + e2[1]
ana_payroll = a1[1] + a2[1]

payroll = {
    "Engineering": eng_payroll,
    "Analytics": ana_payroll
}

# 2. Company payroll
company_payroll = sum(payroll.values())

# 3. Highest-paid employee
all_employees = (e1, e2, a1, a2)

salaries = (e1[1], e2[1], a1[1], a2[1])
highest_index = salaries.index(max(salaries))
highest_paid = all_employees[highest_index][0]

# 4. Skills shared by all employees
common_skills = e1[2] & e2[2] & a1[2] & a2[2]

# 5. Engineering-only skills
eng_skills = e1[2] | e2[2]
ana_skills = a1[2] | a2[2]

eng_only = eng_skills - ana_skills

# 6. Remaining budget
eng_remaining = eng["budget"] - eng_payroll
ana_remaining = ana["budget"] - ana_payroll

remaining_budget = {
    "Engineering": eng_remaining,
    "Analytics": ana_remaining
}

# 7. Department with higher average salary
eng_avg = eng_payroll / len(eng["employees"])
ana_avg = ana_payroll / len(ana["employees"])

department_averages = {
    "Engineering": eng_avg,
    "Analytics": ana_avg
}

higher_avg = max(department_averages, key=department_averages.get)

# 8. Name-to-salary dictionary
name_salary = {
    e1[0]: e1[1],
    e2[0]: e2[1],
    a1[0]: a1[1],
    a2[0]: a2[1]
}

# 9. All unique skills
all_skills = e1[2] | e2[2] | a1[2] | a2[2]

# 10. Combined budget sufficient?
combined_budget = eng["budget"] + ana["budget"]
budget_sufficient = combined_budget >= company_payroll
print("1. Payroll:", payroll)
print("2. Company Payroll:", company_payroll)
print("3. Highest Paid:", highest_paid)
print("4. Common Skills:", common_skills)
print("5. Engineering Only:", eng_only)
print("6. Remaining Budget:", remaining_budget)
print("7. Higher Average Department:", higher_avg)
print("8. Name Salary:", name_salary)
print("9. All Skills:", all_skills)
print("10. Budget Sufficient:", budget_sufficient)

