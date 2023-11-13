import shutil
import sys

shutil.copy(sys.argv[1],f"copy{str(sys.argv[1])}")