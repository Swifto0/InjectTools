# InjectTools

## read_byte.py
usage: python read_byte.py
open demon.bin then convert it to shellcode.

## read_payload.py
usage: python read_payload.py
someone shellcode is too long.So this pyScript help you convert shellcode to comfortable unsigned char array.
like this:
"\xfc\x48...............(too long and single line)
=>         "\xfc\x48\x11\x56",
           "\xa1\x35\x00\x51",
           "\x52\x31\x54\c2";
