# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2020, Yazılımcıların Mola Yeri (ymy-discord)
#

import config
from cogs.utils import role
from cogs.utils import emoji as e

from discord.ext import commands
from discord.utils import get
import discord


class Events(commands.Cog):
    """The description for Events goes here."""

    def __init__(self, bot):
        self.bot = bot

    def get_emoji(self, emoji):
        if emoji.id == None:
            return e.unicode_to_name(emoji)
        else:
            return emoji.id

    def get_role(self, guild, emoji):
        return get(guild.roles, name=role.roles[str(emoji)])

    # Bu kodlara el atılacak. Asıl fonksiyonlar utils altına alınacak.

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild_id = payload.guild_id
        channel_id = payload.channel_id
        message_id = payload.message_id
        user_id = payload.user_id
        emoji = payload.emoji

        if guild_id == config.ymy_guild_id:
            if (
                channel_id == config.reaction_role_channel_id
                and message_id in config.reaction_role_message_ids
            ):
                guild = self.bot.get_guild(id=guild_id)
                user = guild.get_member(user_id)

                try:
                    role = self.get_role(guild, self.get_emoji(emoji))
                    await user.add_roles(role)
                    await user.send(f"`{role}` adlı rol alındı!")

                except KeyError:
                    channel = self.bot.get_channel(channel_id)
                    message = await channel.fetch_message(message_id)
                    await message.remove_reaction(emoji=emoji, member=user)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        guild_id = payload.guild_id
        channel_id = payload.channel_id
        message_id = payload.message_id
        user_id = payload.user_id
        emoji = payload.emoji

        if guild_id == config.ymy_guild_id:
            if (
                channel_id == config.reaction_role_channel_id
                and message_id in config.reaction_role_message_ids
            ):
                guild = self.bot.get_guild(id=guild_id)
                user = guild.get_member(user_id)

                try:
                    role = self.get_role(guild, self.get_emoji(emoji))
                    await user.remove_roles(role)
                    await user.send(f"`{role}` adlı rol bırakıldı!")

                except KeyError:
                    pass


def setup(bot):
    bot.add_cog(Events(bot))
