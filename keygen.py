import hashlib
import os
import zcash
from zcash import SelectParams
from zcash.core import x, b2x, lx
from zcash.wallet import CKey, CBitcoinSecret, P2PKHBitcoinAddress
from binascii import hexlify, unhexlify
from mnemonic import Mnemonic

def gen_keys():
    SelectParams('testnet')
    m = Mnemonic('english')

    randbytes = os.urandom(16)
    random_code = m.to_mnemonic(randbytes)
    print(random_code)

    # h = hashlib.sha256(randbytes).digest()
    seckey = CBitcoinSecret.from_secret_bytes(randbytes)

    key = CKey(seckey)
    pubkey = key.pub
    print(b2x(pubkey))

    return seckey, b2x(pubkey)

def encode_addr(pubkey):
    address = P2PKHBitcoinAddress.from_pubkey(x(pubkey))
    return address
