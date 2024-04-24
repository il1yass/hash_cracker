# Hash Cracker

This is a simple Python script for cracking hashes using a wordlist.

## Description

The script takes a hash value and a wordlist file as input and attempts to crack the hash by comparing it with the hashed values of words from the wordlist. It supports various hash types such as MD5, SHA-1, SHA-256, etc.

## Features

- Supports multiple hash types including MD5, SHA-1, SHA-256, etc.
- Provides progress visualization using tqdm library.
- Command-line interface for easy usage.
- Gracefully handles errors and exceptions.

## Usage

```
python3 main.py <hash> <wordlist> [--hash-type <hash_type>]
```

- `<hash>`: The hash value to crack.
- `<wordlist>`: The path to the wordlist file.
- `--hash-type <hash_type>`: (Optional) The hash type to use. Default is 'md5'.

Example:
```
python3 main.py daaad6e5604e8e17bd9f108d91e26afe6281dac8fda0091040a7a6d7bd9b43b5 crackstation.txt
```

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/hash-cracker.git
```

2. Navigate to the project directory:

```
cd hash-cracker
```

3. Install dependencies:

```
pip install tqdm
```
