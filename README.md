# HTTPFuzzer (beta version)



### Simple python HTTP fuzzer

HTTPFuzzer is a simple python script to perform multiple fuzzing techniques for HTTP protocol.

The script can fuzz the following :

1. HTTP Methods.
	* GET method.
	* HEAD method.
	* POST method.
	* PUT method.

2. User Agent Header.
3. HOST header.

and much more soon !

### Requirements
you just need to install termcolor to use the script , and you can install it by the following command :

``` root@kali: pip install termcolor```

After installing all the dependencies , you can run this command to start HTTPFuzzer :

```
root@kali:/opt/HTTPFuzzer# python HTTPFuzzer.py
Usage : # ./fuzzer.py ip port option length

    options :
        all : perform all http fuzzing tests
        methods : perform fuzzing on http methods [GET, POST, PUT, HEAD]
        host : perform fuzzing on HOST header
        ua : perform fuzzing on user agent header

```

##### HTTP methods fuzz

using this option you can fuzz all http methods with a pre-defined length entered by the user which is 3000 bytes , and you can use the command as the following :

    root@kali:/opt/HTTPFuzzer# python HTTPFuzzer.py 16.173.240.71 8080 methods 3000

  ##### HOST header fuzz

using this option you can fuzz host header with a pre-defined length entered by the user which is 3000 bytes , and you can use the command as the following :

    root@kali:/opt/HTTPFuzzer# python HTTPFuzzer.py 16.173.240.71 8080 host 3000

  ##### User-Agent header fuzz

using this option you can fuzz User-Agent header with a pre-defined length entered by the user which is 3000 bytes , and you can use the command as the following :

    root@kali:/opt/HTTPFuzzer# python HTTPFuzzer.py 16.173.240.71 8080 ua 3000
