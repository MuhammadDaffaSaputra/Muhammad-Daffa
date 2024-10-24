import PySimpleGUI as sg
sg.theme("DarkBlue9")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM     : 2210010440")],
                           [sg.Text("Nama    : Muhammad Daffa Saputra")],
                           [sg.Text("Kelas   : 5B NonReg Banjarmasin")],
                           [sg.Text("Matkul  : Pemrograman Visual 3")],
                           ],
                        size=(400,200))
window()
window.close()