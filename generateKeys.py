import rsa

(pubkey, privkey) = rsa.newkeys(1024)
# pubkey_pem = pubkey.save_pkcs1()
# privkey_pem = privkey.save_pkcs1()
f = open("privkey.pem", "bw")
f.write(privkey)
f.close()
f = open("pubkey.pem", "bw")
f.write(pubkey)
f.close()


