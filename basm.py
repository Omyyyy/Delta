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
compstart = time.perf_counter()

with open(filename) as f:
    for code in f:
        if code[0] == '#' or code.isspace():
            continue

        code = code.strip()

        compiler.Compiler(code, filename).basm2py() if not code.isspace() and code != "\n" else None

compend = time.perf_counter()

print(f"\n[INFO]: Compiled {filename} in {round((compend - compstart)*1000, 2)}ms\n") if INFO else None

runstart = time.perf_counter()

try:
    exec(pycode.pycode)
    runend = time.perf_counter()
    print(f"\n[INFO]: Run {filename} in {round((runend - runstart)*1000, 2)}ms") if INFO else None

except Exception as e:
    print(f"\n[ERROR]: {e}")
    print(pycode.pycode)
    sys.exit(1)