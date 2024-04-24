from tqdm import tqdm
import hashlib
import argparse

SUPPORTED_HASH_TYPES = [
    'blake2b', 'blake2s', 'md5', 'sha1', 'sha224', 'sha256', 'sha384',
    'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'sha512',
]

def crack_hash(hash_value, wordlist, hash_type='md5'):
    """Crack a hash using a wordlist.

    Args:
        hash_value (str): The hash to crack.
        wordlist (str): The path to the wordlist file.
        hash_type (str): The hash type to use. Default is 'md5'.

    Returns:
        str: The cracked password if found, otherwise None.
    """
    if hash_type not in SUPPORTED_HASH_TYPES:
        print(f"[!] Invalid hash type: {hash_type}. Supported types are: {', '.join(SUPPORTED_HASH_TYPES)}")
        return None

    try:
        print(f"[*] Cracking hash {hash_value} using {hash_type}.")

        with open(wordlist, 'rb') as f:
            for line in tqdm(f, desc='Cracking hash', unit=' lines'):
                try:
                    decoded_line = line.decode('utf-8').strip()
                except UnicodeDecodeError:
                    continue  # Skip lines that can't be decoded
                hashed = getattr(hashlib, hash_type)(decoded_line.encode()).hexdigest()
                if hashed == hash_value:
                    return decoded_line
    except FileNotFoundError:
        print("[!] Wordlist file not found.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

    return None

def main():
    parser = argparse.ArgumentParser(description='Crack a hash using a wordlist.')
    parser.add_argument('hash', help='The hash to crack.')
    parser.add_argument('wordlist', help='The path to the wordlist file.')
    parser.add_argument('--hash-type', help='The hash type to use.', default='md5')
    args = parser.parse_args()

    print()
    password = crack_hash(args.hash, args.wordlist, args.hash_type)
    if password:
        print("[+] Found password:", password)
    else:
        print("[-] Password not found.")

if __name__ == "__main__":
    main()
