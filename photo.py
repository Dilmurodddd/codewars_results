from PIL import Image, ImageDraw, ImageFont
import pandas as pd

class JPG:

    def __init__(self, csv_file, output_file, font_size=20, image_size=(1200, 600)):  # O'lchamni kattalashtirish
        # CSV faylini o'qish
        self.csv_file = csv_file
        self.output_file = output_file
        try:
            df = pd.read_csv(csv_file)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return
    
        # Yangi rasmni yaratish (yuksak sifatli rasm)
        img = Image.new('RGB', image_size, color=(255, 255, 255))  # Oq fon
        draw = ImageDraw.Draw(img)
    
        # Fontni yuklash (Yuqori sifatli fontni tanlash)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)  # Arial fonti
        except:
            font = ImageFont.load_default()  # Agar Arial mavjud bo'lmasa, defaultni ishlatish
    
        # Matn uchun joy belgilash
        x, y = 10, 10  # Boshlang'ich koordinatalar
        line_height = font_size + 10  # Chiziqlar orasidagi masofa
    
        # Sarlavhalarni yozish
        headers = list(df.columns)
        for col in headers:
            draw.text((x, y), col, fill="black", font=font)  # Sarlavhalarni yozish
            x += 250  # Har bir ustunni 250px qilib o'zgartiring (ko'proq joy berish uchun)
    
        # Yangi satrga o'tish
        x = 10
        y += line_height
    
        # Ma'lumotlarni yozish
        for _, row in df.iterrows():
            for cell in row:
                draw.text((x, y), str(cell), fill="black", font=font)  # Har bir katakni yozish
                x += 300  # Har bir ustun o'rtasiga 250px qo'yish
            x = 10  # Yangi satrga o'tish
            y += line_height
    
            # Agar rasmning balandligi o'tib ketgan bo'lsa, to'xtatish
            if y > image_size[1] - 20:
                print("Warning: Data exceeds image height. Not all rows are included.")
                break
    
        # Rasmni saqlash (JPG formatida, sifatni oshirish)
        try:
            img.save(output_file, quality=95)  # 95% sifat bilan JPG formatida saqlash
            print(f"Image saved as {output_file}")
        except Exception as e:
            print(f"Error saving image: {e}")
    
    # Misol uchun
    # csv_file = r"python_0_daily.csv"  # CSV fayl manzili
    # output_file = r"output.jpg"   # Chiqish JPG fayl manzili
    # jpg(csv_file, output_file)
