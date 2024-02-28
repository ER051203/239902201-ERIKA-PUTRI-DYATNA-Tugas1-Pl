print ("---MEMBACA GAJI DAN MEMBAGI JUMLAHNYA DENGAN 12 BULAN---") 

nama = str (input("Masukan Nama Pegawai: "))
gaji_setahun = float(input("Masukan Gaji Anda Selama 1 Tahun: "))

#rumus menghitung gaji perbulan
gaji_perbulan = round (gaji_setahun / 12)

#tampilan output gaji perbulan
print ("gaji perbulan : ", gaji_perbulan)

