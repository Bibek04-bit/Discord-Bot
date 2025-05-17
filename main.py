#discord bot
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
