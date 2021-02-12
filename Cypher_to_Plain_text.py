cypher=input("enter cypher text to  decrypt\n",)
key_ =int(input("Enter key to decrypt\n"))
Text=""
for i in range(0, len(cypher)):
    kee =ord(cypher[i]) - key_
    Text +=chr(kee)
print(Text)