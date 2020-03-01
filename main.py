
import audio_processing
import gcode_generator
import numpy as np

my_audio = audio_processing.audio_main()
g_code = gcode_generator.main('sound',my_audio)
