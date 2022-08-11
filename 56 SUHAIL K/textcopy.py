with open("dark.txt")as f:
    with open("dark1.txt", "w")as f1:
        for line in f:
            f1.write(line)
