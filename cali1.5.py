#tkinker module to gelp in gui coding

from tkinter import *#(imports everthing)

#basic function caling to do calualations
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1

def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1

def sqroot(a):  #funtion defined but accepting in operations part
    c=a ** 2
    return c

def pow(a,b):
    x=pow(a,b)
    return x

def recur_factorial(a):  
   if a == 1:  
       return a  
   else:  
       return a*recur_factorial(a-1)


    
def COMP():  # error 
    print("happy to help")

    
def extraxt_from_text(text):  #it extract the num from text
    l = []  #empty list
    for t in text.split(' '):   
        try:
            l.append(float(t)) #convert every value to float  
        except ValueError:
            pass
    return l


def calculate():  #it does the calcuation part 
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extraxt_from_text(text)
                r = operations[word.upper()](l[0] , l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'1 something went wrong please enter again')
                
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'2 something went wrong please enter again')

operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add  , 'add':add , '+':add ,
                'SUB':sub , 'sub':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub, '-':sub ,
                 'LCM':lcm , 'lcm':lcm , 'HCF':hcf , 'hcf':hcf ,'gcd':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul,'*':mul,
                 'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div, '/': div, 'MOD':mod , 'SQ':sqroot,
                  'REMANDER':mod , 'MODULUS':mod , '%':mod,
              'COMPLETE':COMP}

#LOGIC FOR THE INTIAL USER INTERFACE
win = Tk()
win.geometry('500x300')
win.title('C.A.L.I THE SMART CALCULATOR')
win.configure(bg='orange')

l1 = Label(win , text=' HII I am a smart calculator',width=20 , padx=3)
l1.place(x=160,y=10)
l2 = Label(win , text='My name is C.A.L.I 1.5!' , padx=3)
l2.place(x=170,y=40)
l3 = Label(win , text='HOW CAN I HELP YOU ?' , padx=3)
l3.place(x=170,y=90)
l4 = Label(win , text='THANKS FOR USING ME',width=20 , padx=3)
l4.place(x=145,y=270)

#for string taking into consideration
textin = StringVar()
e1 = Entry(win , width=30 , textvariable = textin)
e1.place(x=110,y=130)

b1 = Button(win , text='find result' ,command=calculate)
b1.place(x=200,y=160)

list = Listbox(win,width=20,height=3)
list.place(x=150,y=200)

win.mainloop()
