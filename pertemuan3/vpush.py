import PySimpleGUI as g

susunan = [
    [g.VPush(),
    g.Text("Uniska MAAB", font=("Helvetica", 24)),
    g.Push()],
    [g.Push(),
    g.Text("BANJARMASIN", font=("Courier", 18)),
    g.Push()],
    [g.VPush()]
]

window = g.Window(
    title="Elemen Text",
    layout=susunan,
    size=(430, 200)
)

window.read()
window.close()

# milik 
# Nama  : Muhammad Saman
# Npm   : 2210010053
# Kelas : 5P Reguler Pagi

