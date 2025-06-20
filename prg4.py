try:
    file=open("myfile.txt","r")
except IOerror:
    print("error:unable to read the file!")
finally:
    file.close()
