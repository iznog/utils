import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import Label, Entry, Button 

class ConverterPDFToPDFA:

    def __init__(self,master):
        self.master=master
        master.title("PDF To PDF/A Converter")
        self.label=Label(master,text="Indique o ficheiro a converter")
        self.label.pack()

        self.originfile=Entry(master)
        self.originfile.pack()

        self.openfile=Button(master,text="Selecionar",command="open_file")
        self.openfile.pack()

        #fr_originfile = tk.Frame(window, relief=tk.RAISED, bd=2)
        #btn_open = tk.Button(fr_originfile, text="Selecciona ficheiro a converter:", command=open_file)





    def open_file():
        """Selecciona diretorio"""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        self.originfile=filepath
        # txt_edit.delete(1.0, tk.END)
        # with open(filepath, "r") as input_file:
        #     text = input_file.read()
        #     txt_edit.insert(tk.END, text)
        # window.title(f"Simple Text Editor - {filepath}")


def main():

    root = tk.Tk()
    App = ConverterPDFToPDFA(root)
    root.geometry("+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()


