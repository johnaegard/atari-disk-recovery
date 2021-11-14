#!/bin/env python3

import re

sector_counter = 0
SECTOR_SIZE = 512
GFA_HEADER = bytes([0x00,0x03,0x47,0x46,0x41,0x2d,0x42,0x41,0x53,0x49,0x43,0x33])
GFA_FOOTER = b'\x00\x04\x00\xB4\xE5'

running = True

with open("./gfa-basic.img", "rb") as f:
  while(running):
    sector_contents = f.read(SECTOR_SIZE)
    filename = ""
    if sector_contents.find(GFA_HEADER) != -1:
      filename = filename + "H" 
    # 6 identifiers
    if re.search(b'[A-Z_]+.[A-Z_]+.[A-Z_]+.[A-Z_]+.[A-Z_]+.[A-Z_]+',sector_contents):
      filename = filename + "I" 
    # 3 statements
    filename = filename + "C"
    # the footer
    if sector_contents.find(GFA_FOOTER) != -1:
      filename = filename + "F" 
    filename = "sectors/" + str(sector_counter) + ".sec" 
    with open(filename,"wb") as writer:
      writer.write(sector_contents)
    if sector_counter == 1440:
      running = False
    else:
      sector_counter = sector_counter +1 
    
print(str(sector_counter) + " sectors scanned")
