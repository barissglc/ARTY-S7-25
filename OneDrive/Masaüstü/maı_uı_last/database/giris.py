import sqlite3 as sql
import datetime
from cryptography.fernet import Fernet
import pickle

# Fernet ile kullanılacak anahtar
anahtar = Fernet.generate_key()
cipher_suite = Fernet(anahtar)

anahtar2 = Fernet.generate_key()
sifreleyici_2 = Fernet(anahtar2)

def generate_key_file():
    with open("universal.key", "wb") as key_file:
        pickle.dump([anahtar, anahtar2], key_file)
        # print(type(anahtar))
        # key_file.writelines(str(anahtar, 'utf-8') +  "\n")
        # key_file.writelines(str(anahtar2,'utf-8'))
        

def create_database():
    conn = sql.connect('welcome.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS welcome (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Kullanici_Adi TEXT NOT NULL,
            Sifre TEXT,
            Tarih TEXT     
        )
    ''')
    conn.commit()
    conn.close()

def kullanici_ekle(Kullanici_Adi, Sifre, Tarih):
    conn = sql.connect('welcome.sqlite')
    cursor = conn.cursor()

    # Şifreyi Fernet ile şifreleme
    sifre_sifrele = cipher_suite.encrypt(Sifre.encode())
    Kullanici_Adi = sifreleyici_2.encrypt(Kullanici_Adi.encode())

    cursor.execute('INSERT INTO welcome (Kullanici_Adi, Sifre, Tarih) VALUES (?, ?, ?)', (Kullanici_Adi, sifre_sifrele, Tarih))
    conn.commit()
    conn.close()

def main():
    generate_key_file()
    create_database()
    try:
        while True:
            Kullanici_Adi = input("Kullanici Adınızı girin: ")
            Sifre = input("Şifrenizi girin: ")

            Tarih = datetime.date.today()
            formatli_tarih = Tarih.strftime("%d/%m/%Y")
            print("Bugünün tarihi:", formatli_tarih)
            
            kullanici_ekle(Kullanici_Adi, Sifre, formatli_tarih)
            print("Kullanıcı bilgileri veritabanına kaydedildi.")
           
    except KeyboardInterrupt:
        print("\nİşlem sona erdi.")

if __name__ == "__main__":
    main()
