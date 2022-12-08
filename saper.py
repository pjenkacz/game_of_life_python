from tkinter import *
from cell import Cell
import settings
import funkcje
root = Tk()
root.geometry(f'{settings.WIDTH}x{settings.HEIGTH}')
root.title('sAGHper')
root.resizable(False,False)
root.configure(bg='black', cursor='pirate')

top_frame = Frame(
    root,
    bg='black',
    width = settings.WIDTH,
    height = funkcje.percentage_heigth(25)

)
top_frame.place(x = 0 ,y = 0)

left_frame = Frame(
    root,
    width = funkcje.percentage_width(20),
    height = funkcje.percentage_heigth(75),
    bg = 'black'
)
left_frame.place(x = 0, y=funkcje.percentage_heigth(25))

center_frame = Frame(
    root,
    bg='blue',
    width = funkcje.percentage_width(80),
    height = funkcje.percentage_heigth(75)
)
center_frame.place(
    x = funkcje.percentage_width(20),
    y = funkcje.percentage_heigth(15)
)



for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c1 = Cell(x,y)
        c1.create_button_object(center_frame)
        c1.cell_btn_object.grid(
            column=x, row=y
        )
root.mainloop()