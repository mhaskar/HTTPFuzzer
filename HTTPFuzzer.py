#!/usr/bin/python

'''
Author : Askar (@mohammadaskar2)
Description : HTTPFuzzer is a simple python script to perform multiple fuzzing
              techniques for HTTP protocol

Requirments : termcolor (pip install termcolor)
'''
import socket
import sys
import time
from termcolor import cprint

if len(sys.argv) != 5:
    print '''Usage : # ./fuzzer.py ip port option length
    options :
        all : perform all http fuzzing tests
        methods : perform fuzzing on http methods [GET, POST, PUT, HEAD]
        host : perform fuzzing on HOST header
        ua : perform fuzzing on user agent header
    '''
    sys.exit(0)
host = sys.argv[1]
port = int(sys.argv[2])
ftype = sys.argv[3]
length = int(sys.argv[4])

buff = "A" * length

def method_template(buff, method):
    method_temp = "{0} /{1} HTTP/1.1\r\n".format(method, buff)
    method_temp += "Host: " + host + ":" + str(port) + "\r\n"
    method_temp += "User-Agent: HaHa\r\n"
    method_temp += "Accept-Language: he,en-us;q=0.7,en;q=0.3\r\n"
    method_temp += "Accept-Encoding: gzip,deflate\r\n"
    method_temp += "Accept-Charset: windows-1255,utf-8;q=0.7,*;q=0.7\r\n"
    method_temp += "Keep-Alive: 220\r\n"
    method_temp += "Connection: keep-alive\r\n\r\n"
    return method_temp


def user_agent_template(buff):
    user_agent_temp = "GET / HTTP/1.1\r\n"
    user_agent_temp += "Host: " + host + ":" + str(port) + "\r\n"
    user_agent_temp += "User-Agent: %s\r\n" % buff
    user_agent_temp += "Accept-Language: he,en-us;q=0.7,en;q=0.3\r\n"
    user_agent_temp += "Accept-Encoding: gzip,deflate\r\n"
    user_agent_temp += "Accept-Charset: windows-1255,utf-8;q=0.7,*;q=0.7\r\n"
    user_agent_temp += "Keep-Alive: 220\r\n"
    user_agent_temp += "Connection: keep-alive\r\n\r\n"
    return user_agent_temp


def host_template(buff):
    host_temp = "GET / HTTP/1.1\r\n"
    host_temp += "Host: " + buff + ":" + str(port) + "\r\n"
    host_temp += "User-Agent: HaHa\r\n"
    host_temp += "Accept-Language: he,en-us;q=0.7,en;q=0.3\r\n"
    host_temp += "Accept-Encoding: gzip,deflate\r\n"
    host_temp += "Accept-Charset: windows-1255,utf-8;q=0.7,*;q=0.7\r\n"
    host_temp += "Keep-Alive: 221\r\n"
    host_temp += "Connection: keep-alive\r\n\r\n"
    return host_temp


def buff_create():
    buff = ["A"]
    inc_conuter = 200
    while len(buff) <= (length / 200):
        buff.append("A"*inc_conuter)
        inc_conuter = inc_conuter+200
    return buff


def method_fuzz():
    methods = ["HEAD", "GET", "POST", "PUT"]
    cprint("[+] Fuzzing started for %s"%host, "yellow")
    for method in methods:
        for buff in buff_create():
            try:
                send_socket(method_template(buff, method))
                time.sleep(0.5)
                cprint("[+] {0} bytes Sent using method {1}".format(len(buff), method), "red")

            except:
                cprint("[+]Host down , check your debugger !", "green")
                sys.exit(0)


def send_socket(data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.send(data)


def header_fuzz(header):
    if header == "HOST":
        for buff in buff_create():
            try:
                send_socket(host_template(buff))
                time.sleep(0.5)
                cprint("[+] {0} bytes Sent using HOST header".format(len(buff)), "red")
            except:
                cprint("[+]Host down , check your debugger !", "green")
                sys.exit(0)

    elif header == "UA":
        for buff in buff_create():
            try:
                send_socket(user_agent_template(buff))
                time.sleep(0.5)
                cprint("[+] {0} bytes Sent using user agent".format(len(buff)), "red")
            except:
                cprint("[+]Host down , check your debugger !", "green")
                sys.exit(0)


if ftype == "all":
    header_fuzz("HOST")
    header_fuzz("UA")
    method_fuzz()

elif ftype == "host":
    header_fuzz("HOST")

elif ftype == "ua":
    header_fuzz("UA")

elif ftype == "methods":
    method_fuzz()
else:
    print '''
    options :
        all : perform all http fuzzing tests
        methods : perform fuzzing on http methods [GET, POST, PUT, HEAD]
        host : perform fuzzing on HOST header
        ua : perform fuzzing on user agent header
    '''
