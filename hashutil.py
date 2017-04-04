import hashlib
# import sys
from optparse import OptionParser
#############################################################
#File Hasher
def fileHasher(fileToHash):
    sha =  hashlib.sha256()
    try:
        with open(file=fileToHash, mode="rb") as fileObject:
            sha.update(fileObject.read())
            return sha.hexdigest()
    except FileNotFoundError:
        print("INPUT ERROR :  File Does Not Exist")
##############################################################
#String Hasher
def stringHasher(stringToHash):
    sha = hashlib.sha256()
    try:
        sha.update(stringToHash.encode('ascii'))
        return sha.hexdigest()
    except ValueError:
            print("INPUT ERROR")
#############################################################
#List of Supported Hash
supportedHash = ['md5','sha1','sha224','sha256','sha384','sha512']
#############################################################
#Input Processing
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",action="store",
                  help="File input for hashing", metavar="FILE")
parser.add_option("-s", "--string", dest="stringHash",action="store",
                  help="String input for hashing", metavar="String")
parser.add_option("-c","--compare",dest="inputHash",action="store",metavar="Hash_String",
                  help="Input the string to match with the file. Use along with -f option.")
#TODO: Developing a function for following section
parser.add_option("-a","--hash",dest="hashAlgo",action="store",metavar="Hashing_Algorithm",
                  help="Hashing algorithm to use. Default is sha256"
                       "\nAvaliable Options :'md5', 'sha1','sha224', 'sha256', 'sha384', 'sha512'")
(options, args) = parser.parse_args()
####################################################################################################
if options.filename != None:
    print("Hash for the file '{0}' is {1}".format(options.filename,fileHasher(options.filename)))
    if options.inputHash != None:
        print('Compare string MATCHED') if (options.inputHash==fileHasher(options.filename)) else print('Compare string does NOT MATCH')

if options.stringHash != None:
    print("Hash for '{0}' is {1}".format(options.stringHash,stringHasher(options.stringHash)))
    if options.inputHash != None:
        print('Compare string MATCHED') if (options.inputHash==stringHasher(options.stringHash)) else print('Compare string does NOT MATCH')
