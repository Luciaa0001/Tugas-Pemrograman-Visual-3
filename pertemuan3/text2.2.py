import PySimpleGUI as g

# Create the Window
g.theme("darkgreen4")
g.theme_text_color("#FFFF00")

layout = [
    [g.Text('FAKULTAS TEKNOLOGI INFORMASI', size=(25, 1), justification="center")],
    [g.Text('FAKULTAS TEKNOLOGI INFORMASI', size=(25, 1), justification="left")],
    [g.Text('FAKULTAS TEKNOLOGI INFORMASI', size=(25, 1), justification="right")],
    [g.Text(('FAKULTAS TEKNOLOGI INFORMASI' + '') * 2, size=(25, 2), justification="center")],
    [g.Text('UNISKA MAB BANJARMASIN', text_color=("#ffcc00"))]
]

window = g.Window('Profile', layout, size=(430, 200), font=("Times", 18))

window()
window.close()

# milik 
# Nama  : Muhammad Saman
# Npm   : 2210010053
# Kelas : 5P Reguler Pagi

