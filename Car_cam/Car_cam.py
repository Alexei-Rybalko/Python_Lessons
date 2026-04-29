Cars = input("Напишите количество машин: ")
speed = input("Напишите скорости машин через запятую: ")
speed1 = speed.split(", ")
speed_no_30 = 0
Max = 0
Min = 301
Oshibka = False
for speeds in speed1:
    if int(Cars) > 30 or int(Cars) < 1:
        Oshibka = True
        break
    if int(speeds) < 1 or int(speeds) > 300:
        Oshibka = True
        break
    if int(speeds) > Max:
        Max = int(speeds)
    if int(speeds) < Min:
        Min = int(speeds)
if Oshibka != True:
    for norm in speed1:
        if int(norm) <= 30:
            speed_no_30 += 1
if Oshibka != True:
    print(Max - Min)
    print(speed_no_30)
if Oshibka == True:
    print("ERROR")


