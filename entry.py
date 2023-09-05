import tkinter as tk
from tkinter import ttk, messagebox as msg

root = tk.Tk()
root.title("Formulario")
root.config(padx=20, pady=20)

#accion del boton iniciar sesion
def login() :
    username = in_username.get()
    password = in_password.get()
    gender = selectedGender.get()
    team = selectedTeam.get()

    if (gender == 1) : gender = "Hombre" 
    else : gender = "Mujer"

    msg.showinfo(title="¡Registrado!",
                 message=f"Usuario: {username}\
                \nContraseña:  {password}\
                \nGénero: {gender}\
                \nEquipo: {team.capitalize()}")

#OPCIONES RADIOBUTTONS

#--------equipo

#variable conjunta - equipo
selectedTeam = tk.StringVar()

#-------genero

#variable conjunta - genero
selectedGender = tk.IntVar()
selectedGender.set(value=1)

#opcion 1 hombre
rb_gender1 = ttk.Radiobutton(root, text="Hombre", value=1, variable=selectedGender)
rb_gender1.grid(row=3, column=1, sticky="w")

#opcion 2 mujer
rb_gender2 = ttk.Radiobutton(root, text="Mujer", value=2, variable=selectedGender)
rb_gender2.grid(row=4, column=1, sticky="w")




#--------equipo

separator = ttk.Separator(root, orient="horizontal")
separator.grid(column=0, columnspan=2, row=5, sticky="ew", pady=5)

#variable conjunta - equipo
selectedTeam = tk.StringVar()
selectedTeam.set("rojo")

lb_selectTeam = tk.Label(root, text="Selecciona un equipo: ").grid(column=0, row=6)

teams = [["Equipo Rojo", "rojo"],
         ["Equipo Azul", "azul"],
         ["Equipo Amarillo", "amarillo"],
         ["Equipo Verde", "verde"],
         ["Equipo Naranja", "naranja"]]

i = 6

for equipo, valor in teams :
    ttk.Radiobutton(root, text=equipo, value=valor, variable=selectedTeam).grid(column=1, row=i, sticky="w")
    i += 1

#LABELS

#Titulo
lb_title = tk.Label(root, text="Registro")
lb_title.grid(column=0, row=0, columnspan=2)
lb_title.config(font=("", 20))

#nombre de usuario
lb_username = tk.Label(root, text="Nombre de usuario: ")
lb_username.grid(column=0, row=1)
lb_username.config(padx=10, pady=10)

#contraseña
lb_password = tk.Label(root, text="Contraseña: ")
lb_password.grid(column=0, row=2)
lb_password.config(padx=10, pady=10)

#género
lb_selectGender = tk.Label(root, text="Selecciona tu género: ").grid(column=0, row=3)



#ENTRIES

#nombre de usuario
in_username = ttk.Entry(root)
in_username.grid(column=1, row=1)
in_username.config(width=30, font=("", 12))

#contraseña
in_password = ttk.Entry(root, show="*")
in_password.grid(column=1, row=2)
in_password.config(width=30, font=("", 12))

#BUTTONS
btn_login = ttk.Button(root, text="Entrar", command=login)
btn_login.grid(column=1, row=20, sticky="ew", pady=(10, 0))


root.mainloop()