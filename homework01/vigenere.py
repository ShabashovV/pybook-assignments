up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    j = 0
    for i in plaintext:
        keyletter = keyword[j % len(keyword)]
        if keyletter in up:
            k = up.index(keyletter)
        else:
            k = low.index(keyletter)
        if i in up:
            x = up.index(i)
            ciphertext += up[(x + k) % len(up)]
            j+=1
        elif i in low:
            x = low.index(i)
            ciphertext += low[(x + k) % len(up)]
            j += 1
        else:
            ciphertext += i
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    j = 0
    for i in ciphertext:
        keyletter = keyword[j % len(keyword)]
        if keyletter in up:
            k = up.index(keyletter)
        else:
            k = low.index(keyletter)
        if i in up:
            x = up.index(i)
            plaintext += up[(x - k) % len(up)]
            j += 1
        elif i in low:
            x = low.index(i)
            plaintext += low[(x - k) % len(up)]
            j += 1
        else:
            plaintext += i
    return plaintext
