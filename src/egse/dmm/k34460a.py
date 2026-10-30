class K34460A:
    def __init__(self, rm):
        self.inst = rm.open_resource(f"USB0::10893::5889::MY59023523::0::INSTR") # Currently limited to USB as we don't have a license for LAN.
        self.inst.read_termination = '\n'
        self.inst.write_termination = '\n'

    
    def about(self):
        """
        Returns information about the multimeter.
        """
        try:
            idn = self.inst.query("*IDN?").split(',')
        except Exception as e:
            print(f"Error querying IDN: {e}")
        else:
            return {
                "manufacturer": idn[0],
                "model": idn[1],
                "serial": idn[2],
                "firmware": idn[3],
            }
        
    def get_measure(self, measure_type: str, range: str = "auto"):
            """
            Measure the voltage or current of a channel. Returns the measured value in mV/mA.
                measure_type: "vdc" for DC voltage
                range: "auto" for auto range, or 0.1, 1, 10, 100, or 1000 for manual range
            """
            if measure_type not in ["vdc"]:
                raise ValueError("Invalid measure type. Use 'vdc' for DC voltage.")
            if range not in ["auto"] + ["0.1", "1", "10", "100", "1000"]:
                raise ValueError("Invalid range. Use 'auto' or 0.1, 1, 10, 100, or 1000")

            try:
                if measure_type == "vdc":
                    res = self.inst.query(f':MEAS:VOLT:DC? {range}')
            except Exception as e:
                print(f"Error measuring {measure_type}: {e}")
            else:
                return float(res) * 1000 # return in mV/mA


    def query(self, command: str):
        """
        Manually send a command to the power supply. Returns the response.
            command: SCPI command string
        """
        return self.inst.query(command)
