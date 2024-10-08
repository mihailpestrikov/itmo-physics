import pygame_menu

import program

screen = program.screen


def draw_background():
    screen.fill('white')


def on_start():
    menu_data = menu.get_input_data()
    m1 = menu_data['M1']
    m2 = menu_data['M2']
    return program.main_loop(m1, m2)


menu = pygame_menu.Menu('', 700, 300)

menu.add.text_input('M1 weight: ', default='10000', textinput_id='M1')
menu.add.text_input('M2 weight: ', default='1', textinput_id='M2')

menu.add.button(title="Start", action=on_start)

menu.mainloop(screen, draw_background)
