# Session 5
import random
brands = {
    1: {
        "name": "Cosrx",
        "products": {
            "Cleanser": {"price": 12, "stock": random.randint(0, 250)},
            "Sun Cream": {"price": 20, "stock": random.randint(0, 250)},
            "Micellar Water": {"price": 15, "stock": random.randint(0, 250)}
        }
    },
    2: {
        "name": "Skin1004",
        "products": {
            "Moisturizer": {"price": 18, "stock": random.randint(0, 250)},
            "Oil Cleanser": {"price": 12, "stock": random.randint(0, 250)},
            "Ampoule": {"price": 25, "stock": random.randint(0, 250)}
        }
    },
    3: {
        "name": "Round Lab",
        "products": {
            "Sunscreen": {"price": 23, "stock": random.randint(0, 250)},
            "Moisturizer": {"price": 22, "stock": random.randint(0, 250)},
            "Toner": {"price": 20, "stock": random.randint(0, 250)}
        }
    },
    4: {
        "name": "Anua",
        "products": {
            "Cleansing Oil": {"price": 19, "stock": random.randint(0, 250)},
            "Cleansing Foam": {"price": 15, "stock": random.randint(0, 250)},
            "Toner": {"price": 22, "stock": random.randint(0, 250)}
        }
    },
    5: {
        "name": "Manyo",
        "products": {
            "Essence": {"price": 28, "stock": random.randint(0, 250)},
            "Cleansing Oil": {"price": 22, "stock": random.randint(0, 250)},
            "Serum": {"price": 35, "stock": random.randint(0, 250)}
        }
    },
    6: {
        "name": "Some By Mi",
        "products": {
            "Cream": {"price": 17, "stock": random.randint(0, 250)},
            "Toner": {"price": 15, "stock": random.randint(0, 250)},
            "Serum": {"price": 25, "stock": random.randint(0, 250)}
        }
    },
    7: {
        "name": "Mixsoon",
        "products": {
            "Essence": {"price": 28, "stock": random.randint(0, 250)},
            "Cleansing Foam": {"price": 15, "stock": random.randint(0, 250)},
            "Cream": {"price": 32, "stock": random.randint(0, 250)}
        }
    },
    8: {
        "name": "Beauty of Joseon",
        "products": {
            "Sunscreen": {"price": 16, "stock": random.randint(0, 250)},
            "Eye Cream": {"price": 28, "stock": random.randint(0, 250)},
            "Essence": {"price": 25, "stock": random.randint(0, 250)}
        }
    },
    9: {
        "name": "Tirtir",
        "products": {
            "Serum": {"price": 30, "stock": random.randint(0, 250)},
            "Ampoule": {"price": 35, "stock": random.randint(0, 250)},
            "Cream": {"price": 28, "stock": random.randint(0, 250)}
        }
    },
    10: {
        "name": "Innisfree",
        "products": {
            "Clay Mask": {"price": 15, "stock": random.randint(0, 250)},
            "Sun Serum": {"price": 20, "stock": random.randint(0, 250)},
            "Cream": {"price": 25, "stock": random.randint(0, 250)}
        }
    }
}
def notavailable():
  print("\nMohon maaf saat ini brand tidak tersedia, silahkan input brand yang terdaftar")
def invoice(items, qtys, brands):
  total = brands[brand]["products"][item]['price'] * qty
  print("\nInvoice")
  print(f"Produk: {item}")
  print(f"Harga: ${brands[brand]['products'][item]['price']}")
  print(f"Jumlah: {qty}")
  print(f"Total harga: ${round(total, 2)}")
  money_paid = float(input("\nMasukkan jumlah uang yang dibayar: $"))
  if money_paid == total:
    print(f"Uang pas, Terima kasih telah berbelanja!")
    menu = int(input("\nMenu: \n 1. Tampilkan produk \n 2. Lakukan pembelian \n 3. Pilih brand lain \n 4. Keluar dari aplikasi \n Ketik (1/2/3/4): "))
  elif money_paid > total:
    change = money_paid - total
    print(f"Uang kembalian: ${round(change, 2)}")
    menu = int(input("\nMenu: \n 1. Tampilkan produk \n 2. Lakukan pembelian \n 3. Pilih brand lain \n 4. Keluar dari aplikasi \n Ketik (1/2/3/4): "))
  else:
    print("Uang yang dibayar tidak mencukupi")
    if total - money_paid > 0:
      print(f"Uang yang kurang: ${round(total - money_paid, 2)}")
      cont = input("\nApakah Anda ingin melanjutkan transaksi? Yes/No: ")
      while cont.lower == "yes" or "no":
        if cont.lower() == "yes":
          money_extra = float(input("Masukkan jumlah uang yang ditambahkan: $"))
          money_total = money_paid + money_extra
          print(f"Total uang: ${money_total}")
          if money_total == total:
            print(f"Uang pas, Terima kasih telah berbelanja!")
            menu = int(input("\nMenu: \n 1. Tampilkan produk \n 2. Lakukan pembelian \n 3. Pilih brand lain \n 4. Keluar dari aplikasi \n Ketik (1/2/3/4): "))
            break
          elif money_total > total:
            changes = money_total - total
            print(f"Uang kembalian: ${round(changes, 2)}")
            menu = int(input("\nMenu: \n 1. Tampilkan produk \n 2. Lakukan pembelian \n 3. Pilih brand lain \n 4. Keluar dari aplikasi \n Ketik (1/2/3/4): "))
            break
          else:
            print("Uang masih tidak cukup, silahkan berbelanja di lain waktu \nTerima kasih")
            menu = int(input("\nMenu: \n 1. Tampilkan produk \n 2. Lakukan pembelian \n 3. Pilih brand lain \n 4. Keluar dari aplikasi \n Ketik (1/2/3/4): "))
            break
        elif cont.lower() == "no":
          print("Terima kasih")
          menu = int(input("\nMenu: \n 1. Tampilkan produk \n 2. Lakukan pembelian \n 3. Pilih brand lain \n 4. Keluar dari aplikasi \n Ketik (1/2/3/4): "))
          break
        else:
          print("Respon tidak valid, mohon coba lagi")
          cont = input("\nApakah Anda ingin melanjutkan transaksi? Yes/No: ")
