import tkinter as tk
from tkinter import filedialog

def select_files() :
    files = filedialog.askopenfilenames(
        title='Select PDF Files',
        filetypes=[('PDF Files','*.pdf'),('All files','*')]
    )
    if files:
        entry1.delete(0, tk.END)                
        entry1.insert(0, ", ".join(files))     


def select_folder() :
    folder = filedialog.askdirectory(
        title=('Select Folder'),   
    )
    if folder:
        entry2.delete(0, tk.END)                
        entry2.insert(0,folder)     

# Main window
window = tk.Tk() 
window.title('PDF marger')
window.geometry('900x600')
window.resizable(False,False)
window.config(bg='gray')

imag = tk.PhotoImage(file='Small code projects/Pdf Marger/Logo.png')
img_small = imag.subsample(2,2)
Logo = tk.Label(window,image=img_small)
Logo.place(relx=0.35,rely=0.005)

button1 = tk.Button(window,text = 'Browse',width=10,command=select_files)
button1.place(relx=0.1,rely=0.5)

button2 = tk.Button(window,text = 'Select',width=10,command=select_files)
button2.place(relx=0.1,rely=0.6)

entry1 = tk.Entry(window,width=100)
entry1.place(relx=0.2,rely=0.505)

entry2 = tk.Entry(window,width=100)
entry2.place(relx=0.2,rely=0.605)

window.mainloop()