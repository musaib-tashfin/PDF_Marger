import tkinter as tk

window = tk.Tk() 
window.title('PDF marger')
window.geometry('900x600')
window.resizable(False,False)


imag = tk.PhotoImage(file='Small code projects\Pdf Marger\Logo.png')

Logo = tk.Label(window,image=imag)
Logo.place(relx=0.27)

entry1 = tk.Entry(window,width=100)
entry1.place(relx=0.2,rely=0.41)

button1 = tk.Button(window,text = 'Browse',width=10)
button1.place(relx=0.1,rely=0.4)

entry2 = tk.Entry(window,width=100)
entry2.place(relx=0.2,rely=0.51)

button2 = tk.Button(window,text = 'Select',width=10)
button2.place(relx=0.1,rely=0.5)

window.mainloop()