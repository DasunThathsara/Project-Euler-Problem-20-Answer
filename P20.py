n=1
t=1
f=0
for n in range(1,101):
    t=t*n
x=str(t)
for a in x:
    f=f+int(a)
print(f)
print(t)
