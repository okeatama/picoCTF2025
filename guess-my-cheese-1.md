### Guess my cheese

We got a netcat as usual, let's see what pops up

![netcat result](https://github.com/alexbravo17/picoCTF2025/blob/main/images/guess-my-cheese-1.png)

A quick testing shows that:

1. You have 2 chance to encrypt and 1 chance to guess
2. The cheese to be guessed changes everytime you run it
3. What you encrypt and what you need to guess are types of cheeses
4. Cipher is same length as plaintext
5. Letter sequence is preserved, i.e. in the image above I use 'double gloucester', ciphertext shows 'ou' as 'DR' in both cases

From 4. and 5. it's reasonable to guess that its a simple substitution cipher, where one letter is mapped to another. Therefore, to make this simpler, I made a simple python program to automatically replace known letters. Retrying to get a smaller ciphertext to be guessed may also help.

I'm not a cheese connoisseur, so I asked AI (DeepSeek this time) to give me a combination of 2 cheese with the least overlap in letters while maximizing coverage of the alphabet. After a bit of tinkering, I got 'double gloucester' and 'kefalotyri'. All that's left is to attempt a lot of time, hoping that its enough to guess the cheese

![DeepSeek result](https://github.com/alexbravo17/picoCTF2025/blob/main/images/guess-my-cheese-1-deepseek.png)

The successful attempt goes as the image below:
![successful attempt python](https://github.com/alexbravo17/picoCTF2025/blob/main/images/guess-my-cheese-1-success.png)

"baCariaS bergkaselbo" is my final cipher/plaintext combo. Searching 'bergkaselbo' shows nothing, so I have to guess the first word as well, which after looking at the DeepSeek result of which letters are not covered, turns out to be "bavarian bergkaselbo". Idk if they intended to make it harder, but the actual cheese is Bavarian Bergkase (https://www.cheese.com/bavarian-bergkase/), but I got the flag nonetheless