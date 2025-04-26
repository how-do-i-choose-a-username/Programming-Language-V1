fileToRun = input("Enter name of .ral file to run: ")
fileToRun = fileToRun.replace(".ral", "")

code = open(fileToRun + ".ral", "r")
code = code.read()

while "include " in code:
    location = code[code.find("include "):]
    location = location.splitlines()[0]
    code = code.replace(location, "")
    location = location.replace("include ", "")
    extraCode = open(location, "r").read()
    code = "\n" + extraCode + "\n\n\n" + code

code = code.splitlines()
print("Running file\n")

newCode = ""
spacing = 0
inVar = False
variables = ["lst", "int"]

def removevariables(data):
    temp = data
    for i in range(len(variables)):
        temp = temp.replace("(" + variables[i] + " " , "( ")
        temp = temp.replace(" " + variables[i] + " ", " ")
        temp = temp.replace("," + variables[i] + " ", ", ")
    return temp

def defaultfunctionstuff(data):
    temp = data.replace("(", "(self, ", 1)
    temp += ":"
    temp = removevariables(temp)
    return temp

newCode = open("testing.py", "r").read()
newCode += "\n\n"

for i in range(len(code)):
    newCode += " " * spacing

    line = code[i]
    if "//" in line:
        line = line.split("//")[0]
    line = line.strip()

    if '{' in line:
        spacing += 4
        line = line.replace("{","")
    if '}' in line:
        spacing -= 4
        line = line.replace("}","")

    if spacing == 0:
        inVar = False

    if "@" in line:
        line = line.replace("@", "convert(")
        line += ")"

    skip = False
    for i in range(1, len(variables)):
        if line.startswith(variables[i] + " "):
            temp = line.replace(variables[i] + " ", "")
            temp = temp.strip()
            temp = temp + " = " + variables[i] + "()"
            newCode += temp
            newCode += "\n"
            skip = True
    if skip:
        continue

    if "my." in line and inVar:
            line = line.replace("my.", "self.")

    if line.startswith("lst "):
        temp = line.replace("lst ", "")
        temp = temp.strip()
        newCode += temp + " = []"
    elif line.startswith("repeat"):
        newCode += "while True:"
    elif line.startswith("exit"):
        newCode += "break"
    elif line.startswith("if"):
        temp = line.replace("if", "", 1)
        #temp = temp.replace("(", "", 1)
        #location = temp.rfind(")")
        #temp = temp[:location] + temp[location + 1:]
        temp = temp.replace("||", " or ")
        temp = temp.replace("&&", " and ")
        temp = temp.strip()
        newCode += "if " + temp + ":"
    elif line.startswith("else"):
        temp = line + ":"
        newCode += temp
    elif line.startswith("import "):
        continue    #   Stop people running potentally harmful code
    elif inVar:
        if line.startswith("new"):
            temp = line.replace("new", "def __init__", 1)
            temp = defaultfunctionstuff(temp)
            newCode += temp
        elif line.startswith("add"):
            temp = line.replace("add", "def __add__", 1)
            temp = defaultfunctionstuff(temp)
            newCode += temp
        elif line.startswith("subtract"):
            temp = line.replace("subtract", "def __sub__", 1)
            temp = defaultfunctionstuff(temp)
            newCode += temp
        elif line.startswith("multiply"):
            temp = line.replace("multiply", "def __mul__", 1)
            temp = defaultfunctionstuff(temp)
            newCode += temp
        elif line.startswith("divide"):
            temp = line.replace("divide", "def __truediv__", 1)
            temp = defaultfunctionstuff(temp)
            newCode += temp
        elif line.startswith("equals"):
            temp = line.replace("equals", "def __eq__", 1)
            temp = defaultfunctionstuff(temp)
            newCode += temp
        elif line.startswith("length"):
            temp = line.replace("length", "def __len__", 1)
            temp = defaultfunctionstuff(temp)
            newCode += temp
        elif line.startswith("modulus"):
            temp = line.replace("modulus", "def __mod__", 1)
            temp = defaultfunctionstuff(temp)
            newCode += temp
        else:
            newCode += line
    elif line.startswith("function "):
        temp = line.replace("function", "def", 1)
        temp += ":"
        extraTemp = ""
        temp = removevariables(temp)
            #extraTemp += "if (!isinstance(data, int)):\n" + (" " * (spacing + 4)) + 'raise Exception("Type mismatch")'
        newCode += temp
    elif line.startswith("variable "):
        temp = line.replace("variable ", "class ")
        temp += ":"
        newCode += temp
        temp = temp[:temp.find(":")]
        temp = temp.replace("class ", "")
        variables.append(temp)
        inVar = True
    else:
        newCode += line

    newCode += "\n"

output = open("output.py", "w")
output.write(newCode)
output.close()

exec(compile(newCode, "output", "exec"))