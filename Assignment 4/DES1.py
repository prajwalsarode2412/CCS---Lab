from Crypto.Cipher import DES
from secrets import token_bytes
key = token_bytes(8)
cipher = DES.new(key, DES.MODE_EAX)
nonce = cipher.nonce
msg = str(input("Enter the message: "))
data = msg.encode()
#data = "Hello Everyone, I am From Sanjivani!!!".encode()
ciphertext = cipher.encrypt(data)
print("Cipher text:", ciphertext)
cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print("Plain text:", plaintext)