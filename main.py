import string

lowercase_list = list(string.ascii_lowercase)

x_list = lowercase_list
print(x_list)


def encrypt(message, shift_amount):
    encrypt_word = ""
    for letters in message:
        position = x_list.index(letters)
        new_position = position + shift_amount
        new_word = x_list[new_position]
        encrypt_word += new_word
    print(f"The encrypted word is: \n{encrypt_word}")


def decrypt(cypher_text, shift_amount):
    decrypt_word = ""
    for letters in cypher_text:
        position = x_list.index(letters)
        new_position = position - shift_amount
        new_word = x_list[new_position]
        decrypt_word += new_word
    print(f"The decoded word is: \n{decrypt_word}")


end = True
while end:
    text = input("Enter the word: \n")
    shift = int(input("Enter the shift number: \n"))
    shift = shift % 250
    decision = input("type 'encrypt' or decrypt: \n").lower()

    if decision == "encrypt":
        encrypt(message=text, shift_amount=shift)

    elif decision == "decrypt":
        decrypt(cypher_text=text, shift_amount=shift)
    restart = input("Do you what to restart 'yes' or 'no': \n").lower()
    if restart == "no":
        end = False
        print("good bye...")
