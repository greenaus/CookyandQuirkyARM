
import audio_processing
import gcode_generator
import numpy as np

my_audio = audio_processing.audio_main()
print(my_audio)
gcode_generator.main('image',my_audio)
