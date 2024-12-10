data = '''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''.strip()


lines = [list(map(int, row.split())) for row in data.split("\n")]

safe = 0
len_line = len(lines[0])


for line in lines:
    print(line)
    is_Safe = True 
    if line[0] < line[1]:
        print("<")
        for i in range(1, len_line):
            print(line[i-1] < line[i])
            print(abs(line[i-1]-line[i]))

            if (line[i-1] < line[i]) and (0 < abs(line[i-1] - line[i]) < 4):
                
                pass
            else:
                is_Safe = False
                break
    else:
        print(">")
        for i in range(1, len_line):
            if (line[i-1] > line[i]) and (0 > abs(line[i-1] - line[i]) > 4):
                pass
            else:
                is_Safe = False
                break
    

    if is_Safe:
        print(is_Safe)
        safe += 1

print(safe)


