ANALOG_REF_VOLTAGE = 3.3;
    
    # sensor #1
CO_WORKING_ELECTRODE_ZERO_OFFSET_MV  = 310;
CO_AUXILIARY_ELECTRODE_ZERO_OFFSET_MV  = 272;
CO_SENSITIVITY = 0.197; # mV/ppb
# reverse to raw readings
def reverse_co(CO_working=None, CO_aux=None, ppbCO=None):
    
    raw_CO_working_1 = CO_working * 1024.0 / (1000.0 *ANALOG_REF_VOLTAGE)
    
    raw_CO_aux = CO_aux * 1024.0 / (1000.0 * ANALOG_REF_VOLTAGE)

    raw_CO_working_2 = (ppbCO * CO_SENSITIVITY + CO_WORKING_ELECTRODE_ZERO_OFFSET_MV) * 1024.0 / (1000.0 * ANALOG_REF_VOLTAGE)
    
    
    return raw_CO_working_1, raw_CO_working_2, raw_CO_aux

readings = [ reverse_co(ppbCO = 670.768, CO_aux = 350.734, CO_working = 442.138),
reverse_co(ppbCO = 755.324, CO_aux = 349.612, CO_working = 458.793),
reverse_co(ppbCO = 882.585, CO_aux = 349.344, CO_working = 483.866)]
merged_with_kings = zip(readings,(200,300,400))

### This gives right trend and right order of magnitude

for x in merged_with_kings:
    print (x[0][0] -  (x[0][2] )  )/CO_SENSITIVITY, x[1] 
