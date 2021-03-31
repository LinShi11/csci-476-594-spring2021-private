## Intro to Crypto
###### Lin Shi (n92s773)
###### linshi1768@gmail.com
###### CSCI 476
###### March 30, 2021
<br>

### Task 1:
**What is cryptography?**

Cryptography is the science of secure communication techniques that will allow the information/data to be sent between a sender and a receiver and the unintended receiver have no access to the information. Cryptography will use some kind of key to encrypt the message into a unreadable form unless one has the key to decrypt the message.

**What problems does it solve?**

Cryptography will ensure the message/data is only between the sender and the intended receiver. Since the message has been transformed into some unreadable combination, they would not be able to read the information unless they have the key. This was widely used during war time as well as today on internet while data are being transferred everywhere.

**What potential issues are there in using and designing cryptography?**

In the earlier days, since cryptography is only shifting the letter by some space, one could brute force to find the answer. Additionally, the English language will contain some letters or phrases that will repeat more often than other, such as "th", "e", "the", and etc.. Therefore, one could use frequency analysis to find what has occurred more often and decrypt the message a little at a time. In fact, that is what we are doing for Task 2. Overall, many cryptography ideas are not perfect and it contains some logic, the only perfect cryptography is to use a key as long as your message every time where there are no patterns to observe. However, this is too expensive to accomplish every time.

**What are some of the big, important ideas in cryptography?**

Cryptography is important to ensure the message are secret among the sender and receiver(s). The process contains the encrypt program, decrypt program, encrypt key, decrypt key, the plaintext message, and the ciphertext. When the sender is sending the information, he/she will use the encrypt key and encrypt program to modify the plaintext. Then the modified text, ciphertext, will be send to the intended receiver, who will use the decrypt key and decrypt program to get the original message. When the receiver finds an error, he/she will know the message has been changed by some unintended viewer. In most of the private sessions, the encrypt key and decrypt key are the same. However, there are some public sessions, where the public key is available for everyone, and anyone could send the receiver messages using the public key and only the private key could be used to decrypt the message. Today, both public and private key communication is used everyday.

