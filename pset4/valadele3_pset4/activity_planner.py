#!/usr/bin/env python3.6

import requests, sys

if __name__ == "__main__":

    data = {'domain': open('domain.pddl', 'r').read(),
            'problem': open('problem.pddl', 'r').read()}

    resp = requests.post('http://solver.planning.domains/solve',
                        verify=False, json=data).json()

    plan = []
    for act in resp['result']['plan']:
        plan.append(act['name'])

    print(plan)