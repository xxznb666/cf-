import pywinio
import time
import atexit

# KeyBoard Commands
# Command port
KBC_KEY_CMD = 0x64
# Data port
KBC_KEY_DATA = 0x60

g_winio = None


def get_winio():
    global g_winio

    if g_winio is None:
        g_winio = pywinio.WinIO()
            
        def __clear_winio():
            global g_winio
            g_winio = None
            
        atexit.register(__clear_winio)
            
    return g_winio


def wait_for_buffer_empty():
    '''
    Wait keyboard buffer empty
    '''

    winio = get_winio()

    dwRegVal = 0x02
    while (dwRegVal & 0x02):
        dwRegVal = winio.get_port_byte(KBC_KEY_CMD)


def key_down(scancode):
    winio = get_winio()
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_DATA, scancode)

def key_up(scancode):
    winio = get_winio()

    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_DATA, scancode | 0x80)


def key_press(scancode):
    key_down(scancode)
    key_up(scancode)
    