import json
import math
import os
import tabulate
import uuid
import datetime
import sys
import tabulate
import textwrap
import itertools


# Importing function
sys.path.insert(0, "..")
from enque import Queue
sys.path.insert(0, "..")
from jenis_lisensi import license_main
sys.path.insert(0, "..")
from enstack import Stack

p = Stack()
q = Queue()

def menu():
    print("Menu Lisensi:")
    print("0.Menampilkan lisensi")
    print("1.Mengkontrak lisensi ")
    print("2.Cek Aktivasi lisensi ")
    print("3.Menonaktifkan lisensi ")
    print("4.Search")
    print("5.Sort")
def choice():
        choice=int(input('Enter menu choice: '))
        os.system('cls')
        return choice
# Data Structure

# 1.Struct
''' License.json'''
# 2.Linked List
'''Prosesi pemasukan dan penghapusan'''
# 3.Queue
'''Pemasukan data lisensi'''
# 4.Stack
'''Pemasukan data layer lisensi'''
# 5.Search Operation ( Linear Search )
def linear_search(arr, size , search): 
    for item in arr:
        if item.get(size) == search:
            return item
# 6.Sorting Operation ( Bubble Sort  )
def bubbleSort(data,search):
    arr = data['license_data']
    size = len(arr)
    for i in range(size):
        swapped = False
        for j in range(0, size - i - 1):
            # Membandingkan spesifik json data
            if arr[j][search] > arr[j + 1][search]:
                # Swap jika elemen yang ditemukan lebih besar daripada pointer selanjutnya
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Jika keduanya tidak lebih besar atau kecil, list sudah di swap
        if not swapped:
            break
    return data

# Displaying output to be a Table
def display_table(data):
    
    hasil = data['license']
    
    wrapped_desc = textwrap.fill(hasil['desc'], width=40)

    table_data = [
        [
            data['id'], data['name'], data['type_of_subscribe'] ,data['aktivasi_token'], data['activated_at'], data['expires_at'], data['active'],
        ]
    ]

    headers = [
        "Id", "Name", "TypeOfSubscribe", "TypeOffLicense", "AktivasiToken", 
        "ActivatedAt", "ExpiresAt", "Active", "LicenseType", "LicenseDesc", 
        "LicenseBy", "LicenseSa", "LicenseNc", "LicenseNd"
    ]

    table = tabulate.tabulate(table_data, headers=headers, tablefmt="grid")

    print(table)
# Wrapping each data
def wrap_text(text, width=60):
    return "\n".join(textwrap.wrap(text, width=width))

def option0():
    with open('data.json', 'r') as file:
        hasil = json.load(file)
        item = hasil["license_data"]
        table_data = [
            [
                data['id'], data['name'], data['type_of_subscribe'] ,data['aktivasi_token'], data['activated_at'], data['expires_at']
            ]
            for data in item
        ]

        headers = [
            "Id", "Name", "TypeOfSubscribe", "TypeOffLicense", "AktivasiToken", 
            "ActivatedAt", "ExpiresAt"
        ]

        table = tabulate.tabulate(table_data, headers=headers, tablefmt="grid")

        print(table)
def option1():
 while True:
        name = str(input("Masukkan namamu: "))
        token = str(uuid.uuid4())

        with open('license.json', 'r') as file:
            data = json.load(file)
            licenses = data['license']

            table_data = [
                [license['id'], license['name'], wrap_text(license['desc']), ', '.join(license['type'])]
                for license in licenses
            ]

            headers = ["ID", "Name", "Description", "Type"]
            print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))

        license_type = int(input("Pilih Lisensi yang ingin kamu gunakan [hanya berupa angka!]: "))

        if license_type > 6:
            print("Pilihan diluar opsi")
            continue

        subs = input("Pilih Tipe Berlangganan[Trial/Subscribe/Forever]: ")

        if subs == 'Trial':
            trial_v = 7
            current_trial = datetime.datetime.now()
            expiration_trial = current_trial + datetime.timedelta(days=trial_v)
            activated = current_trial
            expired = expiration_trial
            active = True

        elif subs == 'Subscribe':
            subscribe_v = 30
            current_subs = datetime.datetime.now()
            expiration_subs = current_subs + datetime.timedelta(days=subscribe_v)
            activated = current_subs
            expired = expiration_subs
            active = True

        elif subs == 'Forever':
            forever_v = 36500
            current_forever = datetime.datetime.now()
            expiration_forever = current_forever + datetime.timedelta(days=forever_v)
            activated = current_forever
            expired = expiration_forever
            active = True

        else:
            print("Input salah")
            continue

        license_data = license_main(license_type)  

        unified_data = {
            "name": name,
            "type_of_subscribe": subs,
            "type_off_license": license_type,
            "aktivasi_token": token,
            "activated_at": activated.strftime("%Y-%m-%d %H:%M:%S"),
            "expires_at": expired.strftime("%Y-%m-%d %H:%M:%S"),
            "active": active,
            "license": None  
        }

        q.enqueue(
            name=unified_data["name"],
            subs=unified_data["type_of_subscribe"],
            license_type=unified_data["type_off_license"],
            activated=unified_data["activated_at"],
            expired=unified_data["expires_at"],
            token=unified_data["aktivasi_token"],
            active=unified_data["active"],
            license=unified_data['license']  
        )

        p.enstack(*license_data)  

        license_details = p.peek()  

        if input("Input again? (yes/no): ").strip().lower() != 'yes':
            break
def option2():
    search =str(input("Masukkan tokenmu:"))
    with open('data.json', 'r') as file:
        data = json.load(file)
        wow=data['license_data']
        
    for aktivasi_data in wow: 
        kadaluarsa = datetime.datetime.strptime(aktivasi_data['expires_at'], "%Y-%m-%d %H:%M:%S")
        sekarang = datetime.datetime.now() 
        if aktivasi_data['aktivasi_token'] == search:
            if sekarang > kadaluarsa:
                aktivasi_data['active'] = False
                name =aktivasi_data['name']
                print(f"{name} trial has expired. Deactivating account.")
            else:
                name =aktivasi_data['name']
                print(f"{name} trial is still active.") 
            break
    
def option3():
    search = input("Masukkan tokenmu:")
    data  = json.load(open("data.json", 'r' ))
    new1 = data['license_data']
    for item in new1:
        if item.get('aktivasi_token') == search:
            new1.remove(item)
            break
    with open('data.json', 'w') as f:
        json.dump(data, f)

def option4():
    with open('data.json','r') as f:
        data =json.load(f)
    if 'license_data' in data:
        wow = data['license_data']
        x1 = str(input('Masukkan Nama yang ingin kamu cari:'))
        result = linear_search(wow, 'name' ,x1)
        if result == None :
            print("Not found")
        else :
            display_table(result)
def option5():
    with open('data.json','r' ) as f:
        data = json.load(f)
        result=bubbleSort(data,'name')
        print(json.dumps(result, indent=4))
# Menu
def main():
    menu()
    pilihan= choice()
    if pilihan == 0:
        option0()
    elif pilihan == 1:
        option1()
    elif pilihan ==2:
        option2()
    elif pilihan == 3:  
        option3()
    elif pilihan == 4:
        option4()
    elif pilihan == 5:
        option5()
    else :
        "Diluar pilihan"
if __name__=='__main__':
    pilihan2=""
    while pilihan2 != 'quit':
        main()
        pilihan2=str(input('Done?: '))
        if pilihan2=='yes' or pilihan2=='ya'or pilihan2=='y' :
            pilihan2='quit'
        elif pilihan2== 'no' or pilihan2=='n':
            pass