import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def decode_secret_code(secret_code):
    return secret_code[3:-3]  

sentence = input("Enter the sentence to encode: ")

if len(sentence) < 3:
    secret_code = sentence[::-1]
else:
    random_string = generate_random_string(3)
    secret_code = random_string + sentence + random_string  

print("Encoded Secret Code:", secret_code)

decode_option = input("If you want to decode it, enter your encoded sentence or press Enter to skip: ")
if decode_option:
    decoded_sentence = decode_secret_code(decode_option)
    print("Decoded Sentence:", decoded_sentence)
