## lab01
###### Lin Shi (n92s773)
###### linshi1768@gmail.com
###### CSCI 476
###### February 9, 2021
<br>

### Task 1:

#### Task 1.1:
I ran the printenv command to print out all the environment variables. Additionally, I used the printenc USER to show the information stored in the environment variable USER. The following are part of the environment variables:
```
[02/10/21]seed@VM:~/.../task1$ printenv > printenv_before.txt
[02/10/21]seed@VM:~/.../task1$ cat printenv_before.txt
SHELL=/bin/bash
SESSION_MANAGER=local/VM:@/tmp/.ICE-unix/1906,unix/VM:/tmp/.ICE-unix/1906
SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
DESKTOP_SESSION=ubuntu
SSH_AGENT_PID=1870
PWD=/home/seed/Desktop/lab01/task1
LOGNAME=seed
HOME=/home/seed
USERNAME=seed
MANAGERPID=1664
USER=seed
XDG_DATA_DIRS=/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:.
GDMSESSION=ubuntu
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
_=/usr/bin/printenv
OLDPWD=/home/seed/Desktop/lab01
[02/10/21]seed@VM:~/.../task1$ printenv USER
seed
```
When running the printenv command, it displays all the environment variables saved. For example, the USER is seed, the HOME is home/seed, PWD will show me a path to my current location, SESSION_MANAGER will display a list of network IDs. Additionally, even a environment variable I included in later task LD_PRELOAD will appear here (I deleted it to display the corresponding variables if I ran printenv for the first time). I have only shown part of the list. For all the printed details, please look at [printenv_before.txt](task1/printenv_before.txt).

#### Task 1.2:
In this task I have included export and unset. I understand how export and the action of set could be combine into: export NAME='Lin'; however, I decided to split them so it is easier for me to understand later.
```
[02/10/21]seed@VM:~/.../task1$ printenv NAME
[02/10/21]seed@VM:~/.../task1$ NAME=Lin
[02/10/21]seed@VM:~/.../task1$ printenv NAME
[02/10/21]seed@VM:~/.../task1$ export NAME
[02/10/21]seed@VM:~/.../task1$ printenv NAME
Lin
[02/10/21]seed@VM:~/.../task1$ printenv > printenv_after.txt
[02/10/21]seed@VM:~/.../task1$ cat printenv_after.txt
SHELL=/bin/bash
SESSION_MANAGER=local/VM:@/tmp/.ICE-unix/1906,unix/VM:/tmp/.ICE-unix/1906
SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
DESKTOP_SESSION=ubuntu
SSH_AGENT_PID=1870
NAME=Lin
PWD=/home/seed/Desktop/lab01/task1
LOGNAME=seed
HOME=/home/seed
USERNAME=seed
MANAGERPID=1664
USER=seed
XDG_DATA_DIRS=/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:.
GDMSESSION=ubuntu
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
OLDPWD=/home/seed/Desktop/lab01
_=/usr/bin/printenv
[02/10/21]seed@VM:~/.../task1$ unset NAME
[02/10/21]seed@VM:~/.../task1$ printenv NAME
```
First, I double checked to make sure NAME is not set to anything using printenv NAME. Then I set the NAME using NAME='Lin'. However, if I do not export the variable, it is still not stored as a environment variable; thus, I need to do export NAME. When I do printenv NAME, my name will appear. Additionally, if I do printenv, NAME will appear in the output as well. Furthermore, using the unset NAME will unset the variable, just like deleting the varaible. For all the output, please look at [myprintenv_after.txt](task1/printenv_after.txt)

### Task 2:

#### Task 2.1:
In this task, we are running the program first for the printenv information.
```
[02/11/21]seed@VM:~/.../task2$ gcc myprintenv.c -o myprintenv
[02/11/21]seed@VM:~/.../task2$ ./myprintenv > myenv1.txt
[02/11/21]seed@VM:~/.../task2$ cat myenv1.txt
SHELL=/bin/bash
SESSION_MANAGER=local/VM:@/tmp/.ICE-unix/1906,unix/VM:/tmp/.ICE-unix/1906
DESKTOP_SESSION=ubuntu
SSH_AGENT_PID=1870
PWD=/home/seed/Desktop/lab01/task2
LOGNAME=seed
HOME=/home/seed
USERNAME=seed
LANG=en_US.UTF-8
MANAGERPID=1664
USER=seed
XDG_DATA_DIRS=/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
OLDPWD=/home/seed/Desktop/lab01
_=./myprintenv
```
After running the myprintenv program, I could see that it is almost identical to printenv command. The only differences are in the program we ran and the path since I create a different file (_ and PWD). I have only shown some of the environment variable, for all the information, please look at [myenv1.txt](task2/myenv1.txt)

