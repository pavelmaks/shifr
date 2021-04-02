import rsa
import base64

tempb=base64.b64decode(input())
print(tempb)
f = open("test2.pem", "rb")
keydata = f.read()
f.close()
privkey = rsa.PrivateKey.load_pkcs1(keydata, 'PEM')
message = rsa.decrypt(tempb, privkey)
print(message)