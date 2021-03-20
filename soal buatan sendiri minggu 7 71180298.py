# Aloysius Gonzaga Ardhian Krisna Aji
# 71180298

# Buggy seorang pelajar diberi tugas oleh gurunya untuk membuat program mengubah 
# huruf besar menjadi huruf kecil dan huruf kecil menjadi huruf besar (berkebalikan)
# dan sebagai poin bonus gurunya meminta juga untuk membuat soal 
# yang bisa menampilkan jumlah kata yang disebutkan
# sebagai teman baiknya kamu harus membantu buggy.

# input 
# -input kalimat random
# -inputkan suatu kalimat random degan huruf besar dan kecil
# output
# -kebalikan huruf besar dan kecil dari inputan
# -bisa berupa jumlah kata sesuai pilihan menu

def pembalik(kalimat):
    kebalikan = kalimat.swapcase()
    return kebalikan
def pencari(kalimat,kata):
    cari = kalimat.count(kata)
    return cari

loop = True
while loop:
    print("\n <===Program Method String===>")
    print("1. Program Pembalik")
    print("2. Program Cari Jumlah Kata")
    print("3. Keluar")

    masukan = int(input("Masukan pilihan: "))
    if masukan == 1:
        kalimat = input("Masukan kalimat: ")
        print("Hasil: ",pembalik(kalimat))
    elif masukan == 2:
        kalimat = input("Masukan kalimat: ")
        kata = input("Masukan kata yang dicari: ")
        print("Hasil: ",pencari(kalimat,kata))
    elif masukan == 3:
        print("Terima Kasih...")
        loop = False
    else:
        print("Inputan tidak sesuai")

