	# 2. Employee Record Management System				
					
	# Develop a Python application to manage employee information stored in a CSV file.				
					
	# Requirements				
	# 	Read employee records from employee.csv.			
	# 	Display all employee details.			
	# 	Search for an employee using Employee ID.			
	# 	Accept the filename using command-line arguments.	

import csv
import sys


filename = sys.argv[1] if len(sys.argv) > 1 else "employee.csv"

with open(filename, "r", newline="") as file:
	employees = list(csv.DictReader(file))

print("All Employee Records")
for employee in employees:
	print("Employee ID:", employee["Employee_ID"])
	print("Name:", employee["Name"])
	print("Salary:", employee["Salary"])
	print("--------------------")

search_id = input("Enter Employee ID to search: ")
found = False

for employee in employees:
	if employee["Employee_ID"] == search_id:
		print("Employee found:")
		print("Employee ID:", employee["Employee_ID"])
		print("Name:", employee["Name"])
		print("Salary:", employee["Salary"])
		found = True
		break

if not found:
	print("Employee not found.")
