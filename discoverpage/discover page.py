import tkinter as tk
from PIL import ImageTk, Image


class discoverpage(tk.Tk):    # class for discover window
    def __init__(self):
        super().__init__() # allows inheritance from tk library
        self.title("Discover Page")
        self.geometry("1148x656")
        self.config(bg="#171923") 
        self.resizable(False, False)

        #dashboard frame
        self.dashframe = tk.Frame(self,bg="#282C3E",width=178,height=656,bd=3)
        self.dashframe.pack_propagate(False)
        self.dashframe.pack(side="left",fill="y")

        # dashframe button icons
        discovericon = ImageTk.PhotoImage(Image.open("discovericon.png"))
        messageicon = ImageTk.PhotoImage(Image.open("messageicon.png"))
        connecticon = ImageTk.PhotoImage(Image.open("connecticon.png"))


        self.dbutton = tk.Button(self.dashframe,image= discovericon,bg="#282C3E")
        self.dbutton.pack(side="top",pady=(45,37))
        self.mbutton = tk.Button(self.dashframe,image= messageicon,bg="#282C3E")
        self.mbutton.pack(side="top",pady=(0,45))
        self.cbutton = tk.Button(self.dashframe,image= connecticon,bg="#282C3E")
        self.cbutton.pack(side="top",pady=(0,37))
        self.mainloop()

discoverpage()





# working on a post class to make multiple post objects
class post:
    likebutton = ImageTk.PhotoImage(Image.open("likeicon.png"))
    connectbutton = Image.PhotoImage(Image.open("connecticon.png"))
    
    def __init__(self,postimg,username,userpfp,flag,caption):
        self.postimg = postimg
        self.username = username
        self.userpfp = userpfp
        self.flag = flag
        self.caption = caption