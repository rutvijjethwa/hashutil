import hashlib
##############################################################
# Option Hasher
def decorator(arg1):
    def choice(func):
        #print(arg1)
        x = func()
        x.update(arg1.encode('ascii'))
        spam = x.hexdigest()
        assert isinstance(spam, str)
        return spam
    return choice

@decorator(decInput)
def hashMD5():
    hashObject = hashlib.md5()
    return hashObject

@decorator(decInput)
def hashSHA1():
    hashObject = hashlib.sha1()
    return hashObject


@decorator(decInput)
def hashSHA224():
    hashObject = hashlib.sha224()
    return hashObject


@decorator(decInput)
def hashSHA256():
    hashObject = hashlib.sha256()
    return hashObject


@decorator(decInput)
def hashSHA384():
    hashObject = hashlib.sha384()
    return hashObject


@decorator(decInput)
def hashSHA512():
    hashObject = hashlib.sha512()
    return hashObject