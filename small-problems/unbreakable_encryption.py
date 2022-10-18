from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    tb = token_bytes(length)  # generate length random bytes
    # return bit string from the token bytes in tb with most significant byte at the beginning
    return int.from_bytes(tb, "big")  # bytes to int


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes = original.encode()  # converts str to sequence of UTF-8 bytes
    dummy = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, "big")
    encrypted = original_key ^ dummy
    #print(f"dummy:     {bin(dummy)}")
    #print(f"original:  {bin(original_key)}")
    #print(f"encrypted: {bin(encrypted)}")
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted = key1 ^ key2  # reverse XOR operation, returns original_key
    # +7 to round length up when //8.
    temp = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


if __name__ == "__main__":

    k1, k2 = encrypt("Check this out!")
    print(decrypt(k1, k2))
