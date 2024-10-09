import PySimpleGUI as g

# Create the Window
g.theme("darkgreen4")
g.theme_text_color("#E3cf57")

window = g.Window('Profile',
            layout = [  
            [g.Text('SELAMAT DATANG DI PROFIL SAYA', font=("Arial", "14", "underline", "bold"))],
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
