## NOTE - print() commands are left in code as comments in the case that they may be used if the code is altered, is not working properly, etc. or if the user just wants to see them. Enabling them will slow down the program.

from tkinter import *
class Calc:
    def __init__(self, master):
        root.title('')
        root.geometry('185x270')
        frame = Frame(master=root)
        frame.pack_propagate(0)
        frame.grid()
        self.Eq = [0] #Equation
        self.Ans = [0] #Ans key
        self.blank = True #If current display is result or input; True = result
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
        self.b0 = Button(frame, text="0", command=lambda:self.append(0))
        self.b0.grid(row=6, column=1, ipadx=15, ipady=10)
        self.pt = Button(frame, text=".", command=lambda:self.append('.'), width=3)
        self.pt.grid(row=6, column=2, ipadx=8, ipady=10)
        self.ans= Button(frame, text="Ans", command=self.ans, width=3)
        self.ans.grid(row=6,column=3, ipadx=8, ipady=10)
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
        if 1==1:
            eqn.pop(0)
            print('eqn: ',eqn)
            parts = []
            for i in range(len(eqn)):
                parts.append([]) #adds as many parts as characters
            while eqn:
                for i in range(len(eqn)):
                    while not self.SpecKey(eqn,0):
                        parts[i].append(eqn[0])
                        del eqn[0]
                    if eqn:
                        if not parts[i]:
                            parts[i].append(eqn[0])
                            del eqn[0]

            while parts.count([]) > 0:
                parts.remove([])
            print('p: ',parts)
            if len(parts) == 1:
                return(str(parts[0])[1:-1])

            for m in range(parts.count(['.'])): #DECIMAL
                    pt = parts.index(['.'])
                    while parts[pt+1][-1] == 0:
                        del parts[pt+1][-1]
                    mantissa = float(''.join(str(n) for n in parts[pt+1])) / 10 ** len(parts[pt+1])
                    parts[pt-1] = float(''.join(str(n) for n in parts[pt-1])) + mantissa
                    parts.remove(['.'])
                    parts.remove(parts[pt])
                    print('parts[pt-1]: ',parts[pt-1])
                    print('eqn: ',eqn)
                    print('pts: ',parts)

            for m in parts: #COMBINES PIECES INTO FLOATS
                if type(m) != list:
                    n = list(str(m))
                else:
                    n = m
                print('n: ',n)
                try:
                    if not self.SpecKey(list(n),0):
                        n = float(''.join(str(i) for i in n))
                except:
                    pass

            m = 0
            while m < len(parts): #NEGATIVES
                print('M: ',m)
                print(parts[m])
                if parts[m] == ['-']:
                    if self.SpecKey(parts[m-1],0) or m == 0:
                        print('!')
                        try:
                            print('m+1:',type(parts[m+1]),parts[m+1])
                            err = 'err:115'
                            parts[m+1] = str('-')+str(parts[m+1])
                            err = 'err:116'
                            print('p: ',parts)
                            err = 'err:117'
                            del parts[m]
                        except:
                            if err:
                                print(err)
                            else:
                                print('err')
                    else:
                        print('m127: ', m)
                        m += 1
                else:
                    m += 1
                    print('m131: ', m)
            print('p132: ',parts)
            for m in range(0,len(parts)):
                print('134: ',parts[m])
                if type(parts[m]) == list:
                    parts[m] = ''.join(str(i) for i in parts[m])
                    print('137')
                print('lens: ',len(parts[m]))
                print('speck: ',self.SpecKey(parts[m],0))
                if len(parts[m]) > 1 or not self.SpecKey(parts[m],0):
                    print('139')
                    parts[m] = float(parts[m])
                #parts[m] = ''.join(str(i) for i in parts[m])
                #if len(parts[m]) > 1 and not SpecKey(parts[m],0):
                #    parts[m] = float(parts[m])
                print('p138: ',parts)

            k = 0
            print(k)
            while len(parts) > 1:
                while k in range(0,len(parts)):
                    del_k = True
                    if parts[k] == '×':
                        parts[k-1] = parts[k-1] * parts[k+1]
                        del parts[k],parts[k+1]
                        del_k = False
                    elif parts[k] == '÷':
                        try:
                            parts[k-1] = parts[k-1] / parts[k+1]
                            del parts[k],parts[k+1]
                            del_k = False
                        except:
                            parts = ['Error: cannot divide by zero']
                    
                    if parts[k] == '+':
                        parts[k-1] = parts[k-1] + parts[k+1]
                        del parts[k],parts[k+1]
                        del_k = False
                    elif parts[k] == '-':
                        parts[k-1] = parts[k-1] - parts[k+1]
                        del parts[k],parts[k+1]
                        del_k = False

                    if del_k:
                        del k
            return(str(parts))




                














            


