# Hashutil
Basic hashing utility



```text
Usage: hashutil.py [options]
Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  File input for hashing
  -s String, --string=String
                        String input for hashing
  -c Hash_String, --compare=Hash_String
                        Input the string to match with the file. Use along
                        with -f option.
  -a Hashing_Algorithm, --hash=Hashing_Algorithm
                        Hashing algorithm to use. Default is sha256 Avaliable
                        Options :'md5', 'sha1','sha224', 'sha256', 'sha384',
                        'sha512'
```


### Sample Command
```commandline
python hashutil.py --file=abc.txt 
```
```commandline
python hashutil.py -f abc.txt 
```