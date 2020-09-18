#!/usr/bin/env python3.6

import requests, sys
from  pddlpy import DomainProblem


if __name__ == "__main__":
    domprob = DomainProblem('domain.pddl', 'problem.pddl')

    data = {'domain': open('domain.pddl', 'r').read(),
            'problem': open('problem.pddl', 'r').read()}

    resp = requests.post('http://solver.planning.domains/solve',
                        verify=False, json=data).json()

    # with open('plan.ipc', 'w') as f:
    #     f.write('\n'.join([act['name'] for act in resp['result']['plan']]))
    
    plan = []
    for act in resp['result']['plan']:
        plan.append(act['name'])
    print(plan)