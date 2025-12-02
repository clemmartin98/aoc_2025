with open("./d2/input.txt", "r", encoding="utf-8") as file:
    ids = file.readlines()

total = 0
wrong_ids = []
for id in ids[0].split(","):
# for id in ids:
    start, stop = id.split("-")
    for elem in range(int(start), int(stop)+1):
        elem = str(elem)
        if len(elem)%2 == 0:
            if elem[:int(len(elem)/2)] == elem[int(len(elem)/2):]:
                total += int(elem)

        for i in range(int(len(elem))//2):
            if elem.count(elem[:i+1]) >1:

                char = elem[:i+1]
                count = elem.count(elem[:i+1])
                if len(elem)%len(char) == 0:
                    repeated_char = char*int(len(elem)/len(char))
                    if repeated_char == elem:
                        wrong_ids.append(int(elem))
                    
wrong_ids = sorted(list(set(wrong_ids)))# print(total)

print(f"Sum of wrong ids (part 1) : {total}")
print(f"Sum of wrong ids (part 2) : {sum(wrong_ids)}")