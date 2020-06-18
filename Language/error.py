from __future__ import print_function

import sys
import importlib

keywords = ["draw",]
path = "F+-"

def errorHandler(parts, line):

    if(len(parts) != 4):
        print("\n" + str(line) + " :!SYNTAXERROR Make sure to specify:\n<Fractal Name> <Keyword> <Shape> <Path>\n\n * check the documentation or README for more information")
        return True

    if(parts[1] not in keywords):
        print(" " * (len(parts[0]) + 6) + "^" + "~" * (len(parts[1]) - 2) + "^\n")
        print(str(line) + " :!FUNC_ERROR " + parts[1] + " function not found, try: 'draw'")
        printSyntaxInfo()
        return True

    for i in parts[2]:
        if i not in path:
            print(" " * (len(parts[0]) + len(parts[1]) + 10) + "^" + "~" * (len(parts[2]) - 2) + "^\n")
            print(str(line) + " :!SHAPE_ERROR Shape contains invalid arguments, be sure to use 'F' or '+' & '-':\n\nF = forward\n+ = Clockwise turn\n- = Counter-clockwise turn")
            printSyntaxInfo()
            return True

    for i in parts[3]:
        if i not in path:
            print(" " * (len(parts[0]) + len(parts[1]) + len(parts[2]) + 14) + "^" + "~" * (len(parts[3]) - 2) + "^\n")
            print(str(line) + " :!PATH_ERROR Path contains invalid arguments, be sure to use 'F' or '+' & '-':\n\nF = forward\n+ = Clockwise turn\n- = Counter-clockwise turn")
            printSyntaxInfo()
            return True

    return False

def printSyntaxInfo():
    print("\nSyntax:\n<Fractal Name> <Keyword> <Shape> <Path>\n\n * check the documentation or README for more information")