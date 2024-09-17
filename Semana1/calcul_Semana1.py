import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from fractions import Fraction
import pdoc

# html = pdoc.pdoc("calcul_Semana1")


class Calculadora:
    """
    Clase que representa una calculadora para sistemas de ecuaciones lineales 2x2.

    La calculadora resuelve sistemas de dos ecuaciones lineales con dos incógnitas
    utilizando la regla de Cramer y muestra todo el proceso paso a paso. La interfaz
    gráfica permite ingresar los coeficientes y constantes, y muestra los resultados
    de manera clara y detallada.
    """

    def __init__(self):
        """
        Inicializa la interfaz gráfica y los elementos necesarios para la interacción
        con el usuario.
        """
        # Crear la ventana principal de la interfaz gráfica
        self.root = ctk.CTk()
        self.root.title("Calculadora de Ecuaciones 2x2")
        self.root.geometry("600x600")

        # Crear y mostrar etiquetas y campos de entrada para la primera ecuación
        self.label1 = ctk.CTkLabel(self.root, text="Primera ecuación (ax + by = c)")
        self.label1.pack(pady=10)

        frame1 = ctk.CTkFrame(self.root)
        frame1.pack(pady=5)

        self.entry_a1 = ctk.CTkEntry(
            frame1, placeholder_text="Coeficiente de x1 (a)", width=150
        )
        self.entry_a1.grid(row=0, column=0, padx=5, pady=5)

        self.operacion1 = ctk.CTkOptionMenu(frame1, values=["+", "-"], width=50)
        self.operacion1.grid(row=0, column=1, padx=5, pady=5)

        self.entry_b1 = ctk.CTkEntry(
            frame1, placeholder_text="Coeficiente de y1 (b)", width=150
        )
        self.entry_b1.grid(row=0, column=2, padx=5, pady=5)

        ctk.CTkLabel(frame1, text="=").grid(row=0, column=3, padx=5, pady=5)

        self.entry_c1 = ctk.CTkEntry(
            frame1, placeholder_text="Valor del resultado c1", width=150
        )
        self.entry_c1.grid(row=0, column=4, padx=5, pady=5)

        # Crear y mostrar etiquetas y campos de entrada para la segunda ecuación
        self.label2 = ctk.CTkLabel(self.root, text="Segunda ecuación (dx + ey = f)")
        self.label2.pack(pady=10)

        frame2 = ctk.CTkFrame(self.root)
        frame2.pack(pady=5)

        self.entry_a2 = ctk.CTkEntry(
            frame2, placeholder_text="Coeficiente de x2 (d)", width=150
        )
        self.entry_a2.grid(row=0, column=0, padx=5, pady=5)

        self.operacion2 = ctk.CTkOptionMenu(frame2, values=["+", "-"], width=50)
        self.operacion2.grid(row=0, column=1, padx=5, pady=5)

        self.entry_b2 = ctk.CTkEntry(
            frame2, placeholder_text="Coeficiente de y2 (e)", width=150
        )
        self.entry_b2.grid(row=0, column=2, padx=5, pady=5)

        ctk.CTkLabel(frame2, text="=").grid(row=0, column=3, padx=5, pady=5)

        self.entry_c2 = ctk.CTkEntry(
            frame2, placeholder_text="Valor del resultado f", width=150
        )
        self.entry_c2.grid(row=0, column=4, padx=5, pady=5)

        # Crear un área de texto para mostrar el proceso y resultados
        self.result_area = ctk.CTkTextbox(self.root, width=500, height=250)
        self.result_area.pack(pady=10)

        # Crear botones para resolver el sistema y para iniciar un nuevo cálculo
        self.solve_button = ctk.CTkButton(
            self.root, text="Resolver", command=self.resolver_ecuaciones
        )
        self.solve_button.pack(pady=10)

        self.new_button = ctk.CTkButton(self.root, text="Nuevo", command=self.reiniciar)
        self.new_button.pack(pady=10)

        # Iniciar el bucle principal de la interfaz gráfica
        self.root.mainloop()

    def extraer_coeficiente(self, term, operation):
        """
        Extrae el coeficiente de un término dado, considerando la operación
        (+ o -) que lo precede. El coeficiente se ajusta según el signo de la operación.

        :param term: El término que contiene el coeficiente (por ejemplo, "2x").
        :param operation: La operación entre los términos, "+" o "-".
        :return: El coeficiente como una fracción.
        """
        try:
            coef = Fraction(term)
            if operation == "-":
                coef *= -1
            return coef
        except ValueError:
            raise ValueError(f"Término inválido: {term}")

    def mostrar_matriz(self, a1, b1, a2, b2, c1, c2):
        """
        Muestra la matriz de coeficientes y los valores de las ecuaciones en el área de resultados.

        :param a1: Coeficiente de x en la primera ecuación.
        :param b1: Coeficiente de y en la primera ecuación.
        :param a2: Coeficiente de x en la segunda ecuación.
        :param b2: Coeficiente de y en la segunda ecuación.
        :param c1: Constante de la primera ecuación.
        :param c2: Constante de la segunda ecuación.
        """
        # Separador visual
        self.result_area.insert(tk.END, "---------------------\n")
        # Mostrar las ecuaciones recibidas
        self.result_area.insert(tk.END, f"Ecuaciones recibidas:\n")
        self.result_area.insert(tk.END, f" {a1}x {b1}y = {c1}\n")
        self.result_area.insert(tk.END, f" {a2}x {b2}y = {c2}\n")
        # Separador visual
        self.result_area.insert(tk.END, "---------------------\n")
        # Mostrar la matriz Delta inicial
        self.result_area.insert(tk.END, f"Matriz Delta inicial:\n")
        self.result_area.insert(tk.END, f" | {a1}  {b1} |\n")
        self.result_area.insert(tk.END, f" | {a2}  {b2} |\n")
        # Separador visual
        self.result_area.insert(tk.END, "---------------------\n")
        # Mostrar la matriz de resultados
        self.result_area.insert(tk.END, f"Igual a:\n | {c1} |\n | {c2} |\n")
        # Separador visual
        self.result_area.insert(tk.END, "---------------------\n")

    def resolver_ecuaciones(self):
        """
        Resuelve el sistema de ecuaciones utilizando el método de matrices (regla de Cramer).
        Calcula los determinantes necesarios para encontrar las soluciones de x e y,
        y muestra el proceso y resultados en el área de resultados.
        """
        try:
            # Extraer coeficientes y constantes para la primera ecuación
            a1 = self.extraer_coeficiente(self.entry_a1.get(), "+")
            b1 = self.extraer_coeficiente(self.entry_b1.get(), self.operacion1.get())
            c1 = Fraction(self.entry_c1.get())

            # Extraer coeficientes y constantes para la segunda ecuación
            a2 = self.extraer_coeficiente(self.entry_a2.get(), "+")
            b2 = self.extraer_coeficiente(self.entry_b2.get(), self.operacion2.get())
            c2 = Fraction(self.entry_c2.get())
        except ValueError as e:
            # Mostrar error si hay problemas con la entrada
            messagebox.showerror("Error", str(e))
            return

        # Limpiar el área de resultados antes de mostrar el nuevo proceso
        self.result_area.delete(1.0, tk.END)
        # Mostrar la matriz inicial
        self.mostrar_matriz(a1, b1, a2, b2, c1, c2)

        # Calcular el determinante de Delta
        delta = a1 * b2 - a2 * b1
        self.result_area.insert(
            tk.END, f"\nDeterminante de Delta = {a1} * {b2} - {a2} * {b1} = {delta}\n"
        )
        if delta == 0:
            self.result_area.insert(
                tk.END,
                "\nEl sistema no tiene solución (Delta = 0).\n",
            )
            return

        # Calcular el determinante de Delta_x (intercambiando la columna de c)
        delta_x1 = c1 * b2 - c2 * b1
        self.result_area.insert(
            tk.END, f"\nMatriz Delta_x (reemplazo de columna de x):\n"
        )
        self.result_area.insert(tk.END, f" | {c1}  {b1} |\n")
        self.result_area.insert(tk.END, f" | {c2}  {b2} |\n")
        self.result_area.insert(
            tk.END,
            f"\nDeterminante de Delta_x = {c1} * {b2} - {c2} * {b1} = {delta_x1}\n",
        )

        # Calcular el determinante de Delta_y (intercambiando la columna de y)
        delta_y1 = a1 * c2 - a2 * c1
        self.result_area.insert(
            tk.END, f"\nMatriz Delta_y (reemplazo de columna de y):\n"
        )
        self.result_area.insert(tk.END, f" | {a1}  {c1} |\n")
        self.result_area.insert(tk.END, f" | {a2}  {c2} |\n")
        self.result_area.insert(
            tk.END,
            f"\nDeterminante de Delta_y = {a1} * {c2} - {a2} * {c1} = {delta_y1}\n",
        )

        # Calcular las soluciones finales
        x = Fraction(delta_x1, delta)
        y = Fraction(delta_y1, delta)

        # Mostrar las soluciones finales
        if x is not None and y is not None:
            # Separador visual
            self.result_area.insert(tk.END, "---------------------\n")
            # Mostrar la solución para x
            self.result_area.insert(
                tk.END, f"\nSolución para x: x = Delta_x / Delta = {x}\n"
            )
            # Mostrar la solución para y
            self.result_area.insert(
                tk.END, f"Solución para y: y = Delta_y / Delta = {y}\n"
            )
        else:
            self.result_area.insert(
                tk.END,
                f"\nEl sistema no tiene solución o tiene infinitas soluciones (Delta = 0).\n",
            )
            return

    def reiniciar(self):
        """
        Limpia todos los campos de entrada y el área de resultados para permitir
        un nuevo cálculo sin necesidad de reiniciar la aplicación.
        """
        self.entry_a1.delete(0, tk.END)
        self.entry_b1.delete(0, tk.END)
        self.entry_c1.delete(0, tk.END)
        self.entry_a2.delete(0, tk.END)
        self.entry_b2.delete(0, tk.END)
        self.entry_c2.delete(0, tk.END)
        self.result_area.delete(1.0, tk.END)


# Inicializar la calculadora si el script es ejecutado directamente
if __name__ == "__main__":
    calculadora = Calculadora()
    # print(html)