print("Welcome to K-commerce! \nSelamat memborong K-skincare! \nSilahkan pilih brand skincare yang ingin dibeli: \n 1. Cosrx \n 2. Skin1004 \n 3. Round Lab \n 4. Anua \n 5. Manyo \n 6. Some By Mi \n 7. Mixsoon \n 8. Beauty of Joseon \n 9. Tirtir \n 10. Innisfree \n K-skincare apa yang anda cari?")
brand = int(input("Silahkan pilih brand skincare yang ingin dibeli (1-10): "))
while brand < 1 or brand > 10:
  notavailable()
  brand = int(input("Silahkan pilih brand skincare yang ingin dibeli (1-10): "))
else:
    print(f"\nWelcome to {brands[brand]['name']} \nSelamat berbelanja!")
    menu = int(input("\nMenu: \n 1. Tampilkan produk \n 2. Lakukan pembelian \n 3. Pilih brand lain \n 4. Keluar dari aplikasi \n Ketik (1/2/3/4): "))
    while True:
      if menu < 1 or menu > 4:
        print("\nMenu yang Anda pilih tidak tersedia, mohon dicoba lagi")
        menu = int(input("\nMenu: \n 1. Tampilkan produk \n 2. Lakukan pembelian \n 3. Pilih brand lain \n 4. Keluar dari aplikasi \n Ketik (1/2/3/4): "))
      else:
        if menu == 1:
          print("\nDaftar Produk:")
          for product, details in brands[brand]["products"].items():
            print(f"- {product}: ${details['price']} | Stok: {details['stock']}")
          menu = int(input("\nMenu: \n 1. Tampilkan produk \n 2. Lakukan pembelian \n 3. Pilih brand lain \n 4. Keluar dari aplikasi \n Ketik (1/2/3/4): "))
        elif menu == 2:
          print("\nPembelian:")
          item = (input("Silahkan tulis barang yang Anda inginkan: "))
          item = item.title()
          if item in brands[brand]["products"]:
            qty = int(input("Silahkan masukkan jumlah barang yang Anda inginkan: "))
            if qty <= brands[brand]["products"][item]["stock"]:
              invoice(item, qty, brands)
              break
            else:
              print("\nMohon maaf, stok barang tidak mencukupi \nAnda bisa melihat stok yang tersedia pada bagian menu tampilkan produk terlebih dahulu \nTerima kasih")
              menu = int(input("\nMenu: \n 1. Tampilkan produk \n 2. Lakukan pembelian \n 3. Pilih brand lain \n 4. Keluar dari aplikasi \n Ketik (1/2/3/4): "))
          else:
            print("\nMohon maaf, produk yang Anda inginkan tidak tersedia")
        elif menu == 3:
          print("\nSilahkan pilih brand skincare yang ingin dibeli: \n 1. Cosrx \n 2. Skin1004 \n 3. Round Lab \n 4. Anua \n 5. Manyo \n 6. Some By Mi \n 7. Mixsoon \n 8. Beauty of Joseon \n 9. Tirtir \n 10. Innisfree \n K-skincare apa yang anda cari?")
          brand = int(input("Silahkan pilih brand skincare yang ingin dibeli (1-10): "))
        else:
          print("\nTerima kasih telah menggunakan K-commerce! \nMenutup aplikasi...")
          break
          quit()