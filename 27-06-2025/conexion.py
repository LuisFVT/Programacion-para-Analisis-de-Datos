import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Conexión
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="carritos"
)

cursor = conexion.cursor()

def guardar():
    marca = entrada_marca.get()
    anio = entrada_anio.get()
    kilometraje = entrada_km.get()
    trans = entrada_trans.get()
    precio = entrada_precio.get()
    eco = entrada_econ.get()

    try:
        cursor.execute(
            "INSERT INTO autos (marca,anio,transmision,kilometraje,precio,economico) VALUES (%s,%s,%s,%s,%s,%s)",
            (marca, anio, trans, kilometraje, precio, eco)
        )
        conexion.commit()
        messagebox.showinfo("Éxito", "Auto Guardado")
        limpiar_campos()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar: {e}")

def limpiar_campos():
    entrada_marca.delete(0, tk.END)
    entrada_anio.delete(0, tk.END)
    entrada_km.delete(0, tk.END)
    entrada_trans.delete(0, tk.END)
    entrada_precio.delete(0, tk.END)
    entrada_econ.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Registro de autos")

tk.Label(ventana, text="Marca:").grid(row=0, column=0)
entrada_marca = tk.Entry(ventana)
entrada_marca.grid(row=0, column=1)

tk.Label(ventana, text="Año:").grid(row=1, column=0)
entrada_anio = tk.Entry(ventana)
entrada_anio.grid(row=1, column=1)

tk.Label(ventana, text="Kilometraje:").grid(row=2, column=0)
entrada_km = tk.Entry(ventana)
entrada_km.grid(row=2, column=1)

tk.Label(ventana, text="Transmisión:").grid(row=3, column=0)
entrada_trans = tk.Entry(ventana)
entrada_trans.grid(row=3, column=1)

tk.Label(ventana, text="Precio:").grid(row=4, column=0)
entrada_precio = tk.Entry(ventana)
entrada_precio.grid(row=4, column=1)

tk.Label(ventana, text="Económico:").grid(row=5, column=0)
entrada_econ = tk.Entry(ventana)
entrada_econ.grid(row=5, column=1)

tk.Button(ventana, text="Guardar", command=guardar).grid(row=6, column=0, columnspan=2, pady=10)

ventana.mainloop()
