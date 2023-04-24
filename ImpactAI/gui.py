import tkinter as tk
from PIL import ImageTk, Image
import customtkinter as ctk
import os
import webbrowser
from botbuilder.core import BotFrameworkHttpClient
from botbuilder.schema import Activity, ActionTypes


file_path = os.path.dirname(os.path.realpath(__file__))
asset_path = os.path.join(file_path, "Assets")
img_path = os.path.join(asset_path, "_therapy_.png")
inappimg = os.path.join(asset_path, "therapy_logo_circle.png")

splash = tk.Tk()
x = (splash.winfo_screenwidth()/2)-165
y = (splash.winfo_screenheight()/2)-165
splash.geometry(f"330x330+{int(x)}+{int(y)}")
img = ImageTk.PhotoImage(Image.open(img_path))
splash.overrideredirect(True)
splash_frame = tk.Frame(master=splash)
img_lbl = tk.Label(master=splash_frame, image=img)
splash_frame.pack()
splash_frame.place(anchor='center', relx=0.5, rely=0.5)
img_lbl.pack()

def mainwindow():
    def openlink0():
        webbrowser.open("https://www.nimh.nih.gov/about")
    def openlink1():
        webbrowser.open("https://www.veteranscrisisline.net/")
    def openlink2():
        webbrowser.open("https://www.samhsa.gov/find-help/disaster-distress-helpline")
    def openlink3():
        webbrowser.open("https://988lifeline.org/")

    """def sendmsg():
        usermsg = userinput.get()
        activity = Activity(type='message', text=usermsg)

        bot_client = BotFrameworkHttpClient()
        response = bot_client.post_activity("", activity, "")"""


    splash.destroy()
    root = ctk.CTk()
    root.title("TheraPy AI Chatbot")
    root.attributes('-fullscreen',True)
    ctk.set_default_color_theme("green")
    ctk.set_appearance_mode("dark")
    left_frame = ctk.CTkFrame(master=root, width = 640, height=1080)
    img_inapp = ImageTk.PhotoImage(Image.open(inappimg))
    img_lbl_inapp = ctk.CTkLabel(master=left_frame, image=img_inapp, text="")
    right_frame = ctk.CTkFrame(master=root, width = 1280, height = 1080)
    scrollable_frame = ctk.CTkScrollableFrame(master=right_frame, width=1240, height=1000)
    input_frame = ctk.CTkFrame(master=right_frame)
    userinput = ctk.CTkEntry(master=input_frame, width=900)
    sendbtn = ctk.CTkButton(master=input_frame, width=180, text='Send')
    quitbtn = ctk.CTkButton(master=left_frame, width=100, text='Quit', command=root.destroy)
    help_frame = ctk.CTkFrame(master=left_frame)
    buttonframe = ctk.CTkFrame(master=help_frame)
    lbl_helplinks = ctk.CTkLabel(master=help_frame, text="Helpful Links for Mental Health support: ", font=('Helvetica', 20))
    btn_link1=ctk.CTkButton(master=buttonframe, text='https://www.nimh.nih.gov/about', command=openlink0)
    btn_link2=ctk.CTkButton(master=buttonframe, text='https://www.veteranscrisisline.net/', command=openlink1)
    btn_link3=ctk.CTkButton(master=buttonframe, text='https://www.samhsa.gov/find-help/disaster-distress-helpline',command=openlink2)
    btn_link4=ctk.CTkButton(master=buttonframe, text='https://988lifeline.org/',command=openlink3)
    left_frame.pack(side='left', padx=5)
    quitbtn.grid(row=0, column=0, sticky='nw', padx=5, pady=20)
    img_lbl_inapp.grid(row=1, column=0, padx=200, pady=180)
    right_frame.pack(side='right')
    scrollable_frame.pack()
    input_frame.pack()
    userinput.grid(row=0, column=0, padx=20, pady=5)
    sendbtn.grid(row=0, column=1, padx=20, pady=5)
    help_frame.grid(row=2, column=0, pady=10)
    lbl_helplinks.pack(side='left')
    buttonframe.pack(side='right', padx=5, pady=15)
    btn_link1.pack(padx=5, pady=10)
    btn_link2.pack(padx=5, pady=10)
    btn_link3.pack(padx=5, pady=10)
    btn_link4.pack(padx=5, pady=10)
    
    root.mainloop()
splash.after(3000, mainwindow)
splash.mainloop()