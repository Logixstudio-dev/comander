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
                res.append([i, "loopToken"])
            elif re.fullmatch(r'[-+]?\d+[.]\d+', i):
                res.append([i, "data"])

        return res

    def parseCMD(self, tokenize_array):

        val = tokenize_array[self.x][0]
        val = tokenize_array[self.x][1]

        pass


t = Core()

print(t.lexer(input()))
