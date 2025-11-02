def decimal_to_binary(decimal):
    binary = ""
    masukan = decimal
    
    if masukan == 0:
        return "0"
    
    while masukan > 0:
        sisa = masukan % 2
        binary = str(sisa) + binary
        masukan = masukan // 2
    
    return binary

def decimal_to_hexa(decimal):
    hexa = ""
    masukan = decimal
    hexa_digits = "0123456789ABCDEF"
    
    if masukan == 0:
        return "0"
    
    while masukan > 0:
        sisa = masukan % 16
        hexa = hexa_digits[sisa] + hexa
        masukan = masukan // 16
    
    return hexa

def decimal_to_octal(decimal):
    octal = ""
    masukan = decimal
    
    if masukan == 0:
        return "0"
    
    while masukan > 0:
        sisa = masukan % 8
        octal = str(sisa) + octal
        masukan = masukan // 8
    
    return octal

print("\nProgram Konversi Bilangan")
print("========================")
print("1. Decimal ke Binary")
print("2. Decimal ke Hexadecimal")
print("3. Decimal ke Octal")

pilihan = int(input("\nMasukkan pilihan (1-3): "))
                
if pilihan == 1:
    angka = int(input("\nMasukkan angka: "))
    if angka<0:
        print("\nMasukkan bilangan positif")
    else:
        hasil = decimal_to_binary(angka)
        print(f"Hasil konversi ke binary: {hasil}")
                
elif pilihan == 2:
    angka = int(input("\nMasukkan angka: "))
    if angka<0:
        print("\nMasukkan bilangan positif")
    else:
        hasil = decimal_to_hexa(angka)
        print(f"Hasil konversi ke hexadecimal: {hasil}")
                
elif pilihan == 3:
    angka = int(input("\nMasukkan angka: "))
    if angka<0:
        print("\nMasukkan bilangan positif")
    else:
        hasil = decimal_to_octal(angka)
        print(f"Hasil konversi ke octal: {hasil}")
    
else:
    print("Masukkan angka yang tersedia (1-3")