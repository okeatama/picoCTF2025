### guess my cheese 2

`nc verbal-sleep.picoctf.net 58535`

This time we got a hash, which after looking at the hints, it is a SHA-256 hash with 1 byte of hexadecimal character salt. We also got the word list of possible cheeses, so I think a dictionary attack is possible

Let's give hashcat a try using a combinator attack. I'm not sure if the salt is appended or prepended or other methods, so I'll try what I can

```
hashcat -a 6 -m 1400 ciphertext.txt cheese_list.txt ?H
hashcat -a 6 -m 1400 ciphertext.txt cheese_list.txt ?h
hashcat -a 7 -m 1400 ciphertext.txt ?H cheese_list.txt
hashcat -a 7 -m 1400 ciphertext.txt ?h cheese_list.txt
hashcat -a 6 -m 17400 ciphertext.txt cheese_list.txt ?H
hashcat -a 6 -m 17400 ciphertext.txt cheese_list.txt ?h
hashcat -a 7 -m 17400 ciphertext.txt ?H cheese_list.txt
hashcat -a 7 -m 17400 ciphertext.txt ?h cheese_list.txt
```

It exhausted all of these attacks, so I guess it won't be so easy. Third hint mentions about rainbow tables, so I'm wondering if the hash is a result of multiple salt+hash methods.