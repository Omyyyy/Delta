import pycode

class Compiler:
    def __init__(self, line: str, filename):
        self.line = line
        self.cmd = line.split()[0]
        self.args = [arg.strip() for arg in line.split(" ")[1:]]
        self.arglen = len(self.args)
        self.filename = filename

    def basm2py(self):
        if self.cmd == "print":
            toprint = " ".join(self.args).removeprefix('"').removesuffix('"')
            pycode.pycode += f"print('{toprint}')\n"
        
        elif self.cmd == "printf":
            toprint = eval(" ".join(self.args))
            pycode.pycode += f"print('{toprint}')\n"