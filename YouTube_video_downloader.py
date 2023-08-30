
from pytube import YouTube

link = input("Lütfen video linkini giriniz :")

yt = YouTube(link)
yr = yt.streams.get_highest_resolution()

print("Videonuz indiriliyor lütfen bekleyiniz . . .")

wait = 1

for i in range(3):
    print("".format(wait))
    wait += 1

yr.download()

print("Video başarılı bir şekilde indirildi .")
