import tkinter as tk
import speedtest

def check_speed():
    try:
        sp = speedtest.Speedtest()
        sp.get_servers()
        download_speed = str(round(sp.download() / (10**6), 3))+" mbps"
        upload_speed = str(round(sp.upload() / (10**6), 3))+" mbps"
        lab_down.config(text=download_speed)
        lab_up.config(text=upload_speed)
    except Exception as e:
        # Handle the exception gracefully
        print("An error occurred:", e)

sp = tk.Tk()
sp.title("Internet Speed Test")
sp.geometry("500x650")
sp.config(bg="#0d1137")

lab = tk.Label(sp, text="Internet Speed Tester", font=("Forte", 30,"bold","underline"), bg="#0d1137",fg="white")
lab.place(x=60, y=40, height=50, width=380)

lab = tk.Label(sp, text="Download Speed", font=("Comic Sans MS", 20,"bold"), bg="#0d1137",fg="white")
lab.place(x=60, y=130, height=50, width=380)

lab_down = tk.Label(sp, text="00", font=("Agency FB", 15), bg="#0d1137",fg="white")
lab_down.place(x=60, y=200,height=50, width=380)

lab = tk.Label(sp, text="Upload Speed", font=("Comic Sans MS", 20,"bold"), bg="#0d1137",fg="white")
lab.place(x=60, y=290, height=50, width=380)

lab_up = tk.Label(sp, text="00", font=("Agency FB", 15), bg="#0d1137",fg="white")
lab_up.place(x=60, y=360, height=50, width=380)

button = tk.Button(sp, text="Check Speed", font=("Times New Roman", 15),relief=tk.RAISED,bg="#0d1137",fg="pink", command=check_speed)
button.place(x=60, y=460, height=50, width=380)

sp.mainloop()
