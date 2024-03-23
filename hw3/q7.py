import cvxpy as cp
import numpy as np
import veh_speed_sched_data as data

t = cp.Variable(data.d.shape)
fuel_consumption = cp.sum(data.a *  cp.multiply(cp.square(data.d), cp.inv_pos(t)) + data.b * data.d + data.c)

objective = cp.Minimize(fuel_consumption)

constraints = [t >= 0, t<= data.d/data.smin, t >= data.d/data.smax]

for i in range(data.n):
    sum = cp.sum(t[:i + 1])
    constraints += [data.tau_min[i] <= sum, sum <= data.tau_max[i]]

problem = cp.Problem(objective , constraints)
problem.solve()

print(problem.value)
print (t.value)

