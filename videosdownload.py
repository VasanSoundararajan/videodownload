import pytube

# importing pytube
key = input("enter a key word to search:")
# key word to download that may be link
# try to import search from google
try:
    from googlesearch import search
# if error in it it should not show error
except:
    importError: print("no module named 'google' found")
# searching for videos
print("\n searching for youtube videos...\n")
try:
    I = []
    for j in search(key, tld="co.in", num=50, stop=50, pause=2):
        if 'https://www.youtube.com/watch' in j:
            print("WE Found THE VIDEO \n DOWNLOADING THE VIDEO")
            I.append(j)
            if I != []:
                pathvideo = input('<save_path_goes_here>')
                print('Video Found')
                youtube = pytube.YouTube(j)
                video = youtube.streams.get_highest_resolution()
                flna = video.title + '.mp4'
                video.download(pathvideo, flna)
                print('\n' + video.title + 'has been downloaded !')
                break
# if key is not found then else print sorry message
        else:
            print("SORRY , unable to get that video or playlist")
# if the google is not import then expect for error in above code
except:
    print("Sorry , unable to get that video or playlist")
