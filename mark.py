
# make terminal call

import os
import sys

# get the path of the current file
path = "./a2.py"
call = "flake8" + " " + path
# get output from stdout
output = os.popen(call).read()

error_codes = [a[1] for a in [b.split() for b in output.split("\n") if b != ""]]
too_longs = len(list(filter(lambda a: a == "E501", error_codes)))
global_vars = len(list(filter(lambda a: a == "GV400:", error_codes)))
missing_docs = len(list(filter(lambda a: a == "D101" or a == "D103", error_codes)))

call = "rg uv_to_speed_direction"
output = os.popen(call).read()

print("Too long lines: " + str(too_longs))
print("Global variables: " + str(global_vars))
print("Missing docstrings: " + str(missing_docs))
print(output)




