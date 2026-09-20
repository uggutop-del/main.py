import os
import random
import asyncio
import discord
from discord.ext import tasks, commands

# 1. ดึง Token จาก Railway Environment Variable
BOT_TOKEN = os.getenv("BOT_TOKEN")


# ⚠️ เปลี่ยนตัวเลขตรงนี้ให้เป็น Channel ID จริงใน Discord ของคุณ (ไม่มีเครื่องหมายคำพูด)
CHANNEL_ID = 11543974302175465502

# ข้อมูลไข่ในแมพ Ride a Pet / Steal an Egg
EGGS = [
    {"name": "Cherub Egg", "rarity": "Ethereal", "rate": "1/2,500", "color": 0xFFD700},
    {"name": "Black Hole Egg", "rarity": "Void", "rate": "1/10,000", "color": 0x301934},
    {"name": "Dragon Egg", "rarity": "Cosmic", "rate": "1/1,000", "color": 0xFF4500},
    {"name": "Yeti Egg", "rarity": "Snow", "rate": "1/500", "color": 0x00FFFF}
]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ ล็อกอินสำเร็จในชื่อ: {bot.user}")
    if not spawn_loop.is_running():
        spawn_loop.start()

@tasks.loop(minutes=3)
async def spawn_loop():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        egg = random.choice(EGGS)
        embed = discord.Embed(
            title="🥚 ไข่สุ่มเกิดแล้ว!",
            description=f"**ประเภท:** {egg['name']}\n**ระดับ:** {egg['rarity']}\n**อัตราสุ่ม:** {egg['rate']}",
            color=egg["color"]
        )
        embed.set_footer(text="Ride a Pet / Steal an Egg Notifier")
        await channel.send(content="@everyone", embed=embed)
    else:
        print(f"⚠️ ไม่พบช่องแชท ID: {1543974302175465502} (กรุณาเช็ค ID ช่องแชทอีกครั้ง)")

@spawn_loop.before_loop
async def before_spawn():
    await bot.wait_until_ready()

if __name__ == "__main__":
    if not BOT_TOKEN:
        print("❌ Error: ไม่พบค่า BOT_TOKEN ใน Railway Variables!")
    else:
      bot.run(BOT_TOKEN)

