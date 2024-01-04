import tkinter as tk
import datetime, time
import Download
import Read

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess LV")
        self.root.geometry('720x480') 
        
        # Button to download 
        self.download_button = tk.Button(root, text="Download regulations", command=self.download)
        self.download_button.pack()
        
        # Button to display tournaments
        self.display_tournaments_button = tk.Button(root, text="Display tournaments", command=self.reset)
        self.display_tournaments_button.pack()
        
        # Button to select tournament
        self.select_tournaments_button = tk.Button(root, text="Select tournament", command=self.reset)
        self.select_tournaments_button.pack()

        # Button to send email
        self.send_email_button = tk.Button(root, text="Send email", command=self.reset)
        self.send_email_button.pack()

        # Label to display the last download time
        self.display_label = tk.Label(root, text="Last updated time: NONE")
        self.display_label.pack()

    def download(self):
        self.download_button.config(state="disabled")
        self.display_tournaments_button.config(state="disabled")
        self.select_tournaments_button.config(state="disabled")
        self.send_email_button.config(state="disabled")

        # Update label text to indicate downloading
        self.display_label.config(text="Downloading...")

        # Schedule the download process in the background
        self.root.after(100, self.perform_download)
        
    def perform_download(self):
        Download.download()
        Read.read_regulations()
        TIME = str(datetime.datetime.now())[:19]
        self.display_label.config(text="Last updated time: " + TIME)

        # Enable buttons after download
        self.download_button.config(state="normal")
        self.display_tournaments_button.config(state="normal")
        self.select_tournaments_button.config(state="normal")
        self.send_email_button.config(state="normal")
        

    def reset(self):
        
        self.display_label.config(text="")
        

if __name__ == "__main__":
    root = tk.Tk()
    clock = Application(root)
    root.mainloop()