import configparser
import time
from discord_webhook import DiscordWebhook

temp_url = ''
# Configs
try:
    read_config = configparser.ConfigParser()
    read_config.read("LogSentinelARK.ini")
    runner_name = read_config.get('General', 'name')
    temp_url = read_config.get('Webhooks', 'alert_webhook')
    runner_name = read_config.get('General', 'names')
except Exception as e:
    print(type(e).__name__)


# Variables for timers
last_alert = [0.0, 0.0, 0.0, 0.0]
alert_counter = [1, 1 , 1, 1]

def send_discord_message(webhook_url, message):
    webhook = DiscordWebhook(url=webhook_url, content=message)
    response = webhook.execute()

def is_time_to_send_alert(alert_type):
    global last_alert
    global alert_counter
    alert_counter[alert_type] += 1
    if time.time() - last_alert[alert_type] <= 3:
        last_alert[alert_type] = time.time()
        if alert_counter[alert_type] >= 3:
            return True
        else:
            return False
    else:
        alert_counter[alert_type] = 1
        last_alert[alert_type] = time.time()
        return False

def say_something(is_good):
    if is_good:
        print('good')
    else:
        print('bad')

send_discord_message(temp_url, 'u gay')

say_something(is_time_to_send_alert(0))
say_something(is_time_to_send_alert(0))
say_something(is_time_to_send_alert(0))
say_something(is_time_to_send_alert(0))
say_something(is_time_to_send_alert(0))
time.sleep(5.0)
say_something(is_time_to_send_alert(0))
say_something(is_time_to_send_alert(0))
say_something(is_time_to_send_alert(0))