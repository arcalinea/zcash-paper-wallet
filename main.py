from keygen import *
from createqr import *

keys = gen_keys()
addr = encode_addr(keys[1])

print("In main")
print(addr)

easy_qr(addr)
