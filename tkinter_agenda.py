#!/usr/bin/env python3

import tkinter as tk
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
from json import dump
from json import loads

def agregar():
	datos = {}
	
	datos["nombre"] = sd.askstring("Datos Personales", "Ingrese su nombre")
	
	datos["apellido"] = sd.askstring("Datos Personales", "Ingrese su apellido")
	
	datos["telefono"] = sd.askstring("Datos Personales", "Ingrese su telefono")
	
	with open("datos.json", "w") as barby:
		dump(datos, barby)

def mostrar():
	vertical = 90
	
	datos = loads(open("datos.json").read())
	
	for key, value in datos.items():
		dataLabel = tk.Label(mainForm, text = key + ": " + value)
		dataLabel.place(x = 10, y = vertical)
		vertical += 20

mainForm = tk.Tk()
mainForm.title("Agenda")
mainForm.geometry("400x200")

agregarButton = tk.Button(mainForm, text = "Agregar datos", command = agregar)
agregarButton.place(x = 10, y = 10)

mostrarButton = tk.Button(mainForm, text = "Mostrar datos", command = mostrar)
mostrarButton.place(x = 120, y = 10)

mainForm.mainloop()
