Text=input("enter text to  encript\n",)
key_ =int(input("Enter key to encript\n"))
cypher=""
for i in range(0, len(Text)):
    kee =ord(Text[i]) + key_
    cypher +=chr(kee)
print(cypher)