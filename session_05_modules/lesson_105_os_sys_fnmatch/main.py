# https://ffmpeg.org/

"""
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt -map v:a -map 1:0 -ss 00:00:00 -to 00:00:10 "SAIDA"
"""

import fnmatch
import os
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'

# Aula não terminada
