import json
from yt_extractor import get_audio_url, get_video_info
from api import save_transcript

def save_vedio_sentiments(url):
    vedio_info=get_video_info(url)
    audio_url=get_audio_url(vedio_info)
    print(audio_url)
    title=vedio_info['title']
    title=title.strip().replace('','_')
    title="data/" + title
    save_transcript(audio_url, title, sentiment_analysis=True)


if __name__=="__main__":
    #save_vedio_sentiments("https://www.youtube.com/watch?v=Zak0XAGVm4c")
    with open('data/sentiment.json','r') as f:
        data=json.load(f)

    positive=[]
    negative=[]
    nuetral=[]

    for result in data:
        text=result['text']
        if result['sentiment']=="NEUTRAL":
            nuetral.append(text)
        elif result['sentiment']=="POSITIVE":
            positive.append(text)
        elif result['sentiment']=="NEGATIVE":
            negative.append(text)

    len_pos=len(positive)
    len_neg=len(negative)
    len_nue=len(nuetral)

    print("Nuetral" ,len_nue)
    print("Possitive", len_pos)
    print('Negative', len_neg)

    r= len_pos/(len_pos+len_neg)

    print("Positive Ratio", r)