##            while len(parts) > 1:
##                
##                k = 1
##                while k in range(len(parts)): #MULTIPLICATION
##                    print(k, parts)
##                    n1, n2 = '',''
##                    if parts[k] == '×' or parts[k] == '÷':
##                        print('len:',len(parts))
##                        print('ind:',parts[k])
##                        print('p1:',parts[k-1])
##                        if type(parts[k-1]) != float:
##                            n1 = float(parts[k-1])
##                        elif type(parts[k-1]) != n1:
##                            n1 = parts[k-1]
##                        print('n1:',n1)
##                        print('p2:',parts[k+1])
##                        if type(parts[k+1]) != float:
##                            n2 = str(''.join(str(i) for i in parts[k+1]))
##                            print('n2: ',n2)
##                            n2 = float(n2)
##                        elif type(parts[k+1]) != n2:
##                            n2 = parts[k+1]
##                        print('n2',n2)
##                        op = parts[k]
##                        ix = parts[k]
##                        del parts[k+1]
##                        if op == '×':
##                            parts[k-1] = float(n1*n2)
##                            print(n1,'x',n2)
##                        else:
##                            try:
##                                parts[k-1] = float(n1/n2)
##                            except:
##                                parts = ['Error: cannot divide by zero']
##                        try:
##                            del parts[k]
##                        except:
##                            print('err')
##                        print('p168: ',parts)
##                    else:
##                        k += 1
##
##                k = 1
##                while k in range(len(parts)): #ADDITION
##                    print(k, parts)
##                    n1, n2 = '',''
##                    if parts[k] == ['+'] or parts[k] == ['-']:
##                        print('len:',len(parts))
##                        print('ind:',parts[k])
##                        print('p1:',parts[k-1])
##                        if type(parts[k-1]) != float:
##                            n1 = str(''.join(str(i) for i in parts[k-1]))
##                            print('n1: ',n1)
##                            n1 = float(n1)
##                        elif type(parts[k-1]) != n1:
##                            n1 = parts[k-1]
##                        print('n1:',n1)
##                        print('p2:',parts[k+1])
##                        if type(parts[k+1]) != float:
##                            n2 = str(''.join(str(i) for i in parts[k+1]))
##                            print('n2: ',n2)
##                            n2 = float(n2)
##                        elif type(parts[k+1]) != n2:
##                            n2 = parts[k+1]
##                        print('n2',n2)
##                        op = parts[k]
##                        ix = parts[k]
##                        del parts[k+1]
##                        if op == ['+']:
##                            parts[k-1] = float(n1+n2)
##                            print(n1,'+',n2)
##                        else:
##                            parts[k-1] = float(n1-n2)
##                        try:
##                            del parts[k]
##                        except:
##                            print('err')
##                        print('p205:',parts)
##                    else:
##                        k += 1
##            return(str(parts[0]))
        else:
            return('Error')

    
    ### SPECIAL FUNCTIONS ###
    def SpecKey(self,eqn,n): #determine if item at index n is "special" (not numerical)
        try:
            char = int(eqn[n])
            return(False)
        except:
            return(True)
        
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

    def append(self,n):
        if self.blank:
            self.Eq = [0]
        if len(self.Eq) == 1 and type(n) != int:
            self.Eq.append(0)
        if len(self.Eq) < 25:
            self.Eq.append(n)
        lbl = ''.join(str(i) for i in self.Eq)
        self.li.configure(text=lbl[1:])
        self.blank = False

    def ans(self):
        if not self.blank:
            if self.Ans[0] == 0:
                del self.Ans[0]
            for i in self.Ans:
                self.Eq.append(i)
            lbl = ''.join(str(i) for i in self.Eq)
            self.li.configure(text=lbl[1:])  
        else:
            self.blank = False

    ## SYMBOLS ##
            
    def enter(self): #WIP
        if self.Eq != [0] and self.Eq:
            try:
                lbl = str(self.solve(self.Eq))
                if float(lbl) == int(float(lbl)):
                    lbl = int(float(lbl))
                lbl = list(str(lbl))
            except:
                lbl = str(self.solve(self.Eq))
            #if lbl == "['Error']":
            #    lbl = 'Error'
            self.Eq = [0]
            for i in lbl:
                self.Eq.append(i)
            self.Ans = self.Eq[:]
            lbl = ''.join(str(i) for i in lbl)
            self.li.configure(text=str(lbl))
            self.blank = True
        #Display Ans
        
root = Tk()
calculator = Calc(root)
root.mainloop()
