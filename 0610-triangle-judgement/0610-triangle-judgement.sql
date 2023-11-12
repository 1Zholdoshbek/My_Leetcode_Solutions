# Write your MySQL query statement below
select x,y,z,if(x+y>z and x+z>y and z+y>x,'Yes','No') as triangle from Triangle;