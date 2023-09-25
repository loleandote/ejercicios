import struct

# Define the format string for the struct
fmt = '<H6s'

# Define the values to pack
my_int = 12345
my_str = 'hello!'.encode()

# Pack the values into a bytes object
packed_data = struct.pack('<H6s', my_int, my_str)

# Print the packed data
print(struct.unpack(fmt,packed_data)[1].decode())