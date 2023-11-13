from urllib import request
import sys

print(request.urlopen(sys.argv[1]).getcode()==200)