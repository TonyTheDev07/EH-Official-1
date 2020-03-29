import discord
import os
import json
from discord.ext import commands, tasks
import random
import discord
from discord.ext import commands
from datetime import datetime
import colorsys
import asyncio
from itertools import cycle

client = commands.Bot(command_prefix =commands.when_mentioned_or("`"))



@client.event
async def on_ready():
    activity = discord.Activity(name='Tony And K!ng', type=discord.ActivityType.listening)
    await client.change_presence(status=discord.Status.dnd, activity=activity)
    print("Bot is ready to use :-) ")



@client.command()
async def printroles(ctx):
    listofroles = []
    for role in ctx.message.guild.roles:
        listofroles.append(role.name)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    embed = discord.Embed(title="List of Guild Roles", description=str(listofroles), color = discord.Color((r << 16) + (g << 8) + b))

    await ctx.send(embed=embed, delete_after=60)


@client.command(aliases=["es"])
async def embedsay(ctx, heading, *, message):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    embed = discord.Embed(title= heading, description=message, color = discord.Color((r << 16) + (g << 8) + b))
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command()
async def dm(ctx, member: discord.Member, message):
    user = client.get_user(member.id)
    try:
            await user.send(message)
            await ctx.send("DM Sent To : {}".format(member), delete_after=5)
    except:
            await ctx.send("DM can't Sent To : {}".format(member), delete_after=5)
    pass


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked.')
    
@client.command()
@commands.has_permissions(mute_members=True)
async def mute(self, ctx, member: discord.Member, *, reason=None):
    await member.mute(reason=reason)
    await ctx.send(f'User {member} has been muted.')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'user {member} has vanished!')

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
    if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.mention}')
    return
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(self, ctx, ammount=2):
    await ctx.channel.purge(limit=ammount)

@client.command(aliases=["echo"])
async def say(self, ctx, *, words):
    await ctx.send(words)
    await ctx.delete_after(delay='0.1')




client.run('Njc1NTg4NzUzMTg3Nzk5MDQx.XoCXbg.7Ha7BwSDRh6jvXuMQbiHNvAI6W8')
