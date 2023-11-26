import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.geometry("500x300")

number = 0

def up():
    global number
    number = number + 1
    score_click.configure(text=number)
    
def down():
    global number
    number = number - 1
    score_click.configure(text=number)
    

button = customtkinter.CTkButton(window, text="+", command=up)
button.pack(padx=10,pady=50)

score_click = customtkinter.CTkLabel(window, text="0")
score_click.pack(padx=10, pady=10)    
    
button = customtkinter.CTkButton(window, text="-", command=down)
button.pack(padx=10,pady=50)
    
window.mainloop()