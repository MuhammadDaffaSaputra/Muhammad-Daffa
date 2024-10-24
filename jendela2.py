import PySimpleGUI as sg
sg.theme("DarkBlue9")
sg.theme_text_color("#00FFF")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Arial",25,"italic","bold","underline"))],
                           [sg.Text("NPM   : 2210010440 ")],
                           [sg.Text("Nama  : Muhammad Daffa Saputra ")],
                           [sg.Text("Kelas : 5B NonReg Banjarmasin ")]
                           ],
                   size=(510,200),
                   font=("Arial", 18))
window()
window.close()