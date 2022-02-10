from json import detect_encoding
from tkinter import *
from PIL import Image,ImageTk
import requests
import API

class MyWeather:
    def __init__(self,root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry('500x500+700+200')  
        self.root.config(bg = '#f5f0e1')

        #=====ICONS==========================

        self.search_icon = Image.open("icons/search.png")
        self.search_icon = self.search_icon.resize((30,30),Image.ANTIALIAS)
        self.search_icon = ImageTk.PhotoImage(self.search_icon)

        #=====VARIABLE========================

        self.var_search=StringVar()

        
        title = Label(self.root,text="Weather App",font=("goudy old style",30,"bold"),bg = "#11052C",fg="#ffc13b").place(x=0,y=0,relwidth=1,height=60)
        
        lbl_city = Label(self.root,text="City Name",font=("Ubuntu",15),bg="#3D087B",fg="White",anchor='w',padx=5).place(x=0,y=60,relwidth=1,height=40)
        
        txt_city = Entry(self.root,textvariable=self.var_search,font=("goudy old style",15),bg="lightyellow",fg="black").place(x=120,y=65,width=300,height=30)
        
        btn_search = Button(self.root,cursor="hand2",image=self.search_icon,bg="#6b7b8c",activebackground="#6b7b8c",bd=0,command=self.get_weather).place(x=450,y=65,width=32,height=32)
        
        
        # ====== FOOTER ==================


        lbl_footer = Label(self.root,text="Developed By Ashutosh",font=("goudy old style",12),bg="#FFE459",fg="black",pady=5).pack(side=BOTTOM,fill=X)
        
        title = Label(self.root,bg = "white").place(x=0,y=100,relwidth=1,height=370)

       
        #=====RESULTS======================
        
        self.lbl_city=Label(self.root,font=("Ubuntu",17),bg="white",fg="green")
        self.lbl_city.place(x=150,y=100,height=40)

        self.lbl_icons=Label(self.root,font=("Ubuntu",17),bg="white")
        self.lbl_icons.place(x=150,y=180,height=100)
        
        self.lbl_temp=Label(self.root,font=("Ubuntu",17),bg="white",fg="orange")
        self.lbl_temp.place(x=150,y=260,height=50)
        
        self.lbl_wind = Label(self.root,font=("Ubuntu",17),bg="white",fg="#262626")
        self.lbl_wind.place(x=150,y=340,height=50)
        
        self.lbl_Error = Label(self.root,font=("Ubuntu",17),bg="white",fg="red")
        self.lbl_Error.place(x=150,y=380,height=50)

    def get_weather(self):
            Api_key=API.Api_key
            complete_url=f"http://api.openweathermap.org/data/2.5/weather?q={self.var_search.get()}&appid={Api_key}"
            if self.var_search.get() == "":
                self.lbl_city.config(text="")
                self.lbl_icons.config(image="")
                self.lbl_temp.config(text="")
                self.lbl_wind.config(text="")
                self.lbl_Error.config(text="Invalid City")
                self.lbl_Error.config(text="City Name Required")
            else:
                result=requests.get(complete_url)
                if result :
                    json=result.json() 
                    city_name=json["name"]
                    country=json["sys"]["country"]
                    icons=json["weather"][0]["icon"]
                    temp_c=json["main"]["temp"]-273.15
                    temp_f=(json["main"]["temp"]-273.15)* 9/5 +32
                    wind=json["weather"][0]["main"]
                    self.lbl_city.config(text=city_name+" , "+country)

                    #=====NEW ICONS==========================
                    self.search_icon2 = Image.open(f"icons/{icons}.png")
                    self.search_icon2 = self.search_icon2.resize((100,100),Image.ANTIALIAS)
                    self.search_icon2 = ImageTk.PhotoImage(self.search_icon2)


                    self.lbl_icons.config(image=self.search_icon2)
                    deg=u"\N{DEGREE SIGN}"
                    self.lbl_temp.config(text=str(round(temp_c,2))+deg+"C |"+str(round(temp_f,2))+deg+"f")
                    self.lbl_wind.config(text=wind)
                    self.lbl_Error.config(text="")
                    
                else:
                    self.lbl_city.config(text="")
                    self.lbl_icons.config(image="")
                    self.lbl_temp.config(text="")
                    self.lbl_wind.config(text="")
                    self.lbl_Error.config(text="Invalid City Name")


root = Tk() 
Object = MyWeather(root)
root.mainloop()    