
def get_the_file():
    
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    host = socket.gethostname() # Get local machine name
    port = 3360 # Reserve a port for your service.
    s.connect((host, port)) # Bind to the port

    f = open("Trump.dat", "w")
    data = None
    while True:
        m = s.recv(1024)
        data = m
        if m:
            while m:
                m = s.recv(1024)
                data += m
            else:
                break
    f.write(data)
    f.close()
    print("Received the file..")
    return


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


# To get the file, remove hash from following line
get_the_file()

length = 4
KEY = [" "]*length

with open("Trump.dat", "r") as h:
    crypt_txt = h.readlines()
    
first_letters = [line[0] for line in crypt_txt]
last_chars = [line[-2] for line in crypt_txt]
last_char_loc = [(len(line) - 2) % length for line in crypt_txt]

first_ords = list(map(ord, first_letters))
last_ords = list(map(ord, last_chars))

KEY[0] = chr(min(first_ords) + 30) 

try:
    assert length == len(set(last_char_loc))
    for i in range(1, length):
        for k, j in enumerate(last_char_loc):
            if j == i:
                val = last_ords[k] - 46
                if val < 32 : val += 95
                KEY[i] = chr(val)
                break
    
    #print("KEY =", "".join(KEY))
    
    shifts = list(map(ord, KEY))
    
    # Read Encrypted Message
    with open("Trump.dat", "r") as h:
        con_txt = h.readlines()
    
    # Decrypt Message
    decrypted = []
    for line1 in con_txt:
        line2 = decrypt(line1)
        decrypted.append(line2)
    
    print("".join(decrypted))
    
except:
    print("Message too short, decrypting not possible")



