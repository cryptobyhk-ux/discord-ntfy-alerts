"""Discord -> ntfy alert bot.

Jab bhi server ke kisi channel me naya message aata hai, ye bot
ntfy topic par ek notification trigger karta hai. Message ka text
NAHI parhta, sirf trigger bhejta hai (isliye koi privileged
Discord intent nahi chahiye).

Env vars:
    DISCORD_TOKEN  - bot token (required)
    NTFY_TOPIC     - ntfy topic name (default: inspired-analyst-alerts-7cbe9834)
    NTFY_SERVER    - ntfy server (default: https://ntfy.sh)
"""

import asyncio
import os
import urllib.request

import discord

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", "").strip()
NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "inspired-analyst-alerts-7cbe9834").strip()
NTFY_SERVER = os.environ.get("NTFY_SERVER", "https://ntfy.sh").rstrip("/")

# Default intents only - NO privileged intents (no message content, no members, no presence).
intents = discord.Intents.default()
client = discord.Client(intents=intents)


def send_ntfy(title: str, message: str) -> None:
    """Publish one notification to the ntfy topic (blocking; run in a thread)."""
    req = urllib.request.Request(
        f"{NTFY_SERVER}/{NTFY_TOPIC}",
        data=message.encode("utf-8"),
        headers={"Title": title, "Tags": "speech_balloon"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"ntfy -> HTTP {resp.status}", flush=True)
    except Exception as exc:  # never let a failed push kill the bot
        print(f"ntfy failed: {exc}", flush=True)


@client.event
async def on_ready() -> None:
    print(f"Logged in as {client.user} (id: {client.user.id})", flush=True)
    print(
        f"Watching {len(client.guilds)} server(s); notifying ntfy topic '{NTFY_TOPIC}'",
        flush=True,
    )


@client.event
async def on_message(message: discord.Message) -> None:
    # Apne ya doosre bots ke messages par trigger nahi - loop se bachao.
    if message.author.bot:
        return
    guild = message.guild.name if message.guild else "Direct Message"
    channel = getattr(message.channel, "name", "DM")
    text = f"#{channel} ({guild}) me naya message - by {message.author}."
    await asyncio.to_thread(send_ntfy, "Discord Alert", text)


if __name__ == "__main__":
    if not DISCORD_TOKEN:
        raise SystemExit("DISCORD_TOKEN env var missing - bot token set karo.")
    client.run(DISCORD_TOKEN)
