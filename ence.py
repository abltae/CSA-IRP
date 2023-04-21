def encryptDecrypt(inpString, xorKey):
    # calculate length of input string and key
    strLen = len(inpString)
    keyLen = len(xorKey)
 
    # perform XOR operation of key
    # with every character in string
    result = ""
    for i in range(strLen):
        # use modulo operator to cycle through the key
        xorIndex = i % keyLen
        result += chr(ord(inpString[i]) ^ ord(xorKey[xorIndex]))
     
    return result
