import tkinter
import requests

def download(link):

    downloads = []

    #download = requests.get(link)
    #print(download.url)
    #open("Download.exe", 'wb').write(download.content)

    for program in downloads:
        download = requests.get(link)
        open("Download.exe", 'wb').write(download.content)
        
window = tkinter.Tk()
window.title("Program Downloader")
window.geometry('300x250')

var1 = tkinter.IntVar()
check_select = tkinter.Checkbutton(text="Discord", variable=var1, command= lambda: download("https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86"))
check_select.pack()

var2 = tkinter.IntVar()
check_select = tkinter.Checkbutton(text="Steam", variable=var2, command= lambda: download("https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe"))
check_select.pack()

var3 = tkinter.IntVar()
check_select = tkinter.Checkbutton(text="Spotify", variable=var3, command= lambda: download("https://download.scdn.co/SpotifySetup.exe"))
check_select.pack()

var4 = tkinter.IntVar()
check_select = tkinter.Checkbutton(text="Firefox", variable=var4, command= lambda: download("https://www.mozilla.org/en-US/firefox/download/thanks/"))
check_select.pack()

var5 = tkinter.IntVar()
check_select = tkinter.Checkbutton(text="VSCode", variable=var5, command= lambda: download("https://code.visualstudio.com/download#"))
check_select.pack()

var6 = tkinter.IntVar()
check_select = tkinter.Checkbutton(text="CoreTemp", variable=var6, command= lambda: download("https://www.alcpu.com/CoreTemp/Core-Temp-setup.exe"))
check_select.pack()

var7 = tkinter.IntVar()
check_select = tkinter.Checkbutton(text="Github", variable=var7, command= lambda: download("https://central.github.com/deployments/desktop/desktop/latest/win32"))
check_select.pack()

var8 = tkinter.IntVar()
check_select = tkinter.Checkbutton(text="Python 3.11.5", variable=var8, command= lambda: download("https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"))
check_select.pack()

window.mainloop()