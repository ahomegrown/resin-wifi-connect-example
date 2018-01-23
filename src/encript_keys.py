import base64

filename = "KEYFILE"
with open(filename, "rb") as key_file:
    key = key_file.read()
    encoded_key = base64.b64encode(key)
    print(encoded_key.decode("ascii") )
