import time
from datetime import datetime
import socket

import pychromecast

def play(mc, volume, path):
    mc.play_media(path, 'audio/mp3')
    mc.block_until_active()
    mc.pause()
    time.sleep(0.5)
    ghome.set_volume(volume)
    time.sleep(1)
    mc.play()
    while not mc.status.player_is_idle:
        time.sleep(1)
    mc.stop()

ghome_ip = '192.168.0.26'
mp3_ip = '192.168.1.3'

time_str = datetime.now().strftime("%I")

ghome = pychromecast.Chromecast(ghome_ip)
ghome.wait()

volume = ghome.status.volume_level
ghome.set_volume(0)

mc = ghome.media_controller

play(mc, volume, 'http://{}/hours/mp3/intro.mp3'.format(mp3_ip))
play(mc, volume, 'http://{}/hours/mp3/{}.mp3'.format(mp3_ip, time_str))

ghome.quit_app()