### Task 2:
In this task, we are trying to decrypt the ciphertext. Since we know this is a monoalphabetic substitution cipher, which means the cipher went in and replaced the each letter with some other letter. We will use the frequency analysis to get started: (Note: I also used [mypixwords](https://www.mypixwords.com/answers/) to find some words with missing letters.)
```
...
top 10 trigrams:
ybu : 70 (1.25%)
rxz : 55 (0.98%)
hto : 43 (0.77%)
xzf : 39 (0.70%)
uty : 33 (0.59%)
ptl : 30 (0.54%)
cxf : 26 (0.46%)
pii : 24 (0.43%)
ybp : 24 (0.43%)
quf : 23 (0.41%)
writing csv data to: 3grams.csv
...done!
```
```
[03/31/21]seed@VM:~/.../files$ tr 'ybu' 'THE' <ciphertext.txt> output1.txt
```
Since we know, THE, is the most frequently used trigrams, we could start here and replace all ybu with THE and store the first result in [output1](output1.txt).


```
top 10 trigrams:
THE : 70 (1.25%)
rxz : 55 (0.98%)
hto : 43 (0.77%)
xzf : 39 (0.70%)
EtT : 33 (0.59%)
ptl : 30 (0.54%)
cxf : 26 (0.46%)
pii : 24 (0.43%)
THp : 24 (0.43%)
qEf : 23 (0.41%)
writing csv data to: 3grams.csv
...done!
[03/31/21]seed@VM:~/.../files$ tr 'p' 'A' <output1.txt> output2.txt
```
As we observe the trigram after the modification, we can see THp is also on the list. Then by consulting the [wikipedia](https://en.wikipedia.org/wiki/Trigram), we know that THA is also very common; therefore, we will modify p to A and here is the [full output](output2.txt)

```
At ATTAjk
```
```
top 10 bigrams:
TH : 116 (2.07%)
ht : 102 (1.82%)
xz : 99 (1.77%)
fE : 97 (1.73%)
Ef : 88 (1.57%)
xf : 86 (1.53%)
HE : 84 (1.50%)
Ee : 76 (1.36%)
Et : 76 (1.36%)
tT : 75 (1.34%)
writing csv data to: 2grams.csv
...done!

top 10 trigrams:
THE : 70 (1.25%)
rxz : 55 (0.98%)
hto : 43 (0.77%)
xzf : 39 (0.70%)
EtT : 33 (0.59%)
Atl : 30 (0.54%)
cxf : 26 (0.46%)
Aii : 24 (0.43%)
THA : 24 (0.43%)
qEf : 23 (0.41%)
writing csv data to: 3grams.csv
...done!
[03/31/21]seed@VM:~/.../files$ tr 't' 'N' <output2.txt> output3.txt
```
Then with the example of At ATTAjk, we know the second word stars with a vowel; therefore, we should be using an not a. Additionally, on [wikipedia](https://en.wikipedia.org/wiki/Bigram), we can see that an is a frequently used bigram, so we will try making t to N. [Here](output3.txt) is the full output.


```
NEqEf ohqE exvExNE fEvxTE AjjEee Tx rxzf jxvazTEf EqEN hc THEr eAr THErfE jAii
```
```
[03/31/21]seed@VM:~/.../files$ tr 'qf' 'VR' <output3.txt> output4.txt
```
From the previous output, I found the phase NEqEf and EqEN. Then, I used [mypixword.com](https://www.mypixwords.com/answers/) to look for possible words and if we replace q with V and f with R, it will make up never and even. Which makes perfect sense. [Here](output4.txt) is the full output.

```
mHENEVER rxz eTART Tx mxNlER mHETHER exvETHhNo he vArsE A ihTTiE shT czNNr AsxzT
```
```
[03/31/21]seed@VM:~/.../files$ tr 'me' 'WS' <output4.txt> output5.txt
```
Next, within the previous output, it contains mHENEVER, which should be WHENEVER; eTART looks like START. [Here](output5.txt) is the output.

```
xNE, Tx
```
```
[03/31/21]seed@VM:~/.../files$ tr 'x' 'O' <output5.txt> output6.txt
```
When I was reading through to find patterns, I found two phrases that repeated many time, xNE and Tx. Therefore, I decided to try and replace x with O. [Here](output6.txt) is the output.

```
NEVER ohVE SOvEONE REvOTE AjjESS TO rOzR jOvazTER EVEN hc THEr SAr THErRE jAii
```
```
[03/31/21]seed@VM:~/.../files$ tr 'vjazr' 'MCPUY' <output6.txt> output7.txt
```
After all the replacement, we can read some of the sentences, NEVER something SOMEONE REMOTE ACCESS TO YOUR COMPUTER ... So I decided to replace all v, j, a, z, and r with the appropriate letters to make up that sentence. [Here](output7.txt) is the full output.

```
NEVER PAY ONihNE EwTORThON lEMANlS hT dUST ENCOURAoES MORE RANSOMWARE ATTACkS
```
```
[03/31/21]seed@VM:~/.../files$ tr 'ihwlok' 'LIXDGK' <output7.txt> output8.txt
```
Additionally, I found another sentence, which I assume, with the help of [mypixwords.com](https://www.mypixwords.com/answers/), to be NEVER PAY ONLINE EXTORTION DEMANDS something something ENCOURAGES MORE RANSOMWARE ATTACKS. Once again, I replaced the necessary letters. [Here](output8.txt) is the full output.  

```
IN THE PAST cEW YEARS UNIVERSITIES LIKE EVERYONE ELSE HAVE sECOME INCREASINGLY
AWARE Oc ONLINE THREATS CAMPUSES HAVE SEEN THEIR PAYROLL SYSTEMS COMPROMISED sY
 CRIMINALS WHO STEAL cACULTY AND STAcc PASSWORDS OcTEN sY MEANS Oc PHISHING EMAILS
```
```
[03/31/21]seed@VM:~/.../files$ tr 'cs' 'FB' <output8.txt> output9.txt
```
After those replacement, the words are pretty clear, cEW is FEW, sECOME is BECOME. [Here](output9.txt) is the full output.

```
NEVER PAY ONLINE EXTORTION DEMANDS IT dUST ENCOURAGES MORE RANSOMWARE ATTACKS
FOR INSTANCE ONE TRAINING HAD EIGHT MULTIPLE CHOICE gUESTIONS ONE OF WHICH ASK
EVEN DONT RECOGNInE AT THE END OF THEIR NAMES nIP RAR EXE JAR OR IF THEY
```
```
[03/31/21]seed@VM:~/.../files$ tr 'dgn' 'JQZ' <output9.txt> output10.txt
```
Lastly, I did a few cleanup by checking the letters that have not been modified. dUST is JUST, gUESTIONS would be QUESTIONS, and RECOGNInE is RECOGNIZE. [Here](output10.txt) is the final message after decryption.
```
[03/31/21]seed@VM:~/.../files$ tr [:upper:] [:lower:] <output10.txt> test1.txt
[03/31/21]seed@VM:~/.../files$ tr 'abcdefghijklmnopqrstuvwxyz' 'psjlucobhdkivtxagfeyzqmwrn' < test1.txt > test2.txt
[03/31/21]seed@VM:~/.../files$ diff test2.txt ciphertext.txt
[03/31/21]seed@VM:~/.../files$
```
Even after the decryption, I wanted to verify everthing, so I went backwards to encrypt all my message. First I made all uppercase letter to lowercase letter and store it in [test1](test1.txt). Then I gathered all my decryption key and stored it as encrypted test1 and stored the result in [test2](test2.txt). Then when I compared the encrypted file to the ciphertext given to us, there was no differences.

```
[03/31/21]seed@VM:~/.../files$ tr 'psjlucobhdkivtxagfeyzqmwrn' 'a-z' <test2.txt> test3.txt
[03/31/21]seed@VM:~/.../files$ diff test3.txt test1.txt
[03/31/21]seed@VM:~/.../files$
```
Additionally, I did the decryption in one step since I know what they are modified to and stored the result in [test3](test3.txt). When I compared test3 with what I came up with one step at a time (test1 since it is all lowercase), there was no difference. Thus I can guarantee that psjlucobhdkivtxagfeyzqmwrn is the key used to encrypt the message. Overall, when the monoalphabetic cipher is used, the frequency of words and phases are not changed. When we view those and find the common combinations used, we could decrypt the ciphertext one step at a time and get the correct result.
