print("\n\n   SELAMAT DATANG DI PROGRAM KASIR RAMEN ICIRAKU") 
print(50*"-")
print(50*" ")

def menu():
    print("	menu pilihan")
    print(28*"=")
    print("1.Daftar menu")
    print("2.Kasir")
    print("3.Laporan penjualan")
    print("4.exit")
    print(28*"=")
    pilih=int(input("masukan pilihan : "))
    return pilih
				
def daftarmenu():
	print("		::::::::M E N U::::::::	")
	check= True
	#deklarasi list
	menumakanan = [
	" => Beef Ramen		   |",
	" => Chiken Karaage Curry Ramen   |",
	" => Ebi Tempura Ramen            |",
	" => Chiken Miso Ramen            |",
	" => Volcano Ramen                |",
	" => Karaage Ramen                |",
	" => Legendary Chiken Ramen       |",
	" => Chiken Popcorn Ramen         |",
	" => HOT Nakedmen                 |",
	"=> Original Ten Ten-Men	   |",
	"=> Spicy Ten Ten-Men		   |",
	"=> Tori Miso-Men	           |",
	"=> Tori Curry-Men	       	   |",
	"=> Spicy Tori Miso-Men    	   |",
	"=> Naked Popcorn Spicy          |"]
	hargamakanan=[54000,52000,50000,42000,60000,47000,40000,46000,59000,45000,43500,55000,62000,57000,61000]

	menuminuman=[
	" => Machalatte                   |",
	" => Ice Shake Tea                |",
	" => Mango Punch                  |",
	" => Orange Punch                 |",
	" => Sparkling Lychee             |",
	" => Sparkling Strowberry         |",
	" => Melon Breeze                 |",
	" => Lime Yakult                  |",
	" => Mango Yakult 		   |", 
	"=> Orange Yakult  		   |",
	"=> Lychee Yakult  		   |",
	"=> Melon Breeze    		   |",
	"=> Lime Breeze	 	   |",
	"=> Ice Tea                      |",
	"=> Lemon Tea                    |"]
	hargaminuman=[38000,35000,34000,34000,37000,37000,29000,35000,22000,22000,26000,36000,32000,35000,40000]

	menutoppingtambahan=[
	" => Udang keju                   |",
	" => Chili Paste                  |",
	" => Katsuobushi                  |",
	" => Tteokbokki	           |",
	" => Fried Egg                    |",
	" => Odeng		           |",
	" => Horenzo	                   |",
	" => Gyoza		           |",
	" => Kimbab		           |",
	"=> Cumi		           |"]
	hargatoppingtambahan=[15000,10000,14000,16000,12000,15000,16000,13000,16000,12000]
	print()

	#Logika Perulangan 
	while(check):
		print("                                                      ")
		print(50*"=")
		print("            Daftar Menu Ramen Iciraku           ") 
		print(50*"=")
		print()
		print(18*"=","Menu Makanan",18*"=",)
		break
	
	#untuk mencetak tabel makanan/minuman mengambil dari list
	for i in range(len(menumakanan)):
		print(i+1, menumakanan[i], '\t- Rp', hargamakanan[i])
	print()

	print(18*"=","Menu Minuman",18*"=",)
	for i in range(len(menuminuman)):
	    print(i+1, menuminuman[i], '\t- Rp', hargaminuman[i])
	print()
	    
	print(14*"=","Menu Topping Tambahan",14*"=",)
	for i in range(len(menutoppingtambahan)):
	    print(i+1, menutoppingtambahan[i], '\t- Rp', hargatoppingtambahan[i])
	print(50*"=")
	back=input("kembali (y)/keluar (t):")
	if back == "y" or back == "t" :
		print("")
		pilih
	else :
		print()

