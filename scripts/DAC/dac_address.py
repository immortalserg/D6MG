#!/usr/bin/python

from MCP4728 import MCP4728_address
import time

# MCP_address(scl_gpio,sda_gpio,ldac_gpio)
dac = MCP4728_address(19,26,21)

# GET ADDRESS
# getaddress()
cur=dac.getaddress()
print('0x{0:02X}'.format(cur))
time.sleep(1)

# SET ADDRESS
# setaddress(curent_address,new_address)
dac.setaddress(cur,1)
time.sleep(1)

cur=dac.getaddress()
print('0x{0:02X}'.format(cur))
