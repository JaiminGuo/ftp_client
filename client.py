#!/usr/bin/env python
"FTP Server Module"
import tkinter
from tkinter import END
import ftplib
FTP_CLIENT = ftplib.FTP()


def connectserver():
    "连接服务器"
    server_ip = ENT_IP.get()
    port = int(ENT_PORT.get())
    try:
        msg = FTP_CLIENT.connect(server_ip, port)
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, msg)
        LBL_LOGIN.place(x=150, y=20)
        ENT_LOGIN.place(x=150, y=40)
        LBL_PASSWD.place(x=150, y=60)
        ENT_PASSWD.place(x=150, y=80)
        BTN_LOGIN.place(x=182, y=110)
    except BaseException:
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, "Unable to connect")


def loginserver():
    "登陆服务器"
    user = ENT_LOGIN.get()
    password = ENT_PASSWD.get()
    try:
        msg = FTP_CLIENT.login(user, password)
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, msg)
        displaydir()
        LBL_LOGIN.place_forget()
        ENT_LOGIN.place_forget()
        LBL_PASSWD.place_forget()
        ENT_PASSWD.place_forget()
        BTN_LOGIN.place_forget()
    except BaseException:
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, "Unable to login")


def displaydir():
    "显示目录"
    dirlist = []
    LIBOX_SERVERDIR.insert(0, "--------------------------------------------")
    dirlist = FTP_CLIENT.nlst()
    for item in dirlist:
        LIBOX_SERVERDIR.insert(0, item)

# FTP commands


def changedirectory():
    "更改目录"
    directory = ENTINPUT.get()
    try:
        msg = FTP_CLIENT.cwd(directory)
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, msg)
    except BaseException:
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, "Unable to change directory")
    displaydir()


def createdirectory():
    "创建目录 "
    directory = ENTINPUT.get()
    try:
        msg = FTP_CLIENT.mkd(directory)
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, msg)
    except BaseException:
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, "Unable to create directory")
    displaydir()


def deletedirectory():
    "删除目录 "
    directory = ENTINPUT.get()
    try:
        msg = FTP_CLIENT.rmd(directory)
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, msg)
    except BaseException:
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, "Unable to delete directory")
    displaydir()


def deletefile():
    "删除文件"
    file = ENTINPUT.get()
    try:
        msg = FTP_CLIENT.delete(file)
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, msg)
    except BaseException:
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, "Unable to delete file")
    displaydir()


def downloadfile():
    "下载文件"
    file = ENTINPUT.get()
    down = open(file, "wb")
    try:
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, "Downloading " + file + "...")
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, FTP_CLIENT.retrbinary("RETR " + file, down.write))
    except BaseException:
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, "Unable to download file")
    displaydir()


def uploadfile():
    "上传文件"
    file = ENTINPUT.get()
    try:
        file_up = open(file, "rb")
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, "Uploading " + file + "...")
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, FTP_CLIENT.storbinary("STOR " + file, file_up))
    except BaseException:
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, "Unable to upload file")
    displaydir()


def closeconnection():
    "关闭连接"
    try:
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, "Closing connection...")
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, FTP_CLIENT.quit())
    except BaseException:
        TEXT_SERVERMSG.insert(END, "\n")
        TEXT_SERVERMSG.insert(END, "Unable to disconnect")


WINDOW = tkinter.Tk()
WINDOW.title("FTP Client")
WINDOW.wm_iconbitmap("favicon.jpg")
WINDOW.geometry("1000x600")

# Connect
LBL_IP = tkinter.Label(WINDOW, text="IP Address")
ENT_IP = tkinter.Entry(WINDOW)
ENT_IP.insert(0, "192.168.1.104")
LBL_PORT = tkinter.Label(WINDOW, text="Port")
ENT_PORT = tkinter.Entry(WINDOW)
ENT_PORT.insert(0, "21")
BTN_CONNECT = tkinter.Button(WINDOW, text="Connect", command=connectserver)

# Server response text box
TEXT_SERVERMSG = tkinter.Text(WINDOW)

# Login
LBL_LOGIN = tkinter.Label(WINDOW, text="Username")
ENT_LOGIN = tkinter.Entry(WINDOW)
ENT_LOGIN.insert(0, "root")
LBL_PASSWD = tkinter.Label(WINDOW, text="Password")
ENT_PASSWD = tkinter.Entry(WINDOW)
ENT_PASSWD.insert(0, "admin")
BTN_LOGIN = tkinter.Button(WINDOW, text="Login", command=loginserver)
# Directory listing
LBL_DIR = tkinter.Label(WINDOW, text="Directory listing:")
LIBOX_SERVERDIR = tkinter.Listbox(WINDOW, width=40, height=14)

# Options
LBL_INPUT = tkinter.Label(WINDOW, text="Input")
ENTINPUT = tkinter.Entry(WINDOW)
BTN_CHDIR = tkinter.Button(
    WINDOW, text="Change Directory", command=changedirectory, width=15)
BTN_CRDIR = tkinter.Button(
    WINDOW, text="Create Directory", command=createdirectory, width=15)
BTN_DELDIR = tkinter.Button(
    WINDOW, text="Delete Directory", command=deletedirectory, width=15)
BTN_DELFILE = tkinter.Button(
    WINDOW, text="Delete File", command=deletefile, width=15)
BTN_DOWNFILE = tkinter.Button(
    WINDOW, text="Download File", command=downloadfile, width=15)
BTN_UPFILE = tkinter.Button(
    WINDOW, text="Upload File", command=uploadfile, width=15)
BTN_QUIT = tkinter.Button(WINDOW, text="Disconnect",
                          command=closeconnection, width=15)

# Place widgits
LBL_IP.place(x=20, y=20)
ENT_IP.place(x=20, y=40)
LBL_PORT.place(x=20, y=60)
ENT_PORT.place(x=20, y=80)
BTN_CONNECT.place(x=52, y=110)
TEXT_SERVERMSG.place(x=20, y=150)

LBL_DIR.place(x=700, y=143)
LIBOX_SERVERDIR.place(x=700, y=165)

LBL_INPUT.place(x=700, y=400)
ENTINPUT.place(x=700, y=420)
BTN_CHDIR.place(x=700, y=450)
BTN_CRDIR.place(x=700, y=480)
BTN_DELDIR.place(x=700, y=510)
BTN_DELFILE.place(x=700, y=540)

BTN_DOWNFILE.place(x=850, y=450)
BTN_UPFILE.place(x=850, y=480)
BTN_QUIT.place(x=850, y=510)


# Create
WINDOW.mainloop()
