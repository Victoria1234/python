import pprint

message = 'It was a brightcold day in paril, and the clocks were striking thirteeen'
count = {}

for character in message.upper(): #this reads all as uppercase so get total count of characters
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count)
