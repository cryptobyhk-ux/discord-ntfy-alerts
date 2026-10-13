# Discord → ntfy Alert Bot

Jab bhi Discord server ke kisi channel me naya message aata hai, ye bot
**ntfy** topic par ek notification trigger karta hai. Message ka text **nahi**
parhta — sirf trigger (isliye Discord ke koi privileged intent nahi chahiye).

## Kaam kaise karta hai

`on_message` event → ntfy topic par POST:
`#channel (Server) me naya message - by @user.`

## Env vars

| Var | Required | Default |
|---|---|---|
| `DISCORD_TOKEN` | yes | — |
| `NTFY_TOPIC` | no | `inspired-analyst-alerts-7cbe9834` |
| `NTFY_SERVER` | no | `https://ntfy.sh` |

ntfy par topic "banane" ka koi button nahi hota — bot ka pehla trigger hi
topic bana deta hai. Members ntfy app (Play Store) me usi topic name ko
subscribe kar lein; pehli notification aate hi sab live.

## Koyeb (free) par deploy

1. Koyeb me GitHub se login karo, **Create Service → GitHub** se ye repo select karo.
2. Builder: **Buildpack**, Run command: `python bot.py` (Procfile bhi mojood hai).
3. Instance: **Nano** (free tier), region apni marzi.
4. Env vars me `DISCORD_TOKEN` (bot token) aur `NTFY_TOPIC` set karo → Deploy.
5. Logs me `Logged in as ...` nazar aaye to bot live hai.

## Bot ko Discord server me add karna

Invite URL (CLIENT_ID apne bot ka daalo, Discord Developer Portal → Application):

```
https://discord.com/oauth2/authorize?client_id=CLIENT_ID&scope=bot&permissions=0
```

Koi privileged intent on karne ki zaroorat nahi.
