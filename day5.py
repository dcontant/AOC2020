file_name = "aoc2020_5.txt"

with open(file_name, 'r') as f:
    data = f.read().splitlines()

def seat(boarding_pass: str) -> tuple:
    '''return seat number as a tuple (row,column)'''
    seat = ''
    for char in boarding_pass:
        if char in 'FL':
            seat += '0'
        elif char in 'BR':
            seat += '1'
    row = int(seat[:7],2)
    column = int(seat[7:],2)
    return (row, column)

def seat_id(seat: tuple) -> int:
    row, column = seat
    return row*8 + column

all_seats_id = [seat_id(seat_tuple) for seat_tuple in [seat(boarding_pass) for boarding_pass in data]]

lowest = min(all_seats_id)
part1 = max(all_seats_id)
part2 = set(range(lowest,part1+1)) - set(all_seats_id)

print(f'part1 = {part1} , part2 = {part2.pop()}')

#part1 = 913 , part2 = 717
