import PySimpleGUI as g

# Create the Window
g.theme("darkgreen4")

window = g.Window('Window Title',
            layout = [  
            [g.Text('NPM        :         2210010053')],
            [g.Text('Nama       :         Muhammad Saman')],
            [g.Text('Kelas        :        5P Reguler Pagi')],
            [g.Text('Matkul     :         Pemrograman Visual')]
        ], size=(400,200), font=("Times", "12"))

window()
window.close()

# milik 
# Nama  : Muhammad Saman
# Npm   : 2210010053
# Kelas : 5P Reguler Pagi
