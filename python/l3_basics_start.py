# Dərs 3 · Blok 1 — Python-un 10 kərpici
# İşə salma (de-praktikum qovluğundan): python src/l3_basics_start.py
# Dərsdə hər kərpicin kodunu slayddan öz bölməsinə yazırıq.
# Hər bölmə əvvəlcə öz başlığını çap edir — terminalda həmişə
# ən aşağıdakı bölməyə baxın. Tam kod dərsdən sonra Teams-də olacaq.

print("=== Kərpic 1 ===")   # Proqram — əmrlər ardıcıllığı
# TODO: print(...) ilə 4 sətir (slayd «Kərpic 1»)

print("=== Kərpic 1 ===")
# Bu sətir şərhdir: Python onu icra etmir, bu — insan üçün qeyddir
print("Salam, data mühəndisliyi!")
print("Baza stansiyası:", "BAK-0207")
print(2 + 3)
print("2 + 3")

print("=== Kərpic 2 ===")   # Dəyişən — adı olan qutu
# TODO: cell, rsrp, drops

print("=== Kərpic 2 ===")
cell = "BAK-0207" # qutu: adı cell, içində mətn
rsrp = -95.5 # qutu: adı rsrp, içində ədəd
print(cell, rsrp)
rsrp = -108.1 # yeni dəyər qoyduq — köhnəsi itdi
print(cell, rsrp)
drops = 2
drops = drops + 1 # götür, 1 əlavə et, geri qoy
print("drops =", drops)

print("=== Kərpic 3 ===")   # Tiplər: int, float, str, bool, None
# TODO: type(...) və «mətn ≠ ədəd»

print("=== Kərpic 3 ===")
print(type(3)) # int — tam ədəd
print(type(-95.5)) # float — kəsr ədəd
print(type("BAK-0207")) # str — mətn (dırnaq içində)
print(type(True)) # bool — məntiqi: True / False
print(type(None)) # None — «dəyər yoxdur»

name = input("please enter your name")
age = int(input("please enter your age"))
if age > 25:
   print("hello I am",name, "and I am", age, "years old, I am older than 25 years old")
if age < 25:
    print("hello I am",name, "and I am", age, "years old, I am not older than 25 years old")
print("=== Kərpic 4 ===")   # Müqayisə → True / False
# TODO: rsrp < -105, ==

print("=== Kərpic 5 ===")   # Siyahı (list)
# TODO: rsrp_list, indeks, len, orta

numbers = [-22.5, 12, 0.12, 23, 29.7, 100, 0.001]
number = int(input("please enter a number:"))
print(numbers[number - 1])


print("=== Kərpic 6 ===")   # Lüğət (dict)
# TODO: row = {...}, row["region"]

print("=== Kərpic 7 ===")   # Dövr (for) və şərt (if / else)
# TODO: zəif ölçmələri saymaq

print("=== Kərpic 8 ===")   # Funksiya: çağırmaq və yaratmaq
# TODO: round, len, max; def is_weak(rsrp)

print("=== Kərpic 9 ===")   # Nöqtə: metod
# TODO: name.strip().capitalize()

print("=== Kərpic 10 ===")  # import — hazır alət qutusu
# TODO: import math; import pandas as pd
