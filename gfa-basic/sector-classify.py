#!/usr/bin/env python3

import glob
import os
import sys

directories = ['scrap', 'gurps-characters', 'gurps-combat', 'gurps-vehicles', 'startrek', 'starwars', 'warden','rolrdroid','contents','unknowm']

for d in directories:
  os.system("mkdir -p sectors/" +d)
  
for filepath in glob.iglob(r'sectors/*I*'):
  os.system('hd ' + filepath)
  print(filepath)
  for i,d in enumerate(directories):
    sys.stdout.write(str(i)+"-"+d+" ")
  v = None
  while v == None:
    v = input(":")
    try:
      v = int(v)
    except:
      v = None
      continue
    if v >= len(directories) or v < 0:
      v = None
  cmd = "mv -v " +filepath + " sectors/" + directories[v]
  print(cmd)
  os.system(cmd)  
