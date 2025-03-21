salts = ["{:01X}".format(i) for i in range(16)]

new_wordlist = open("salted_cheese_list.txt", "a")

with open("cheese_list.txt", "r") as file:
    for line in file:
        line = line.strip()
        for salt in salts:
            for i in range(len(line)):
                word = line[:i] + salt + line[i:] + '\n'
                new_wordlist.write(word)

            # word = line.strip() + salt + '\n'
            # new_wordlist.write(word)

            # word = salt + line.strip() + '\n'
            # new_wordlist.write(word)

            # salt = salt.lower()

            # word = line.strip() + salt + '\n'
            # new_wordlist.write(word)

            # word = salt + line.strip() + '\n'
            # new_wordlist.write(word)

new_wordlist.close()