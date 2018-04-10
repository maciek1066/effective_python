#  turning bytes into string
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # str


#  turning string into bytes
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # bytes


a = 'kółko się ślizga'
byt1 = to_bytes(a)
print(byt1)
str1 = to_str(byt1)
print(str1)
