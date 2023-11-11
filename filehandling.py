
import os
while True:
    a=(input('enter the choice'))
    def f():
        print("1.create the file")
        print("2.list the file")
        print("3.read the file")
        print("4.edit the file")
        print("5.delete the file")
        print("6.stop the program")
    match a:
        case"1":
            print("creating a file")
            name=input("enter the file name:")
            name=name+".txt"
            file=open(name,"w")
            file.write("welcome")
            print("-------------------------")
            print("file craeted successfully")
            print("-------------------------")
        case "2":
            print("reading a file")
            name=input("enter the file name:")
            name=name+".txt"
            file=open(name,"r")
            print(file.read())
            f()
        case"3":
            path="D:\lateefa"
            files=os.listdir(path)
            for file in files:
                print(file)
                f()
        case"4":
            print("edit a file")
            name=input("enter the file name:")
            name=name+".txt"
            file=open(name,"a")
            (file.write("lateefa"))
            print("---------------------------")
            f()      
        case"5":
            print("deleting file")
            name=input("enter the file name:")
            name=name+".txt"
            os.remove(name)
            print("file ",name,"\ndeleted sucessfully")
            print("---------------------------------")
            f()
        case"6":
            print("************program end**************")
            break
            
                  
                  
            
