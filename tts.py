import os
from gtts import gTTS

dir = 'mp3'
hours = ["한시", "두시", "세시", "네시", "다섯시", "여섯시", "일곱시", "여덟시", "아홉시", "열시", "열한시", "열두시"]

os.makedirs(dir, exist_ok=True)

for i, hour in enumerate(hours):
    tts = gTTS(hour, lang='ko')
    fname = '{}/{:02}.mp3'.format(dir, i+1)
    tts.save(fname)