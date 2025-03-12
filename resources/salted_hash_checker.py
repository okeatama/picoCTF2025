from hashlib import sha256, sha3_256

hash_count = 1
found = False

target = input("Target: ").strip()

with open("salted_cheese_list.txt", "r") as file:
    while hash_count < 200000:
        for line in file:
            sha256hash = sha256(line.strip().encode("utf-8"))
            string_hash = sha256hash.hexdigest()
            for i in range(hash_count - 1):
                sha256hash = sha256(string_hash.encode("utf-8"))
                string_hash = sha256hash.hexdigest()
            
            if target == string_hash:
                print("Plaintext:", line)
                found = True
                break

        if found:
            break
        
        hash_count += 1

if not found:
    print("Not found")
    print(hash_count)