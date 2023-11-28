#!/usr/bin/python3
for i in range(1 , 100):
    if i in range(1,10):
        print ("0{0}".format(i),end=", ")
    elif i == 99:
        print ("{0}".format(i),)
    else:
        print ("{0}".format(i),end=", ")
