#File basics

print "1.Create a file, 2.Write, 3.Read, 4.Exit"

ch=input("Enter the choice:")

if ch==1:
    fp=open("cse.txt","w")
    print "File is created"
    fp.close()
    
elif ch==2:
    fp=open("cse.txt","w")
    fp.write("Hello CSE")
    fp.close()
    
elif ch==3:
    fp=open("cse.txt","r")
    text=fp.read()
    print text
    fp.close()
    
elif ch==4:
    exit
    




