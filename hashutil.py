import hashlib
import sys
from optparse import OptionParser


#############################################################
# File Hasher
def fileHasher(fileToHash):
    """Return a string of Hash
    Takes file object as input. 
    Make sure to open the file in read-binary mode. for ex. open('abc.txt','rb')"""
    sha = hashlib.sha256()
    try:
        with open(file=fileToHash, mode="rb") as fileObject:
            sha.update(fileObject.read())
            return sha.hexdigest()
    except FileNotFoundError:
        print("INPUT ERROR :  File Does Not Exist")


##############################################################
# Option Parser
def decorator(arg1):
    """Decorator to warp Hashing module
    Return Hashed string
    """
    def choice(func):
        print("Argument for Hashing {}".format(arg1))
        x = func()
        if type(arg1) is str:
            x.update(arg1.encode('ascii'))
        else:
            try:
                x.update(arg1.read())
            except AttributeError:
                print("INVALID INPUT")
                sys.exit(0)
        spam = x.hexdigest()
        assert isinstance(spam, str)
        return spam

    return choice


###########################
def hashMD5():
    """Returns and MD5 Hashlib Object"""
    hashObject = hashlib.md5()
    return hashObject

def hashSHA1():
    """Returns and SHA1 Hashlib Object"""
    hashObject = hashlib.sha1()
    return hashObject

def hashSHA224():
    """Returns and SHA224 Hashlib Object"""
    hashObject = hashlib.sha224()
    return hashObject

def hashSHA256():
    """Returns and SHA256 Hashlib Object"""
    hashObject = hashlib.sha256()
    return hashObject

def hashSHA384():
    """Returns and 384 Hashlib Object"""
    hashObject = hashlib.sha384()
    return hashObject

def hashSHA512():
    """Returns and SHA512 Hashlib Object"""
    hashObject = hashlib.sha512()
    return hashObject

# decorator(stringHash)(hashMD5) #solution
#################################################################
if __name__ == '__main__':
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

    if options.filename is not None:
        print("Hash for the file '{0}' is {1}".format(options.filename, fileHasher(options.filename)))
        # print("Hash for the file '{0}' is {1}".format(options.filename, decorator(options.filename)(hashSHA256)))

        if options.inputHash is not None:
            print('Compare string MATCHED') if (options.inputHash == fileHasher(options.filename)) else print(
                "Compare string does NOT MATCH")
        ##################################################################################################
    if options.filename is None:
        if options.hashAlgo is not None and options.hashAlgo.lower() in supportedHash:
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
        # COMPARE
        ###################################################################################################
    if options.inputHash is not None and options.filename is None:
        print('Compare string MATCHED') if (options.inputHash == stringHashOutput) else print(
            'Compare string does NOT MATCH')
