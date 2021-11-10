#!/usr/bin/env python3

def read_32bit_int_bigendian(f):
  bites = f.read(4)
  bites_hex = '{:02x}'.format(bites[0]) + '{:02x}'.format(bites[1]) + '{:02x}'.format(bites[2]) + '{:02x}'.format(bites[3]) 
  return int(bites_hex,16)

id_classes = ['#','$','%','!','#[]','$[]','%[]','![]','&','|','10',' procedure','&[]','|[]']

sep = []
num_ids = []

with open("identifiers.bin", "rb") as f:
  f.read(2)  # 2 bytes of version
  f.read(10) # 10 bytes of magic number
  for i in range(38):
    sep.append(read_32bit_int_bigendian(f))

  for i in range(38):
    print('{:d} {:08x}'.format(i,sep[i]))

  print("identifier block is {:d} bytes long".format(sep[16] - sep[0]))
  for i in range(14):
    num_ids.append(int((sep[20+i] - sep[19+i]) / 4))

  for id_class in range(14):
    print("{:d} {:s} IDENTIFIERS".format(num_ids[id_class],id_classes[id_class]))
    id_counter=0
    while id_counter < num_ids[id_class]:
      id_length = int(f.read(1)[0])
      if id_length ==0:
        continue
      identifier = f.read(id_length).decode("utf-8")
      print("  {:x} {:s}{:s}".format(id_counter,identifier,id_classes[id_class]))
      id_counter+=1 


