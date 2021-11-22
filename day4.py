import re

file_name = "AOC2020_4.txt"

def extract_data(file:str) -> list:
    '''get the raw data and return a list of passports, each individual one as a dictionnary'''
    with open(file, 'r') as f:
        data = f.read().splitlines()+[''] # blank line is added so the last passport entry will be recorded
    output = []
    passport = dict()
    for line in data:
        if line:
            for key,value in [temp.split(':') for temp in line.split()]:
                passport[key] = value
        else:
            output.append(passport)
            passport = dict()
    return output

def all_fields_presents(passport: dict) -> bool:
    '''True if all necessary fields are presents, country ID is optional for North Pole credentials'''
    obligatory_keys = set(['byr', 'iyr','eyr', 'hgt', 'hcl','ecl', 'pid'])
    return obligatory_keys.issubset(set(passport.keys()))

def all_fields_values_valid(passport: dict) -> bool:
    '''True if data for each field value is valid'''
    byr = re.match('^19[2-9]\d$|^200[0-2]$', passport['byr']) # birth year 1920-2002
    iyr = re.match('^201\d$|^2020$', passport['iyr']) # issue year 2010-2020
    eyr = re.match('^202\d$|^2030$', passport['eyr']) # expiration year 2020-2030
    hgt = re.match('^1[5-8]\dcm$|^19[0-3]cm$|^59in$|^6\din$|^7[0-6]in$', passport['hgt']) # height 150-193 cm or 59-76 in
    hcl = re.match('^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$', passport['hcl']) # hair color 6 hex char
    ecl = re.match('^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$', passport['ecl']) # eye color
    pid = re.match('^\d\d\d\d\d\d\d\d\d$', passport['pid']) # Passport ID - exactly 9 digits
    return all([byr, iyr, eyr, hgt, hcl, ecl, pid])

passports = extract_data(file_name)

passports_all_fields_presents = [pp for pp in passports if all_fields_presents(pp) ]

passports_valid_data = [pp for pp in passports_all_fields_presents if all_fields_values_valid(pp)]

print(f'part 1 = {len(passports_all_fields_presents)},  part 2 = {len(passports_valid_data)}')

#part 1 = 182,  part 2 = 109
