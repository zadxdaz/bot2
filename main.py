import time

import PySimpleGUI as sg
import keyboard
import pyautogui as pg
import keyboard as key


def que_color_es_la_flecha(x, y):
    pixel = pg.pixel(x, y)
    print(pixel)


def menu():
    layout = [[sg.Button("Setear flecha", key="set_flecha")],
              [sg.Button("Empezar", key="start")],
              [sg.Button("Stop", key="stop")],
              [sg.Text("Color         ", key="color")]]
    window = sg.Window("Menu", layout)
    return window


def main():
    flecha_x = 0
    flecha_y = 0
    menu_window = menu()
    proceso = False
    tiempo = 0
    while True:
        event, values = menu_window.read(timeout=34)
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
            if tiempo == 0:
                tiempo = time.time()
            if time.time() >= tiempo:
                color = pg.pixel(flecha_x, flecha_y)
                menu_window["color"].update(color)
                if pg.pixelMatchesColor(flecha_x, flecha_y, (255, 255, 255), tolerance=10):
                    print("white")
                tiempo = tiempo + 5.0

        if event == "start":
            if flecha_x == 0 or flecha_y == 0:
                print("No seteaste la flecha pelotudo")
                continue
            proceso = True


if __name__ == '__main__':
    main()
