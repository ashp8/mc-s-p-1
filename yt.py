import subprocess
import os, glob, shutil


class YoutubeDownloader(object):
    def __init__(self, url=""):
        print("Enter URL: ")
        self.url = input() # take youtube link from user
        self.runcommand()  # run the youtube-dl -F link command
        self.q = input()   # take the format code from the user


    def runcommand(self): # run command function
        self.data = subprocess.run(['youtube-dl', '-F', self.url])
        print(self.data.stdout)

    def downloadAudio(self): # downloads audio
        self.audio = subprocess.run(['youtube-dl', '-f', '140', self.url])
        print(self.audio)

    def downloadVideo(self): # downloads video
        self.video = subprocess.run(['youtube-dl', '-f', self.q, self.url])
        print(self.video)

    def managedir(self): #mangages video dir in the system
        if(os.path.exists('video')):
            shutil.rmtree("video")
        os.mkdir('video')
        os.chdir('video');

    def merge(self): # merge the video audio file
        file = glob.glob("*mp4")
        audio = glob.glob("*m4a")
        self.log = subprocess.run(
            ['ffmpeg', '-i', file[0], '-i', audio[0], '-c:v', 'copy', file[0].replace('mp4', 'mkv')])

    def move(self): #mv the mkv file in the system
        final = glob.glob("*mkv")
        subprocess.run(['mv', final[0], "/outdir/"])


ls = YoutubeDownloader();ls.managedir();ls.downloadAudio();ls.downloadVideo();ls.merge()
ls.move()
