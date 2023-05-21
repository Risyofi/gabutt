pendataan = {"nama": [], "email": [], "alamat": [], "nomor_telepon": [], "keperluan": [], "jumlah_keperluan": [], "jumlah_uang": [], "tanggal": []}

def menu():
    print("Selamat Datang di PT Nawakara")
    print("Silahkan pilih menu di bawah:")
    print("1. Security System")
    print("2. Electronic Security System")
    print("3. Cash and Valuable in Transit")
    print("4. Database")
    print("5. Keluar")

def tambah_data1():
    nama = input("Nama  : ")
    email = input("Email: ")
    nomor_telepon = input("Nomor Telepon: ")
    alamat = input("Alamat: ")
    keperluan = input("Keperluan: ")
    jumlah_keperluan = input("Jumlah: ")
    
    pendataan['nama'].append(nama)
    pendataan['email'].append(email)
    pendataan['nomor_telepon'].append(nomor_telepon)
    pendataan['alamat'].append(alamat)
    pendataan['keperluan'].append(keperluan)
    pendataan['jumlah_keperluan'].append(jumlah_keperluan)

def tambah_data2():
    nama = input("Nama  : ")
    email = input("Email: ")
    nomor_telepon = input("Nomor Telepon: ")
    alamat = input("Alamat: ")
    tanggal = input("Keperluan: ")
    jumlah_uang= input("Jumlah: ")
    
    pendataan['nama'].append(nama)
    pendataan['email'].append(email)
    pendataan['nomor_telepon'].append(nomor_telepon)
    pendataan['alamat'].append(alamat)
    pendataan['tanggal'].append(tanggal)
    pendataan['jumlah_uang'].append(jumlah_uang)

def menu1():
    print("============== SECURITY SYSTEM ==============")
    print("========= SECTION 1: PEMILIHAN JASA =========")
    print("1. Manned guarding service")
    print("2. Event security service")
    while True:
        pilihan = int(input("pilihan: "))
        if pilihan == 1:
            print("========== Manned Guarding Service ==========")
            print("============ SECTION 2: DATA DIRI ===========")
            tambah_data1()
        elif pilihan == 2:
            print("=========== Event Security Service ==========")
            print("============ SECTION 2: DATA DIRI ===========")
            tambah_data1()
        elif pilihan == 3:
            print("Terima kasih!!")
            break
        else:
            print("Pilihan Tidak valid!!")

def menu2():
    print("============== SECURITY SYSTEM ==============")
    print("========= SECTION 1: PEMILIHAN JASA =========")
    print("1. Manned guarding service")
    print("2. Event security service")
    print("3. Keluar")
    while True:
        pilihan = int(input("pilihan: "))
        if pilihan == 1:
            print("========== Manned Guarding Service ==========")
            print("============ SECTION 2: DATA DIRI ===========")
            tambah_data1()
        elif pilihan == 2:
            print("=========== Event Security Service ==========")
            print("============ SECTION 2: DATA DIRI ===========")
            tambah_data1()
        elif pilihan == 3:
            print("Terima kasih!!")
            break
        else:
            print("Pilihan Tidak valid!!")

def menu3():
    print("============== SECURITY SYSTEM ==============")
    print("========= SECTION 1: PEMILIHAN JASA =========")
    print("1. Manned guarding service")
    print("2. Event security service")
    while True:
        pilihan = int(input("pilihan: "))
        if pilihan == 1:
            print("========== Manned Guarding Service ==========")
            print("============ SECTION 2: DATA DIRI ===========")
            tambah_data1()
        elif pilihan == 2:
            print("=========== Event Security Service ==========")
            print("============ SECTION 2: DATA DIRI ===========")
            tambah_data2()
        elif pilihan == 3:
            print("Terima kasih!!")
            break
        else:
            print("Pilihan Tidak valid!!")

def menu4():
    print("============== SECURITY SYSTEM ==============")
    print("========= SECTION 1: PEMILIHAN JASA =========")
    print("1. Manned guarding service")
    print("2. Event security service")
    while True:
        pilihan = int(input("pilihan: "))
        if pilihan == 1:
            print("========== Manned Guarding Service ==========")
            print("============ SECTION 2: DATA DIRI ===========")
            tambah_data2()
        elif pilihan == 2:
            print("=========== Event Security Service ==========")
            print("============ SECTION 2: DATA DIRI ===========")
            tambah_data1()
        elif pilihan == 3:
            print("Terima kasih!!")
            break
        else:
            print("Pilihan Tidak valid!!")

## Main Program
while True:
    menu()
    pilihan = int(input("pilihan: "))

    if pilihan == 1:
        menu1()
    elif pilihan == 2:
        menu2()
    elif pilihan == 3:
        menu3()
    elif pilihan == 4:
        menu4()
    elif pilihan == 5:
        print("Terima kasih!!")
        break
    else:
        print("Pilihan Tidak valid!!")
