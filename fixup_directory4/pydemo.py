value = b'\xb9\x01\xef'
print(len(value))
value2=value.hex()
print(len(value2))
print(value2)
'b901ef'
value.hex(':')
'b9:01:ef'
value.hex(':', 2)
'b9:01ef'
value.hex(':', -2)
'b901:ef'