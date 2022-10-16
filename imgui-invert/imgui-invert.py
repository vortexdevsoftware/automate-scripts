# Theme color inverter
# This script will load theme.txt containing various ImVec4() matches with float values inside
# The goal is to invert first 3 values for each ImVec4() automatically, e.x (1.00f, 0.45f, 0.00f, 1.00f) becomes (0.00f, 0.55f, 1.00f, 1.00f)
# This is easily done by subtracting each of the first 3 values from 1.00, thus inverting it.
# The text file will be modified with the inverted values, it may be a good idea to backup it before using this.
import re

# Open the file
with open('theme.txt', 'r') as file:
    # Read the contents of the file into memory.
    data = file.read()

# Compile a regex to capture the text we want to manipulate.
pattern = re.compile(r'ImVec4\((.*?), (.*?), (.*?), (.*?)\)')

# For each match, extract the text
for match in re.finditer(pattern, data):
    # Extract the matched text.
    s = match.group(0)
    # Extract the first 3 values.
    r = match.group(1)
    g = match.group(2)
    b = match.group(3)
    # Invert the values. (to convert r,g,b to float, the character 'f' should be removed) and then readded after the inversion
    # remember: only add first 2 float decimals.
    r = str(round(1.00 - float(r[:-1]), 2)) + 'f'
    g = str(round(1.00 - float(g[:-1]), 2)) + 'f'
    b = str(round(1.00 - float(b[:-1]), 2)) + 'f'
    # Replace the original text with the inverted text.
    data = data.replace(s, 'ImVec4(' + r + ', ' + g + ', ' + b + ', ' + match.group(4) + ')')

# Write the modified text back to the file.
with open('text.txt', 'w') as file:
    file.write(data)
