encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
def decrypt_message(encrypted):
    msg = list(encrypted)
    s, e = 1, len(msg) - 2  # Adjusted for zero-based indexing

    while s < e:
        msg[s], msg[e] = msg[e], msg[s]
        s, e = s + 2, e - 2

    return "".join(msg)

# Decrypt the message
decrypted = decrypt_message(encrypted_message)

# Print the decrypted message
print(decrypted)