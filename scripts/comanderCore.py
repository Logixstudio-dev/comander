import re

tokens  = {
    "in": "zero",
    "out": "uno",
    "get": "uno",
    "set": "uno",
    "if": "duo",
    "jump": "uno",
    "true": "data",
    "false": "data",
    "null": "data",
    "add": "uno",
    "sub": "uno",
    "mul": "uno",
    "div": "uno",
    "delete": "uno",
    "import": "duo",
    "convert": "duo",
    "<int>": "type",
    "<str>": "type",
    "<log>": "type"
}

class Core:

    def __init__(self):
        self.stesh = []
        self.x = 0

    def lexer(self, code):

        res = []

        p = re.findall(r'[-+]?\d+[.]\d+|<int>|<log>|<str>|\w+|"[^"]*"|#[^#]*#|/[^/]*/', code)

        for i in p:
            if i in tokens:
                res.append([i, tokens[i]])
            elif i.startswith('"') and i.endswith('"'):
                res.append([i, "data"])
            elif i.startswith('/') and i.endswith('/'):
                res.append([i, "loop"])
            elif re.fullmatch(r'[-+]?\d+[.]\d+', i):
                res.append([i, "data"])

        return res

    def parseCMD(self, token):

        res = []

        val = token[self.x][0]
        typ = token[self.x][1]

        self.x += 1

        if typ in ("zero", "data", "type", "loop"):
            return [val]
        elif typ == "uno":
            arg = self.parseCMD(token[self.x])
            return [val, arg]
        elif typ == "duo":
            arg = self.parseCMD(token[self.x])
            arg2 = self.parseCMD(token[self.x])
            return [val, arg, arg2]


    def parser(self, tokenize_arr):
        self.x = 0
        res = []
        while self.x < len(tokenize_arr):
            res.append(self.parseCMD(tokenize_arr))

        return res
        
            


t = Core()

print(t.parser(t.lexer(input())))