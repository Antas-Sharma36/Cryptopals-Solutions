from base64 import b16decode, b64encode
hexstring=b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

raw_data = b16decode(hexstring,casefold=True)
# print(type(raw_data))
encoded_data = b64encode(raw_data)
print(encoded_data)