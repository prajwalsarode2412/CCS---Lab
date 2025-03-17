from Crypto.Cipher import AES
from secrets import token_bytes
key = token_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
msg = str(input("Enter the message : "))
data = msg.encode()
#data = "Hello Everyone!!!".encode()
ciphertext = cipher.encrypt(data)
print("Cipher text is:", ciphertext)
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print("Plain text is:", plaintext)