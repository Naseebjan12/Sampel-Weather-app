from tkinter import *
import requests
import json
window= Tk()

def weather():
    city = q.get()
    url = f"http://api.weatherapi.com/v1/current.json?key=b1254569109744b781291028232803&q={city}"
    r = requests.get(url)
    wdic = json.loads(r.text)
    temp_c = wdic['current']['temp_c']
    temp_f = wdic['current']['temp_f']
    cloud = wdic['current']['cloud']
    w_direction=wdic['current']['wind_dir']
    # print(temp_c)
    # print(temp_f)
    # for temp in celsius
    c_temp = Label(text=f'temperature in celcius is {temp_c}', bg='light blue')
    c_temp.place(x=120, y=130)
    # for temp in farnheit
    f_temp = Label(text=f'temperature in Farnheit is {temp_f}', bg='light blue')
    f_temp.place(x=120, y=170)
    # pressure
    p = Label(text=f'clouds percantage {cloud}', bg='light blue')
    p.place(x=120, y=200)
    # wind
    w = Label(text=f'wind direction is {w_direction}', bg='light blue')
    w.place(x=120, y=230)


# changing the color of the window
window.config(bg='light blue')
window.title('Weather App By Naseeb jan')
window.minsize(width=400,height=300)
window.maxsize(width=400,height=300)
window.resizable(False,False)
# label for user
label=Label(text='Search for any city: ',bg='light blue')
label.place(x=150,y=20)
# entry for the city
q=Entry(width=30,font=('arial',12))
q.place(x=70,y=60)
# button to search for the weather
labe=Label(text='',bg='light blue')
labe.pack()
btn=Button(text='Search Weather',width=20,bg='light blue',command=weather)
btn.place(x=120,y=90)



window.mainloop()