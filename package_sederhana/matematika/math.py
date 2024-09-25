def opening():
    import os
    os.system("cls")

    print("-"*53)
    print("|                 MODUL MATEMATIKA                  |")
    print("-"*53)
    print()

def penjumlahan():
    print("A). PENJUMLAHAN")
    data = 0
    count = 0
    masukan = int(input("Mau Masukin Berapa Angka? "))
    for i in range(masukan):
        count = count + 1
        nilai = int(input(f"Masukkan Angka {count} = "))
        data = data + nilai
    print(f"Hasil Penjumlahan Data diatas Adalah = {data}\n")

def pengurangan():
    print("B). PENGURANGAN")
    data = 0
    count = 0
    masukan = int(input("Mau Masukin Berapa Angka? "))
    for i in range(masukan):
        count = count + 1
        nilai = int(input(f"Masukkan Angka {count} = "))
        data = data - nilai
    print(f"Hasil Pengurangan Data diatas Adalah = {data}\n")

def perkalian():
    print("C). PERKALIAN")
    data = 1
    count = 0
    masukan = int(input("Mau Masukin Berapa Angka? "))
    for i in range(masukan):
        count = count + 1
        nilai = int(input(f"Masukkan Angka {count} = "))
        data = data * nilai
    print(f"Hasil Perkalian Data diatas Adalah = {data}\n")

def pembagian():
    print("D). PEMBAGIAN")
    data = 1
    masukan = int(input("Mau Masukin Angka Berapa? "))
    nilai = int(input(f"Dibagi dengan? "))
    data = masukan / nilai
    print(f"Hasil Pembagian diatas Adalah {masukan} / {nilai} = {data}\n")

def perpangkatan():
    print("E). PERPANGKATAN")
    data = 1
    masukan = int(input("Mau Masukin Angka Berapa? "))
    nilai = int(input(f"Dipangkatkan dengan? "))
    data = masukan ** nilai
    print(f"Hasil Perkalian pangkat diatas Adalah {masukan} ^ {nilai} = {data}\n")
