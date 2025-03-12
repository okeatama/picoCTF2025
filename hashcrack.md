### hashcrack

The only we are given is a netcat to a url: nc verbal-sleep.picoctf.net 57192, then it gives 3 consecutive hashes

For this, I used hashcat and the dictionary is rockyou.txt

First hash: 482c811da5d5b4bc6d497ffa98491e38 (128-bit) so I tried MD5
hashcat -m 0 482c811da5d5b4bc6d497ffa98491e38 rockyou.txt
Result: password123

Second hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 (160-bit) I tried SHA1
hashcat 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745 -m 1400 rockyou.txt
Result: letmein

Third hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745 (256-bit) this could be one of the SHA-256, so I tried SHA2-256 first
hashcat 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745 -m 1400 rockyou.txt
Result: qwerty098