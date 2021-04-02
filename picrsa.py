import Crypto
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto import Random

import base64

data=input()
datab64=base64.b64decode(data)
print(datab64)
private_key = RSA.importKey(open('privkeycrypto.pem').read())
print(private_key)
dsize = SHA.digest_size
sentinel = Random.new().read(dsize)
cipher_rsa = PKCS1_v1_5.new(private_key)
#datab64=input()
print(datab64)
message = cipher_rsa.decrypt(datab64,sentinel)
print(message)
data=str(message)
print(data)