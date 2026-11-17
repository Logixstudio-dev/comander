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

    #init parametres
    
    def __init__(self):
        self.stesh = []
        self.x = 0
        self.y = 0
        self.loopTokens = {}

    #lexer for text to tokenize array
    
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
            elif re.fullmatch(r'[-+]?\d+[.]\d+', i) or re.fullmatch(r'[-+]?\d+', i):
                res.append([i, "data"])
            else:
                print("ожидался токен или данные в позиции:" + str(i))
                return 1

        return res

    #recursive parsing of a tokenized list

    def parseCMD(self, token):

        res = []

        val = token[self.x][0]
        typ = token[self.x][1]

        self.x += 1

        if typ in ("zero", "data", "type", "loop"):
            return [val]
        elif typ == "uno":
            arg = self.parseCMD(token)
            return [val, arg]
        elif typ == "duo":
            arg = self.parseCMD(token)
            arg2 = self.parseCMD(token)
            return [val, arg, arg2]


    def parser(self, tokenize_arr):
        self.x = 0
        res = []
        while self.x < len(tokenize_arr):
            res.append(self.parseCMD(tokenize_arr))
            if self.x >= len(tokenize_arr):
                break
        return res

    #running parsed list

    def runCMD(self, CMD):

        name = CMD[0]


        if len(CMD) == 1:

            if name == "in":
                return input()

            if re.fullmatch(r'[-+]?\d+[.]\d+', name):
                return float(name)
            elif re.fullmatch(r'[-+]?\d+', name):
                return int(name)
            elif name == "true":
                return True
            elif name == "false":
                return False
            elif name == "null":
                return None
            elif name in ("<int>", "<str>", "<log>"):
                return name
            elif name.startswith('/') and name.endswith('/'):
                return name
            else:
                return str(name)
        else:
            if name == "out":
                 arg = self.runCMD(CMD[1])
                 print(arg)
            elif name == "set":
                arg = self.runCMD(CMD[1])
                self.stesh.append(arg)
            elif name == "get":
                arg = self.runCMD(CMD[1])
                return self.stesh[arg]
            elif name == "delete":
                arg = self.runCMD(CMD[1])
                self.stesh.pop(arg)
            elif name == "add":
                arg = self.runCMD(CMD[1])
                self.stesh[-1] += arg
            elif name == "sub":
                arg = self.runCMD(CMD[1])
                self.stesh[-1] -= arg
            elif name == "mul":
                arg = self.runCMD(CMD[1])
                self.stesh[-1] *= arg
            elif name == "div":
                arg = self.runCMD(CMD[1])
                self.stesh[-1] /= arg
            elif name == "jump":
                arg = self.runCMD(CMD[1])
                self.y = self.loopTokens.get(arg)
            elif name == "if":
                arg = self.runCMD(CMD[1])
                arg2 = self.runCMD(CMD[2])
                if self.stesh[len(self.stesh) - 1] != arg:
                    self.y = self.loopTokens.get(arg2)
            elif name == "convert":
                arg = self.runCMD(CMD[1])
                arg2 = self.runCMD(CMD[2])
                if arg2 == "<int>":
                    self.stesh[arg] = int(self.stesh[arg])
                elif arg2 == "<str>":
                    self.stesh[arg] = str(self.stesh[arg])
                elif arg2 == "<log>":
                    self.stesh[arg] = bool(self.stesh[arg])

    def run(self, code):
        c = self.parser(self.lexer(code))
        self.y = 0
        self.loopTokens = {}

        for i in range(len(c)):
            if len(c[i]) == 1 and c[i][0].startswith('/') and c[i][0].endswith('/'):
                self.loopTokens[c[i][0]] = i
        
        while self.y < len(c):
            self.runCMD(c[self.y])
            self.y += 1
            if self.y >= len(c):
                break

        return 0

    def startCodefromFile(self, FilePath):
        with open(FilePath, 'r') as file:
            self.run(file.read())


t = Core()

t.startCodefromFile("D:/comander/scripts/testing_programms/adding_two_numbers.cn")