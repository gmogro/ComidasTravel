import tkinter as tk
import json
from tkinter import ttk
import tkintermapview
from ubicacion import Ubicacion

def mostraUbicacion(event):
    indice = lista_ubicaciones.curselection()
    for data in data_ubicaciones:
        if data["id"] == indice[0]:
            print(data["nombre"])
            print(data["direccion"])   

root = tk.Tk()
root.title("Comidas Travel")
root.geometry("600x500")
root.iconbitmap("icon-principal.ico")

#la lectura de los archivos json
with open("Ubicacion.json","r") as file:
    data_ubicaciones = json.load(file)

#frames o contenedores de las ventanas
frame_mapa = ttk.Frame(root)
frame_mapa.grid(row=0,column=0)
frame_lista = ttk.Frame(root)
frame_lista.grid(row=0,column=1)
#crear mapa
map_widget = tkintermapview.TkinterMapView(frame_mapa, width=800, height=600, corner_radius=0)
# centro en Salta al mapa
map_widget.set_position(-24.782347970202725, -65.4237663021064) 
map_widget.set_zoom(12)
map_widget.pack()

#widget de lista para mostrar la ubicaciones
lista_ubicaciones = tk.Listbox(frame_lista)
lista_ubicaciones.pack()

for data in data_ubicaciones:
    ubicacion = Ubicacion.from_json(data)
    lista_ubicaciones.insert(tk.END,ubicacion.nombre)
    map_widget.set_marker(ubicacion.coordenadas[0],ubicacion.coordenadas[1],text=ubicacion.nombre)

lista_ubicaciones.bind("<Double-Button-1>",mostraUbicacion)




root.mainloop()