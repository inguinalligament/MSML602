## This code is to solve problem 8 of the first HW asisgnment
import pulp as p

Lp_prob = p.LpProblem('Problem', p.LpMinimize)

# Create problem Variables 
x11 = p.LpVariable("x11", lowBound = 0, upBound = 1, cat = 'Continuous')   # Create a variable x11 >= 0
x12 = p.LpVariable("x12", lowBound = 0, upBound = 1, cat = 'Continuous')   # Create a variable x12 >= 0
x21 = p.LpVariable("x21", lowBound = 0, upBound = 1, cat = 'Continuous')   # Create a variable x21 >= 0
x22 = p.LpVariable("x22", lowBound = 0, upBound = 1, cat = 'Continuous')   # Create a variable x22 >= 0


# Objective Function
Lp_prob +=   1* x11 +  2 * x12 +  2 * x21 +  1 * x22
  
# Constraints:
Lp_prob += x11+x12 == 1
Lp_prob += x21+x22 == 1
Lp_prob += x11+x21 == 1
Lp_prob += x12+x22 == 1

Lp_prob += x11 >= x22*2.1
Lp_prob += x21*0.5 >= x12

  
# Display the problem
print(Lp_prob)
  
status = Lp_prob.solve()   # Solver
print(p.LpStatus[status])   # The solution status
  
# Printing the final solution
print(p.value(x11), p.value(x12), p.value(x21), p.value(x22), p.value(Lp_prob.objective))

## This code is to solve problem 5 of the first HW asisgnment
import pulp as p
Lp_prob = p.LpProblem('Problem', p.LpMaximize)

# Create problem Variables 
x = p.LpVariable("x", lowBound = 0, cat = 'Continuous')   # Create a variable x >= 0
y = p.LpVariable("y", lowBound = 0, cat = 'Continuous')   # Create a variable x >= 0
z = p.LpVariable("z", lowBound = 0, cat = 'Continuous')   # Create a variable x >= 0

# Objective Function
Lp_prob += 15 * x + 2 * y + z  

# Constraints:
Lp_prob += x <= 10
Lp_prob += x + y <= 17
Lp_prob += 2*x + 3*z <= 25
Lp_prob += y + z >= 11

status = Lp_prob.solve()   # Solver

print(p.LpStatus[status])   # The solution status

# Printing the final solution
print(p.value(x), p.value(y), p.value(z), p.value(Lp_prob.objective))
