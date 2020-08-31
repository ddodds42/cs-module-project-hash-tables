array = [
    'Waltz','Waltz','Tango', 'Tango', 'Tango', 'Viennese Waltz', 'Foxtrot',
    'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive'
    ]

# for each thing
# is it new? Is it in the dictionary?
# if new, add it with a value of 1!
# if not, increment the value under its key

dances = {}

for dance in array:
    if dance in dances:
        dances[dance] += 1
    else:
        dances[dance] = 1

print(dances)