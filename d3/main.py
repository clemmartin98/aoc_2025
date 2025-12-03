with open("./d3/input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()



lines = [line.strip() for line in lines]

def get_max_joltage_list(label, n):
        vals = []
        rating_list = list(str(label))
        for i in range(1,n+1):
            end = (i-n)
            cropped_list = rating_list[:end] if end !=0 else rating_list
            max_index = cropped_list.index(max(cropped_list))
            val = rating_list[max_index]
            rating_list = rating_list[max_index+1:]
            vals.append(val)
        return "".join(vals)
    

joltage_list_2 = []
joltage_list_12 = []
# Part 1
for label in lines:
    vals_2 = get_max_joltage_list(label, 2)
    vals_12 = get_max_joltage_list(label, 12)

    joltage_list_2.append(int(vals_2))
    joltage_list_12.append(int(vals_12))

print(f"Sum of joltage list (part 1) : {sum(joltage_list_2)}")
print(f"Sum of joltage list (part 2) : {sum(joltage_list_12)}")

