#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
from pathlib import Path
import argparse
import numpy as np
from pydub import AudioSegment
from moviepy.editor import AudioFileClip, VideoClip


def generate_white_noise_video(output, width, height, fps, duration):
    output_path = Path(output)
    audio_without_video = str(output_path.with_name(output_path.parent.resolve().stem + "_without_video.mp3"))

    # Create white noise video
    def make_frame(t):
        return np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

    video = VideoClip(make_frame, duration=duration)
    video = video.set_fps(fps)

    # Create white noise audio
    audio_sample_rate = 44100
    audio_data = np.random.uniform(-1, 1, size=(duration * audio_sample_rate,)) * 32767
    audio_data = audio_data.astype(np.int16)
    AudioSegment(audio_data.tobytes(), frame_rate=audio_sample_rate, sample_width=2, channels=1).export(audio_without_video, format="mp3")

    # Combine video and audio
    audio = AudioFileClip(audio_without_video)
    final_video = video.set_audio(audio)
    final_video.write_videofile(output, codec='libx264', audio_codec='aac')

    # Clean up temporary files
    os.remove(audio_without_video)


def main():
    parser = argparse.ArgumentParser(description="Generate a white noise video with audio.")
    parser.add_argument("-o", "--output", type=str, default="white_noise_video.mp4", help="Output video file path.")
    parser.add_argument("-w", "--width", type=int, default=640, help="Video width.")
    parser.add_argument("-t", "--height", type=int, default=480, help="Video height.")
    parser.add_argument("-f", "--fps", type=int, default=30, help="Video frames per second.")
    parser.add_argument("-d", "--duration", type=int, default=10, help="Video duration in seconds.")

    args = parser.parse_args()

    generate_white_noise_video(args.output, args.width, args.height, args.fps, args.duration)


if __name__ == "__main__":
    main()
