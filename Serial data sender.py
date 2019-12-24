
# import random
# import time
import tkinter as tk
from tkinter import  ttk
from tkinter.messagebox import showinfo

import bluetooth
from bluetooth import BluetoothSocket


window = tk.Tk()
window.title('SERIAL DATA SENDER')

window.configure(background="light grey")

# FOR CONNECTING DEEVICES


def connect():

    try:
        server_address_index = found_devices_list.index(device_select.get())

        server_address = nearby_devices[server_address_index]
        print(server_address)
        global sock
        sock = BluetoothSocket(RFCOMM)
        sock.connect((server_address, port_select.get()))
    except OSError:

        os_error()
    except ValueError:

        value_error()
    except NameError:
        value_error()

    else:
        paired()

        print(
            f'pairing succesfull {device_select.get()} having adress {server_address}')

        print('bounded')
        # sock.send("hello!!")
        # sock.close()


def send_data():

    # print(user_data.get())
    try:
        sock.send(user_data.get())
    except:
        os_error()


def sock_close():
    try:
        sock.close()

    except:
        os_error()
    else:
        conn_clos()
        print("connection closed")
# FOR SCANNING DEVICES


def bluetooth_finder():

    try:
        global nearby_devices
        nearby_devices = []
        nearby_devices = bluetooth.discover_devices()
        print(nearby_devices)

    except OSError:

        os_error()

    except:
        os_error()

    else:
        global found_devices_list
        found_devices_list = [bluetooth.lookup_name(
            found_device) for found_device in nearby_devices]
        print(found_devices_list)
        if found_devices_list:

            device_select_box['values'] = tuple(found_devices_list)


# POPUPS
def value_error():
    showinfo("Error", "Please Scan or Select Device first")


def os_error():
    showinfo("Error", "INTERNAL ERROR.TRY AGAIN")


def conn_clos():
    showinfo("Info", "connection closed succesfully")


def paired():
    showinfo("Info", f"CONNECTION SUCCESSFUL WITH {device_select.get()}")


# MAIN SCREEN GUI
ttk.Label(window, text='WELCOME\n NOTE:please wait 8-10 seconds after pressing scan button\n i). if not connected then restart the application\n ii). if problem continues contact admin..thanks'.upper(),
          font=("Courier", 14, "bold"), foreground='red', background="light grey").pack(pady=(10, 0))
tk.Button(window, text='SCAN', width=20, font=("Courier", 13, "bold"),
          bg="light blue", command=bluetooth_finder).pack(pady=(10, 0))
ttk.Label(window, background="light grey", text='select devices below for further action'.upper(
), font=("Courier", 14, "bold")).pack(pady=(10, 0))
global device_select
device_select = tk.StringVar()
device_select_box = ttk.Combobox(
    window, width=20, height=25, text='select device', state='readonly', textvariable=device_select)
device_select_box.pack()

ttk.Label(window, background="light grey", text='select port (usually no. 1)'.upper(
), font=("Courier", 14, "bold")).pack(pady=(10, 0))
global port_select
port_select = tk.IntVar()
port_selecet_box = ttk.Combobox(
    window, width=15, height=25, textvariable=port_select)
port_selecet_box.pack()
port_selecet_box['values'] = tuple([port_no for port_no in range(0, 31)])
port_selecet_box.current(1)

tk.Button(window, bg="light blue", width=18, text='Connect', font=(
    "Courier", 13, "bold"), command=connect).pack(pady=(10, 0))
user_data = tk.StringVar()
ttk.Entry(window, width=36, textvariable=user_data).pack(pady=(10, 0))

tk.Button(window, bg="light blue", width=14, text='SEND', font=(
    "Courier", 13, "bold"), command=send_data).pack(pady=(10, 0))
ttk.Label(window, background="light grey", text="Please press DONE when finished sending data to securely close connection",
          foreground="red", font=("Courier", 14, "bold")).pack(pady=(10, 0))
tk.Button(window, bg="light blue", width=14, text='DONE', font=(
    "Courier", 13, "bold"), command=sock_close).pack(pady=(10, 0))
window.mainloop()
