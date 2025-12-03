import psutil
import logging
import time
import asyncio
from telegram import Bot

# Thay thế bằng mã token bot của bạn
BOT_TOKEN = '8335872033:AAEFkZ7mTTUjbLBaDBVs-B0K4arVl7My6bY'
# Thay thế bằng chat_id của bạn
CHAT_ID = '-5098653020'

# Cấu hình logging
logging.basicConfig(level=logging.INFO, filename="system_monitor_bot.log",
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Hàm ghi log
def log_info(category, message):
    logger.info(f"{category}: {message}")
    print(f"{category}: {message}")

# Hàm gửi tin nhắn Telegram
async def send_telegram_message(message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)

# Hàm giám sát CPU và RAM
def monitor_cpu_memory():
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    log_info("CPU", f"Usage: {cpu_percent}%")
    log_info("Memory", f"Usage: {memory_info.percent}%")
    # Gửi thông báo Telegram
    message = f"CPU Usage: {cpu_percent}%\nMemory Usage: {memory_info.percent}%"
    asyncio.run(send_telegram_message(message))

# Hàm giám sát tổng thể
def monitor_system():
    log_info("System Monitor", "Starting system monitoring ...")
    while True:
        monitor_cpu_memory()
        log_info("System Monitor", "Monitoring cycle completed.\n")
        time.sleep(60)  # Lặp lại mỗi phút

if __name__ == "__main__":
    monitor_system()