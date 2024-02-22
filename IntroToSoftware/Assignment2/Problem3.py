with open("myfile1.txt", 'r') as f:
    data = f.read()
    with open('myfile2.txt', 'w') as f:
        f.write(data)
