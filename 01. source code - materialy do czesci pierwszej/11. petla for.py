
name = "KalaQfiory"

samogloski = 0
spolgloski = 0

for litera in name:

    if litera in "aeuioy":
        samogloski += 1
    else:
        spolgloski += 1

    if litera == 'Q':
        break		


print("Spółgłoski:", spolgloski)
print("Samogłoski:", samogloski)


