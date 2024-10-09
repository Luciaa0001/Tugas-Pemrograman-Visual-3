import PySimpleGUI as g

susunan = [
    [g.Push(),
    g.Text("Uniska MAAB", font=("Helvetica", 24)),
    g.Push()],
    [g.Push(),
    g.Text("BANJARMASIN", font=("Courier", 18)),
    g.Push()]
]

window = g.Window(
    title="Elemen Text",
    layout=susunan,
    size=(430, 200)
)

window()
window.close()

# milik 
# Nama  : Muhammad Saman
# Npm   : 2210010053
# Kelas : 5P Reguler Pagi

