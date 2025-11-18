# ROSALIND PROBLEMS + ANSWERS

# 1
# given two int give the int for the square of the hypotense of the right triangle
# whose legs have lengths a and b

with open('Variables and Arithmetic (3).txt', 'r') as f: # read file
    a, b = map(int, f.read().split()) 
result = a**2 + b**2
print(result)
    # f.read reads the entire file as string 
    # split splits the string by whitespace into list 
    # map converts string to int


# 2
# slice out a-b + c-d ... then join slices with a space
S = "Psalmopoeusa3ezSG8BPFk9J70lJjACB3XN8kF7lg3PbCKFLcWdWYWW9gGOM0GPPX3Y1KAmEnlBwKaoSSAcateniferZEFpcJjKlQumJERNqQ1nIHKQosP2TXUYwoNZov0QZOxxnf4hIPxALmXZjFX3peOEQFcXghnFXTBRrKAzLHzq" # strip  removes any extra lines or spaces (cleaning the input)
a, b, c, d = 0, 10, 82, 90
slice1 = S[a:b+1] # +1 because python grabs from start - not including end... i.e., for boundaries
slice2 = S[c:d+1]
result = slice1 + " " + slice2
print(result)
# from file
with open('Rosalind Strings and Lists.txt', 'r') as file:
    S = file.readline().strip()
    numbers = file.readline().strip()
a, b, c, d = map(int, numbers.split())
slice1 = S[a:b+1]
slice2 = S[c:d+1]
result = slice1 + " " + slice2
print(result)


#3
# given a < b < 10,000: give the sum of all odd integers from a-b, inclusively
odd = []
for i in range(4940, 9340+1):
    if i % 2 == 1:
        odd.append(i) # adds to list (in loop)
print(sum(odd))
# from file
with open('Conditions and Loops (1).txt', 'r') as file:
    numbers = file.readline().strip()
    a, b = map(int, numbers.split())
    odd = []
    for i in range(a, b+1):
        if i % 2 == 1:
            odd.append(i)
print(sum(odd))


# 4
# given a file containing < 1000 lines: give a file w all even numbered lines
with open('Rosalind ini5.txt', 'r') as file:
    lines = file.readlines()
even_lines = []
for line_numb, line in enumerate(lines, start=1):
     if line_numb % 2 == 0:
        even_lines.append(line)
with open('output.txt', 'w') as file:
    file.writelines(even_lines)

