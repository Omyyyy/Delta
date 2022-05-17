import pycode

class Compiler:
    def __init__(self, line: str, filename):
        self.line = line
        self.cmd = line.split(" ", 1)[0]
        self.args = [arg.strip() for arg in line.split(" ", 1)[1].split(",")]
        self.arglen = len(self.args)
        self.filename = filename

    def basm2py(self):
        if self.cmd == "print":
            toprint = self.args[0]
            pycode.pycode += f"print('{toprint}')\n"
        
        elif self.cmd == "printf":
            toprint = self.args[0]
            pycode.pycode += f"print({toprint})\n"

        elif self.cmd == "input":
            prompt = self.args[0]
            varname = self.args[1]
            pycode.pycode += f"{varname} = input({prompt})\n"

        elif self.cmd == "var":
            varthing = self.args[0]
            pycode.pycode += f"{varthing}\n"
