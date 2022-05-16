import compiler
import sys
import os
import pycode
import time

INFO = False

filename = sys.argv[-1]
argv = sys.argv[1:-1]

if argv != []:
    if "-i" in argv:
        INFO = True

filenamewithoutext = os.path.splitext(filename)[0]
compstart = time.process_time()

with open(filename) as f:
    for i in f:
        if i[0] == '#':
            continue
        else:
            code = i

        code = code.strip()

        compiler.Compiler(code, filename).basm2py()

compend = time.process_time()

print(f"\n[INFO]: Compiled {filename} in {round((compend - compstart)*1000, 2)}ms\n") if INFO else None

runstart = time.process_time()

try:
    exec(pycode.pycode)
    runend = time.process_time()
    print(f"\n[INFO]: Run {filename} in {round((runend - runstart)*1000, 2)}ms") if INFO else None

except Exception as e:
    print(f"\n[ERROR]: {e}")
    print(pycode.pycode)
    sys.exit(1)