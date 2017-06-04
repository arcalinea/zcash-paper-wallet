import hashlib
import os
import zcash
from zcash import SelectParams
from zcash.wallet import CKey, CBitcoinSecret, P2PKHBitcoinAddress
from binascii import hexlify, unhexlify
from mnemonic import Mnemonic


SelectParams('testnet')
m = Mnemonic('english')

randbytes = os.urandom(16)
random_code = m.to_mnemonic(randbytes)
print(random_code)

# h = hashlib.sha256(randbytes).digest()
seckey = CBitcoinSecret.from_secret_bytes(randbytes)

key = CKey(seckey)
pubkey = key.pub

address = P2PKHBitcoinAddress.from_pubkey(pubkey)
print(address)
