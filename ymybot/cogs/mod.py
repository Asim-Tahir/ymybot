# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2020, Yazılımcıların Mola Yeri (ymydepo)
#

from discord.ext import commands
import discord


class Mod(commands.Cog):
    """The description for Mod goes here."""

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Mod(bot))
