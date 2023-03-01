kalimat = str(input("Masukkan sebuah kalimat: "))

def klmt_potong():
    potong = kalimat.split()
    return(potong)
def jmlh():
    panjang = len(klmt_potong())
    return panjang

print(klmt_potong())
print(jmlh())