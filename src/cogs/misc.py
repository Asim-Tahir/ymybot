# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2020, Yazılımcıların Mola Yeri (ymy-discord)
#

import time

from cogs.utils import emoji

import discord
from discord.ext import commands


class Misc(commands.Cog):
    """The description for Misc goes here."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["gecikme"])
    async def ping(self, ctx):
        """ Gecikme süresini hesaplar """
        before = time.monotonic()
        message = await ctx.send("Pinging...")

        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"{emoji.pong} Pong! `{int(ping)}`ms")


def setup(bot):
    bot.add_cog(Misc(bot))