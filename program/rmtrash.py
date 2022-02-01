# Copyright (C) 2021 By RishabhMusicProject

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from driver.filters import command, other_filters
from driver.decorators import sudo_users_only, errors

downloads = os.path.realpath("program/inme")
raw = os.path.realpath(".")

@Client.on_message(command(["rmd", "temizleme"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **indirilen tüm dosyalar sildi**" 
    else:
        await message.reply_text("❌ **indirilen dosya yok**") 

        
@Client.on_message(command(["rmw", "temizleme"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw)
    if ls_dir:
        for file in os.listdir(raw):
            if file.endswith('.raw'):
                os.remove(os.path.join(raw, file))
        await message.reply_text("✅ **tüm  dosyalar silindi**")
    else:
        await message.reply_text("❌ **dosya bulunamadı**")


@Client.on_message(command(["temizleme"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.raw *.jpg")
        await message.reply_text("✅ **temizleme**")
    else:
        await message.reply_text("✅ **Zaten temizledi**")
