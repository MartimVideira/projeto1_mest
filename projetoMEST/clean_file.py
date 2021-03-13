import tkinter as tk
from tkinter import filedialog
import cleaner as cl


def get_file(operacao, percentagem):

    filepath = filedialog.askopenfilename(
        initialdir="/", title="Select File To Clean Up", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

    if operacao == 2:
        cl.remove_below_40(filepath, int(percentagem))

    if operacao == 1:
        cl.change_mail_code(filepath)

    if operacao == 0:
        print(cl.dic_percent(filepath))


base = tk.Tk()
base.title('MEST Grupo T3-11')

operacao = tk.IntVar()
operacao.set(-1)

percent_radio = tk.Radiobutton(
    base, text='Percentagens dados em Falta', variable=operacao, value=0)
percent_radio.grid(column=0, row=0, sticky='W')

address_state_radio = tk.Radiobutton(
    base, text='Formatar o endereço', variable=operacao, value=1)
address_state_radio.grid(column=0, row=1, sticky='W')

remove_below_radio = tk.Radiobutton(
    base, text='Remover dados em Falta  Percentagem: ', variable=operacao, value=2)
remove_below_radio.grid(column=0, row=2, sticky='W')
percent_entry = tk.Entry(base)
percent_entry.grid(column=1, row=2, sticky='W')

continue_button = tk.Button(
    base, text='Escolher CSV', height=5, width=15, command=lambda: get_file(operacao.get(), percent_entry.get()))
continue_button.grid(column=0, row=3)


base.mainloop()

# cl.change_mail_code(filename)
