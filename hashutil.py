import hashlib
from optparse import OptionParser

#file Hasher
def fileHasher(fileToHash):
    sha =  hashlib.sha256()
    with open(file=fileToHash, mode="rb") as fileObject:
        sha.update(fileObject.read())
        return sha.hexdigest()

#List of Supported Hash
supportedHash = ['md5','sha1','sha224','sha256','sha384','sha512']

#Input Processing
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",action="store",
                  help="File input for hashing", metavar="FILE")
parser.add_option("-s", "--string", dest="stringToHash",action="store",
                  help="String input for hashing", metavar="String")
parser.add_option("-c","--compare",dest="inputHash",action="store",metavar="Hash_String",
                  help="Input the string to match with the file. Use along with -f option.")
parser.add_option("-a","--hash",dest="hashAlgo",action="store",metavar="Hashing_Algorithm",
                  help="Hashing algorithm to use. Default is sha256"
                       "\nAvaliable Options :'md5', 'sha1','sha224', 'sha256', 'sha384', 'sha512'")
(options, args) = parser.parse_args()


# con1 = options.filename != None

HashVal = fileHasher(options.filename)
print(HashVal)