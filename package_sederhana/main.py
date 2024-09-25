#Muhammad Rafi Fatihul Ihsan
#25-9-2024
#first package sederhana

import os
import matematika
import fisika

while(True):
    os.system("cls")
    print("-"*31)
    print("[   PROGRAM MATH AND PHYSIC   ]")
    print("-"*31)

    cek = int(input("\nPilih Mata Pelajaran\n\n1.Matematika\n2.Fisika\n\nkamu pilih?(ex.1) : "))
    if cek == 1:
        cek_mtk = int(input("\nPilih Operasi matematika!\n1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian\n5.Perpangkatan\nPilih salah satu(ex.1) : "))
        if cek_mtk == 1:
            print(matematika.math.opening())
            print(matematika.math.penjumlahan())
        elif cek_mtk == 2:
            print(matematika.math.opening())
            print(matematika.math.pengurangan())
        elif cek_mtk == 3:
            print(matematika.math.opening())
            print(matematika.math.perkalian())
        elif cek_mtk == 4:
            print(matematika.math.opening())
            print(matematika.math.pembagian())
        elif cek_mtk == 5:
            print(matematika.math.opening())
            print(matematika.math.perpangkatan())
        else:
            print("\nOpsi salah!\n")
    elif cek == 2:
        cek_fisika = int(input("\nPilih Operasi fisika!\n1.Rumus Gaya\n2.Rumus Energi Kinetik\n3.Rumus Percepatan\nPilih salah satu(ex.1) : "))
        if cek_fisika == 1:
            print(fisika.physic.fisika())
            print(fisika.physic.gaya())
        elif cek_fisika == 2:
            print(fisika.physic.fisika())
            print(fisika.physic.eKinetik())
        elif cek_fisika == 3:
            print(fisika.physic.fisika())
            print(fisika.physic.percepatan())
        else:
            print("\nOpsi salah!\n")
    else:
        print("\nOpsi salah!\n")

    inputnya = input("apakah lanjut(y/n)? ")
    if inputnya == "n" or inputnya == "N":
        break
print("\nProgram selesai\nTerimakasih dan sampai jumpa><\n")







