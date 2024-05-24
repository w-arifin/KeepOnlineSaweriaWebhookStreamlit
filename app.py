import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

discord_webhook_url = "https://discord.com/api/webhooks/1241035350181286062/HCurocljFrzWCuy95QumP80Vn-pLH5piD41K3PKKtJldBQmPzw4om_MXj7Lg6s4C_8sf"

def send_discord_message(content):
    payload = {
        "content": content
    }
    response = requests.post(discord_webhook_url, json=payload)
    if response.status_code == 204:
        print("Message sent to Discord successfully!")
    else:
        print("Failed to send message to Discord. Status code:", response.status_code)

@app.route('/')
def home():
    return 'Welcome to the webhook server!', 200

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        
        # Contoh memproses dan mencetak informasi dari JSON
        version = data.get('version')
        created_at = data.get('created_at')
        donation_type = data.get('type')
        amount_raw = data.get('amount_raw')
        donator_name = data.get('donator_name')
        message = data.get('message')
        
        # Konversi amount_raw dari string ke integer dan format
        amount_raw = int(amount_raw)
        formatted_amount = f"{amount_raw:,}".replace(",", ".")
        
        # Cetak informasi yang diproses
        print(f"Version: {version}")
        print(f"Created At: {created_at}")
        print(f"Donation Type: {donation_type}")
        print(f"Amount: {formatted_amount}")
        print(f"Donator Name: {donator_name}")
        print(f"Message: {message}")
        
        # Kirim pesan ke Discord
        content = f"New donation received!\nDonator: {donator_name}\nAmount: {formatted_amount}\nMessage: {message}"
        send_discord_message(content)
        
        response = {
            "status": "success",
            "data": data
        }
        return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
