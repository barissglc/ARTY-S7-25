import sqlite3 as sql
from cryptography.fernet import Fernet

def loadKey():
    key = open("universal.key","rb").read()
    return key

def Decrypt(encryptSecret):
    key = loadKey()
    fer  = Fernet(key)
    decryptSecret = fer.decrypt(encryptSecret)
    return decryptSecret.decode()


def main():
    conn = sql.connect('welcome.sqlite')
    cursor = conn.cursor()

    cursor.execute('SELECT Kullanici_Adi, Sifre FROM welcome')
    rows = cursor.fetchall()

    for row in rows:
        encrypted_username = row[0]
        encrypted_password = row[1]

        print(f"Şifrelenmiş Kullanıcı Adı: {encrypted_username}")
        print(f"Şifrelenmiş Şifre: {encrypted_password}")

        print()

    conn.close()

if __name__ == "__main__":
    main()
