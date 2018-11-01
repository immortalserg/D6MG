#!/usr/bin/python

from MCP4728 import MCP4728

# MCP4728(i2c_address)
dac = MCP4728(0x61)

# specify the voltage of a channel using internal reference, voltage in absolute value
# single_internal(channel_number,absolute_voltage)
dac.single_internal(2,3)

# specify the voltage of a channel using external reference, voltage relative to VDD 
# single_external(channel_number,relative_voltage)
dac.single_external(2,0.5)
