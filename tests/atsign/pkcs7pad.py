import os
import sys
TEST_PATH = os.getcwd()
sys.path.append(TEST_PATH+'/../../src')
sys.path.append(TEST_PATH+'/../../src/lib')
import atclient

print(str.encode(atclient.pkcs7pad("abc")))
print(str.encode(atclient.pkcs7pad("")))
print(str.encode(atclient.pkcs7pad("1")))
print(str.encode(atclient.pkcs7pad("12")))
print(str.encode(atclient.pkcs7pad("123")))
print(str.encode(atclient.pkcs7pad("1234")))
print(str.encode(atclient.pkcs7pad("12345")))
print(str.encode(atclient.pkcs7pad("123456")))
print(str.encode(atclient.pkcs7pad("1234567")))
print(str.encode(atclient.pkcs7pad("12345678")))
print(str.encode(atclient.pkcs7pad("123456789")))
print(str.encode(atclient.pkcs7pad("123456789a")))
print(str.encode(atclient.pkcs7pad("123456789ab")))
print(str.encode(atclient.pkcs7pad("123456789abc")))
print(str.encode(atclient.pkcs7pad("123456789abcd")))
print(str.encode(atclient.pkcs7pad("123456789abcde")))
print(str.encode(atclient.pkcs7pad("123456789abcdef")))
print(str.encode(atclient.pkcs7pad("123456789abcdef1")))
print(str.encode(atclient.pkcs7pad("The quick brown fox jumps over the lazy dog!")))
print(str.encode(atclient.pkcs7pad("These characters are {, }, |, \, ^, ~, [, ], and `.")))
print(str.encode(atclient.pkcs7pad('The characters ";", "/", "?", ":", "@", "=" and "&" are the characters which may be reserved for special meaning within a scheme.')))
