try:
    with open("data_grup2.csv", "r", encoding="utf-8") as file:
        data = file.read()

except UnicodeDecodeError:
    print("UTF-8 decoding failed. Trying ISO-8859-1...")
    with open("data_grup2.csv", "r", encoding="iso-8859-1") as file:
        data = file.read()

import re

cleaned_data = []
for line in data:
    # Hanya menyimpan huruf, angka, spasi, dan tanda baca umum
    cleaned_line = re.sub(r"[^a-zA-Z0-9\s.,!?']", "", line)
    cleaned_data.append(cleaned_line)

with open("data_grup_cleaned.csv", "w", encoding="utf-8") as file:
    file.writelines(cleaned_data)



