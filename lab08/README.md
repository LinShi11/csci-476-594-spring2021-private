## Lab 08 RSA Public-Key Encryption and Signature Lab
###### Lin Shi (n92s773)
###### linshi1768@gmail.com
###### CSCI 476
###### April 20, 2021
<br>

### Task 1:
In this task, we are trying to derive the private key d that we will be using.
```
#include <stdio.h>
#include <openssl/bn.h>

void print_BN(char* msg, BIGNUM* a) {
    char* number_str = BN_bn2hex(a);
    printf("%s %s\n", msg, number_str);
    OPENSSL_free(number_str);
}

int main() {
    BN_CTX* ctx = BN_CTX_new();
    BIGNUM* p = BN_new();
    BIGNUM* q = BN_new();
    BIGNUM* e = BN_new();
    BIGNUM* n = BN_new();
    BIGNUM* pTwo = BN_new();
    BIGNUM* qTwo = BN_new();
    BIGNUM* d = BN_new();

    BN_hex2bn(&p, "F7E75FDC469067FFDC4E847C51F452DF");
    BN_hex2bn(&q, "E85CED54AF57E53E092113E62F436F4F");
    BN_hex2bn(&e, "0D88C3");

    BN_sub(pTwo, p, BN_value_one());
    BN_sub(qTwo, q, BN_value_one());
    BN_mul(n, pTwo, qTwo, ctx);

    print_BN("p: ", p);
    print_BN("q: ", q);
    print_BN("e: ", e);
    print_BN("n: ", n);

    BN_mod_inverse(d, e, n, ctx);
    print_BN("private key d is ", d);

    return 0;
}
```
Based on the example code given, we are going to modify it slightly. First, we need to initialize the space with all the BN_new(). Therefore, we have the necessary key components p, q, e, n, and d. Within the five, p, q, and e are given, n is just the product of p and q. Then, we plug the necessary information in the appropriate variables. Next, we calculate n by using pTwo times qTwo. Where pTwo is p-1 and qTwo is q-1. For demonstration purposes, we will print the information out. Lastly, we will use the BN_mod_inverse to find d.

```
[04/21/21]seed@VM:~/.../lab08$ nano bigNum.c
[04/21/21]seed@VM:~/.../lab08$ gcc -o task1.out bigNum.c -lcrypto
[04/21/21]seed@VM:~/.../lab08$ ./task1.out
p:  F7E75FDC469067FFDC4E847C51F452DF
q:  E85CED54AF57E53E092113E62F436F4F
e:  0D88C3
n:  E103ABD94892E3E74AFD724BF28E78348D52298BD687C44DEB3A81065A7981A4
private key d is  3587A24598E5F2A21DB007D89D18CC50ABA5075BA19A33890FE7C28A9B496AEB
```
As we can see, I first created the c program with all the code above. Then I complied it with the -lcrypto flag. Then I ran the executable and the information is present. The private key, d, is 3587A24598E5F2A21DB007D89D18CC50ABA5075BA19A33890FE7C28A9B496AEB.

### Task 2:
In this task, we are trying to show the encryption and decryption process using the keys that we have.
```
#include <stdio.h>
#include <openssl/bn.h>

void print_BN(char* msg, BIGNUM* a) {
    char* number_str = BN_bn2hex(a);
    printf("%s %s\n", msg, number_str);
    OPENSSL_free(number_str);
}

int main() {
    BN_CTX* ctx = BN_CTX_new();
    BIGNUM* n = BN_new();
    BIGNUM* e = BN_new();  
    BIGNUM* d = BN_new();
    BIGNUM* m = BN_new();
    BIGNUM* enc = BN_new();
    BIGNUM* dec = BN_new();

    BN_hex2bn(&n, "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
    BN_hex2bn(&e, "010001");
    BN_hex2bn(&d, "74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");
    BN_hex2bn(&m, "4120746f702073656372657421");

    print_BN("m: ", m);
    print_BN("e: ", e);
    print_BN("n: ", n);
    print_BN("d: ", d);

    BN_mod_exp(enc, m, e, n, ctx);
    print_BN("\nThe encryption (m^e mod n): ", enc);

    BN_mod_exp(dec, enc, d, n, ctx);
    print_BN("\nThe decryption (enc^d mod n):", dec);

    return 0;
}
```
Similar to the previous task, we are using the example code before and modifying it. Once again, I initialize the variables necessary. In this task, the n, e, d, and m are known. Additionally, since I am using hex, I will convert my message to hex before using it in the program. Then I print the information to the user. Lastly, I calculate the enc and dec message. I encrypted using m^e mod n and the decryption used enc ^d mod n.

