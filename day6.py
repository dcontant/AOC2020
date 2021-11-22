file_name = "AOC2020_6.txt"

with open(file_name, 'r') as f:
    data = f.read().splitlines()+ ['']

part1 = 0
partt2 = 0
group_answers= []
for passenger in data:
    if passenger:
        group_answers.append(set(passenger))
    else:
        part1 += len(group_answers[0].union(*group_answers[1:]))
        part2 += len(group_answers[0].intersection(*group_answers[1:]))
        group_answers = []
        
    
print(f'part1 = {part1}, part2 = {part2}')
# part1 = 6763, part2 = 7024
