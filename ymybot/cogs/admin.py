# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2020, Yazılımcıların Mola Yeri (ymydepo)
#

import copy
import asyncio
import subprocess

from cogs.utils import checks

# from cogs.utils import emoji

from discord.ext import commands
import discord


class Admin(commands.Cog):
    """The description for Admin goes here."""

    def __init__(self, bot):
        self.bot = bot

    async def run_process(self, command):
        try:
            process = await asyncio.create_subprocess_shell(
                command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            result = await process.communicate()
        except NotImplementedError:
            process = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            result = await self.bot.loop.run_in_executor(None, process.communicate)

        return [output.decode() for output in result]

    @checks.is_owner()
    @commands.command(aliases=[], hidden=True)
    async def load(self, ctx, *, module):
        try:
            self.bot.load_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f"{e.__class__.__name__}: {e}")
        else:
            await ctx.send("Ok !")

    @checks.is_owner()
    @commands.command(aliases=[], hidden=True)
    async def unload(self, ctx, *, module):
        try:
            self.bot.unload_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f"{e.__class__.__name__}: {e}")
        else:
            await ctx.send("Ok !")

    @checks.is_owner()
    @commands.command(aliases=[], hidden=True)
    async def reload(self, ctx, *, module):
        try:
            self.bot.reload_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f"{e.__class__.__name__}: {e}")
        else:
            await ctx.send("Ok !")

    @commands.command(aliases=[], hidden=True)
    async def off(self, ctx):
        await ctx.send("Ok !")
        await self.bot.logout()

    @checks.is_owner()
    @commands.command(aliases=[], hidden=True)
    async def do(self, ctx, times: int, *, command):
        msg = copy.copy(ctx.message)
        msg.content = ctx.prefix + command

        new_ctx = await self.bot.get_context(msg, cls=type(ctx))

        for i in range(times):
            await new_ctx.reinvoke()

    @checks.is_owner()
    @commands.command(aliases=[], hidden=True)
    async def shell(self, ctx, *, command):
        async with ctx.typing():
            stdout, stderr = await self.run_process(command)

        if stderr:
            text = f"stdout:\n{stdout}\nstderr:\n{stderr}"
        else:
            text = stdout

        await ctx.send(f"```Output:\n\n{text}```")


def setup(bot):
    bot.add_cog(Admin(bot))