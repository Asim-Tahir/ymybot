# -*- coding: utf-8 -*-
#
# Copyright (C) 2019, Yazılımcıların Mola Yeri (ymy-gitrepo)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import config

from discord.ext import commands
import discord


"""
async def check_guild_permissions(ctx, perms, *, check=all):
    is_owner = await ctx.bot.is_owner(ctx.author)
    if is_owner:
        return True

    if ctx.guild is None:
        return False

    resolved = ctx.author.guild_permissions
    return check(getattr(resolved, name, None) == value for name, value in perms.items())
"""


def is_owner():
    def predicate(ctx):
        return ctx.message.author.id in config.owner_ids

    return commands.check(predicate)


def is_admin():
    def predicate(ctx):
        return ctx.message.author.id in config.admin_ids

    return commands.check(predicate)


def is_mod():
    def predicate(ctx):
        return ctx.message.author.id in config.mod_ids

    return commands.check(predicate)
