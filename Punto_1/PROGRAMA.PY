
import tkinter as tk
from tkinter import messagebox
import math


class Notas:
    def __init__(self):
        self.listaNotas = [0] * 5

    def calcularPromedio(self):
        suma = 0
        for i in range(5):
            suma += self.listaNotas[i]
        return suma / 5

    def calcularDesviacion(self):
        promedio = self.calcularPromedio()
        suma = 0

        for i in range(5):
            suma += (self.listaNotas[i] - promedio) ** 2

        return math.sqrt(suma / 5)

    def calcularMayor(self):
        return max(self.listaNotas)

    def calcularMenor(self):
        return min(self.listaNotas)


class VentanaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Notas")
        self.ventana.geometry("350x400")
        self.ventana.resizable(False, False)

        self.campos = []

        for i in range(5):
            etiqueta = tk.Label(
                ventana, text=f"Nota {i + 1}:"
            )
            etiqueta.grid(row=i, column=0, padx=15, pady=8)

            campo = tk.Entry(ventana)
            campo.grid(row=i, column=1, padx=10, pady=8)
            self.campos.append(campo)

        botonCalcular = tk.Button(
            ventana, text="Calcular",
            command=self.calcularNotas
        )
        botonCalcular.grid(row=5, column=0, pady=15)

        botonLimpiar = tk.Button(
            ventana, text="Limpiar",
            command=self.limpiar
        )
        botonLimpiar.grid(row=5, column=1, pady=15)

        self.promedio = tk.Label(
            ventana, text="Promedio = "
        )
        self.promedio.grid(row=6, column=0, columnspan=2)

        self.desviacion = tk.Label(
            ventana, text="Desviación estándar = "
        )
        self.desviacion.grid(row=7, column=0, columnspan=2)

        self.mayor = tk.Label(
            ventana, text="Nota mayor = "
        )
        self.mayor.grid(row=8, column=0, columnspan=2)

        self.menor = tk.Label(
            ventana, text="Nota menor = "
        )
        self.menor.grid(row=9, column=0, columnspan=2)

    def calcularNotas(self):
        notas = Notas()

        for i in range(5):
            valor = self.campos[i].get().strip()

            if valor == "":
                messagebox.showwarning(
                    "Campo vacío",
                    f"Debe ingresar la nota {i + 1}"
                )
                return

            try:
                numero = float(valor)
                if not math.isfinite(numero):
                    raise ValueError
                notas.listaNotas[i] = numero
            except ValueError:
                messagebox.showerror(
                    "Error",
                    f"La nota {i + 1} debe ser numérica"
                )
                return

        self.promedio.config(
            text=f"Promedio = {notas.calcularPromedio():.2f}"
        )

        self.desviacion.config(
            text=f"Desviación estándar = "
                 f"{notas.calcularDesviacion():.2f}"
        )

        self.mayor.config(
            text=f"Nota mayor = {notas.calcularMayor()}"
        )

        self.menor.config(
            text=f"Nota menor = {notas.calcularMenor()}"
        )

    def limpiar(self):
        for campo in self.campos:
            campo.delete(0, tk.END)

        self.promedio.config(text="Promedio = ")
        self.desviacion.config(text="Desviación estándar = ")
        self.mayor.config(text="Nota mayor = ")
        self.menor.config(text="Nota menor = ")


ventana = tk.Tk()
app = VentanaPrincipal(ventana)
ventana.mainloop()
