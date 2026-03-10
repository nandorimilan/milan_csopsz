file = open('forras.txt', 'r', encoding='utf-8').read()

chars = [',', '.', ';', '(', ')', '[', ']', '\n']
for char in chars:
    file.replace(char, ' ')

oText = file.lower()
words:list = oText.split()

Counter1 = 0
for word in words:
    if len(word) == 4:
        Counter1 += 1
else:
    print('4 betus szavak:', Counter1)

Counter2 = 0
for word in words:
    if word.startswith('a'):
        Counter2 += 1
else:
    print('a-val kezdodo szavak:', Counter2)

Counter3 = 0
for word in words:
    if word.endswith('e'):
        Counter3 += 1
else:
    print('e-re vegzodo szavak:', Counter3)

Counter4 = 0
for word in words:
    if word == "dc":
        Counter4 += 1
else:
    print('hanyszor talalhato meg benne a dc szo:', Counter4)

Counter5 = 0
for word in words:
    if len(word) >= 8:
        Counter5 += 1
else:
    print('8 betus szavak:', Counter5)

Counter6 = 0
for word in words:
    if word.startswith('19') and len(word) == 4:
        Counter6 += 1
else:
    print('19-el kezdodo evszamok:', Counter6)

Counter7 = 0
for word in words:
    if word == 'batman':
        Counter7 += 1
else:
    print('hanyszor talalhato meg benne a batman szo:', Counter7)

Counter8 = 0
for word in words:
    if word.endswith('s'):
        Counter8 += 1
else:
    print('s-re vegzodo szavak:', Counter8)

Counter9 = 0
for word in words:
    if len(word) <= 3:
        Counter9 += 1
else:
    print('max 3 betus szavak:', Counter9)

Counter10 = 0
for word in words:
    if word.isdigit():
        Counter10 += 1
else:
    print('hany szam van a szovegben:', Counter10)



# TANULO CSOPORT HINT: az endswith vagy a startswith helyetesitheto lehetne amit oran tanultunk, word[ : ], de erdemes megtanulni
# startswith -> ezzel kezdodik, lehet betu vagy szam vagy eppen szo 
# endswith -> ezzel zarodik, szinten lehet betu vagy szam vagy eppen szo 
# isDigit -> ez szam? nem kell szorakozni az int + type fuggvenyekkel  


