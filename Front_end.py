import tkinter as tk
import PyPDF2 as pd
import os
from tkinter import filedialog

def pdf_merging() :
    files = entry1.get().split(', ')
    output_folder = entry2.get()

    if not files or not output_folder:
        tk.messagebox.showerror('Error','Please select files or folder first')
        return
    try:
        merger = pd.PdfWriter()
        for pdf in files:
            merger.append(pdf)
        
        output_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        title="Save Merged PDF As"
        )
        if not output_path:
            return  # user cancelled
        merger.write(output_path)


        tk.messagebox.showinfo('Success',f'PDF merger successfully!\nSaved at {output_path}')
    except Exception as e:
        tk.messagebox.showerror('Error',f'Something went wrong:\n{e}')

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

imag = tk.PhotoImage(file='D:\Workshop\Programming\Small code projects\Pdf Marger\Logo.png')
img_small = imag.subsample(2,2)
Logo = tk.Label(window,image=img_small)
Logo.place(relx=0.35,rely=0.005)

button1 = tk.Button(window,text = 'Browse',width=10,command=select_files)
button1.place(relx=0.1,rely=0.5)

button2 = tk.Button(window,text = 'Select',width=10,command=select_folder)
button2.place(relx=0.1,rely=0.6)

entry1 = tk.Entry(window,width=100)
entry1.place(relx=0.2,rely=0.505)

entry2 = tk.Entry(window,width=100)
entry2.place(relx=0.2,rely=0.605)

merger_button = tk.Button(window,text='Merge PDf',width=18,command=pdf_merging,bg='red')
merger_button.place(relx=0.4,rely=0.8)

window.mainloop()