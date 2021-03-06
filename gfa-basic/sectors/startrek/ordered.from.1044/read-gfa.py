#!/usr/bin/env python3

import sys

identifiers = []

def gosub_parms(bites):
  bites_hex = '{:02x}'.format(bites[0]) + '{:02x}'.format(bites[1])
  proc_idx = int(bites_hex,16)
  return identifiers[11][proc_idx] + " " +dump_parms(bites[2:])

def no_parms(bites):
  return ""

def comment_parms(bites):
  return bites.decode("utf-8")

def dump_parms(bites):
  retval = ""
  for b in range(0,len(bites),2):
    retval = retval + "{:02x} {:02x} ".format(bites[b],bites[b+1])
  return retval  

def sput_parms(bites):
  bites_hex = "00" + '{:02x}'.format(bites[1])
  str_idx = int(bites_hex,16)
  return identifiers[1][str_idx]

def obg_parms(bites):
  bites_hex = '00' + '{:02x}'.format(bites[1])
  proc_idx = int(bites_hex,16)
  return identifiers[11][proc_idx]

def let_fp_parms(bites):
  return let_parms(0,bites)

def let_string_parms(bites):
  return let_parms(1,bites)

def let_bool_parms(bites):
  return let_parms(3,bites)

def let_fp_ary_parms(bites):
  return let_parms(4,bites)

def let_bool_ary_parms(bites):
  return let_parms(7,bites)

def let_parms(id_type, bites):
  bites_hex = '{:02x}'.format(bites[0]) + '{:02x}'.format(bites[1])
  var_idx = int(bites_hex,16)
  return identifiers[id_type][var_idx] + " " +dump_parms(bites[2:])
  
default_op = { "name" : "????", "args": lambda x: "", "openindent":False, "closeindent":False}

