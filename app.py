import os, importlib, pkgutil
from problems.problem import Problem
from collections import OrderedDict

# Import all the modules in the problems directory
pkg_dir = os.path.dirname(__file__) + "/problems"
for (module_loader, name, ispkg) in pkgutil.iter_modules([pkg_dir]):
    importlib.import_module('.' + name, "problems")

# Create a dictionary from problem class name to the class object, sort by the name to order output
problem_class_info = {cls.__name__: cls for cls in Problem.__subclasses__()}
problems = OrderedDict(sorted(problem_class_info.items()))

# Instantiate each problem and run the solve functions
for class_name, class_type in problems.items():
    problem = class_type()
    print(f"--- {problem.name} ---")
    problem.solve_a()
    problem.solve_b()
    print()