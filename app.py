import asyncio
from telegram import Bot
from telegram.ext import Application
import schedule
import time

# Bot tokeni ve grup kimliği
BOT_TOKEN = '7164667892:AAFNZIaXzWrscAySnECUpreTeyNW4sUDfJ8'
GROUP_ID = '-1002426296728'  # Grubunuzun chat ID'sini buraya ekleyin

# Telegram botu başlat
app = Application.builder().token(BOT_TOKEN).build()

# Hatırlatıcı mesajı gönderme fonksiyonu
async def send_reminder():
    message = """Dikkat ⚠️

Grubumuzda admin olmayan ve özelden size ulaşan kişilere karşı dikkatli olunuz. Bilinmeyen kaynaklardan gelen talepleri dikkate almayınız.


Takipte Kal
@paraloper 

Yapay Zeka Haber Algoritması
@premiumtraderhaber 

Yapay Zeka Kripto Al Sat Botu
@coinradarofficialbot

Güncel piyasa haberleri için takipte kalın!
"""
    await app.bot.send_message(chat_id=GROUP_ID, text=message)
    print("Hatırlatma mesajı gönderildi.")

# schedule modülünü asenkron bir yapıya dönüştüren fonksiyon
async def run_scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)  # 1 saniye bekle

# Programın ana işlevi
async def main():
    # Bot başlar başlamaz deneme mesajı gönder
    await send_reminder()

    # Her 32 saatte bir mesaj gönderme zamanlaması
    schedule.every(32).hours.do(lambda: asyncio.create_task(send_reminder()))
    await run_scheduler()

# Ana döngüyü başlatır
asyncio.run(main())
