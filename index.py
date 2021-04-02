import rsa
import base64

with open('pubkey.pem', mode='rb') as publicfile:
    keydata = publicfile.read()
pubkey = rsa.PublicKey.load_pkcs1(keydata, 'PEM')

with open('privkey.pem', mode='rb') as publicfile:
    keydata = publicfile.read()
privkey = rsa.PrivateKey.load_pkcs1(keydata, 'PEM')

message = 'hello Bob!'.encode('utf-8')
print(message)
crypto = rsa.encrypt(message, pubkey)
print(crypto)
temp = str(crypto)

print(temp)
# f = open("temp.bin", "bw")
# f.write(temp)
# f.close()
#
# with open('temp.bin', mode='rb') as publicfile:
#     temp2 = publicfile.read()

# message = rsa.decrypt(temp, privkey)
#
# print(message.decode('utf8'))
