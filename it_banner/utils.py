import moviepy
from moviepy.editor import *
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip

import logging

logger = logging.getLogger(__name__)


def make_banner(some_text: str):
    clip = (VideoFileClip('it_banner/media/white.mp4', audio=False)
            .subclip(0, 5)
            .speedx(0.7)
            .fx(vfx.colorx, 0.7))

    data = some_text

    if len(data) <= 10:
        w, s, st = 100, 150, 100
        duration = 2
    elif 10 < len(data) <= 50:
        w, s, st = 300, 200, 300
        duration = 3
    else:
        w, s, st = 400, 270, 400
        duration = 4

    txt = (TextClip(data, fontsize=140, font='arial', color='white').set_duration(duration))
    txt_mov = moviepy.video.fx.all.scroll(txt, h=150, w=w, x_speed=s, y_speed=0, x_start=st, y_start=200)
    # txt_col = txt.on_color(size=(clip.w + txt.w, txt.h - 10),
    #                        color=(0, 0, 0), pos=(0, 'center'), col_opacity=0.8)
    # txt_mov = txt_col.set_pos(lambda t: (max(1, int(w - 0.5 * w * t)),
    #                                      max(5.4 * h / 6, int(0 * t))))
    txt_mov1 = txt_mov.set_pos('center')
    final = CompositeVideoClip([clip, txt_mov1], size=[400, 400])
    banner = final.subclip(0, duration).write_videofile("it_banner/media/wgite1.mp4")

    return banner