ip_cimek = []
hossz = 0
# 1. feladat
with open('ip.txt') as file:
    for ip_cim in file:
        ip_cim = ip_cim.strip()
        ip_cimek.append(ip_cim)
        hossz += 1

print('2.feladat')
print(f'{len(ip_cimek)}')
print(f'{hossz}')