def kasir():
	check = True
	print("		::::::::K A S I R::::::::	")
	#deklarasi list
	menumakanan = [
	" => Beef Ramen		   |",
	" => Chiken Karaage Curry Ramen   |",
	" => Ebi Tempura Ramen            |",
	" => Chiken Miso Ramen            |",
	" => Volcano Ramen                |",
	" => Karaage Ramen                |",
	" => Legendary Chiken Ramen       |",
	" => Chiken Popcorn Ramen         |",
	" => HOT Nakedmen                 |",
	"=> Original Ten Ten-Men	   |",
	"=> Spicy Ten Ten-Men		   |",
	"=> Tori Miso-Men	           |",
	"=> Tori Curry-Men	       	   |",
	"=> Spicy Tori Miso-Men    	   |",
	"=> Naked Popcorn Spicy          |"]
	hargamakanan=[54000,52000,50000,42000,60000,47000,40000,46000,59000,45000,43500,55000,62000,57000,61000]

	menuminuman=[
	" => Machalatte                   |",
	" => Ice Shake Tea                |",
	" => Mango Punch                  |",
	" => Orange Punch                 |",
	" => Sparkling Lychee             |",
	" => Sparkling Strowberry         |",
	" => Melon Breeze                 |",
	" => Lime Yakult                  |",
	" => Mango Yakult 		   |", 
	"=> Orange Yakult  		   |",
	"=> Lychee Yakult  		   |",
	"=> Melon Breeze    		   |",
	"=> Lime Breeze	 	   |",
	"=> Ice Tea                      |",
	"=> Lemon Tea                    |"]
	hargaminuman=[38000,35000,34000,34000,37000,37000,29000,35000,22000,22000,26000,36000,32000,35000,40000]

	menutoppingtambahan=[
	" => Udang keju                   |",
	" => Chili Paste                  |",
	" => Katsuobushi                  |",
	" => Tteokbokki	           |",
	" => Fried Egg                    |",
	" => Odeng		           |",
	" => Horenzo	                   |",
	" => Gyoza		           |",
	" => Kimbab		           |",
	"=> Cumi		           |"]
	hargatoppingtambahan=[15000,10000,14000,16000,12000,15000,16000,13000,16000,12000]
	print()
	print()

	#Logika Perulangan 
	while(check):
			print("                                                      ")
			print(50*"=")
			print("            Program Kasir Ramen Iciraku            ") 
			print(50*"=")
			print()
			print(18*"=","Menu Makanan",18*"=",)
			break
		
		#untuk mencetak tabel makanan/minuman mengambil dari list
		for i in range(len(menumakanan)):
			print(i+1, menumakanan[i], '\t- Rp', hargamakanan[i])
		print()

		print(18*"=","Menu Minuman",18*"=",)
		for i in range(len(menuminuman)):
		    print(i+1, menuminuman[i], '\t- Rp', hargaminuman[i])
		print()

		print(14*"=","Menu Topping Tambahan",14*"=",)
		for i in range(len(menutoppingtambahan)):
		    print(i+1, menutoppingtambahan[i], '\t- Rp', hargatoppingtambahan[i])


		#inputan untuk memilih menu makanan/minuman/topping tambahan
		# Tipe Data Integer dan 
		print()
		Pembeli = input("Nama Pembeli	   :")
		kasir = input("Nama Kasir   	   :")
		pesanan=input("Take away/ditempat :")

		print()
		for i in range(len(menumakanan)):
			print("nomor ke ", str(i+1))
			try :
				a = int(input("Masukkan nomor makanan :"))
				if a >=1 :
					print()
				try:
					b = input("lagi (y/n)	? : ")
					if b == "y" :
						print()
					elif b == "n" :
						print()
						break
				except ValueError:
					print("kesalahan dalam penginputan \nsilahkan masukan huruf !")	
			except ValueError :
				print("kesalahan dalam penginputan \nsilahkan masukan angka !")
		porsi_makanan = int(input("Masukan jumlah porsi :"))

		print()
		for i in range(len(menuminuman)):
			print("nomor ke ", str(i+1))
			try :
				c = int(input("Masukkan nomor minuman :"))
				if c >=1 :
					print()
				try:
					d = input("lagi (y/n)	? :")
					if d == "y" :
						print()
					elif d == "n" :
						print()
						break
				except ValueError :
					print("kesalahan dalam penginputan \nsilahkan masukan huruf !")	
			except ValueError :
				print("kesalahan dalam penginputan \nsilahkan masukan angka !")
		porsi_minuman = int(input("Masukan Jumlah Porsi\t        : "))


		print()
		for i in range(len(menutoppingtambahan)):
			print("nomor ke ", str(i+1))
			try :
				e = int(input("Masukkan nomor topping tambahan :"))
				if e >=1 :
					print()
				try:
					f = input("lagi (y/n)	? :")
					if f == "y" :
						print()
					elif f == "n" :
						print()
						break
				except ValueError :
					print("kesalahan dalam penginputan \nsilahkan masukan huruf !")	
			except ValueError :
				print("kesalahan dalam penginputan \nsilahkan masukan angka !")
		porsi_topping= int(input("Masukan Jumlah Porsi\t        : "))

		print()
		print(50*"=")
		print()


		#untuk menghitung 
		# Program Operator 
		print("Nomor makanan  :",a)   
		print("Porsi makanan  :",porsi_makanan)
		print("Nomor minuman  :",c)
		print("Porsi minuman  :",porsi_minuman)
		print("Nomor topping  :",e)
		print("Porsi topping  :",porsi_topping)


		harga_total = (hargamakanan[a-1]*porsi_makanan) + (hargaminuman[c-1]*porsi_minuman) + (hargatoppingtambahan[e-1]*porsi_topping)
		print('\nHarga Total Pesanan\t	:Rp', harga_total)
		uang_dibayarkan = int(input("Uang Pembayaran\t		:Rp "))
		print()
		print("Kembalian anda\t		:Rp", uang_dibayarkan-harga_total)
		print()
		cetak_struk = input("Ingin mencetak struk? (y/t):")

		#cetak struk
		if cetak_struk == "y":
				print()
				print(50*"=")
				print("            S T R U K   P E M B E L I A N           ") 
				print("                   ~Ramen Iciraku~                  ") 
				print(50*"=")
				# print(f"Today's date: {today}")
				import time;
				localtime = time.asctime( time.localtime(time.time()) )
				print( localtime)
				print ('Nama Kasir   	  :',kasir)
				print ('Nama Pembeli	  :',Pembeli)
				print ('pesanan			:',pesanan)
				print ('Menu yang dipesan\t:')
				print ('=> Makanan          :X',porsi_makanan,menumakanan[a-1])
				print ('=> Minuman          :X',porsi_minuman,menuminuman[c-1])
				print ('=> Topping Tambahan :X',porsi_topping,menutoppingtambahan[e-1])
				print ('')
				print ('=> Total            :Rp',harga_total )
				print ('=> Uang             :Rp', uang_dibayarkan)
				print ('=> Kembalian        :Rp', uang_dibayarkan-harga_total)
				print ()
				print(50*"=")
				print ('          Terima Kasih Telah Berkunjung       ')
				print ('                di Ramen Iciraku               ')
				print(50*"=")
				print ()
		a=("\nwaktu                   :{}\nNama Kasir		:{}\nNama Pembeli		:{}\npesanan	:{}\nMakanan		        :{}\nPorsi Makanan	        :{}\nMinuman		        :{}\nPorsi Minuman	        :{}\nTopping tambahan	:{}\nPorsi topping	        :{}\nTotal			:{}\nUang			:{}\nKembalian		:{}\n".format(localtime,kasir,Pembeli,pesanan,menumakanan[a-1],porsi_makanan,menuminuman[c-1],porsi_minuman,menutoppingtambahan[e-1],porsi_topping,harga_total,uang_dibayarkan,uang_dibayarkan-harga_total))
		y=open("laporan.txt","a")
		y.write(a)
		y.close()
		back=input("kembali (y/t):")
		if back == "y":
			print("")
			pilih
		else :
			exit()

