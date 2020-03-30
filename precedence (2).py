f=open("precedence.txt",'w')
ho = ['*','/','+','-']
a=input("Enter expression: ")
k=[]
s=''
t=''
for j in a:
    if j in ho:
        if not(s==''):
          k.append(s)
          s=''
        k.append(j)
    else:
        t=s+j
        s=t
        t=''
if not(s==''):
    k.append(s)
    s=''
print(k)
i = len(k)-1
while i>=0:
    if k[i] in ho:
        if k[i-1] == '*':
            a = k.pop(i-2)
            k.pop(i-2)
            k.pop(i - 2)
            b = k.pop(i-2)
            k.insert(i-2,str(int(a)**int(b)))
            i-=1
            f.write("checking .... **{0} accepted\n".format(b))
    i-=1
i=0
while i<len(k):
    if k[i] =='*':
        a=k.pop(i-1)
        k.pop(i-1)
        b=k.pop(i-1)
        k.insert(i-1,str(int(int(a)*int(b))))
        i-=1
        f.write("checking {0}*....  accepted\n".format(a))
    elif k[i] =='/':
        a=k.pop(i-1)
        k.pop(i-1)
        b=k.pop(i-1)
        k.insert(i-1,str(int(int(a)/int(b))))
        i-=1
        f.write("checking {0}/....  accepted\n".format(a))
    i+=1
print(k)
i=0
while i<len(k):
    if k[i] =='+':
        a=k.pop(i-1)
        k.pop(i-1)
        b=k.pop(i-1)
        k.insert(i-1,str(int(a)+int(b)))
        i-=1
        f.write("checking {0}+....  accepted\n".format(a))
    elif k[i] =='-':
        a=k.pop(i-1)
        k.pop(i-1)
        b=k.pop(i-1)
        k.insert(i-1,str(int(a)-int(b)))
        i-=1
        f.write("checking {0}-....   accepted\n".format(a))
    i+=1
print(k)
f.close()
