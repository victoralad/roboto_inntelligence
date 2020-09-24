# CS 7469 - PSet3: Problem 2
# Solution (by E. Seraj - TA)

import requests, sys

# environments
env1 = 'blocksworld'
env2 = 'lunar'

env = env2  # PICK THE DESIRED ENVIRONMENT FROM ABOVE (e.g., either env1 or env2)

# building file names
file_ext = '.pddl'
domain_name = env + file_ext
problem_name = env + '_pb1' + file_ext

# read the PDDL data
data = {'domain': open(domain_name, 'r').read(), 'problem': open(problem_name, 'r').read()}

# calling solver, sitting back, taking a sip of my coffee and waiting for the majic to happen!
majic = requests.post('http://solver.planning.domains/solve', verify = False, json = data).json()

print('================== Solution Found =======================')
for stuff in majic['result']['plan']:
    print(stuff['name'])
print('=========================================================')
