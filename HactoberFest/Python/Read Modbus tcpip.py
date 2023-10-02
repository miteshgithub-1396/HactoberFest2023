from pymodbus.client.sync import ModbusTcpClient

# Replace these values with your Modbus TCP/IP device's information
host = "your_modbus_device_ip"  # IP address or hostname of the Modbus device
port = 502                      # Modbus TCP/IP port (usually 502)
unit_id = 1                     # Modbus unit ID
register_address = 0            # Starting address of the holding registers
num_registers = 5               # Number of registers to read

try:
    # Create a Modbus TCP/IP client
    client = ModbusTcpClient(host, port)

    # Connect to the Modbus device
    client.connect()

    # Read the holding registers
    response = client.read_holding_registers(register_address, num_registers, unit=unit_id)

    if response.isError():
        print("Modbus Error: {}".format(response))
    else:
        # Extract the data from the response
        data = response.registers

        # Print the data
        print("Holding Registers:")
        for i, value in enumerate(data, start=register_address):
            print("Register {}: {}".format(i, value))

finally:
    # Close the Modbus connection
    client.close()
