## NOTE - print() commands are left in code as comments in the case that they may be used if the code is altered, is not working properly, etc. or if the user just wants to see them. Enabling them will slow down the program.

from tkinter import *
class Calc:
    def __init__(self, master):
        root.title('Calc')
        root.geometry('185x270')
        frame = Frame(master=root)
        frame.pack_propagate(0)
        frame.grid()
        self.Eq = [0] #Equation
        lbl = ''.join(str(i) for i in self.Eq)
        self.li = Label(frame, text=lbl, anchor=W) #Equation Bar
        self.li.grid(row=1, column=1, ipadx=10, ipady=10, columnspan=4)
        self.de = Button(frame, text="←", command=self.delete)
        self.de.grid(row=2, column=1, ipadx=13, ipady=10) #Delete last character
        
        self.clr = Button(frame, text="CLEAR", command=self.clear)
        self.clr.grid(row=2, column=2, columnspan=2, ipadx=24, ipady=10) #Clear Equation
    ### NUMBERS & OPERATORS ###
        self.b7 = Button(frame, text="7", command=lambda:self.append(7))
        self.b7.grid(row=3, column=1, ipadx=15, ipady=10)
        self.b8 = Button(frame, text="8", command=lambda: self.append(8))
        self.b8.grid(row=3, column=2, ipadx=15, ipady=10)
        self.b9 = Button(frame, text="9", command=lambda:self.append(9))
        self.b9.grid(row=3, column=3, ipadx=15, ipady=10)
        self.b4 = Button(frame, text="4", command=lambda:self.append(4))
        self.b4.grid(row=4, column=1, ipadx=15, ipady=10)
        self.b5 = Button(frame, text="5", command=lambda:self.append(5))
        self.b5.grid(row=4, column=2, ipadx=15, ipady=10)
        self.b6 = Button(frame, text="6", command=lambda:self.append(6))
        self.b6.grid(row=4, column=3, ipadx=15, ipady=10)
        self.b1 = Button(frame, text="1", command=lambda:self.append(1))
        self.b1.grid(row=5, column=1, ipadx=15, ipady=10)
        self.b2 = Button(frame, text="2", command=lambda:self.append(2))
        self.b2.grid(row=5, column=2, ipadx=15, ipady=10)
        self.b3 = Button(frame, text="3", command=lambda:self.append(3))
        self.b3.grid(row=5, column=3, ipadx=15, ipady=10)
        self.b0 = Button(frame, text="0", command=lambda:self.append(0), width=12)
        self.b0.grid(row=6, column=1, ipady=10, columnspan=2)
        self.pt = Button(frame, text=".", command=lambda:self.append('.'), width=3)
        self.pt.grid(row=6, column=3, ipadx=8, ipady=10)
        self.di = Button(frame, text="÷", command=lambda:self.append('÷'), width=5)
        self.di.grid(row=2, column=4, ipady=10)
        self.cr = Button(frame, text="×", command=lambda:self.append('×'), width=5)
        self.cr.grid(row=3, column=4, ipady=10)
        self.mn = Button(frame, text="-", command=lambda:self.append('-'), width=5)
        self.mn.grid(row=4, column=4, ipady=10)
        self.pl = Button(frame, text="+", command=lambda:self.append('+'), width=5)
        self.pl.grid(row=5, column=4, ipady=10)
        self.en = Button(frame, text="=", command=self.enter, width=5)
        self.en.grid(row=6, column=4, ipady=10)
        
    ### PARSE EQUATION (WIP) ###
    def solve(self,eqn): #parse equation
        try:
            eqn.pop(0)
            #print(eqn)
            parts = []
            Len = len(eqn)
            for i in range(Len):
                parts.append([]) #adds as many parts as characters
            while eqn:
                for i in range(Len):
                    while not self.SpecKey(eqn,0):
                        parts[i].append(eqn[0])
                        del eqn[0]
                    if eqn:
                        if not parts[i]:
                            parts[i].append(eqn[0])
                            del eqn[0]
            while parts.count([]) > 0:
                parts.remove([])
            #print(parts) 

            while len(parts) > 1:
                for m in range(parts.count(['.'])): #DECIMAL
                    pt = parts.index(['.'])
                    while parts[pt+1][-1] == 0:
                        del parts[pt+1][-1]
                    mantissa = float(''.join(str(n) for n in parts[pt+1])) / 10 ** len(parts[pt+1])
                    parts[pt-1] = float(''.join(str(n) for n in parts[pt-1])) + mantissa
                    parts.remove(['.'])
                    parts.remove(parts[pt])
                    # print(parts[pt-1])
                    # print(eqn)

                k = 1
                while k in range(len(parts)): #MULTIPLICATION
                    # print(k)
                    n1, n2 = '',''
                    if parts[k] == ['×'] or parts[k] == ['÷']:
                        # print('len:',len(parts))
                        # print('ind:',parts[k])
                        # print('p1:',parts[k-1])
                        if type(parts[k-1]) != float:
                            n1 = float(''.join(str(i) for i in parts[k-1]))
                        elif type(parts[k-1]) != n1:
                            n1 = parts[k-1]
                        # print('n1:',n1)
                        # print('p2:',parts[k+1])
                        if type(parts[k+1]) != float:
                            n2 = float(''.join(str(i) for i in parts[k+1]))
                        elif type(parts[k+1]) != n2:
                            n2 = parts[k+1]
                        # print('n2',n2)
                        op = parts[k]
                        ix = parts[k]
                        del parts[k+1]
                        if op == ['×']:
                            parts[k-1] = float(n1*n2)
                            # print(n1,'x',n2)
                        else:
                            try:
                                parts[k-1] = float(n1/n2)
                            except:
                                parts = ['Error: cannot divide by zero']
                        try:
                            del parts[k]
                        except:
                            pass
    
                    else:
                        k += 1
                    # print('p:',parts)

                k = 1
                while k in range(len(parts)): #ADDITION
                    # print(k)
                    n1, n2 = '',''
                    if parts[k] == ['+'] or parts[k] == ['-']:
                        # print('len:',len(parts))
                        # print('ind:',parts[k])
                        # print('p1:',parts[k-1])
                        if type(parts[k-1]) != float:
                            n1 = float(''.join(str(i) for i in parts[k-1]))
                        elif type(parts[k-1]) != n1:
                            n1 = parts[k-1]
                        # print('n1:',n1)
                        # print('p2:',parts[k+1])
                        if type(parts[k+1]) != float:
                            n2 = float(''.join(str(i) for i in parts[k+1]))
                        elif type(parts[k+1]) != n2:
                            n2 = parts[k+1]
                        # print('n2',n2)
                        op = parts[k]
                        ix = parts[k]
                        del parts[k+1]
                        if op == ['+']:
                            parts[k-1] = float(n1+n2)
                            # print(n1,'+',n2)
                        else:
                            parts[k-1] = float(n1-n2)
                        del parts[k]

                    else:
                        k += 1
                    # print('p:',parts)
                print(parts)
                return(str(parts[0]))
        except:
            return(['Error: Syntax'])

    
    ### SPECIAL FUNCTIONS ###
    def SpecKey(self,eqn,n): #determine if item at index n is "special" (not numerical)
        try:
            char = int(eqn[n])
            return(False)
        except:
            return(True)

    def append(self,n):
        if len(self.Eq) == 1 and type(n) != int:
            self.Eq.append(0)
        if len(self.Eq) < 25:
            self.Eq.append(n)
        lbl = ''.join(str(i) for i in self.Eq)
        self.li.configure(text=lbl[1:])

        
    ### BUTTON COMMANDS ###
    def delete(self):
        if self.Eq != [0]:
            del self.Eq[-1]
        if self.Eq != [0]:
            lbl = ''.join(str(i) for i in self.Eq)
            self.li.configure(text=lbl[1:])
        else:
            lbl = '0'
            self.li.configure(text=lbl)
    def clear(self):
        self.Eq = [0]
        self.li.configure(text='0')

    ## SYMBOLS ##
            
    def enter(self): #WIP
        if self.Eq != [0] and self.Eq:
            try:
                lbl = str(self.solve(self.Eq))
                if float(lbl) == int(float(lbl)):
                    lbl = int(float(lbl))
                lbl = list(str(lbl))
            except:
                lbl = str(lbl)
            if lbl == "['Error: Syntax']":
                lbl = 'Error: Syntax'
            self.Eq = [0]
            for i in lbl:
                self.Eq.append(i)
            lbl = ''.join(str(i) for i in lbl)
            self.li.configure(text=str(lbl))
        #Display Ans
        
root = Tk()
calculator = Calc(root)
root.mainloop()
