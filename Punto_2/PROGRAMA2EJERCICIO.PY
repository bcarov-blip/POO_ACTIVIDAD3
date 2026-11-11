
import tkinter as tk
from tkinter import ttk, messagebox
import math


# Clase padre
class FiguraGeometrica:
    def calcularVolumen(self):
        raise NotImplementedError

    def calcularSuperficie(self):
        raise NotImplementedError


# Cilindro
class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def calcularVolumen(self):
        return math.pi * self.radio ** 2 * self.altura

    def calcularSuperficie(self):
        return 2 * math.pi * self.radio * (
            self.radio + self.altura
        )


# Esfera
class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcularVolumen(self):
        return (4 / 3) * math.pi * self.radio ** 3

    def calcularSuperficie(self):
        return 4 * math.pi * self.radio ** 2


# Pirámide de base cuadrada
class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def calcularVolumen(self):
        return self.base ** 2 * self.altura / 3

    def calcularSuperficie(self):
        return self.base ** 2 + 2 * self.base * self.apotema


# Propuesta 1: Cubo
class Cubo(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcularVolumen(self):
        return self.lado ** 3

    def calcularSuperficie(self):
        return 6 * self.lado ** 2


# Propuesta 1: Prisma rectangular
class Prisma(FiguraGeometrica):
    def __init__(self, largo, ancho, altura):
        self.largo = largo
        self.ancho = ancho
        self.altura = altura

    def calcularVolumen(self):
        return self.largo * self.ancho * self.altura

    def calcularSuperficie(self):
        return 2 * (
            self.largo * self.ancho +
            self.largo * self.altura +
            self.ancho * self.altura
        )


# Interfaz gráfica
class VentanaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Figuras Geométricas")
        self.ventana.geometry("480x600")
        self.ventana.resizable(False, False)

        tk.Label(
            ventana,
            text="CÁLCULO DE FIGURAS GEOMÉTRICAS",
            font=("Arial", 14, "bold")
        ).pack(pady=15)

        tk.Label(
            ventana, text="Seleccione una figura:"
        ).pack()

        self.figura = ttk.Combobox(
            ventana,
            values=[
                "Cilindro",
                "Esfera",
                "Pirámide",
                "Cubo",
                "Prisma"
            ],
            state="readonly"
        )
        self.figura.pack(pady=8)
        self.figura.current(0)
        self.figura.bind(
            "<<ComboboxSelected>>",
            self.actualizarCampos
        )

        self.marco = tk.Frame(ventana)
        self.marco.pack(pady=10)

        self.campos = {}

        # Propuesta 2: dibujo de la figura
        self.canvas = tk.Canvas(
            ventana, width=230, height=180,
            bg="white", highlightthickness=1,
            highlightbackground="gray"
        )
        self.canvas.pack(pady=10)

        tk.Button(
            ventana,
            text="Calcular",
            width=15,
            command=self.calcular
        ).pack(pady=5)

        tk.Button(
            ventana,
            text="Limpiar",
            width=15,
            command=self.limpiar
        ).pack(pady=5)

        self.resultadoVolumen = tk.Label(
            ventana, text="Volumen = ",
            font=("Arial", 11)
        )
        self.resultadoVolumen.pack(pady=5)

        self.resultadoSuperficie = tk.Label(
            ventana, text="Superficie = ",
            font=("Arial", 11)
        )
        self.resultadoSuperficie.pack(pady=5)

        self.actualizarCampos()

    def actualizarCampos(self, evento=None):
        for widget in self.marco.winfo_children():
            widget.destroy()

        self.campos = {}
        figura = self.figura.get()

        datos = {
            "Cilindro": ["Radio", "Altura"],
            "Esfera": ["Radio"],
            "Pirámide": ["Base", "Altura", "Apotema"],
            "Cubo": ["Lado"],
            "Prisma": ["Largo", "Ancho", "Altura"]
        }

        for i, nombre in enumerate(datos[figura]):
            tk.Label(
                self.marco,
                text=f"{nombre} (cm):"
            ).grid(row=i, column=0, padx=10, pady=5)

            entrada = tk.Entry(self.marco)
            entrada.grid(row=i, column=1, pady=5)
            self.campos[nombre] = entrada

        self.resultadoVolumen.config(text="Volumen = ")
        self.resultadoSuperficie.config(text="Superficie = ")
        self.dibujarFigura()

    def dibujarFigura(self):
        self.canvas.delete("all")
        figura = self.figura.get()

        if figura == "Cilindro":
            self.canvas.create_rectangle(
                65, 45, 165, 135,
                fill="#b3d9ff", outline="black"
            )
            self.canvas.create_oval(
                65, 25, 165, 65,
                fill="#b3d9ff"
            )
            self.canvas.create_arc(
                65, 115, 165, 155,
                start=180, extent=180,
                style=tk.ARC
            )

        elif figura == "Esfera":
            self.canvas.create_oval(
                50, 20, 180, 150,
                fill="#b3d9ff", outline="black"
            )
            self.canvas.create_oval(
                50, 65, 180, 105,
                outline="gray", dash=(4, 3)
            )

        elif figura == "Pirámide":
            self.canvas.create_polygon(
                115, 20, 40, 125, 145, 155,
                fill="#b3d9ff", outline="black"
            )
            self.canvas.create_polygon(
                115, 20, 145, 155, 195, 115,
                fill="#80bfff", outline="black"
            )
            self.canvas.create_line(
                40, 125, 195, 115,
                dash=(4, 3)
            )

        elif figura == "Cubo":
            self.canvas.create_rectangle(
                45, 65, 135, 155,
                fill="#b3d9ff"
            )
            self.canvas.create_polygon(
                45, 65, 85, 25, 175, 25, 135, 65,
                fill="#d9ecff", outline="black"
            )
            self.canvas.create_polygon(
                135, 65, 175, 25, 175, 115, 135, 155,
                fill="#80bfff", outline="black"
            )

        elif figura == "Prisma":
            self.canvas.create_rectangle(
                35, 70, 155, 145,
                fill="#b3d9ff"
            )
            self.canvas.create_polygon(
                35, 70, 75, 35, 195, 35, 155, 70,
                fill="#d9ecff", outline="black"
            )
            self.canvas.create_polygon(
                155, 70, 195, 35, 195, 110, 155, 145,
                fill="#80bfff", outline="black"
            )

    def calcular(self):
        try:
            valores = {}

            for nombre, campo in self.campos.items():
                texto = campo.get().strip()

                if not texto:
                    messagebox.showwarning(
                        "Campo vacío",
                        f"Ingrese el valor de {nombre}"
                    )
                    return

                numero = float(texto)

                if not math.isfinite(numero) or numero <= 0:
                    raise ValueError

                valores[nombre] = numero

            figura = self.figura.get()

            if figura == "Cilindro":
                objeto = Cilindro(
                    valores["Radio"],
                    valores["Altura"]
                )

            elif figura == "Esfera":
                objeto = Esfera(valores["Radio"])

            elif figura == "Pirámide":
                objeto = Piramide(
                    valores["Base"],
                    valores["Altura"],
                    valores["Apotema"]
                )
                if valores["Apotema"] < math.hypot(
                    valores["Altura"], valores["Base"] / 2
                ) - 1e-9:
                    messagebox.showerror(
                        "Error",
                        "La apotema no corresponde a "
                        "las dimensiones de la pirámide."
                    )
                    return

            elif figura == "Cubo":
                objeto = Cubo(valores["Lado"])

            elif figura == "Prisma":
                objeto = Prisma(
                    valores["Largo"],
                    valores["Ancho"],
                    valores["Altura"]
                )

            self.resultadoVolumen.config(
                text=f"Volumen = "
                     f"{objeto.calcularVolumen():.2f} cm³"
            )

            self.resultadoSuperficie.config(
                text=f"Superficie = "
                     f"{objeto.calcularSuperficie():.2f} cm²"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Ingrese números válidos mayores que cero."
            )

    def limpiar(self):
        for campo in self.campos.values():
            campo.delete(0, tk.END)

        self.resultadoVolumen.config(text="Volumen = ")
        self.resultadoSuperficie.config(text="Superficie = ")


# Programa principal
if __name__ == "__main__":
    ventana = tk.Tk()
    app = VentanaPrincipal(ventana)
    ventana.mainloop()
