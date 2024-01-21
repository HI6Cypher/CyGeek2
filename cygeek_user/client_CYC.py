import cyc_ceasar
import hashlib
import sys

def sum_digits(n) :
    x = sum(int(digit) for digit in str(n))
    if x < 10 :
        return x
    else:
        return sum_digits(x)

def cyc_hash(passkey) :
    data = hashlib.sha256(passkey.encode() if not isinstance(passkey, bytes) else passkey).digest()
    data = int.from_bytes(data, sys.byteorder)
    return data

def CYC(raw_data, passkey, backward = False) :
    hash = cyc_hash(passkey)
    k = sum_digits(hash) if not backward else -sum_digits(hash)
    ceasar = cyc_ceasar.cyc_ceasar(k, raw_data)
    data = ceasar
    return data


g = """What does EHLO do in SMTP?
EHLO ("Extended Hello") is the SMTP command the client uses to tell the server that it is an SMTP client ( HELO is the old SMTP protocol, while EHLO is the extended SMTP initialisation command)."""
d = CYC(g, "helloworld")
j = CYC(d[1], "helloworld", True)
print(j[1])