def encryption(ch, n):
    return chr((ord(ch) + ord(n)) % 256)


def decryption(ch, n):
    return chr((ord(ch) + (256 - ord(n))) % 256)


x = input("Enter text to be encrypted : ")
n = input("Enter the key to be used : ")
enc = ""
dec = ""
print("Encrypted")
inc = 0
for i in x:
    enc = enc + encryption(i, n[inc%len(n)])
    inc=inc+1
print("Encrypted message : ", enc)
print("Decrypted")
inc=0
for i in enc:
    dec = dec + decryption(i, n[inc%len(n)])
    inc=inc+1
print("Decrypted message : ", dec)
