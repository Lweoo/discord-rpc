import rpc
import time
from time import mktime

print("Demo for python-discord-rpc Adobe illustrator")
client_id = '870045374335828029'  # Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = mktime(time.localtime())
while True:
    activity = {
            "state": "Playing on play.pika-network.net",  # anything you like
            "details": "Solo",  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "",  # anything you like
                "small_image": "badlion-logo",  # must match the image key
                "large_text": "",  # anything you like
                "large_image": "badlion-logo"  # must match the image key
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(900)
