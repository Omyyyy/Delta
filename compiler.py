import pycode

class Compiler:
    def __init__(self, line: str, filename):
        self.line = line
        self.cmd = line.strip().split(" ", 1)[0].strip()
        self.args = [arg.strip() for arg in line.strip().split(" ", 1)[1].split(",")]
        self.arglen = len(self.args)
        self.filename = filename

    def basm2py(self):
        ind = " " * (len(self.line) - len(self.line.lstrip()))

        if self.cmd == "print":
            toprint = self.args[0]
            pycode.pycode += ind + f"print('{toprint}')\n"
        
        elif self.cmd == "printf":
            toprint = self.args[0]
            pycode.pycode += ind + f"print({toprint})\n"

        elif self.cmd == "input":
            prompt = self.args[0]
            varname = self.args[1]
            pycode.pycode += ind + f"{varname} = input({prompt})\n"

        elif self.cmd == "var":
            varthing = self.args[0]
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
