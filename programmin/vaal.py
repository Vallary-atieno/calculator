with open("example00.txt", "r")as file:
    lines=file.readline()
    for line in lines:
        print(line.strip())
     #while line:
        #print(line.strip())
        #line=file.readline()
    #content=file.read()
    #print(content)