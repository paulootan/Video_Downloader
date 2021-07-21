import pytube
link = input("Enter Youtube Link Here >> ") #enter link here
SAVE_PATH = "D:\"                          #file path comment edited
yt = pytube.YouTube(link) #link is the  web url of youtube video
stream = yt.streams.first()
stream.download(SAVE_PATH) 