```
[04/21/21]seed@VM:~/.../lab08$ nano bigNumTwo.c
[04/21/21]seed@VM:~/.../lab08$ gcc -o task2.out bigNumTwo.c -lcrypto
[04/21/21]seed@VM:~/.../lab08$ ./task2.out
m:  4120746F702073656372657421
e:  010001
n:  DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5
d:  74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D

The encryption (m^e mod n):  6FB078DA550B2650832661E14F4F8D2CFAEF475A0DF3A75CACDC5DE5CFC5FADC

The decryption (enc^d mod n): 4120746F702073656372657421
[04/21/21]seed@VM:~/.../lab08$ python2 -c 'print("4120746F702073656372657421".decode("hex"))'
A top secret!
```
As we can see, I created the new c program. Then I compiled using the -lcrypto flag again. Next, I will run the executable. Lastly, I will run a python program that convert hex-encoded message to ASCII. As we can see, after the encryption and decryption process, our message is "A top secret!", which is identical to our original message. Thus, we can conclude that the encryption and decryption process is correct.

### Task 3:
In this task, we are using the same keys as task two and we are trying to decrypt some ciphertext.
```
#include <stdio.h>
#include <openssl/bn.h>

void print_BN(char* msg, BIGNUM* a) {
    //char* number_str = BN_bn2dec(a);
    char* number_str = BN_bn2hex(a);
    printf("%s %s\n", msg, number_str);
    OPENSSL_free(number_str);
}

int main() {
    BN_CTX* ctx = BN_CTX_new();
    BIGNUM* n = BN_new();
    BIGNUM* e = BN_new();  
    BIGNUM* d = BN_new();
    BIGNUM* m = BN_new();
    BIGNUM* enc = BN_new();
    BIGNUM* dec = BN_new();

    BN_hex2bn(&n, "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
    BN_hex2bn(&e, "010001");
    BN_hex2bn(&d, "74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");
    BN_hex2bn(&enc, "8C0F971DF2F3672B28811407E2DABBE1DA0FEBBBDFC7DCB67396567EA1E2493F");

    BN_mod_exp(dec, enc, d, n, ctx);
    print_BN("\nThe decryption (enc^d mod n):", dec);

    print_BN("m: ", dec);
    print_BN("e: ", e);
    print_BN("d: ", n);
    print_BN("d: ", d);

    return 0;
}

```
I will start by modifying the task 2 program used since the keys are the same. This time, we do not know the m, original message; however, we do know the ciphertext, enc. Therefore, I will plug the value of enc with the ciphertext and delete the unnecessary code such as finding the encrypted text. Then, I am using the enc ^ d mod n to find our original message, in hex.

```
[04/21/21]seed@VM:~/.../lab08$ nano bigNumTwo.c
[04/21/21]seed@VM:~/.../lab08$ gcc -o task3.out bigNumTwo.c -lcrypto
[04/21/21]seed@VM:~/.../lab08$ ./task3.out

The decryption (enc^d mod n): 50617373776F72642069732064656573
m:  50617373776F72642069732064656573
e:  010001
d:  DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5
d:  74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D
[04/21/21]seed@VM:~/.../lab08$ python2 -c 'print("50617373776F72642069732064656573".decode("hex"))'
Password is dees
```
This time, I will compile the program to another executable name and run that executable. The program will output the decrypted message (in hex), the keys. Then, to find the ASCII string, I will run the python program that does the conversion. Thus, the decrypted message says "Password is dees".
