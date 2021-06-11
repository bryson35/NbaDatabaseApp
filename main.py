import requests
import json
import tkinter as tk
from tkinter import messagebox


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        #welcome message
        self.welcome = tk.Message(self, width=500, font=("Arial", 15))
        self.welcome["text"] = "Welcome to the All-Time NBA Player Database!\n" \
                               "Please enter a player's name to search for."
        self.welcome.pack(side="top")
        #text input
        self.txt = tk.Entry(self, width=20)
        self.txt.pack(side="top")

        self.btn = tk.Button(self, text="SEARCH", command=self.printPlayer)
        self.btn.pack(side="top")



    # Prints player(s) name in a scrollable list format
    def printPlayer(self):
        self.btn.destroy()
        self.clear = tk.Button(self, text="CLEAR", command=self.clearSearch)
        self.clear.pack(side="top")

        self.scroll = tk.Scrollbar(self)
        self.scroll.pack(side="right", fill="y")
        self.list = tk.Listbox(self, width=self.winfo_width(), height=self.winfo_height(), yscrollcommand=self.scroll.set)
        self.text = ""
        nameResponse = requests.request("GET", url, headers=headers, params={"search": self.txt.get()})
        playerInfo = nameResponse.json()["data"]
        for n in playerInfo:
            self.text = (f'\n{n["first_name"]} {n["last_name"]}, '
            f'\n{n["team"]["name"]}')
            self.list.insert("end", self.text)
            self.list.insert("end", "--------------------------")
        self.list.pack(side="top")




    def clearSearch(self):
        self.clear.destroy()
        self.list.destroy()
        self.scroll.destroy()
        self.btn = tk.Button(self, text="SEARCH", command=self.printPlayer)
        self.btn.pack(side="top")



#url for API
url = "https://free-nba.p.rapidapi.com/players"
queryString = {}
headers = {
    'x-rapidapi-key': "76de4c5a30mshba1167ef4405a88p120bacjsn0b2458029be4",
    'x-rapidapi-host': "free-nba.p.rapidapi.com"
}
# GET response
response = requests.request("GET", url, headers=headers)
#check to make sure request works
print(response.status_code)

#Prints all data in json format
def printJson(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)



# Prints the information of the current page where the player is located
def printMeta():
    meta = response.json()["meta"]
    print("PAGE INFORMATION")
    print(meta)





## START APPLICATION
root = tk.Tk()
root.geometry("500x500")
app = App(master=root)
app.mainloop()


