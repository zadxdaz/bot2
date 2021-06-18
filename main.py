import time

import PySimpleGUI as sg
import keyboard
import pyautogui as pg
import keyboard as key


def que_color_es_la_flecha(x, y):
    pixel = pg.pixel(x, y)
    print(pixel)

def buscar_tren(imagen):
    try:
        pos = pg.center(pg.locateOnScreen(imagen,confidence=0.9))
        print(pos)
        return pos
    except:
        print("error al buscar el tren")
        return False
def click_on_thing(imagen):
    if buscar_tren(imagen) != False:
        pg.click(buscar_tren(imagen))


def menu():
    layout = [[sg.Button("Setear flecha", key="set_flecha")],
              [sg.Button("Empezar", key="start")],
              [sg.Button("Stop", key="stop"),sg.Input(" ",key="IN"),sg.FileBrowse("Buscar imagen del tren",key="tren_imag",target="IN")],
              [sg.Button("Probar Tren",key="tren"),sg.Button("Start auto tren",key="start_tren")],
              [sg.Text("Color         ", key="color")]]
    window = sg.Window("Menu", layout)
    return window


def main():
    flecha_x = 0
    flecha_y = 0
    menu_window = menu()
    proceso = False
    process_timer = 0
    tren_imagen_link="tren_notebook.png"
    tren_timer=0
    tren_process=False
    while True:
        event, values = menu_window.read(timeout=100)
        if event == sg.WIN_CLOSED:
            break
        if event == "set_flecha":
            while True:
                if key.is_pressed("c"):
                    flecha_x, flecha_y = pg.position()
                    break
        if event == "stop":
            proceso = False
        if proceso == True :
            if process_timer == 0:
                process_timer = time.time()
            if time.time() >= process_timer:
                color = pg.pixel(flecha_x, flecha_y)
                menu_window["color"].update(color)
                if pg.pixelMatchesColor(flecha_x, flecha_y, (255, 255, 255), tolerance=10):
                    print("white")
                process_timer = process_timer + 5.0

        if event == "start":
            if flecha_x == 0 or flecha_y == 0:
                print("No seteaste la flecha pelotudo")
                continue
            proceso = True
        if event == "tren_imag":
            print(values["IN"])
            print("a")

        if event == "tren":
            tren_imagen_link=values["IN"]
            click_on_thing(tren_imagen_link)

        if event== "start_tren":
            tren_process=True

        if tren_process:
            if tren_timer == 0:
                tren_timer = time.time()
                continue
            if time.time() >= tren_timer:
                click_on_thing(tren_imagen_link)
                tren_timer += 300


if __name__ == '__main__':
    main()
