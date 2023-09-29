import art

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


print(art.logo)


def caesar(start_text, shift, cipher_dir):
    endText = ""
    if cipher_dir == "decode":
        shift *= -1
    for ch in start_text:
        if ch in alphabet:
            pos = alphabet.index(ch)
            newPos = pos + shift
            endText += alphabet[newPos]
        else:
            endText += ch
    print(f"The {cipher_dir}d text is {endText}")


# def encrypt(plain_text, shift):
#     cipherText = ""
#     for ch in plain_text:
#         pos = alphabet.index(ch)
#         newPos = pos + shift
#         newPos = newPos % 26
#         cipherText += alphabet[newPos]
#     print(f"The encrypted text is {cipherText}")


# def decrypt(cipher_text, shift):
#     plainText = ""
#     for ch in cipher_text:
#         pos = alphabet.index(ch)
#         newPos = pos + 26 - shift
#         newPos = newPos % 26
#         plainText += alphabet[newPos]
#     print(f"The decrypted text is {plainText}")


# encrypt(plain_text=text, shift=shift)

should_run = True

while should_run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift=shift, cipher_dir=direction)
    wantAgain = input("Type 'yes' if you want to go again. Otherwise type 'no' \n")
    if wantAgain == "no":
        should_run = False
        print("Goodbye!")
