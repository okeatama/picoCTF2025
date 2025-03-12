### hash-only-1  

Interestingly enough, this time it gives a ssh instead of a hash or nc
`ssh ctf-player@shape-facility.picoctf.net -p 56301`

Here's the MD5 hash: 8c9735f569157a799a98bd2014190786  /root/flag.txt

I'll try to use hashcat again. I'm guessing the content would be something like picoCTF{flag}, so I'll have to make a rule

My hash-only.rule file:
```
^{ ^F ^T ^C ^o ^c ^i ^p $}
```

^ signifies to prepend and $ to append

`hashcat -m 0 8c9735f569157a799a98bd2014190786 rockyou.txt -r hash-only.rules`

It's not in the rockyou text file, maybe I should try other wordlists?

`hashcat -m 0 8c9735f569157a799a98bd2014190786 /usr/share/john/password.lst -r hash-only.rules`

Not in this one either... I tried a few others and I also haven't found it

I was also thinking of doing mask attacks, but that would be sort-of brute force and take too long

`hashcat -m 0 8c9735f569157a799a98bd2014190786 rockyou.txt -a 3 picoCTF{?a?a?a}`

I'll try John the Ripper just in case its a problem with hashcat maybe?

`john --format=raw-md5 --wordlist=rockyou.txt hash-only.txt --rules=hash-only`
`john --format=raw-md5 --wordlist --rules=hash-only hash-only.txt`

It still doesn't give anything...

### SOLVED BY tsumu

It's in fact not a hash cracking problem, but a reverse engineering problem. When putting in ghidra, the binary just calls "/bin/bash -c 'md5sum /root/flag.txt". Since it doesn't explicitly say which md5sum, we can make our own md5sum which just gives (cat) the flag instead of hashing it