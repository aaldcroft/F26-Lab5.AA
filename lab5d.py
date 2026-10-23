# Add comments before you do anything else.
#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Process File data.
# Usage: ./lab5d.py

# TO DO 1: Copy the files pythonStatements.txt and machineCode.txt in folder.
# TO DO 2: Follow the instructions from the readme.me file to create the exact output.
p=open("pythonStatements.txt","r")
m=open("machineCode.txt","r")
p_line=p.readline()
m_line=m.readline()
output=open("output.txt","w")

while p_line and m_line != "": 
    py=p_line.strip().split('#')[0].strip()
    mc=m_line.strip()
    output.write(py+'\t'+mc+'\n')
    p_line=p.readline()
    m_line=m.readline()
p.close
m.close


