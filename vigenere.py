# Jakub Opólski
import sys
import os
from collections import Counter
import numpy as np

FREQUENCIES = [
    0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 
    0.067, 0.075, 0.029, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001
]

def read_file(filename):
    if not os.path.exists(filename):
        return ""
    with open(filename, 'r') as file:
        return file.read().strip()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def vigenere_e(plain, key):
    key_length = len(key)
    crypto = ''
    key_int = [ord(i) - 97 for i in key]
    plain_int = [ord(i) - 97 for i in plain if i.isalpha()]
    for i in range(len(plain_int)):
        value = (plain_int[i] + key_int[i % key_length]) % 26
        crypto += chr(value + 97)
    return crypto

def vigenere_d(crypto, key):
    key_length = len(key)
    decrypt = []
    key_int = [ord(i) - 97 for i in key]
    key_index = 0

    for char in crypto:
        if char.isalpha():
            offset = 97 if char.islower() else 65
            value = (ord(char.lower()) - offset - key_int[key_index % key_length]) % 26
            decrypt.append(chr(value + offset))
            key_index += 1
        else:
            decrypt.append(char)

    return ''.join(decrypt)

def vignere_p(plain):
    return ''.join([char.lower() for char in plain if char.isalpha()])

def calculate_coincidences(text, shift):
    coincidences = 0
    for i in range(len(text) - shift):
        if text[i] == text[i + shift]:
            coincidences += 1
    return coincidences

def find_key_length(crypto):
    min_shift = 4
    max_shift = min(20, len(crypto) // 2)
    coincidences = []

    for shift in range(min_shift, max_shift + 1):
        matches = sum(1 for i in range(len(crypto) - shift) if crypto[i] == crypto[i + shift])
        coincidences.append((shift, matches))

    best_shift = min(coincidences, key=lambda x: (-x[1], x[0]))[0]
    
    return best_shift

def frequency_analysis(crypto, key_length):
    key = ''
    freq_vector = np.array(FREQUENCIES)
    
    for i in range(key_length):
        subtext = crypto[i::key_length]
        freq = Counter(subtext)
        
        subtext_vector = np.zeros(26)
        for letter, count in freq.items():
            subtext_vector[ord(letter) - 97] = count / len(subtext)

        best_shift = max(range(26), key=lambda j: np.dot(freq_vector, np.roll(subtext_vector, -j)))

        key += chr(97 + best_shift)

    return key

def vigenere_k(crypto):
    key_length = find_key_length(crypto)
    key = frequency_analysis(crypto, key_length)
    return key

def main():
    operation = sys.argv[1]
    
    if operation == '-p':
        plain = read_file('orig.txt')
        write_file('plain.txt', vignere_p(plain))
    elif operation == '-e':
        plain = read_file('plain.txt')
        key = read_file('key.txt')
        write_file('crypto.txt', vigenere_e(plain, key))
    elif operation == '-d':
        crypto = read_file('crypto.txt')
        key = read_file('key.txt')
        write_file('decrypt.txt', vigenere_d(crypto, key))
    elif operation == '-k':
        crypto = read_file('crypto.txt')
        key = vigenere_k(crypto)
        write_file('key-found.txt', key)
        write_file('decrypt.txt', vigenere_d(crypto, key))

if __name__ == "__main__":
    main()

