def suku(a,s,b):
    jumlah = a + (b-1)*s
    jumlah_akh = b/2 * (a + jumlah)
    return jumlah_akh

print("="*20, "BARIS ARITMATIKA", "="*20)
a = int(input("Masukkan bilangan awal : "))
s = int(input("Masukkan selisih bilangan : "))
b = int(input("Masukkan banyaknya suku : "))
print("Total dari deret aritmatika tersebut adalah : ", suku(a,s,b))