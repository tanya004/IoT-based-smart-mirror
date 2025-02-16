from tkinter import *
from time import sleep
import news, weather
import datetime
import webbrowser

newsUrl = None
class MyFrame:
    i = 0
    weatherInfo = None
    newsInfo = None

    def __init__(self, parent):

        self.parent = parent
        self.parent.title("Smart Mirror")

        self.myContainer = Frame(parent)
        self.myContainer.pack(fill=BOTH, expand= True)

        self.loadData()
        self.initGUI()

    def dataInit(self):
        global weatherInfo
        global newsInfo

        weatherInfo = GetWeatherInfo.__init__()
        newsInfo = GetNewsInfo.__init__()


    def loadData(self):
        self.dataInit()

        # DataSetting
        # TimeInfo
        self.time = datetime.datetime.now().strftime('%Y %m %d %H:%M')
        # WeatherInfo
        self.weather = weather.getData()
        # NewsInfo
        self.newsInfo = news.getData()
        

    def initGUI(self):

        self.frameTitle = Frame(self.myContainer, background="black")
        self.frameTitle.pack(fill=X)

        lbltime = Label(self.frameTitle, text=self.time, width=20, foreground='white',
                        background='black', font = "Helvetica 35 bold")
        lbltime.pack(side=TOP, padx=10, pady=10)

        # Title
        self.frameTime = Frame(self.myContainer, background="black")
        self.frameTime.pack(fill=BOTH)

        lblWeatherInfo = Label(self.frameTime, text="<Bangalore Weather Today>", width=30, foreground='white',
                               background='black', font = "Helvetica 16 bold")
        lblWeatherInfo.pack(side=LEFT, padx=10, pady=10)


        self.frameStation = Frame(self.myContainer, background="black")
        self.frameStation.pack(fill=BOTH, expand=True)

        #Temperature
        lblTemperature = Label(self.frameStation, text=" Temperature : " + self.weather[0], width=16, foreground='white',
                               background='black', font = "Helvetica 16 bold")
        lblTemperature.pack(side=LEFT, padx=50, pady=2)

        self.frameStationNum = Frame(self.myContainer, background="black")
        self.frameStationNum.pack(fill=X)

        # Weather Info
        lblWeather = Label(self.frameStationNum, text=" Weather : " + self.weather[1], width=16, foreground="#ffffff",
                           background="black", font = "Helvetica 16 bold")
        lblWeather.pack(side=LEFT, padx=50, pady=2)

        self.frameCityName = Frame(self.myContainer, background="black")
        self.frameCityName.pack(fill=BOTH, expand=True)

        #City name 
        lblCityName = Label(self.frameCityName, text="Bangalore", width=18, foreground='white', background='black', font = "Helvetica 16 bold")
        lblCityName.pack(side=RIGHT, padx=10, pady=8)
        
        # Rainfall
        lblRainfall = Label(self.frameCityName, text=" Rainfall : " + self.weather[2], width=16, foreground='white',
                            background='black', font = "Helvetica 16 bold")
        lblRainfall.pack(side=LEFT, padx=50, pady=2)

        #News 
        for i in range(len(self.newsInfo[0])):
            self.frameNews = Frame(self.myContainer, background="black")
            self.frameNews.pack(fill=X)
            plusNewsTitleInfo(self.frameNews, self.newsInfo[0][i], self.newsInfo[1][i])


#Weather forecast 
def plusNewsTitleInfo(frame, txtNewsTitle, txtNewsUrl):
    newsUrl = txtNewsUrl
    lblNewsTitle = Label(frame, text=txtNewsTitle, width=40, foreground="#ffffff", background='black', font = "Helvetica 16 bold")
    lblNewsTitle.pack(side=LEFT, padx=5, pady=5)
    lblNewsTitle.bind("<Button-1>",lambda event, text=newsUrl: callback(event,newsUrl))


def callback(event, text):
    webbrowser.open_new(text)
    webbrowser.attributes('-fullscreen', True)

def main():
    root = Tk()
 
    root.geometry("1080x920+900+500")
    root.attributes('-fullscreen', True)
    app = MyFrame(root)
    app.loadData()
    app.initGUI()
   # root.update_idletasks()
    #root.update()
    #sleep(1)
    #app.myContainer.destroy()



 #   while True:
 #       app = MyFrame(root)
  #      app.loadData()
   #     app.initGUI()
    #    root.update_idletasks()
     #   root.update()
     #   sleep(1)
      #  app.myContainer.destroy()

    root.mainloop()

if __name__ == '__main__':
    main()
