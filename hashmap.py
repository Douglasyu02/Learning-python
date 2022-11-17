#hashmaps in py
array = [2,6,7,8]
target = 9
seen = set()
for number in array:
    if target - number in seen:
        print(target - number, number)
    seen.add(number)
    