def laporanharian():
	print("		::::::::L A P O R A N  P E N J U A L A N::::::::	")
	print(50*"=")
	print("             LAPORAN HASIL PENJUALAN        ") 
	print(50*"=")
	o=open("laporan.txt","r")
	p=o.read()
	print(p)
	o.close()

	back=input("kembali (y/t):")
	if back == "y":
		print("")
		pilih
	else :
		exit()

def exit():
	print("		::::::::Terimakasih Sudah Berkunjung ::::::::	")
	print("				ke R A M E N   I C I R A K U			")
	exit()

print(50*"=")
print("             Silahkan Login Untuk Masuk        ") 
print(50*"=")

x=2
while x>=2:
	try:
		username=input("\nmasukan username :")
		password=int(input("masukan password :"))
		if password==123:
			print()
			print(18*":","Login User Berhasil",18*":")
			print(25*" ")
			break
			pilih
		else:
			print("\npasword salah !")
	except ValueError:
		print("kesalahan dalam inputan \n Silahkan ulang kembali pasword dengan angka  !")
			
			
pilih=0			
while(pilih<4):
	pilih=menu()
	if(pilih>=4 or pilih ==0 ):
		break
	else:
		if pilih == 1:
			daftarmenu()
		elif pilih == 2:
			kasir()
		elif pilih ==3 :
			laporanharian()
		else:
			print("terimakasih")
	
		
				
