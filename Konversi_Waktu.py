import math
#logicnya kayak konversi hari ke tahun,bulan,minggu,hari
def timeConverter():
    try:  
        MasukkanDetik = int(input("Masukkan detik : "))#menerima inputan beraupa integer karena merupakan angka
        if 0 < MasukkanDetik <= 359999:  #mengecek angka apabila melebihi range yang ditentukan
            Hours = math.floor(MasukkanDetik/3600) #menggunakan fungsi math.floor yang telah di import sebelumya untuk membulatkan hasil bagi antara MasukkanDetik dengan 3600(konversi jam ke detik)
            jam = MasukkanDetik%3600 #menggunakan modulus untuk menampilkan sisa bagi antara MasukkanDetik dengan 360
            Minutes = math.floor(jam/60) #menggunakan fungsi math.floor untuk membulatkan ke bawah hasil bagi antara variabel jam dengan 60(konversi menit ke detik)
            menit = jam%60 #menggunakan modulus untuk menampilkan sisa bagi antara jam dengan menit
            detik = math.floor(menit/1) #menggunakan math.floor untuk menampilkan sisa bagi
            return "{}:{}:{}".format(Hours,Minutes,detik) #menggunakan return function untuk mengembalikan nilai hours,minutes.seconds dengan metode .format
    except:
        return "Invalid Input!" #mengembalikan nilai selain aturan def ini dengan return function untuk selain tipe ada int

print(timeConverter())

