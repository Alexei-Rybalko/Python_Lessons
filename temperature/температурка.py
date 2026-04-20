import csv
q=0
f=0
Chislo_dney = input('Число дней: ')
with open("temperatura1.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        if row >= list('0') and row != 0:
            q += int(row[-1])
            f += 1

print(f)
print(q/f)
