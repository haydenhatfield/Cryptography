"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"




i = input("Enter e to encrypt, d to decrypt, or q to quit: ")
if(i != e or i != d or i != q):
    print("Did not understand command, try again.")
if(i = e):
    me = input("Message: ")
    ke = input("Key: ")
if(i = d):
    me = input("Message: ")
    ke = input("Key: ")
if(i = q):
    print("Goodbye")