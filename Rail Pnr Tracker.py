import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as font
import requests , json


win = tk.Tk()
win.title("PNR Stutas Checker")
win.iconbitmap('download.ico')
win.geometry('1000x1000')
win.maxsize(width=950 ,height=500)
win.minsize(width=950 ,height=500)
win.config(bg='blue')
heading_font = font.Font(family='Helvetica')
heading_size = font.Font(size=30)


Heading = ttk.Label(win, text = "PNR STATUS CHECKER" ,background='DARKSALMON' , borderwidth=2, relief="groove")
Heading['font']= heading_font
Heading['font'] = heading_size
Heading.grid(row=0,columnspan=4,padx = 255)

lEnter_pnr = ttk.Label(win,text='Enter PNR Number',background="DARKSALMON",borderwidth=2, relief="groove")
lEnter_pnr['font']= heading_font
lenter_pnr = font.Font(size=20)
lEnter_pnr['font'] = lenter_pnr
lEnter_pnr.grid(row=3,column=1 ,pady=40 ,padx=10)


Enter_pnr = ttk.Entry(win)
Enter_pnr.focus_set()
Enter_pnr.grid(row=3,column=2 ,ipady=6 ,ipadx=30 , padx=0)



def procces():
    number1=Entry.get(Enter_pnr)
    pnr_no = number1
    sxp = tk.StringVar()
    E4 = Entry(win, state='readonly',textvariable = sxp)
    E4.grid(row=5, columnspan=6, ipady=115, ipadx=250, padx=20, pady=10)
    a = "https://indianrailapi.com/api/v2/PNRCheck/apikey/44d10aa46d74e7be6ca65710c2fa9ce1/PNRNumber/" + pnr_no + "/"
    dk = requests.get(a)
    result = dk.json()
    if result["ResponseCode"] == '200':
        pnr_number = result['PnrNumber']
        train_name = result["TrainNumber"]
        Journey_class = result["JourneyClass"]
        Chat_Prepared = result["ChatPrepared"]
        from_station = result["From"]
        to_station = result["To"]
        dateof_journey = result["JourneyDate"]
        passengers_list = result["Passangers"]
        sxp.set(
            f"PnrNumber {pnr_number}\nTrain Name {train_name}\nJourney Class {Journey_class}\nChart Preadared {Chat_Prepared}\nFrom Station {from_station} To {to_station}\nJourney Date {dateof_journey}")

        for passenger in passengers_list:
            passenger_num = passenger["Passenger"]

            current_status = passenger["CurrentStatus"]

            booking_status = passenger["BookingStatus"]
            sxp.set(
            	(" passenger number : " + str(passenger_num)
                  + "\n current status : " + str(current_status)
                  + "\n booking_status : " + str(booking_status))
            )

    else:
        sxp.set("Wrong Pnr Number")

btn = ttk.Button(win, text='Sumbit',command = procces)
btn.grid(row =4 ,columnspan= 5 , ipady = 10 , ipadx=10 , padx = 20)

win.mainloop()
