#python function and howpython_function it works

def changeme(mylist):
    mylist.append([1,2,3,4])
    print "Values inside the function: ", mylist
    return

def printinfo(name,age):
    print "Name: " , name
    print "Age: ", age
    return


a = [10,20,30];
changeme(a)
print "Values outside the function: ", a
printinfo(age=24,name="Mohon")
