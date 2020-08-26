f = open("Arduino/script.py", "w")
indent = 0
indentA = 0
i = 0 

array = ['from time import sleep\n', 'from functions import *\n', 'LED_BUILTIN = 13\n', 'OUTPUT = "OUTPUT"\n', 'INPUT = "INPUT"\n','HIGH = True\n', 'LOW = False\n','render = 0\n', 'pin = 0\n', 'Serial = 0\n', 'lcd =0\n','def init(renderA, pinA, SerialA, lcdA, starttime):\n', '    global render\n', '    global pin\n', '    global Serial\n', '    global lcd\n', '    lcd = lcdA\n','    Serial = SerialA\n', '    render = renderA\n', '    pin = pinA\n', '    initsc(render, pin, starttime)\n', '\n']
for i in array:
    f.write(i)
with open("compiler/test.txt") as file_in:

    lines = []
    
    for line in file_in:
        indent = indentA
        if("{"in line):
            indentA = indentA + 1
        elif("}"in line):
            indentA = indentA - 1
        elif("LiquidCrystal" in line):
            line = ""
        elif("#include <LiquidCrystal.h>" in line):
            line = ""
        elif("rs =" in line and "en =" in line and "d4 =" in line):
            line = ""
        i = 0
        if("} else {" in line):
            line = "else:"
            indent = indent - 1
            indentA = indentA - 1
        lock = 0
        out = ""
        while i != len(line):
            if(lock == 1):
                out = out + line[i]
            elif(line[i] == " "):
                out = out + ''
            else:
                lock = 1
                out = out + line[i]
            i = i + 1
        #print(out)
        line = out
        line = line.replace("//", "#")
        line = line.replace("/*", '"""')
        line = line.replace("*/", '"""')
        line = line.replace(";", "")
        line = line.replace("int ", "")
        line = line.replace("const ", "")
        line = line.replace("delay(", "sleep(")
        line = line.replace("{", ":")
        line = line.replace("}", "")
        line = line.replace("loop()", "script()")
        line = line.replace("void", "def ")
        if("sleep(" in line):
            time = line.replace(')', '')
            time = time[6:]
            outtime = 0
            text = ""
            read = 0
            print(time)
            for char in time:
                if(char in "12234567890"):
                    outtime = (outtime * 10) + int(char)
                elif(char == "#"):
                    text = text + char
                    read = 1
                elif(read == 1):
                    text = text + char
            time = float(outtime / 1000)
            print(time)
            line = "sleep("+str(time)+")    "+text
        i = 0

        #print(indent)
        if(indent > 0):
            while i != indent:
                #print(i)
                line = "    "+line
                i = i + 1

        lines.append(line)
        f.write(line)
f.close()
#print(lines)