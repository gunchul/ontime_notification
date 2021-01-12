# alarm

On-time notification 

## Sound

Example:
```
python tts.py
```

## Playing

Example:
```
python hours.py
```

## On-time notification

crontab -l
```
# m h  dom mon dow   command
0 * * * * (cd /home/pi/www/hours; ./hours.sh)
```
