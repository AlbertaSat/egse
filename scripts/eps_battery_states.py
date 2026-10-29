import pyvisa

from time import sleep
from instr.psu.dp832a import DP832A

# DP832A_IP = "192.168.57.73" # Rigol DP832 #01 / ABS00086
DP832A_IP = "192.168.23.9" # ABS00003


rm = pyvisa.ResourceManager("@py")
psu = DP832A(rm, DP832A_IP)
try:
    #voltages = [8400, 7400, 7200, 7100, 6400, 5900, 6500, 7300, 7500, 8400]
    voltages = [8400, 5900, 6500, 8400]

    psu.protection_off(1, "ovp")
    psu.protection_on(1, "ocp")
    psu.set_protection(1, "ocp", 100)
    psu.set_function(1, "voltage", voltages[0])
    psu.set_function(1, "current", 1000)

    psu.output_on(1)
    for idx, voltage in enumerate(voltages):
        psu.set_function(1,"voltage", voltage) 
        sleep(10)
        print(f'Voltage Step {idx+1}/{len(voltages)}: Set Voltage: {voltage} mV, Measured Voltage: {psu.get_measure(1, "voltage")} mV')
        sleep(20)

    psu.output_off(1)
    psu.init()
except KeyboardInterrupt:
    print("\nExiting...")
    psu.output_off(1)
    psu.init()
    print("Power supply reset to safe state.")