#### Task 2.2:
In this task, I commented out the printenv() in the child process and uncommented the printenv() in the parent process. Then I recompile and ran the program.
```
[02/11/21]seed@VM:~/.../task2$ gcc myprintenv.c -o myprintenv
[02/11/21]seed@VM:~/.../task2$ ./myprintenv > myenv2.txt
[02/11/21]seed@VM:~/.../task2$ cat myenv2.txt
SHELL=/bin/bash
SESSION_MANAGER=local/VM:@/tmp/.ICE-unix/1906,unix/VM:/tmp/.ICE-unix/1906
SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
DESKTOP_SESSION=ubuntu
SSH_AGENT_PID=1870
PWD=/home/seed/Desktop/lab01/task2
LOGNAME=seed
HOME=/home/seed
USERNAME=seed
LANG=en_US.UTF-8
MANAGERPID=1664
USER=seed
XDG_DATA_DIRS=/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
GDMSESSION=ubuntu
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
OLDPWD=/home/seed/Desktop/lab01
_=./myprintenv
```
After running the program, I think the two program output is identical at first glance. Which makes perfect sense since a child process will inherit all environment variables from its parent. At fork, the child process will create a separate copy of all the data and a separate program counter. However, since child is **copying** the data, its environment variables should be identical. Again, for the full output, [myenv2.txt](task2/myenv2.txt).

#### Task 2.3:
We are running the diff command to ensure that the output of the child and parent process is identical.
```
[02/11/21]seed@VM:~/.../task2$ diff myenv1.txt myenv2.txt
```
After running the diff command, there is not any output, which means that there are no differences between the parent and child process. Since the child is copying (fork) the parent, all of its environment variables should be identical. After some research online, some differences between the child and parent process are different PIDs (proportional integral derivative), separate copy of the data and program counter, and the two processes do not share variable after fork.

### Task 3:

#### Task 3.1:
envp is an array of strings, conventionally of the form key-value, which are passed as environment to the new program
main is defined as int main(int argc, char *argv[], char *envp[]) envp environment pointer
We are running the the command execve with NULL in place of a envp (environment pointer).
```
[02/11/21]seed@VM:~/.../task3$ gcc myenv_execve.c -o myenv_execve
[02/11/21]seed@VM:~/.../task3$ ./myenv_execve
```
Nothing was displayed for the program. Based on man execve, it should be int execve(const char *pathname, char *const argv[], char *const envp[]). envp, the portion we are most interested in is an array of strings, which are passed as environment to the new program. As we look at the program, we have given it the path and array of argument strings (although it is NULL), the environment pointer (envp) is stated to be NULL. Thus, it does not know what environment the program is referring to. Which resulted in a blank output.

#### Task 3.2:
This time, we are running the program with environment pointer as environ, not NULL:
```
[02/11/21]seed@VM:~/.../task3$ gcc myenv_execve.c -o myenv_execve
[02/11/21]seed@VM:~/.../task3$ ./myenv_execve > myenv_execve.txt
[02/11/21]seed@VM:~/.../task3$ cat myenv_execve.txt
SHELL=/bin/bash
SESSION_MANAGER=local/VM:@/tmp/.ICE-unix/1906,unix/VM:/tmp/.ICE-unix/1906
SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
DESKTOP_SESSION=ubuntu
SSH_AGENT_PID=1870
PWD=/home/seed/Desktop/lab01/task3
LOGNAME=seed
HOME=/home/seed
USERNAME=seed
LANG=en_US.UTF-8
MANAGERPID=1664
USER=seed
XDG_DATA_DIRS=/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
OLDPWD=/home/seed/Desktop/lab01
_=./myenv_execve
```
When we ran it with environ, we have all the environment variables when printing printenv. In fact, I ran a diff command to find out the only difference is the program ran, which we discussed is a result of the program or command ran. For complete output, please look at [myenv_execve.txt](task3/myenv_execve.txt).

