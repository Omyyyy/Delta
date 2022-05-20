import pycode
from colorama import Fore, init

init(autoreset=True)

def red(string):
    return Fore.RED + string + Fore.RESET

funcnames = []

class Compiler:
    def __init__(self, line: str, filename):
        self.line = line
        self.cmd = line.strip().split(" ", 1)[0].strip()
        try:
            self.args = [arg.strip() for arg in line.strip().split(" ", 1)[1].split(",")]

        except IndexError:
            self.args = []

        self.arglen = len(self.args)
        self.filename = filename

    def bpl2py(self):
        ind = " " * (len(self.line) - len(self.line.lstrip()))

        if self.cmd == "print":
            toprint = self.args[0]
            pycode.pycode += ind + f"print('{toprint}')\n"
        
        elif self.cmd == "printf":
            toprint = self.args[0]
            if "." in toprint:
                if self.args[0].split(" ")[0].split(".")[1] in funcnames:
                    pycode.pycode += ind + f"print({self.bplcalltopy(self.args[0])})\n"

                else:
                    pycode.pycode += ind + f"print({toprint})\n"

            elif self.args[0].split(" ")[0] in funcnames:
                pycode.pycode += ind + f"print({self.bplcalltopy(self.args[0])})\n"

            else:
                pycode.pycode += ind + f"print({toprint})\n"

        elif self.cmd == "input":
            prompt = self.args[0]
            varname = self.args[1]
            pycode.pycode += ind + f"{varname} = input({prompt})\n"

        elif self.cmd == "var":
            varthing = self.args[0].strip()
            varname = self.args[0].split("=", 1)[0].strip()
            vardefin = self.args[0].split("=", 1)[1].strip()
            if "." in vardefin:
                if vardefin.split(" ")[0].split(".")[1] in funcnames:
                    pycode.pycode += ind + f"{varname} = {self.bplcalltopy(vardefin)}\n"

                else:
                    pycode.pycode += ind + f"{varname} = {vardefin}\n"

            elif vardefin.split(" ")[0] in funcnames:
                pycode.pycode += ind + f"{varname} = {self.bplcalltopy(vardefin)}\n"

            else:
                pycode.pycode += ind + f"{varthing}\n"

        elif self.cmd == "cond":
            keyword = self.args[0]

            if keyword == "else":
                pycode.pycode += ind + f"else:\n"
                return

            cond = self.args[1]

            if keyword == "elseif":
                keyword = "elif"

            elif keyword == "unless":
                keyword = "if not"

            pycode.pycode += ind + f"{keyword} {cond}:\n"

        elif self.cmd == "loop":
            keyword = self.args[0]
            cond = self.args[1]

            if keyword == "until":
                keyword = "while not"
                pycode.pycode += ind + f"{keyword} {cond}:\n"

            elif keyword == "while":
                pycode.pycode += ind + f"{keyword} {cond}:\n"

            elif keyword == "for":
                varname = self.args[1]
                start = self.args[2].split("to")[0].strip()
                end = self.args[2].split("to")[1].strip()
                pycode.pycode += ind + f"for {varname} in range({start}, {end}):\n"

            elif keyword == "foreach":
                varname = self.args[1]
                iterablename = self.args[2]
                pycode.pycode += ind + f"for {varname} in {iterablename}:\n"

        elif self.cmd == "func":
            funcname = self.args[0]
            if self.arglen == 1:
                pycode.pycode += ind + f"def {funcname}():\n"
                funcnames.append(funcname)

            else:
                arglist = self.args[1].removeprefix("[").removesuffix("]").split(" ")
                arglist = [arg.strip() for arg in arglist]
                pyarglist = ", ".join(arglist)
                pycode.pycode += ind + f"def {funcname}({pyarglist}):\n"
                funcnames.append(funcname)

        elif self.cmd == "fastfunc":
            funcname = self.args[0]
            if self.arglen == 1:
                pycode.pycode += ind + f"@jit()\n"
                pycode.pycode += ind + f"def {funcname}():\n"
                funcnames.append(funcname)

            else:
                arglist = self.args[1].removeprefix("[").removesuffix("]").split(" ")
                arglist = [arg.strip() for arg in arglist]
                pyarglist = ", ".join(arglist)
                pycode.pycode += ind + f"@jit()\n"
                pycode.pycode += ind + f"def {funcname}({pyarglist}):\n"
                funcnames.append(funcname)

        elif self.cmd == "class":
            classname = self.args[0]
            if self.arglen == 1:
                pycode.pycode += ind + f"class {classname}:\n"

            else:
                superclass = self.args[1]
                pycode.pycode += ind + f"class {classname}({superclass}):\n"

        elif self.cmd == "import":
            importname = self.args[0]

            try:
                with open("builtins/" + importname, "r") as f:
                    for line in f.readlines():
                        if line[0] == '#' or line.isspace():
                            continue

                        line = line.rstrip()
                        Compiler(line, self.filename).bpl2py() if not line.isspace() and line != "\n" else None

            except FileNotFoundError:
                try:
                    with open(importname, "r") as f:
                        for line in f.readlines():
                            if line[0] == '#' or line.isspace():
                                continue

                            line = line.rstrip()
                            Compiler(line, self.filename).bpl2py() if not line.isspace() and line != "\n" else None

                except FileNotFoundError:
                    print(red(f"bpl: ImportError: Could not find module '{importname}'; not a builtin or a file"))


        elif self.cmd == "return":
            if self.arglen == 0:
                pycode.pycode += ind + f"return\n"
            if self.arglen == 1:
                pycode.pycode += ind + f"return {self.args[0]}\n"
            else:
                toreturn = ",".join(self.args)
                pycode.pycode += ind + f"return {toreturn}\n"

        else:
            funcname = self.cmd
            if self.arglen == 0:
                pycode.pycode += ind + f"{funcname}()\n"

            else:
                arglist = self.args[0].removeprefix("[").removesuffix("]").split(" ")
                arglist = [arg.strip() for arg in arglist]
                pyarglist = ", ".join(arglist)
                pycode.pycode += ind + f"{funcname}({pyarglist})\n"

    def bplcalltopy(self, call: str):
        funcname = call.split(" ", 1)[0].strip()
        try:
            arglist = call.split(" ", 1)[1].strip().removeprefix("[").removesuffix("]").split(" ")
        except IndexError:
            arglist = []

        arglist = [arg.strip() for arg in arglist]
        arglen = len(arglist)

        if arglen == 0:
            return f"{funcname}()"

        else:
            pyarglist = ", ".join(arglist)
            return f"{funcname}({pyarglist})"