gfa_ops = {
  0   :  { "name": "DO",              "args": no_parms,    "openindent":True,  "closeindent":False},
  4   :  { "name": "LOOP",            "args": no_parms,    "openindent":False,  "closeindent":True},
  24  :  { "name": "PROCEDURE",      "args": gosub_parms, "openindent":True,  "closeindent":False},
  28  :  { "name": "RETURN",          "args": no_parms,    "openindent":False,  "closeindent":True},
  32  :  { "name": "IF",             "args": dump_parms,  "openindent":True,  "closeindent":False},
  36  :  { "name": "ENDIF",          "args": no_parms,    "openindent":False, "closeindent":True},
  48  :  { "name": "SELECT",         "args": dump_parms,  "openindent":True, "closeindent":False},
  52  :  { "name": "ENDSELECT",      "args": dump_parms,  "openindent":False, "closeindent":True},
  56  :  { "name": "ELSE",            "args": dump_parms,  "openindent":True, "closeindent":True},
  64  :  { "name": "ELSE IF",        "args": dump_parms,  "openindent":True, "closeindent":True},
  76  :  { "name": "FOR",            "args": let_fp_parms,  "openindent":True,  "closeindent":False},
  80  :  { "name": "FOR",            "args": let_fp_parms,  "openindent":True,  "closeindent":False},
  84  :  { "name": "FOR",            "args": let_fp_parms,  "openindent":True,  "closeindent":False},
  88  :  { "name": "FOR",            "args": dump_parms,  "openindent":True,  "closeindent":False},
  92  :  { "name": "FOR",            "args": dump_parms,  "openindent":True,  "closeindent":False},
  96  :  { "name": "FOR",            "args": dump_parms,  "openindent":True,  "closeindent":False},
  100 :  { "name": "FOR",            "args": dump_parms,  "openindent":True,  "closeindent":False},
  104 :  { "name": "FOR",            "args": dump_parms,  "openindent":True,  "closeindent":False},
  108 :  { "name": "FOR",            "args": dump_parms,  "openindent":True,  "closeindent":False},
  112 :  { "name": "FOR",            "args": dump_parms,  "openindent":True,  "closeindent":False},
  120 :  { "name": "FOR",            "args": dump_parms,  "openindent":True,  "closeindent":False},
  124 :  { "name": "NEXT",           "args": dump_parms,  "openindent":False, "closeindent":True},
  128 :  { "name": "NEXT",           "args": dump_parms,  "openindent":False, "closeindent":True},
  132 :  { "name": "NEXT",           "args": dump_parms,  "openindent":False, "closeindent":True},
  136 :  { "name": "NEXT",           "args": dump_parms,  "openindent":False, "closeindent":True},
  140 :  { "name": "NEXT",           "args": dump_parms,  "openindent":False, "closeindent":True},
  144 :  { "name": "NEXT",           "args": dump_parms,  "openindent":False, "closeindent":True},
  148 :  { "name": "NEXT",           "args": dump_parms,  "openindent":False, "closeindent":True},
  152 :  { "name": "NEXT",           "args": dump_parms,  "openindent":False, "closeindent":True},
  156 :  { "name": "NEXT",           "args": dump_parms,  "openindent":False, "closeindent":True},
  160 :  { "name": "NEXT",           "args": dump_parms,  "openindent":False, "closeindent":True},
  164 :  { "name": "NEXT",           "args": dump_parms,  "openindent":False, "closeindent":True},
  168 :  { "name": "NEXT",           "args": dump_parms,  "openindent":False, "closeindent":True},
  176 :  { "name": "SELECT",         "args": dump_parms,  "openindent":True, "closeindent":False},
  208 :  { "name": "LOOP UNTIL",     "args": dump_parms,  "openindent":False, "closeindent":True},
  216 :  { "name": ">PROCEDURE",     "args": gosub_parms,  "openindent":True, "closeindent":False},
  224 :  { "name": "CASE",           "args": dump_parms,   "openindent":True, "closeindent":True},
  240 :  { "name": "@",               "args": gosub_parms,  "openindent":False, "closeindent":False},
  244 :  { "name": "GOSUB",           "args": gosub_parms,  "openindent":False, "closeindent":False},
  304 :  { "name": "LET",            "args": let_fp_parms,  "openindent":False, "closeindent":False},
  308 :  { "name": "LET",            "args": let_string_parms,  "openindent":False, "closeindent":False},
  316 :  { "name": "LET",            "args": let_bool_parms,  "openindent":False, "closeindent":False},
  328 :  { "name": "LET",            "args": let_fp_ary_parms,  "openindent":False, "closeindent":False},
  340 :  { "name": "LET",            "args": let_bool_ary_parms,  "openindent":False, "closeindent":False},
  352 :  { "name": "PLOT",           "args": dump_parms ,  "openindent":False, "closeindent":False},
  460 :  { "name": "'",               "args": comment_parms,  "openindent":False, "closeindent":False},
  468 :  { "name": "DATA",           "args": dump_parms ,  "openindent":False, "closeindent":False},
  528 :  { "name": "ON BREAK GOSUB", "args": obg_parms,  "openindent":False, "closeindent":False},
  588 :  { "name": "PRINT",           "args": dump_parms,  "openindent":False, "closeindent":False},
  596 :  { "name": "TEXT",            "args": dump_parms,  "openindent":False, "closeindent":False},
  620 :  { "name": "LINE",            "args": dump_parms,  "openindent":False, "closeindent":False},
  640 :  { "name": "INC",             "args": let_fp_parms,  "openindent":False, "closeindent":False},
  840 :  { "name": "DIM",             "args": dump_parms,  "openindent":False, "closeindent":False},
  844 :  { "name": "SETCOLOR",        "args": dump_parms,  "openindent":False, "closeindent":False},
  1028 : { "name": "GET",             "args": dump_parms,  "openindent":False, "closeindent":False},
  1032 : { "name": "GET",             "args": dump_parms,  "openindent":False, "closeindent":False},
  1036 : { "name": "GET",             "args": dump_parms,  "openindent":False, "closeindent":False},
  1060 : { "name": "OPEN",            "args": dump_parms,  "openindent":False, "closeindent":False},
  1084 : { "name": "CLEAR",           "args": no_parms ,  "openindent":False, "closeindent":False},
  1108 : { "name": "DEFLINE",        "args": dump_parms,  "openindent":False, "closeindent":False},
  1136 : { "name": "DEFTEXT",        "args": dump_parms,  "openindent":False, "closeindent":False},
  1148 : { "name": "BOX",            "args": dump_parms,  "openindent":False, "closeindent":False},
  1164 : { "name": "CIRCLE",         "args": dump_parms,  "openindent":False, "closeindent":False},
  1260 : { "name": "CLS",            "args": dump_parms,  "openindent":False, "closeindent":False},
  1348 : { "name": "SGET",           "args": sput_parms,  "openindent":False, "closeindent":False},
  1356 : { "name": "SPUT",           "args": sput_parms,  "openindent":False, "closeindent":False},
  1436 : { "name": "CLIP",           "args": dump_parms,  "openindent":False, "closeindent":False},
  1448 : { "name": "EVERY",          "args": dump_parms,  "openindent":False, "closeindent":False},
  1488 : { "name": "READ",           "args": dump_parms,  "openindent":False, "closeindent":False},
  1548 : { "name": "BOUNDARY",       "args": dump_parms,  "openindent":False, "closeindent":False},
  1588 : { "name": "ARRAYFILL",      "args": dump_parms,  "openindent":False, "closeindent":False}
}


