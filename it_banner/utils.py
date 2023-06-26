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

        w, h = clip.size

        data = some_text

        if len(data) <= 10:
            duration = 2
        elif 10 < len(data) <= 50:
            duration = 3
        else:
            duration = 4

        txt = (TextClip(data, fontsize=50, font='Amiri-regular', color='white').set_duration(duration))
        txt_col = txt.on_color(size=(clip.w + txt.w, txt.h - 10),
                               color=(0, 0, 0), pos=(6, 'center'), col_opacity=0.8)
        txt_mov = txt_col.set_pos(lambda t: (max(w / w, int(w - 0.5 * w * t)),
                                             max(5.4 * h / 6, int(0 * t))))
        final = CompositeVideoClip([clip, txt_mov])
        banner = final.subclip(0, duration).write_videofile("it_banner/media/wgite1.mp4")

        return banner