# to use a module we need to import it
import module_01 as module_01
# to use a function from this module, we need to prefix its name with the module name
# eg:
module_01.add(5, 2)

# while importing we can also give it a nickname
import module_01 as mod1
# to use a function from this module, we need to prefix its name with the module nickname
# eg:
mod1.sub(5, 2)

# we can also import everything from a module
from module_01 import *
# this way you don't need to prefix the function name with the module name
# eg:
mul(2,3)

# we can also import a specific function(s) from a module
from module_01 import add
from module_01 import sub, mul
# this way you don't need to prefix the function name with the module name
# but this can also cause name conflicts


import module_02 as mod2

res = mod2.cm_to_inches(1)
print(f"1 cm = {res} inches")

res = mod2.inches_to_cm(1)
print(f"1 inch = {res} cm")
