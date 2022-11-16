from pytube import YouTube

link = "#coloque o link da página do seu video aqui#"

youtube = YouTube(link)

print("titulo:" + youtube.title)

res_youtube_max = youtube.streams.get_highest_resolution()

res_youtube_max.download()