# Your friend, a computer science enthusiast, has recently created a simple password encryption algorithm. 
# They have shared the encryption function with you but are unsure if it's secure enough. 
# Your task is to analyze the algorithm and write a decrypter function to ensure that the passwords can be decrypted correctly.

# Encryption Algorithm:
# Your friend's encryption algorithm works as follows:

# Convert each character in the password to its ASCII code.
# Encrypt each character using a different encryption key from the provided array of keys. 
# If the array of keys is shorter than the password length, reuse the keys cyclically.
# Add each encryption key to the corresponding ASCII code.
# Convert the modified ASCII codes back to characters to generate the encrypted password.

# // const encryptedPassword1 = encryptPassword("password", [1, 2, 3]);
# console.log(encryptedPassword1); // Expected output: "qbtwfsue"
# print(ord('p'))
# 112+1 = 113 => ch(113)
# print(chr(113))

# String.prototype.charCodeAt()
# String.prototype.fromCharCode()
# ord(): This function returns the Unicode code point of the given Unicode character. It is the equivalent of JavaScript's String.prototype.charCodeAt() method.
# chr(): This function returns the character that corresponds to the given Unicode code point. It is the equivalent of JavaScript's String.fromCharCode() method.

def encryptedPassword(password, arr):
  res = []
  for i,ch in enumerate(password):
    # "password", [1, 2, 3] index of s = 3
    # print(i)
    index = i % len(arr)
    res.append(chr(ord(ch) + arr[index]))
  
  return ''.join(res)
print(encryptedPassword("password", [1, 2, 3])) # Expected output: "qcvtyrsf"
