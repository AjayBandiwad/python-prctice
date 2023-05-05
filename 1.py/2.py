with open ("file1.txt","w+") as file 
for i in range(5):
    i=input("write all detatils")
    sum=file.write(i)
    print(sum)