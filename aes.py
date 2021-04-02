from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
key = b'YOURKEYGYOURKEYG'
data = b'2020-10-04T17:42:03.263Z'
# key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_ECB) # CFB mode
# ciphered_data_out1 = cipher.encrypt(data)
ciphered_data_out = cipher.encrypt(pad(data, 16)) # Only need to encrypt the data, no padding required for this mode
# print(ciphered_data_out1)
print(ciphered_data_out)
ciphered_data_base64 = base64.b64encode(ciphered_data_out)
print(ciphered_data_base64)

test = str(ciphered_data_base64,'utf-8')
print(test)

ciphered_data = base64.b64decode(test)
cipher = AES.new(key, AES.MODE_ECB) # CFB mode
result = unpad(cipher.decrypt(ciphered_data), 16)

print(str(result,'utf-8'))