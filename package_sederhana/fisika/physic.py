def fisika():
    import os
    os.system("cls")

    print("-"*49)
    print("|                 MODUL FISIKA                  |")
    print("-"*49)
    print()

def gaya():
    print("A. RUMUS GAYA\n")
    print("Rumus untuk mencari Gaya --> f = m x a\n\nf = gaya(N)\nm = massa(kg)\na = percepatan(m/s2)\n\n*berikan nilai 0 jika tidak diketahui!\n")
    gaya = int(input("Masukkan nilai Gaya(F)\t: "))
    massa = int(input("Masukkan nilai Massa(m)\t: "))
    percepatan = int(input("Masukkan nilai Percepatan(a): "))

    if gaya == 0:
        hasil = massa * percepatan
        print(f"f = m x a --> f = {massa} x {percepatan} = {hasil}")
    elif massa == 0:
        hasil = gaya / percepatan
        print(f"m = f / a --> m = {gaya} / {percepatan} = {hasil}")
    elif percepatan == 0:
        hasil = gaya / massa
        print(f"a = f / m --> f = {gaya} / {massa} = {hasil}")
    else:
        print("\nmaaf,input tidak tepat!")

def eKinetik():
    print("B. RUMUS ENERGI KINETIK")
    print("Rumus untuk Energi kinetik --> Ek = m x v^2 / 2\n\nEk = energi kinetik\nm = massa(kg)\nv = kecepatan(m/s)\n")
    m = int(input("Masukkan nilai Massa(m)\t    : "))
    v = int(input("Masukkan nilai kecepatan(v) : "))
    hasil = m * (v ** 2) / 2
    print(f"\nEk = m x v^2 / 2 --> Ek = {m} x {v}^2 = {hasil}\n")

def percepatan():
    print("A. RUMUS PERCEPATAN\n")
    print("Rumus untuk mencari percepatan --> a = v / t\n\na = percepatan\nv = kecepatan\nt = waktu\n\n*berikan nilai 0 jika tidak diketahui!\n")
    v = int(input("Masukkan nilai kecepatan(v)  : "))
    a = int(input("Masukkan nilai percepatan(a) : "))
    t = int(input("Masukkan nilai waktu(t)\t     : "))
    print()
    if v == 0:
        hasil = a * t
        print(f"v = a x t --> v = {a} x {t} = {hasil}")
    elif a == 0:
        hasil = v / t
        print(f"a = v / t --> m = {v} / {t} = {hasil}")
    elif t == 0:
        hasil = v / a
        print(f"t = v / a --> f = {v} / {a} = {hasil}")
    else:
        print("\nmaaf,input tidak tepat!")