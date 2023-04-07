import youtube_dl
from youtube_dl.utils import DownloadError

ydl = youtube_dl.YoutubeDL()

def get_video_info(url):
    ydl_opts = {
        'extractor': 'generic',
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'verbose': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(
                url,
                download=False
            )
        except DownloadError:
            return None
        except KeyError:
            result = {}
    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # Just a video
        video = result
    
    return video


def get_audio_url(video_info):
   for f in video_info['formats']:
       if f['ext'] == 'm4a':
           return f['url']
       
    

if __name__ == '__main__':
    video_info = get_video_info("https://www.youtube.com/watch?v=Zak0XAGVm4c")
    url = get_audio_url(video_info)
    print(url)
    


