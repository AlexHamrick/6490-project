from struct import pack

def encrypt(string):
    """ TAKEN FROM ..."""
    key = 171
    result = pack(">I", len(string))
    for i in string:
        a = key ^ ord(i)
        key = a
        result += bytes([a])
    return result

def decrypt(string):
    """ TAKEN FROM ..."""
    key = 171
    result = ""
    for i in string:
        a = key ^ i
        key = i
        result += chr(a)
    return result