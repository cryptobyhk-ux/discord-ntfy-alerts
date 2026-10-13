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

## Render (free) par deploy

1. Render dashboard me GitHub se login karo, **New + → Web Service** se ye repo select karo.
   (Free tier me Worker service nahi milta, isliye Web Service + neeche wala health endpoint.)
2. Build command: `pip install -r requirements.txt`, Start command: `python bot.py`.
3. Instance type: **Free**. `PORT` env Render khud set karta hai.
4. Env vars me `DISCORD_TOKEN` (bot token) aur `NTFY_TOPIC` set karo → Deploy.
5. Logs me `Logged in as ...` nazar aaye to bot live hai.

> Note: bot.py me `/` par ek chhota health endpoint hai. Render free services
> 15 min ki khamoshi ke baad so jati hain — is URL ko har 5 min me ping karte
> raho (koi bhi free uptime monitor ya cron) taake bot 24/7 jaagta rahe.
> 750 free hours/month ek mahine ke liye kaafi hain (~720-744h).

## Bot ko Discord server me add karna

Invite URL (CLIENT_ID apne bot ka daalo, Discord Developer Portal → Application):

```
https://discord.com/oauth2/authorize?client_id=CLIENT_ID&scope=bot&permissions=0
```

Koi privileged intent on karne ki zaroorat nahi.
