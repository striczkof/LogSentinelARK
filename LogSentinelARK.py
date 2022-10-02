import atexit
import configparser
import time
from sys import exit
from discord_webhook import DiscordWebhook

# Imports end, config variable starts
try:
    # Read config file
    read_config = configparser.ConfigParser()
    read_config.read("LogSentinelARK.ini")
    # General
    runner_name = read_config.get('General', 'name')
    # Discord webhooks
    log_webhook = read_config.get('Webhooks', 'log_webhook')
    ocr_webhook = read_config.get('Webhooks', 'ocr_webhook')
    alert_webhook = read_config.get('Webhooks', 'alert_webhook')
    # Alert settings
    alert_timer = read_config.getint('Alert_Settings', 'alert_seconds')
    alert_count = read_config.getint('Alert_Settings', 'alert_count')
except Exception as e:
    print(type(e).__name__)

# Config variables end, global variables start

# Index for types of alerts
# 0 = Death/destroyed tribe structures
# 1 = Tek sensors
# 2 = Player Kill
# 3 = Player Tame
# Variables for timers
last_alert = [0.0, 0.0, 0.0, 0.0]
alert_counter = [1, 1 , 1, 1]
# Emergency mode variable
emergency_mode = False

# Variables end, functions start

# Send discord message
def send_discord_message(webhook_url, message):
    webhook = DiscordWebhook(url=webhook_url, content=message)
    response = webhook.execute()

# Function to check whether the alert satisfies the timer
def is_time_to_send_alert(alert_type):
    global last_alert
    global alert_counter
    alert_counter[alert_type] += 1
    if time.time() - last_alert[alert_type] <= alert_timer:
        last_alert[alert_type] = time.time()
        if alert_counter[alert_type] >= alert_count:
            return True
        else:
            return False
    else:
        alert_counter[alert_type] = 1
        last_alert[alert_type] = time.time()
        return False

# Log bot stop function
def stop_bot():
    print("Bot stopped")


def say_something(is_good):
    if is_good:
        print('good')
    else:
        print('bad')

# Functions end, main function starts
def main():
    atexit.register(stop_bot)
    print("Bot started")
    send_discord_message(alert_webhook, 'im alerting beep boop')
    say_something(is_time_to_send_alert(0))
    say_something(is_time_to_send_alert(0))
    say_something(is_time_to_send_alert(0))
    say_something(is_time_to_send_alert(0))
    say_something(is_time_to_send_alert(0))
    time.sleep(5.0)
    say_something(is_time_to_send_alert(0))
    say_something(is_time_to_send_alert(0))
    say_something(is_time_to_send_alert(0))

# Main function ends, main function call starts
if __name__ == "__main__":
    main()