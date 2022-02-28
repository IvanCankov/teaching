ip_cimek = []
# 1. feladat
with open('ip.txt') as file:
    for ip_cim in file:
        ip_cimek.append(ip_cim.strip())

print('2.feladat')
print(f'Az állományban {len(ip_cimek)} darab adatsor van.')

print('3.feladat')
print('A legalacsonyabb tárolt IP-cím:')
print(f'{min(ip_cimek)}')

dok = 0
glob = 0
loc = 0
for ip_cim in ip_cimek:
    if '2001:0db8' in ip_cim[:9]:
        dok += 1
    if '2001:0e' in ip_cim[:7]:
        glob += 1
    if 'fc' in ip_cim[:2] or 'fd' in ip_cim[:2]:
        loc += 1

print('4. feladat:')
print(f'Dokumentációs cím: {dok} darab')
print(f'Globális egyedi cím: {glob} darab')
print(f'Helyi egyedi cím: {loc} darab')

#5. feladat
with open('sok.txt', 'w') as sok:
    for ip_cim in ip_cimek:
        if ip_cim.count('0') >= 18:
            print(f'{ip_cim}', file=sok)

print('6. feladat:')
sorszam = 9 #int(input('Kérek egy sorszámot: ')) - 1
print(f'{ip_cimek[sorszam]}')

parts = ip_cimek[sorszam].split(':')
for index, part in enumerate(parts):
    if part == '0000':
        parts[index] = '0'
print(':'.join(parts))

szam = False
for index, part in enumerate(parts):
    if ip_cimek[index] == '0000' or ip_cimek[index + 1] == '0000' or ip_cimek[index + 2] == '0000' or ip_cimek[index + 3] == '0000':
        ip_cimek[index + 0] = ' '
        ip_cimek[index + 1].pop()
        ip_cimek[index + 2].pop()
        ip_cimek[index + 3].pop()
        szam = True

print('7. feladat:')
if szam:        
    print(':'.join(parts))
else:
    print('nem roviditheto tovabb')