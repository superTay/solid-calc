import tkinter as tk
from tkinter import messagebox
from domain.evaluator import evaluate_expression


class CalculatorUI:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.master.title("Calculator")
        self.master.resizable(False, False)

        self.display_var = tk.StringVar()
        self.expression = ""

        self._build_layout()

    def _build_layout(self):
        entry = tk.Entry(self.master, textvariable=self.display_var, font=("Arial", 20), bd=8, relief=tk.RIDGE, justify='right')
        entry.grid(row=0, column=0, columnspan=4, padx=8, pady=8, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0),
        ]

        for (text, r, c) in buttons:
            if text == '=':
                btn = tk.Button(self.master, text=text, width=32, height=2, command=self.calculate)
                btn.grid(row=r, column=c, columnspan=4, padx=4, pady=4, sticky="nsew")
            else:
                btn = tk.Button(self.master, text=text, width=8, height=2, command=lambda t=text: self.on_button(t))
                btn.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

        for i in range(6):
            self.master.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.master.grid_columnconfigure(j, weight=1)

    def on_button(self, char: str):
        if char == 'C':
            self.expression = ""
            self.display_var.set("")
            return
        self.expression += char
        self.display_var.set(self.expression)

    def calculate(self):
        try:
            result = evaluate_expression(self.expression)

            # Mostrar sin notación innecesaria
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression = str(result)
            self.display_var.set(self.expression)
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir por cero")
        except Exception:
            messagebox.showerror("Error", "Expresión inválida")
            self.expression = ""
            self.display_var.set("")


def main():
    root = tk.Tk()
    app = CalculatorUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
