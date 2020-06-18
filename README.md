# DSL

## Description
This is a DSL project for generating different fractal images. 
We can construct fractals by introducing the idea of *initiators* and *generators*. An initiator is a starting shape. A generator is an arranged collection of scaled copies of the initiator. To generate fractals from initiators and generators, we follow a simple rule called  ***Fractal Generation Rule: At each step, replace every copy of the initiator with a scaled copy of the generator, rotating as necessary.***  We can see this rule applied in following example:
In this program you will generate different types of fractals, which are: 
- box fractal (1),
- cross form (2),
- crystal (3), 
- Koch snowflake (4), 
- Levy cyrve (5), 
- Peano-Gosper curve (6), 
- quadratic Koch island (7), 
- quadratic snowflake (8), 
- rings (9), 
- Sierpinsky sieve (10), 
- Sierpinsky arrowhead (11), 
- snowflake (12)

## Prerequisites
```python
import turtle
import colorsis
import math
```

## Installation 
Using the command line, desired fractal image is generated.
```python
  from __future__ import print_function
  import sys
  import importlib
  ```

The source file is the 1st argument to the script:

```python if len(sys.argv) != 2:
	 print('usage: %s <src.dsl>' % sys.argv[0])
	 sys.exit(1) 
```

Path to the Library (DSL -Library) containing fractal programs:
```python 
sys.path.insert(0, r'C:\Users\Пользователь\PycharmProjects\DSL-Library')
```

Read the .dsl file. Define % symbol as comment keyword and ignore the input after it. Split the input into tokens(parts):
```python with open(sys.argv[1], 'r') as file:
	 for line in file:
    	 line = line.strip()
    	 if not line or line[0] == '%':
        	 continue
    	 parts = line.split()
    	 print(parts)
```

Define the first token as the module. A module(like "koch") is the name of a .py file that generates the fractal(after getting the arguments):
 ```python  
 mod = importlib.import_module(parts[0])
 ```
      
Parsing the module name, function to be called(usually "draw") and arguments(parts[2] - axiom, part[3]):
```python 
getattr(mod, parts[1])(parts[2], parts[3])
```

> To generate a fractal type in the .dsl file , User should introduce following instructions:
        1 - Name of  desired Fractal
        2 - Action to be done (draw)
        3 - Axiom
        4 - Rule

>> boxFractal draw F-F-F-F F-F+F+F-F
>
>> kochSnowflake draw F--F--F F+F--F+F
>
>> quadraticKochIsland draw F+F+F+F F-F+F+FFF-F-F+F
>
>> crystal draw F+F+F+F FF+F++F+F
>
>> quadraticSnowflake draw F--F F-F+F+F-F
>
>> levyCurve draw F +F--F+
>
>> sierpinskiArrowhead draw YF YF+XF+Y
>
>> siepinskiSieve draw FXF--FF--FF FF
>
>> board draw F+F+F+F FF+F+F+F+FF
>
>> tiles draw F+F+F+F FF+F-F+F+FF
>
>> rings draw F+F+F+F FF+F+F+F+F+F-F
>
>> pentaplexity draw F++F++F++F++F F++F++F+++++F-F++F
>
>> peanoGosperCurve draw FX X+YF++YF-FX--FXFX-YF+
>
>> cross draw F+F+F+F F+FF++F+F

To run the program, User should type in the Command Line of his device:
```python 
python nameOfThisFile.py nameOfDSLfile.dsl
```

## Error Handling
In case user is using wrong syntax structure for DSL, the user will be notified about, for example: 

1. SYNTAXERROR : *!SYNTAXERROR Make sure to specify: <Fractal Name> <Keyword> <Shape> <Path> 
	* check the documentation or README for more information")*
2. FUNC_ERROR : *!FUNC_ERROR drew function not found, try: 'draw'*,
3. SHAPE_ERROR : !SHAPE_ERROR Shape contains invalid arguments, be sure to use 'F' or '+' & '-':
	>
	 F = forward
	>
	 `+` = Clockwise turn
	>
	 `-` = Counter-clockwise turn, 
4. PATH_ERROR : !PATH_ERROR Path contains invalid arguments, be sure to use 'F' or '+' & '-':
	>
	F = forward
	>
	`+` = Clockwise turn
	>
	`-` = Counter-clockwise turn.


## Contact Us 
```
alexa.tugulea@isa.utm.md
dominic.flocea@isa.utm.md
cristina.cocieri@isa.utm.md
carina.constantinova@isa.utm.md
```
