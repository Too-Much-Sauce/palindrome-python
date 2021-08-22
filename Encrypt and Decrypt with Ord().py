#program encypts and decrypts text entered by using the ord function



def cipher(string_input):
    new_string = ""
    key = ord(string_input[0])
    for i in string_input:
        new_string += chr(key + ord(i))
    return new_string




def decipher(decode):
    new_decode_string = ""
    key = ord(decode[0])//2
    for i in decode:
        new_decode_string += chr(ord(i) - key)
    return new_decode_string




def main():
    message = input("Enter a phrase: ")
    result = cipher(message)
    print(result)
    print(decipher(result))



main()



