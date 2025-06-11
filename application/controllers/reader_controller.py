import tkinter as tk
from tkinter import messagebox

produtos = {
    "7702018001071": ("Gillette Mach 3", 26.00),
    "7896799210132": ("Tempero Noz Moscada", 1.82)
    
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
