import hashlib
from optparse import OptionParser

#############################################################
# File Hasher
def fileHasher(fileToHash):
    sha = hashlib.sha256()
    try:
        with open(file=fileToHash, mode="rb") as fileObject:
            sha.update(fileObject.read())
            return sha.hexdigest()
    except FileNotFoundError:
        print("INPUT ERROR :  File Does Not Exist")
##############################################################
#Option Parser
def decorator(arg1):
    def choice(func):
        print("Argument for Hashing {}".format(arg1))
        x = func()
        x.update(arg1.encode('ascii'))
        spam = x.hexdigest()
        assert isinstance(spam, str)
        return spam
    return choice
###########################
def hashMD5():
    hashObject = hashlib.md5()
    return hashObject

def hashSHA1():
    hashObject = hashlib.sha1()
    return hashObject

def hashSHA224():
    hashObject = hashlib.sha224()
    return hashObject

def hashSHA256():
    hashObject = hashlib.sha256()
    return hashObject

def hashSHA384():
    hashObject = hashlib.sha384()
    return hashObject

def hashSHA512():
    hashObject = hashlib.sha512()
    return hashObject


#decorator(stringHash)(hashMD5) #solution
#################################################################
if __name__=='__main__':
# List of Supported Hash
    supportedHash = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
#############################################################
# Input Processing
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", action="store",
                     help="File input for hashing", metavar="FILE")
    parser.add_option("-s", "--string", dest="stringHash", action="store",
                  help="String input for hashing", metavar="String")
    parser.add_option("-c", "--compare", dest="inputHash", action="store", metavar="Hash_String",
                  help="Input the string to match with the file. Use along with -f option.")
    parser.add_option("-a", "--hash", dest="hashAlgo", action="store", metavar="Hashing_Algorithm",
                  help="Hashing algorithm to use. Default is sha256"
                       "\nAvaliable Options :'md5', 'sha1','sha224', 'sha256', 'sha384', 'sha512'")
    (options, args) = parser.parse_args()
####################################################################################################

    if options.filename != None and options.inputHash != None:
        print("Hash for the file '{0}' is {1}".format(options.filename, fileHasher(options.filename)))
        print('Compare string MATCHED') if (options.inputHash == fileHasher(options.filename)) else print(
            'Compare string does NOT MATCH')
##################################################################################################
    if options.filename==None:
        if options.hashAlgo != None and options.hashAlgo.lower() in supportedHash:
            decInput = options.stringHash
            # decorator(stringHash)(hashMD5) #solution
            if options.hashAlgo.lower() == 'md5':
                stringHashOutput = decorator(options.stringHash)(hashMD5)
                print("Hash Output: " + stringHashOutput)
            elif options.hashAlgo.lower() == 'sha1':
                stringHashOutput = decorator(options.stringHash)(hashSHA1)
                print("Hash Output: " + stringHashOutput)
            elif options.hashAlgo.lower() == 'sha224':
                stringHashOutput = decorator(options.stringHash)(hashSHA224)
                print("Hash Output: " + stringHashOutput)
            elif options.hashAlgo.lower() == 'sha384':
                stringHashOutput = decorator(options.stringHash)(hashSHA384)
                print("Hash Output: " + stringHashOutput)
            elif options.hashAlgo.lower() == 'sha512':
                stringHashOutput = decorator(options.stringHash)(hashSHA512)
                print("Hash Output: " + stringHashOutput)
        else:
            stringHashOutput = decorator(options.stringHash)(hashSHA256)
            print("Hash Output: " + stringHashOutput)

###################################################################################################
#COMPARE
###################################################################################################
    if options.inputHash != None and options.filename==None:
        print('Compare string MATCHED') if (options.inputHash == stringHashOutput) else print('Compare string does NOT MATCH')
