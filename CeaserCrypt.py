"""
Caeser's Crypt and Decrypt for ASCII Printables
including Space character
Assumptions:
1. Every line ends with a period.
2. Every sentence begins on a new line.
3. First letter of every line is in capital letters.
4. Key-length is 4.
5. All key letters are capital or special characters.
6. First key letter is capital letter.
"""

KEY = "X)($"
shifts = [ord(c) for c in KEY] #shift for each key letter
check = [1 for sh in shifts if 32 > sh or sh > 126]
check = check or ord(KEY[0]) not in range(65, 90)
if check : print("invalid key")


def encrypt(line):
    """Crypting Function"""
    otpt = ""
    for srno, c in enumerate(line):
        i = srno % len(KEY)
        j = ord(c) + shifts[i]
        
        # j should be within 32 to 126
        if j > 126 : j -= 95
        
        otpt += chr(j)
    return otpt + "\n"
        

def decrypt(line):
    """Decrypting Function"""
    otpt = ""
    for srno, c in enumerate(line[:-1]):
        i = srno % len(KEY)
        j = ord(c) - shifts[i]
        
        # j should be between 32 to 126
        if j < 32 : j += 95 #127 - 32
        otpt += chr(j)
    return otpt + "\n"


if not check:
    # Read Given File
    with open("NoWar.dat", "r") as f:
        text = f.readlines()
    
    # Put CR after the last line if missing
    text = [te.strip() + "\n" for te in text]
    
    # Crypt Given Text
    crypted = ""
    for line in text:
        lin1 = line.strip()
        line1 = encrypt(lin1)
        crypted += line1
    
    # Write Encrypted Message
    with open("Trump.dat", "w") as g:
        g.write(crypted)
    
    # Read Encrypted Message
    with open("Trump.dat", "r") as h:
        con_txt = h.readlines()
    
    # Decrypt Message
    decrypted = []
    for line1 in con_txt:
        line2 = decrypt(line1)
        decrypted.append(line2)
    
    # If original message properly retrieved print okay
    if text == decrypted:
        print("Okay")
    else:
        print("Error detected")


