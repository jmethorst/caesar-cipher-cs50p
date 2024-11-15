import sys
from string import ascii_lowercase

def main():
    values = clean_input((get_inputs()))
    conv_text = caesar(*values)
    print(conv_text)


def caesar(message: str, is_encrypt: bool, change: int) -> str:
    converted_txt = ""
    num_letters_alphabet = len(ascii_lowercase)
    if not is_encrypt:
        change = -change
    for char in message:
        if char.isalpha():
            start_num_ascii = ord("A") if char.isupper() else ord("a")
            char = chr((ord(char) + change - start_num_ascii) %
                       num_letters_alphabet + start_num_ascii)
        converted_txt += char
    return converted_txt


def clean_input(values: tuple[str, str, str]) -> tuple[str, bool, int]:
    s, b, n = values
    text = s.strip()
    is_encrypt = b[0].lower() == "e"
    shift_number = int(n)
    return (text, is_encrypt, shift_number)


def get_inputs() -> tuple[str, str, str]:
    t: str = input("Provide the text to use:\n")
    m: str = input("Type E to encrypt, D to decrypt: ")
    s: str = input("provide a number for the shift value: ")
    if validate(t, m, s):
        return (t, m, s)


def validate(text: str, mode: str, shift: str) -> bool:
    if text == "":
        sys.exit("No text given, provide some text")
    if mode.lower() not in ("d", "decrypt", "e", "encrypt"):
        sys.exit("value given is invalid, use encrypt/e or decrypt/d")
    if not shift.isdecimal():
        sys.exit("invalid number given, use 0 or a positif number")
    return True


if __name__ == "__main__":
    main()
