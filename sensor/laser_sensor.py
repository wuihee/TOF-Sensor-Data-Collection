import serial


class LaserCommands:
    GET_STATUS = b"\xaa\x80\x00\x00\x80"
    DISTANCE = b"\xaa\x00\x00\x20\x00\x01\x00\x00\x21"


class LaserSensor:
    def __init__(self) -> None:
        self.PORT = "/dev/ttyUSB0"
        self.BAUDRATE = 115200

        self.ser = serial.Serial(self.PORT, self.BAUDRATE)
        self.ser.reset_input_buffer()

    def status(self) -> None:
        self._send_command(LaserCommands.GET_STATUS)
        protocol = self._read_protocol(9)
        print(self._convert_protocol_to_list(protocol))
        
    def measure_distance(self) -> int:
        self._send_command(LaserCommands.DISTANCE)
        protocol = self._read_protocol(13)
        data = self._convert_protocol_to_list(protocol)
        return int("".join(data[7:10]), base=16)
    
    def _send_command(self, command) -> None:
        self.ser.write(command)

    def _read_protocol(self, number_of_bytes: int) -> str:
        protocol = self.ser.read(number_of_bytes)
        return protocol

    def _convert_protocol_to_list(self, protocol: str) -> list[str]:
        return [f"{byte:02X}" for byte in protocol]
    
    def _get_distance(self, data: list[str]) -> int:
        pass
    
    def _get_signal_strength(self, data: list[str]) -> int:
        pass
        


laser = LaserSensor()
distance = laser.measure_distance()
print(distance / 1000)
