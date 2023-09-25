import struct
string1 = 'Hello!'
string2 = 'Goodbye!'
s = bytes(string1, 'utf-8')
s2 = bytes(string2, 'utf-8')
struct.pack("I I%ds H I%ds" % (len(s), len(s), s), len(s2), len(s2), s2)
struct.unpack("I I%ds H I%ds" % (len(s), len(s), s), (len(s2),), len(s2), s2)

print(s2.decode())