#### Task 3.3:
While I had a good idea of where the environment varaible came from with the discussion above about envp (environment variable), I cannot be sure until I look at environ, the only modification we did to Task 3.2. Since "environ variable is an array of character strings containing environment variable and their values in the form name=value" [citation](https://www.mkssoftware.com/docs/man5/environ.5.asp#:~:text=The%20environ%20variable%20is%20an,of%20.). We have passed in all the environment varaible as the envp, which is the third argument of execve(). Therefore, the environment is inherited through what has been passed in as the environment variable pointer.

### Task 4:

#### Task 4.1:

```
[02/11/21]seed@VM:~/.../task4$ gcc myenv_system.c -o myenv_system
[02/11/21]seed@VM:~/.../task4$ ./myenv_system > myenv_system.txt
[02/11/21]seed@VM:~/.../task4$ cat myenv_system.txt
SHELL=/bin/bash
SESSION_MANAGER=local/VM:@/tmp/.ICE-unix/1906,unix/VM:/tmp/.ICE-unix/1906
SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
DESKTOP_SESSION=ubuntu
SSH_AGENT_PID=1870
PWD=/home/seed/Desktop/lab01/task4
LOGNAME=seed
HOME=/home/seed
USERNAME=seed
LANG=en_US.UTF-8
MANAGERPID=1664
USER=seed
XDG_DATA_DIRS=/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
OLDPWD=/home/seed/Desktop/lab01/task4
_=/usr/bin/env
```
The output is still displaying the same information as printenv. If we look at the program, it is calling env in /usr/bin, which based on the Task 1 and some test, displays the same information as printenv. Therefore, having the same output is not surprising at all. For the complete output, please look at [myenv_system](task4/myenv_system.txt).

### Task 5:

#### Task 5.1:
```
[02/11/21]seed@VM:~/.../task5$ gcc myenv_environ.c -o myenv_environ
[02/11/21]seed@VM:~/.../task5$ ./myenv_environ > myenv_environ1.txt
[02/11/21]seed@VM:~/.../task5$ cat myenv_environ1.txt
SHELL=/bin/bash
SESSION_MANAGER=local/VM:@/tmp/.ICE-unix/1906,unix/VM:/tmp/.ICE-unix/1906
SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
DESKTOP_SESSION=ubuntu
SSH_AGENT_PID=1870
PWD=/home/seed/Desktop/lab01/task5
LOGNAME=seed
HOME=/home/seed
USERNAME=seed
LANG=en_US.UTF-8
MANAGERPID=1664
USER=seed
XDG_DATA_DIRS=/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
OLDPWD=/home/seed/Desktop/lab01
_=./myenv_environ
```
All the environment variables were inherited in the program when first ran by the user (seed). As we can use the USERNAME=seed. Aside from the program ran, there is no difference when compare to the output of printenv. If we look at the code, we are just iterate through environ, which is a list of environment variables; thus, it should be the same as printenv. For the complete output: [myenv_environ1.txt](task5/myenv_environ1.txt).

#### Task 5.2:

We are changing the ownership to root and make it a Set-UID program
```
[02/11/21]seed@VM:~/.../task5$ ls -l myenv_environ
-rwxrwxr-x 1 seed seed 16776 Feb 11 04:14 myenv_environ
[02/11/21]seed@VM:~/.../task5$ sudo chown root myenv_environ
[02/11/21]seed@VM:~/.../task5$ sudo chmod 4755 myenv_environ
[02/11/21]seed@VM:~/.../task5$ ls -l myenv_environ
-rwsr-xr-x 1 root seed 16776 Feb 11 04:14 myenv_environ
[02/11/21]seed@VM:~/.../task5$ ./myenv_environ > myenv_environ2.txt
[02/11/21]seed@VM:~/.../task5$ cat myenv_environ2.txt
SHELL=/bin/bash
SESSION_MANAGER=local/VM:@/tmp/.ICE-unix/1906,unix/VM:/tmp/.ICE-unix/1906
SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
DESKTOP_SESSION=ubuntu
SSH_AGENT_PID=1870
PWD=/home/seed/Desktop/lab01/task5
LOGNAME=seed
HOME=/home/seed
USERNAME=seed
LANG=en_US.UTF-8
MANAGERPID=1664
USER=seed
XDG_DATA_DIRS=/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
OLDPWD=/home/seed/Desktop/lab01
_=./myenv_environ
[02/11/21]seed@VM:~/.../task5$ sudo su
root@VM:/home/seed/Desktop/lab01/task5# ./myenv_environ > myenv_environ3.txt
root@VM:/home/seed/Desktop/lab01/task5# cat myenv_environ3.txt
SHELL=/bin/bash
COLORTERM=truecolor
SUDO_GID=1000
SUDO_COMMAND=/usr/bin/su
SUDO_USER=seed
PWD=/home/seed/Desktop/lab01/task5
LOGNAME=root
HOME=/root
LANG=en_US.UTF-8
TERM=xterm-256color
LESSOPEN=| /usr/bin/lesspipe %s
USER=root
DISPLAY=:0
SHLVL=1
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
SUDO_UID=1000
MAIL=/var/mail/root
_=./myenv_environ
```
In this task, we made the program to a Set-UID program by running the two sudo commands given to us. Then I decided to run the program, which I could conclude that changing it to Set-UID program does not affect the environment variables. Then, out of curiosity, I decided to run the same program with root. Which is outputting the environment variables associated with root. For example, its HOME=/root. [user seed](task5/myenv_environ2.txt), [root](task5/myenv_environ3.txt).

#### Task 5.3:

In this task, we are modifying the PATH, LD_LIBRARY_PATH, and TASK5 and determine whether that will be inherited in the child process.
```
[02/11/21]seed@VM:~/.../task5$ export PATH=/home/seed/Desktop/lab01/task5:$PATH
[02/11/21]seed@VM:~/.../task5$ export LD_LIBRARY_PATH=/home:$LD_LIBRARY_PATH
[02/11/21]seed@VM:~/.../task5$ export TASK5=LIN
[02/11/21]seed@VM:~/.../task5$ ./myenv_environ > myenv_environ4.txt
[02/11/21]seed@VM:~/.../task5$ cat myenv_environ4.txt
SHELL=/bin/bash
SESSION_MANAGER=local/VM:@/tmp/.ICE-unix/1906,unix/VM:/tmp/.ICE-unix/1906
SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
DESKTOP_SESSION=ubuntu
SSH_AGENT_PID=1870
PWD=/home/seed/Desktop/lab01/task5
LOGNAME=seed
HOME=/home/seed
USERNAME=seed
LANG=en_US.UTF-8
MANAGERPID=1664
USER=seed
TASK5=LIN
XDG_DATA_DIRS=/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
PATH=/home/seed/Desktop/lab01/task5:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:.
OLDPWD=/home/seed/Desktop/lab01
_=./myenv_environ
```
After we have export all the variables and ran the program, we were able to see TASK5=LIN and PATH is modified to /home/seed/Desktop/lab01/task5... instead of PATH=/usr/local/sbin.... However, I was not able to find LD_LIBRARY_PATH. I believe since it was prepend the current directory symbol to itself, it does not print out right away. Therefore, the child process does inherit from the parent process in a Set-UID program. [myenv_environ](task5/myenv_environ4.txt)

### Task 6:
We are trying to trick the program into running our fake ls code instead of the system's ls command.
```
[02/11/21]seed@VM:~/.../task6$ vim ls_fake.c
[02/11/21]seed@VM:~/.../task6$ ls
ls_fake.c  ls_vuln.c
[02/11/21]seed@VM:~/.../task6$ export PATH=/home/seed/Desktop/lab01/task6:$PATH
[02/11/21]seed@VM:~/.../task6$ gcc ls_vuln.c -o ls_vuln
[02/11/21]seed@VM:~/.../task6$ gcc ls_fake.c -o ls
[02/11/21]seed@VM:~/.../task6$ sudo chown root ls_vuln
[02/11/21]seed@VM:~/.../task6$ sudo chmod 4755 ls_vuln
[02/11/21]seed@VM:~/.../task6$ ls -l ls_vuln
-rwsr-xr-x 1 root seed 16704 Feb 11 04:39 ls_vuln
[02/11/21]seed@VM:~/.../task6$ ./ls_vuln
I am the ls this time
[02/11/21]seed@VM:~/.../task6$ getent group sudo
sudo:x:27:seed
```
The program does run my fake ls code instead of the /bin/ls. By compiling the fake program to be ls and setting the PATH to be /home/seed/Desktop/lab01/task6:$PATH. The program will be looking in the PATH first before searching else where. I believe this program is ran with root privilege since it is a Set-UID program.

### Task 7:

#### Task 7.1:
We are just following the steps to execute the program.
```
[02/11/21]seed@VM:~/.../task7$ gcc  -fPIC -g -c mylib.c
[02/11/21]seed@VM:~/.../task7$ gcc -shared -o libmylib.so.1.0.1 mylib.o -lc
[02/11/21]seed@VM:~/.../task7$ export LD_PRELOAD=./libmylib.so.1.0.1
[02/11/21]seed@VM:~/.../task7$ gcc myprog.c -o myprog
[02/11/21]seed@VM:~/.../task7$ ./myprog
I'm not sleeping!
```
We could see how we have dynamically linked the library and it is going to run it first. Additionally, by browsing online, I discovered that LD_PRELOAD is used to exploit functionality by providing the dynamic linker on Unix systems. Therefore, it is important for us to declare LD_PRELOAD.

#### Task 7.2:

1. This is running the regular program with regular user.
```
[02/11/21]seed@VM:~/.../task7$ ./myprog
I'm not sleeping!
```
The regular program with regular user will run the dynamically linked library. Which is going to print out I'm not sleeping.

2. This is running the Set-UID program with regualr user.
```
[02/11/21]seed@VM:~/.../task7$ sudo chown root myprog
[02/11/21]seed@VM:~/.../task7$ sudo chmod 4755 myprog
[02/11/21]seed@VM:~/.../task7$ ./myprog
```
When we make it a Set-UID program, the program does not run the dynamically linked library anymore. Instead, it runs the default sleep program c has. As given in the hint, the child process may not inherit the LD_ environment variables; thus, myprog is going to use the default sleep function.

3. This is running the Set-UID program with root as the user.
```
[02/11/21]seed@VM:~/.../task7$ sudo su
root@VM:/home/seed/Desktop/lab01/task7# ./myprog
root@VM:/home/seed/Desktop/lab01/task7# export LD_PRELOAD=./libmylib.so.1.0.1
root@VM:/home/seed/Desktop/lab01/task7# ./myprog
I'm not sleeping!
```
When running the program first, it runs the default sleep program, which waits for a second. If we decided to reexport LD_PRELOAD, it will run the dynamically linked library we have created. Which matches exactly with the idea that LD_ is not inherited.

4. We create a new user named temp and tested LD_PRELOAD with it.
```
[02/11/21]seed@VM:~/.../task7$ sudo useradd -m temp
[02/11/21]seed@VM:~/.../task7$ sudo passwd temp
New password:
Retype new password:
passwd: password updated successfully
[02/11/21]seed@VM:~/.../task7$ sudo chown temp myprog
[02/11/21]seed@VM:~/.../task7$ su temp
Password:
$ ls
libmylib.so.1.0.1  mylib.c  mylib.o  myprog  myprog.c
$ export LD_PRELOAD=./libmylib.so.1.0.1
$ ./myprog
I'm not sleeping!
[02/11/21]seed@VM:~/.../task7$ sudo chown seed myprog
[02/11/21]seed@VM:~/.../task7$ ls -l myprog
-rwxr-xr-x 1 seed seed 16696 Feb 11 03:17 myprog
[02/11/21]seed@VM:~/.../task7$ su temp
Password:
$ ./myprog
$ export LD_PRELOAD=./libmylib.so.1.0.1
$ ./myprog
I'm not sleeping!
```
I was a little unsure whether the new user temp could be the owner; thus, I tried both. The program will still not inherit LD_PRELOAD while in the new temp user. Once I export LD_PRELOAD, it works just fine. Overall, in this task, we have observe that not all environment variables are inherited. For example, LD_ environment variables are not.

#### Task 7.3
The main cause of the difference when running this program is the LD_PRELOAD environment variable. It is special since it could be used to dynamically link libraries to the program; thus, changing the behavior of our program. Additionally, since LD_ environment variables are not inherited, it must be reexported every time we use a new user or change the regular program to be a Set-UID program. Overall, the main cause of the different result is LD_PRELOAD.

### Task 8:

The two files that I used to test were: [readFile](task8/readFile.txt) and [deleteFile](task8/deleteFile.txt).

#### Task 8.1:
We are trying to delete a file in which Bob should have no access to delete through system call.
```
[02/11/21]seed@VM:~/.../task8$ vim readFile.txt
[02/11/21]seed@VM:~/.../task8$ touch deleteFile.txt
[02/11/21]seed@VM:~/.../task8$ gcc catall.c -o catall
[02/11/21]seed@VM:~/.../task8$ ls
catall  catall.c  deleteFile.txt  readFile.txt
[02/11/21]seed@VM:~/.../task8$ ./catall "readFile.txt; rm deleteFile.txt"
Some important information.......
[02/11/21]seed@VM:~/.../task8$ ls
catall  catall.c  readFile.txt
```
When the system command is call and "readFile.txt; rm deleteFile.txt" is passed in, it will break it up into two different command because of the colon. On the other hand, rm is not one of the privilege; however, since we are in system, once it break the string up, it will call rm to remove the deleteFile.txt. This is gives Bob far more power than Vince expected.

#### Task 8.2:
Try the same attack with execve().
```
[02/11/21]seed@VM:~/.../task8$ touch deleteFile.txt
[02/11/21]seed@VM:~/.../task8$ gcc catall.c -o catall
catall.c: In function ‘main’:
catall.c:23:5: warning: implicit declaration of function ‘execve’ [-Wimplicit-function-declaration]
   23 |     execve(v[0], v, 0);
      |     ^~~~~~
[02/11/21]seed@VM:~/.../task8$ ls
catall  catall.c  deleteFile.txt  readFile.txt
[02/11/21]seed@VM:~/.../task8$ ./catall "readFile.txt; rm deleteFile.txt"
/bin/cat: 'readFile.txt; rm deleteFile.txt': No such file or directory
```
When we try the same attack on execve(). It does not seem to work. execve is not breaking the string up, it is looking for a file or directory named "readFile.txt; rm deleteFile.txt", which simply does not exist. Thus, execve is better in this case to protect against this kind of attack.

### Task 9:
We are follwoing the principle of least privilege and we are discussing the idea of Set-UID program relinquish the root privileges when it is not needed.
```
[02/11/21]seed@VM:~/.../task9$ ls -l /etc/zzz
-rw-r--r-- 1 root root 0 Feb 11 03:33 /etc/zzz
[02/11/21]seed@VM:~/.../task9$ echo "test">/etc/zzz
bash: /etc/zzz: Permission denied
[02/11/21]seed@VM:~/.../task9$ gcc cap_leak.c -o cap_leak
[02/11/21]seed@VM:~/.../task9$ ./cap_leak
Cannot open /etc/zzz
[02/11/21]seed@VM:~/.../task9$ sudo chown root cap_leak
[02/11/21]seed@VM:~/.../task9$ sudo chmod 4755 cap_leak
[02/11/21]seed@VM:~/.../task9$ ls -l cap_leak
-rwsr-xr-x 1 root seed 17040 Feb 11 03:36 cap_leak
[02/11/21]seed@VM:~/.../task9$ ./cap_leak
[02/11/21]seed@VM:~/.../task9$ cat /etc/zzz
Malicious Data
```
The file /etc/zzz could be modified, but with only Set-UID program. when we first try to write to it, it denies the action. Even when we try the cap_leak program, it does not even allow us to open the file. However, once we change the program to be a Set-UID program, we could see the that it could be opened. On the other hand, after we have the access to the file, it will determine that the privileges are no longer needed and relinquish the privileges as we can see that Malicious Data has been printed.
