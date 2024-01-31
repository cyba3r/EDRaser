import sqlite3
import base64

XOR_KEY = 0xFF

def decrypt_data(data_xored_b64: bytes):
        data_b64 = bytes([c ^ XOR_KEY for c in data_xored_b64]).decode()
        try:
            decoded_data = base64.b64decode(data_b64).decode('unicode_escape')
        except:
            decoded_data = base64.b64decode(data_b64).decode()
        return decoded_data


con = sqlite3.connect("evilSignatures.db")
cur = con.cursor()
count = 1
for row in cur.execute("SELECT data_xored_b64,Affected_EDR from EvilSignature"):
    zeile=decrypt_data(row[0])
    print(f"'{zeile}'")
    with open(f"./dump/{row[1]}_{count}","+w") as f:
        f.write(zeile)
    f.close()
    count+=1
