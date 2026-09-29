def caesar_cipher(input_text, key, encrypt=True):
    characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
                  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
                  "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
                  "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "/", "+", " "]
    
    result = ""
    for char in input_text:
        if char in characters:
            if encrypt:
                result += characters[(characters.index(char) + key) % len(characters)]
            else:
                result += characters[(characters.index(char) - key) % len(characters)]
        else:
            result += char  
    
    return result


pt = input("Enter a string: ")
key = int(input("Enter a key length: "))
encrypted = caesar_cipher(pt, key, True)
print("Encrypted:", encrypted)

ct = input("Enter cipher text: ")
decrypted = caesar_cipher(ct, key, False)  
print("Decrypted:", decrypted)