# Write your MySQL query statement below
select P.project_id, ROUND(AVG(Employee.experience_years),2) as average_years
from Project P
join Employee on P.employee_id=Employee.employee_id
GROUP BY P.project_id
ORDER BY P.project_id