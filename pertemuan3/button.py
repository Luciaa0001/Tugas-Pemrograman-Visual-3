import PySimpleGUI as g
g.theme("Darkgreen4")
g.theme_text_color("#FFFF00")

window = g.Window(
                title = "contoh button",
                layout = [
                    [g.Text("Contoh Button")],
                    [g.Button("Button Simpan")],
                    [g.Button("Button Keluar")]
                    ],
                size = (400,200),
                font = ("Times", 18)
                )

kejadian,nilai = window.read()
print(kejadian, "=>", nilai)
window.close()

# milik 
# Nama  : Muhammad Saman
# Npm   : 2210010053
# Kelas : 5P Reguler Pagi
