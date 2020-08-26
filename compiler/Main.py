f = open("Arduino/script.py", "w")
print("James amazing compiler")
print("report any bugs plz")
print("Ver 1.1")
print("current support: Arduino ('pins') and LCD")
indent = 0
indentA = 0
i = 0 
lcdneed = False
#pin.disable([rs, en, d4, d5, d6, d7])
array = ['from time import sleep\nfrom functions import *\nLED_BUILTIN = 13\nOUTPUT = "OUTPUT"\nINPUT = "INPUT"\nHIGH = True\nLOW = False\nrender = 0\npin = 0\nSerial = 0\nlcd =0\ndef init(renderA, pinA, SerialA, lcdA, starttime):\n    global render\n    global pin\n    global Serial\n    global lcd\n    lcd = lcdA\n    Serial = SerialA\n    render = renderA\n    pin = pinA\n    initsc(render, pin, starttime)\nA0, A1, A2, A3, A4, A5 = "A0","A1","A2","A3","A4","A5"\n\n']
for i in array:
    f.write(i)
with open("compiler/test.txt") as file_in:

    lines = []
    
    for line in file_in:
        #print("in")
        #print(line)
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
            no = line.replace('rs =', '')
            no = no.replace('en =', '')
            no = no.replace('d4 =', '')
            no = no.replace('d5 =', '')
            no = no.replace('d6 =', '')
            no = no.replace('d7 =', '')
            #print(no)
            text = "rs, en, d4, d5, d6, d7 ="
            line = text + no
            lcdneed = True
        i = 0
        if("} else {" in line):
            line = "else:"
            indent = indent - 1
            indentA = indentA - 1
        lock = 0
        out = ""
        if("void setup()" in line):
            if(lcdneed):
                print("LCD detected and implmented")
                text = "    pin.disable([rs, en, d4, d5, d6, d7]) \n"
                line = line + text
        if("int" in line and ")" in line and "{" in line and "(" in line):
            line = line.replace("int ", "def ")
        
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
            #print(time)
            for char in time:
                if(char in "12234567890"):
                    outtime = (outtime * 10) + int(char)
                elif(char == "#"):
                    text = text + char
                    read = 1
                elif(read == 1):
                    text = text + char
            time = float(outtime / 1000)
            #print(time)
            if(text == ""):
                text = "\n"
            line = "sleep("+str(time)+")    "+text
        i = 0

        #print(indent)
        if(indent > 0):
            while i != indent:
                #print(i)
                line = "    "+line
                i = i + 1
        #print("out")
        #print(line)
        #print("")
        lines.append(line)
        f.write(line)
#print(lines)
f.close()
print("Done! to use run start.sh")
#print(lines)
