import os
import re
import shutil
import sys
file_extension_functions_c = os.path.abspath(sys.argv[1])
os.chdir(os.path.abspath(sys.argv[2]))
shutil.copyfile(file_extension_functions_c, 'extension-functions.c')
#!! with open('extension-functions.c', 'r+') as f:
    #!! text = f.read()
    #!! text = re.sub(
with open('sqlite3.c', 'r+') as f:
    text = f.read()
    text = text.replace(
        'sqlite3_ieee_init(p->db, 0, 0);',
        'sqlite3_ieee_init(p->db, 0, 0);\nsqlite3_extension_init(p->db, 0, 0);'
    )
    text = text.replace(
        '/',
        '#include "extension_functions.c\n/'
    )
    f.seek(0)
    f.write(text)
    f.truncate()
