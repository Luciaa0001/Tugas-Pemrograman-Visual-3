import PySimpleGUI as g

susunan=[[g.Text("UNISKA MAB", font=("helvetica", 24))],
        [g.Text("BANJARMASIN", font=("Courier", 18))]]

window = g.Window(
                title = "new icon",
                layout = susunan,
                element_justification = "center",
                icon = "favicon.ico",
                size=(430,200)
                )

window.read()
window.close()

# milik 
# Nama  : Muhammad Saman
# Npm   : 2210010053
# Kelas : 5P Reguler Pagi
