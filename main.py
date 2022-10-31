# Asumsi terdapat 15 menu barang pada vending machine

# Mengetahui barang yang tersedia
from menu import harga, menu, item_id
print("----------Menu Minuman yang Tersedia----------\n\n")

for i in item_id:
    print(f"Item ID: {item_id[i]} --- Menu: {menu[i]} --- Harga: {harga[i]}")


# fungsi untuk cara kerja mesin
def machine(item_id, jalan, barang):
    sisa_uang = total_uang
    while jalan == True :

        beli = int(input("\nTekan tombol produk yang anda inginkan: "))

        if beli < len(item_id):
          if sisa_uang >= harga[beli]:
            barang.append(menu[beli])
            harga_barang.append(harga[beli])
            sisa_uang -= harga[beli]
            print(f"Minuman yang Anda beli = {menu[beli]}. Sisa uang Anda adalah {sisa_uang}.")
            more_items = str(input("Tekan tombol apa pun untuk melanjutkan pembelian atau tekan Done untuk menyelesaikan transaksi .. "))
          else: 
            print(f"Sisa uang tidak mencukupi. Sisa uang anda adalah {sisa_uang}.")
            more_items = "Done"

        if more_items == "Done":
          jalan = False
          selesai = int(input(("Cetak struk transaksi? 1. Ya 2. Tidak .. ")))
          if selesai == 1:
            print(create_reciept(barang, reciept))
          elif selesai == 2:
            print("Terima kasih atas pembelian Anda. ")
          
# fungsi untuk pembuatan struk transaksi
def create_reciept(barang, reciept):

    for i in range (0, len(barang)):
        reciept += f"""
        \t{barang[i]} -- {harga_barang[i]}
        """

    reciept += f"""
        \tTotal --- {sum(harga_barang)}
        
        """
    return reciept


# inisialisasi
total_uang = 0
run = 0
jalan = True
barang = []
harga_barang = []

reciept = """
\tNAMA BARANG -- HARGA
"""

# untuk memasukkan uang
print("Masukkan uang anda dan tekan Lanjut jika telah selesai ..")
while run == 0 :
  # input yang diterima berupa string 
  # input berupa nominal uang akan terus ditambahkan pada total uang
  # input berupa "Lanjut" akan diteruskan ke pembelian barang
  masuk = str(input("user:  "))
  # untuk filter input berupa uang
  if masuk == "5000" or masuk == "10000" or masuk == "20000" or masuk == "50000" or masuk == "100000":
    if int(masuk) >= 5000 :
      total_uang += int(masuk)
  elif masuk == "Lanjut":
    break

# untuk pembelian barang
machine(item_id, jalan, barang)
