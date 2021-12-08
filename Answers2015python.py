f=open("marks.txt",'w')
i=0;t=0;
n=int(input("enter # of child"))
while (t<n):
    x = int(input("index"))
    if x==-1:
        t = n + 5 
    else:
        y = input("1st")
        z = input("2nd")
        a = input("3rd")
        x = str(a)
        line = x+","+y+","+z+","+a+"\n"
        f.write(line)
    t+=1
else:
    print('thanks')
f.close()
