import threading
import re


class calculator(threading.Thread):
    def __init__(self, eq: str):
        super().__init__()
        self.eq = eq

    def add(self, *args):
        arg1 = 0
        for arg in args:
            arg1 += arg
        return arg1

    def multi(self, *args):
        args1 = 1
        for arg in args:
            args1 *= arg
        return args1

    def devide(self, a, b):
        return a/b

    def rec(self, eq: str):
        # print(eq)
        try:
            brac = eq.index('(')
            try:
                bracend = eq.rindex(')')
            except:
                print("Syntax Error")
            if eq[:brac] != "":
                if eq[brac-1].isnumeric():
                    return self.rec(eq[:brac]+"*"+self.rec(eq[brac+1:bracend])+eq[bracend+1:])
                else:
                    if eq[brac-1] == '-':
                        return self.rec(eq[:brac-1]+"+(-1*"+self.rec(eq[brac+1:bracend])+")"+eq[bracend+1:])
                    else:
                        return self.rec(eq[:brac]+self.rec(eq[brac+1:bracend])+eq[bracend+1:])
            else:
                return self.rec(self.rec(eq[brac+1:bracend])+eq[bracend+1:])
        except:
            pass
        try:
            divindex = eq.index('/')
            i = divindex-1
            _1stno = ""
            _2ndno = ""
            while i < divindex:
                try:
                    if i >= 0:
                        if eq[i].isnumeric():
                            _1stno = eq[i]+_1stno
                        else:
                            if eq[i] == '.':
                                _1stno = "."+_1stno
                            else:
                                break
                        if eq[i-1] == '-':
                            _1stno = "-"+_1stno
                            break
                    else:
                        break
                except:
                    break
                i -= 1
            i = divindex+1
            while i > divindex:
                try:
                    if eq[i].isnumeric():
                        _2ndno = _2ndno+eq[i]
                    else:
                        if eq[i] == '.':
                            _2ndno = _2ndno+"."
                        elif eq[i] == '-':
                            _2ndno = "-"+_2ndno
                        else:
                            break
                except:
                    break
                i += 1
            tempstr = _1stno+"/"+_2ndno
            eq = self.rec(
                str(eq.replace(tempstr, str(self.devide(float(_1stno), float(_2ndno))))))
        except:
            pass
        try:
            divindex = eq.index('*')
            i = divindex-1
            _1stno = ""
            _2ndno = ""
            while i < divindex:
                try:
                    if i >= 0:
                        if eq[i].isnumeric():
                            _1stno = eq[i]+_1stno
                        else:
                            if eq[i] == '.':
                                _1stno = "."+_1stno
                            else:
                                break
                        if eq[i-1] == '-':
                            _1stno = "-"+_1stno
                            break
                    else:
                        break
                except:
                    break
                i -= 1
            i = divindex+1
            while i > divindex:
                try:
                    if eq[i].isnumeric():
                        _2ndno = _2ndno+eq[i]
                    else:
                        if eq[i] == '.':
                            _2ndno = _2ndno+"."
                        elif eq[i] == '-':
                            _2ndno = "-"+_2ndno
                        else:
                            break
                except:
                    break
                i += 1
            tempstr = _1stno+"*"+_2ndno
            # print(tempstr)
            eq = self.rec(
                str(eq.replace(tempstr, str(self.multi(float(_1stno), float(_2ndno))))))
        except:
            pass
        s = [float(s) for s in re.findall(r'-?\d+\.?\d*', eq)]
        eq = str(self.add(*s))
        return eq

    def run(self):
        return self.rec(self.eq)


if __name__ == '__main__':
    while True:
        eq = input()
        try:
            if int(eq) == 0:
                break
        except:
            pass
        mycalculator = calculator(eq)
        print(mycalculator.run())
