echo enter file name
read varname
cp ./$varname ./compiler/test.txt
python3 ./compiler/Main.py
