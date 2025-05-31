import tkinter as tk
from tkinter import messagebox

produtos = {
    "7896102502756": ("Ketchup", 7.50),
    "7891108035321": ("Garrafa térmica", 49.90),
    "7891193010074": ("Pão :)", 7.90),
    "7898641074473": ("Whey Protein Shake velho que Karina abandonou", 7.90)
}

class ReaderController:
    def process_barcode(barcode: str):
        # Initialize Tkinter root window (it will be hidden by default for messagebox)
        root = tk.Tk()
        root.withdraw() # Hide the main window

        if barcode in produtos:
            product_name = produtos[barcode][0]
            product_price = produtos[barcode][1]
            message = f'{product_name}: R${product_price:.2f}' # Format price to 2 decimal places
            title = "Informações do Produto"
            messagebox.showinfo(title, message) # Show an info pop-up
        else:
            message = "Produto não cadastrado. Envie à equipe de gestão de estoque."
            title = "Produto Não Encontrado"
            messagebox.showerror(title, message) # Show an error pop-up

        root.destroy() # Destroy the hidden root window after the pop-up is closed
