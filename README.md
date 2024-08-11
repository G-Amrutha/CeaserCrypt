# Caesar Cipher Programs

This project contains Python scripts that implement encryption and decryption using a modified Caesar cipher for ASCII printable characters.

## Files

- `Program A.py`: Implements a Caesar cipher with a specific key for encrypting and decrypting text.
- `Program B.py`: Receives a file over a network and decrypts its content using a Caesar cipher.
- `CeaserCrypt.py`: Provides functions for encrypting and decrypting text using a Caesar cipher.

## Requirements

- Python 3.x

## Usage

### Program A

1. Open the script `Program A.py`.
2. Modify the text you want to encrypt or decrypt within the script.
3. Run the script using:

   ```bash
   python Program\ A.py
   ```

### Program B

1. Ensure a server is sending a file named `Trump.dat`.
2. Run the script using:

   ```bash
   python Program\ B.py
   ```

3. The script will receive and decrypt the file content.

### CeaserCrypt

1. Use the functions provided in `CeaserCrypt.py` to encrypt or decrypt text.
2. Modify the `KEY` and input text as needed within the script.

## Key Assumptions

- Each line of input ends with a period.
- Each sentence starts on a new line.
- The first letter of each line is capitalized.
- The key length is fixed at 4 characters, starting with a capital letter.
