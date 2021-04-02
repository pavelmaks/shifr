from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
key = b'YOURKEYGYOURKEYG'
#data = b'666'
data = b'1537,2.5,12,8,50,2.4' #18
#data = b'1518120'
# key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_ECB) # CFB mode
ciphered_data_out = cipher.encrypt(pad(data, 16)) # Only need to encrypt the data, no padding required for this mode
print(ciphered_data_out)

ciphered_data_base64 = base64.b64encode(ciphered_data_out)
print(ciphered_data_base64)
test = str(ciphered_data_base64,'utf-8')
print(test)

#test = 'N2ZOOkYpsm5otZHlFKq1aw=='

ciphered_data = base64.b64decode(test)
cipher = AES.new(key, AES.MODE_ECB) # CFB mode
result = unpad(cipher.decrypt(ciphered_data), 16)
result = str(result,'utf-8')
print(result)