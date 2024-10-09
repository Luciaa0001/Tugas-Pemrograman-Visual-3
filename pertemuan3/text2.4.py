import PySimpleGUI as g

# Create the Window
g.theme("darkgreen4")
g.theme_text_color("#FFFF00")

window = g.Window('Profile',
            layout = [  
            [g.Text('FTI UNISKA', font=("Helvetica, 24"))],
            [g.Text('FAKULTAS TEKNOLOGI INFORMASI', font=('courier',18,'italic','bold','underline'))],
            [g.Text('UNISKA MAB BANJARMASIN', text_color=("#ffcc00"))]
        ], size=(430,200), font=("Times", "18"))

window()
window.close()

# milik 
# Nama  : Muhammad Saman
# Npm   : 2210010053
# Kelas : 5P Reguler Pagi
