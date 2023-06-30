import moviepy.editor as mpy
from moviepy.editor import *
from vectortween.Mapping import Mapping

import logging

logger = logging.getLogger(__name__)


def make_banner(some_text):
    video_file = mpy.VideoFileClip('it_banner/media/white.mp4')
    duration = 3
    video_width, video_height = video_file.size
    textclip = mpy.TextClip(some_text, color='black', align='center', fontsize=100, font='Ubuntu-bold',
                            method='label', bg_color='transparent')
    textclip_width, textclip_height = textclip.size

    desired_final_x = 400
    desired_final_y = 0

    def position(t):
        return Mapping.linlin(t, 0, duration, desired_final_x, 0 - textclip_width), desired_final_y

    add_text = textclip.set_position(position).set_duration(duration)
    final = mpy.CompositeVideoClip([video_file, add_text], size=[400, 400])
    video = final.subclip(0, duration).write_videofile("it_banner/media/wgite1.mp4")
    return video

