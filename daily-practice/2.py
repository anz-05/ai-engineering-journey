expressions - part 1 & 2
# --- constants ---
# fixed values that don't change: numbers, or text in single/double quotes
print(123)
print(98.6)
print('Hello World')

# --- reserved words ---
# Cannot be used as variable names, e.g.: True, false, none, if, for, while, import ...

# --- variables ---
# A named location in memory that stores a value, and can be changed later
x = 12.2
y = 14

# --- naming variables: compare the two ---
# Bad (meaningless names):
a = 35.0
b = 12.50
c = a * b
print(c)

# Good (self-explanatory names):
hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)

# --- Sentences/lines: the three basic patterns ---
x = 2          # Assignment statement
X = x + 2      # Assignment statement
print(x)       # print statement

# --- Numeric expressions: arithmetic operators ---
# +  addition        -  subtraction     *  multiplication
# /  division        **  power           %  remainder 

# --- order of evaluation (operator precedence) ---
# Highest to lowest: 
# Parenthesis > Power > Multiplication/Division/Remainder > Addition/Subtraction > left to right when equal
# worked wxample, steo by step:
x = 1 + 2 ** 3 / 4 * 5
# 2**3 = 8   ->   1 + 8/4*5   ->   8/4=2.0, 2.0*5=10.0   ->   1+10.0 = 11.0
print(x)   # should be print 11.0