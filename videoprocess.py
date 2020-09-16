from moviepy.editor import *
import base64
import srbynetease

class Video_model():
    def __init__(self, name, video_full_path,start_time,end_time):
        self.name = name
        self.video_full_path=video_full_path,
        self.start_time=start_time,
        self.end_time=end_time

    def get_audio_base64(self):
        video_clip=VideoFileClip(self.video_full_path).subclip(self.start_time,self.end_time)
        audio=video_clip.audio
        result_path=self.video_full_path.split('.')[0]+'_clip.mp3'
        audio.write_audiofile(result_path)
        audio_base64 = base64.b64encode(open(result_path,'rb').read()).decode('utf-8')
        return audio_base64

    def do_sr(self):
        audio_base64=self.get_audio_base64()
        sr_result=srbynetease.connect(audio_base64)
        print(sr_result)
        if sr_result['errorCode']=='0':
            return sr_result['result']
        else:
            return "Something wrong , errorCode:"+sr_result['errorCode']
