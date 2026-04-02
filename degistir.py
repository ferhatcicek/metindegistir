import pandas as pd

dosya_adi = "port.txt"
yeni_dosya_adi = "new_port.txt"

# Excel dosyasını oku
df = pd.read_excel('liste.xlsx')

def metin_degistir(dosya_adi, degisimler):
    try:
        # Dosyayı oku ve içeriğini al
        with open(dosya_adi, 'r') as dosya:
            satirlar = dosya.readlines()

        # Her satırı işle
        for i in range(len(satirlar)):
            # Satır başındaki ve sonundaki boşlukları sil
            satirlar[i] = satirlar[i].strip()

            # Satırı boşluklara göre böl
            kelimeler = satirlar[i].split()

            # Her kelimeyi kontrol et
            for j in range(len(kelimeler)):
                # Eğer kelime tam olarak mevcut metinle eşleşiyorsa, kelimeyi yeni metinle değiştir
                if kelimeler[j] in degisimler:
                    kelimeler[j] = degisimler[kelimeler[j]]

            # Satırı yeniden oluştur ve değiştirilmiş satırı dosyaya yaz
            satirlar[i] = ' '.join(kelimeler)

        # Dosyayı yazma modunda aç ve yeni içeriği yaz
        with open(yeni_dosya_adi, 'w') as dosya:
            # Boş satırları sil ve dosyaya yaz
            dosya.writelines(satir + '\n' for satir in satirlar if satir)

        print(f"{dosya_adi} dosyasında metinler değiştirildi.")

    except FileNotFoundError:
        print("Belirtilen dosya bulunamadı.")
    except Exception as e:
        print("Bir hata oluştu:", e)

# Her satırı döngüye al ve değişimleri bir sözlükte sakla
degisimler = {row['eski']: row['yeni'] for _, row in df.iterrows()}
metin_degistir(dosya_adi, degisimler)

