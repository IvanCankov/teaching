ip_cimek = []
hossz = 0
# 1. feladat
with open('ip.txt') as file:
    for ip_cim in file:
        ip_cim = ip_cim.strip()
        ip_cimek.append(ip_cim)
        hossz += 1

print('2.feladat')
print(f'Az állományban {len(ip_cimek)} darab adatsor van.')
print(f'{hossz}')

legkisebb = 'zzzz:zzzz:zzzz:zzzz'
for ip_cim in ip_cimek:
    if ip_cim < legkisebb:
        legkisebb = ip_cim

print('3.feladat')
print('A legalacsonyabb tárolt IP-cím:')
print(f'{min(ip_cimek)}')
print(f'{legkisebb}')