import sqlite3 as sql
from cryptography.fernet import Fernet
import pickle

def loadKey():
    with open("universal.key", "rb") as f:
        key1, key2 = pickle.load(f)
        # datakeys = f.read().splitlines()
        # print(datakeys[0])
        # key1 = bytes(datakeys[0], 'utf-8')
        # key2 = bytes(datakeys[1], 'utf-8')

    # key1 = open("universal.key", "rb").readline()
    # key2 = open("universal.key", "rb").readline() 
    print(key1)
    print(key2)
    return key2,key1


def Decrypt(encryptSecret, input):
    key1,key2 = loadKey()
    if input == 1:
        fer1 = Fernet(key1)
        decryptSecret = fer1.decrypt(encryptSecret)
        return decryptSecret.decode()
    elif input == 2:
        fer2 = Fernet(key2)
        decryptSecret = fer2.decrypt(encryptSecret)
        return decryptSecret.decode()

def main():
    conn = sql.connect('welcome.sqlite')
    cursor = conn.cursor()

    cursor.execute('SELECT Kullanici_Adi, Sifre FROM welcome')
    rows = cursor.fetchall()

    for row in rows:
        encrypted_username = row[0]
        encrypted_password = row[1]

        # Şifrelenmiş veriyi çöz
        decrypted_username = Decrypt(encrypted_username,1)
        decrypted_password = Decrypt(encrypted_password,2)

        print(f"Kullanıcı Adı: {decrypted_username}")
        print(f"Şifre: {decrypted_password}")

        print()

    conn.close()

if __name__ == "__main__":
    main()
