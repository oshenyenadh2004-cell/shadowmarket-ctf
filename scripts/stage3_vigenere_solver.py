"""
Stage 3 Solver - Coded Correspondence
Automates Vigenere decryption for the ShadowMarket Takedown Stage 3 challenge.
"""

def vigenere_decode(ciphertext, key):
    decoded = []
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.isupper():
                decoded_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decoded_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decoded.append(decoded_char)
            key_index += 1
        else:
            decoded.append(char)

    return ''.join(decoded)


if __name__ == "__main__":
    ciphertext = "VHRNYJSNT{JBFAUGE7VKCG}"
    key = "DARKKNG"

    result = vigenere_decode(ciphertext, key)
    print(f"Ciphertext: {ciphertext}")
    print(f"Key: {key}")
    print(f"Decoded flag: {result}")
