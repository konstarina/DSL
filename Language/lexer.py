"""
Program to perform tokenization, lexical analysis and parsing of the dsl file.
Short explanation - takes the information from an example.dsl file and splits in into tokens.
These tokens are send to a special function to be parsed.
Using the command line, the fractal image desired is generated.
"""
from __future__ import print_function

import sys
import importlib
import error

invalidSyntax = False

# The source file is the 1st argument to the script
if len(sys.argv) != 2:
    print('usage: %s <lang.dsl>' % sys.argv[0])
    sys.exit(1)

#Path to the Library (DSL -Library) containing fractal programs
sys.path.insert(0, r'..\DSL-Library')

#Read the .dsl file. Define % symbol as comment keyword and ignore the input after it.
#Split the input into tokens(parts)
with open(sys.argv[1], 'r') as file:
    for num, line in enumerate(file, 1):
        line = line.strip()
        if not line or line[0] == '%':
            continue
        parts = line.split()
        print(parts)

    try:
        #Define the first token as the module.
        #A module(like "koch") is the name of a .py file that generates the fractal(after getting the arguments)
        mod = importlib.import_module(parts[0])
    except ModuleNotFoundError:
        print("  ^" + "~" * (len(parts[0]) - 2) + "^\n")
        print(str(num) + " :!ERROR " + parts[0] + " is not a valid library")
        print("\nExamples of valid libraries are: kochSnowflake, crystal, rings etc.\nFor more examples read the documentation or README")
        invalidSyntax = True
    
    invalidSyntax = error.errorHandler(parts, num)

    #Parsing the module name, function to be called(usually "draw") and arguments(parts[2] - axiom, part[3])

    if(invalidSyntax == False):
        getattr(mod, parts[1])(parts[2], parts[3])

    #To generate a fractal type in the .dsl file :
    # 1 - name of the fractal desired
    # 2 - action to be done (draw)
    # 3 - axiom
    # 4 - rules
    # Type in the command line of you device : "python nameOfThisFile.py nameOfDSLfile.dsl