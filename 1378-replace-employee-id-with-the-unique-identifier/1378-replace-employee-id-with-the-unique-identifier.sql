# Write your MySQL query statement below

select EmployeeUNi.unique_id,Employees.name
from Employees
left join EmployeeUni on Employees.id=EmployeeUni.id
