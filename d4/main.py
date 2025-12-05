with open("./d4/input.txt", "r", encoding="utf-8") as file:
    input = file.readlines()

input = [line.strip() for line in input]

def scan_shelf(input, steps=1):
    shelf = [""]*len(input)
    total = 0
    stop = False
    
    while not stop:

        for i,line in enumerate(input):
            new_line = []
            for j, char in enumerate(line):

                neighbor_rows = input[max(i-1,0):min(i+2,len(input))]
                neighbors = [row[max(j-1,0):min(j+2,len(row))] for row in neighbor_rows]
                
                if char == "@":
                    neighbors_count = sum(row.count("@") for row in neighbors)
                    if neighbors_count-1 >= 4:
                        new_line.append("@")
                    else:
                        new_line.append("x")
                else:
                    new_line.append(".")
            shelf[i] = new_line
        subtotal = 0
        for line in shelf:
            subtotal += line.count('x')
        if subtotal == 0 or steps == 1:
            stop = True
        total+=subtotal
        input = shelf
    return total

print(f"First part : {scan_shelf(input, 1)}")
print(f"Second part : {scan_shelf(input, 0)}")

