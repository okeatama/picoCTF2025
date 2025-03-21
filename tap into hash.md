# Tap into hash

Given block_chain.py program, which basically creates a blockchain and encrypt it, and enc_flag containing the key and encrypted blockchain

Funnily enough, the blockchain is just to pad the flag, which is put in the middle of it. Part of encrypt() function:

```
# plaintext is blockchain string, inner_txt is the token/flag
midpoint = len(plaintext) // 2

first_part = plaintext[:midpoint]
second_part = plaintext[midpoint:]
modified_plaintext = first_part + inner_txt + second_part # L + secret + R
```

Analysing the program, the key given is just the raw key, so it is easily converted into the original random hex. This key will be used to XOR with the modified_plaintext, encrypting it.

The encrypted blockchain meanwhile, is the modified_plaintext XOR-ed per block (16 characters) with the SHA256 hash of key, stored in the exact same order. XOR is easily reversible.

tap_into_hash.py shows how it's ultimately done.