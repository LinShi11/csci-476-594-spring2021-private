## Lab05
###### Lin Shi (n92s773)
###### linshi1768@gmail.com
###### CSCI 476
###### March 23, 2021
<br>

### Task 1:
**What is cryptography?**
Cryptography is the study

**What problems does it solve?**

**What potential issues are there in using and designing cryptography?**

**What are some of the big, important ideas in cryptography?**

### Task 2:
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

```
NEqEf ohqE exvExNE fEvxTE AjjEee Tx rxzf jxvazTEf EqEN hc THEr eAr THErfE jAii
```

```
[03/31/21]seed@VM:~/.../files$ tr 'qf' 'VR' <output3.txt> output4.txt
```

```
mHENEVER rxz eTART Tx mxNlER mHETHER exvETHhNo he vArsE A ihTTiE shT czNNr AsxzT
```

```
[03/31/21]seed@VM:~/.../files$ tr 'me' 'WS' <output4.txt> output5.txt
```

```
xNE, Tx
```

```
[03/31/21]seed@VM:~/.../files$ tr 'x' 'O' <output5.txt> output6.txt
```

```
NEVER ohVE SOvEONE REvOTE AjjESS TO rOzR jOvazTER EVEN hc THEr SAr THErRE jAii
```

```
[03/31/21]seed@VM:~/.../files$ tr 'vjazr' 'MCPUY' <output6.txt> output7.txt
```

```
NEVER PAY ONihNE EwTORThON lEMANlS hT dUST ENCOURAoES MORE RANSOMWARE ATTACkS
```

```
[03/31/21]seed@VM:~/.../files$ tr 'ihwlok' 'LIXDGK' <output7.txt> output8.txt
```

```
IN THE PAST cEW YEARS UNIVERSITIES LIKE EVERYONE ELSE HAVE sECOME INCREASINGLY
AWARE Oc ONLINE THREATS CAMPUSES HAVE SEEN THEIR PAYROLL SYSTEMS COMPROMISED sY
 CRIMINALS WHO STEAL cACULTY AND STAcc PASSWORDS OcTEN sY MEANS Oc PHISHING EMAILS
```

```
[03/31/21]seed@VM:~/.../files$ tr 'cs' 'FB' <output8.txt> output9.txt
```

```
NEVER PAY ONLINE EXTORTION DEMANDS IT dUST ENCOURAGES MORE RANSOMWARE ATTACKS
FOR INSTANCE ONE TRAINING HAD EIGHT MULTIPLE CHOICE gUESTIONS ONE OF WHICH ASK
EVEN DONT RECOGNInE AT THE END OF THEIR NAMES nIP RAR EXE JAR OR IF THEY
```

```
[03/31/21]seed@VM:~/.../files$ tr 'dgn' 'JQZ' <output9.txt> output10.txt
```

```
[03/31/21]seed@VM:~/.../files$ tr 'abcdefghijklmnopqrstuvwxyz' 'psjlucobhdkivtxagfeyzqmwrn' < test1.txt > test2.txt
[03/31/21]seed@VM:~/.../files$ diff test2.txt ciphertext.txt
[03/31/21]seed@VM:~/.../files$
```

```
[03/31/21]seed@VM:~/.../files$ tr 'psjlucobhdkivtxagfeyzqmwrn' 'a-z' <test2.txt> test3.txt
[03/31/21]seed@VM:~/.../files$ diff test3.txt test1.txt
[03/31/21]seed@VM:~/.../files$
```
