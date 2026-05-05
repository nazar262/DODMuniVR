#!/usr/bin/env python3
from sys import stderr, stdout, argv

import gurobipy as gp
from gurobipy import GRB

pieces = [1,2,5,10,20,50,100,200,500,1000]

INFEASIBLE = 3
FEASIBLE_AND_BOUNDED = 2

def model_and_optimize_with_gurobi(S):
  with gp.Env(empty=True) as env:
    env.setParam('OutputFlag', 0)
    env.start()
    m = gp.Model(env=env)
    if debug_level<5:
        m.Params.LogToConsole = 0
    # TODO: create variables. For the method addVars see the official documentation at https://www.gurobi.com/documentation/current/refman/py_model_addvars.html 
    m.update()
    # TODO: add constraints
    # TODO: Set objective function
    m.optimize()
    if debug_level > 3:
        print(m.Status)
    assert m.Status==FEASIBLE_AND_BOUNDED        
    # TODO: read out and format the optimal solution computed by gurobi. For the method getObjective and the methods of an Objective object see the official documentation at https://www.gurobi.com/documentation/current/refman/py_model_getobjective.html
    
    optsol = [0] * len(pieces) # this will be just good enough to respect the intended communication protocol with the TALight server
    optval = sum(optsol)
    
    return optval, optsol


if __name__ == "__main__":
    debug_level = 0
    if len(argv) == 2:
        debug_level = int(argv[1])
    T = int(input())
    for t in range(1, 1 + T):
        S = int(input())
        if debug_level > 0:
            print(f"#\n# Testcase {t} ({S=}):", file=stderr)
        optval, optsol = model_and_optimize_with_gurobi(S)
        if debug_level > 1:
            print(f"# {optval=}\n# {optsol=}", flush=True, file=stderr)
        print(optval)
        print(" ".join(map(str,optsol)))