def read_32bit_uint_bigendian(f):
  bites = f.read(4)
  bites_hex = '{:02x}'.format(bites[0]) + '{:02x}'.format(bites[1]) + '{:02x}'.format(bites[2]) + '{:02x}'.format(bites[3]) 
  return int(bites_hex,16)

def read_16bit_uint_bigendian(f):
  bites = f.read(2)
  bites_hex = '{:02x}'.format(bites[0]) + '{:02x}'.format(bites[1])
  return int(bites_hex,16)

indent =0

def read_line(f):
  global indent
  length = read_16bit_uint_bigendian(f)
  op = read_16bit_uint_bigendian(f)
  remainder = f.read(length - 4)
  sys.stdout.write("{:04x}".format(length))
  sys.stdout.write(" ")
  hex_opcode = "{:04x}".format(op)
  sys.stdout.write(hex_opcode + "/")
  sys.stdout.write("{:04d}".format(op)+" ")
  opstruct = gfa_ops.get(op,default_op)
  if opstruct["closeindent"]:
    indent -=1
  for c in range(indent):
    sys.stdout.write("  ")
  sys.stdout.write(opstruct.get("name") + " ")
  sys.stdout.write(opstruct.get("args")(remainder))
  print()
  if opstruct["openindent"]:
    indent +=1

id_classes = ['#','$','%','!','#[]','$[]','%[]','![]','&','|','10',' procedure','&[]','|[]']
suffixes   = ['#','$','%','!','#[]','$[]','%[]','![]','&','|','10','','&[]','|[]']

sep = []
num_ids = []

with open("dsduel.gfa", "rb") as f:
#with open("PROC.GFA", "rb") as f:
  f.read(2)  # 2 bytes of version
  f.read(10) # 10 bytes of magic number
  for i in range(38):
    sep.append(read_32bit_uint_bigendian(f))

  #for i in range(38):
  #  print('{:d} {:08x}'.format(i,sep[i]))

  #print("identifier block is {:d} bytes long".format(sep[16] - sep[0]))
  for i in range(14):
    num_ids.append(int((sep[20+i] - sep[19+i]) / 4))

  for id_class in range(14):
    identifiers.append([])
    print("{:d} {:s} IDENTIFIERS".format(num_ids[id_class],id_classes[id_class]))
    id_counter=0
    while id_counter < num_ids[id_class]:
      id_length = int(f.read(1)[0])
      if id_length ==0:
        continue
      identifiers[id_class].append(f.read(id_length).decode("utf-8").lower() + suffixes[id_class])
      print("  {:x} {:s}".format(id_counter,identifiers[id_class][id_counter]))
      id_counter+=1 

  f.read(6)   # the bits between identifiers and program.

  while(True):
    read_line(f) 
