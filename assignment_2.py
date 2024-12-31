names = ['Diogo', 'DiogoDiogon', 'DiogoDiogoN', 'DiogoDiogoDiogoDiogo', 'DiogoDiogoDiogoDiogonN']

for name in names:
    if len(name) > 5 and 'n' in name or 'N' in name:
        print(f"Name: {name}, Length: {len(name)}")

while names:
    print(f"Removed element {names.pop()} from list")
