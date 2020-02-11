
import audio_processing
import command_parser
import numpy as np

my_audio = audio_processing.audio_main()
print(my_audio)
command_parser.main('image',my_audio)
