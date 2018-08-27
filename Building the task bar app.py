#### fail!!!!! 1.WINDOWS needs the notifications from other apps avaliable
#### fail!!!!! 2.also stuff like notify is broken also another needs issuse support



#import kivy
#from plyer.facades import Notification as n

#n = n.notify

#n(
#    title = 'Service-Now Notification App',
#    message = 'TEST TEST TEST TEST TEST TEST TEST TEST',
#    app_name = 'Service-Now Notification',
#    app_icon = './icons8-sonic-the-hedgehog-filled.png',
#    ticker = 'Notification',)

import time
from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast("Hello World!!!",
                    "Python is 10 seconds awsm!",
                   icon_path="./icons8_sonic_the_hedgehog_filled_32W_icon.ico",
                   duration=20)
while toaster.notification_active(): time.sleep(0.1)

#rom win32api import *
#rom win32gui import *
#mport win32con
#mport sys, os
#mport struct
#mport time
#
#
#lass WindowsBalloonTip:
#   def __init__(self, title, msg):
#       message_map = {
#           win32con.WM_DESTROY: self.OnDestroy,
#       }
#       # Register the Window class.
#       wc = WNDCLASS()
#       hinst = wc.hInstance = GetModuleHandle(None)
#       wc.lpszClassName = "PythonTaskbar"
#       wc.lpfnWndProc = message_map  # could also specify a wndproc.
#       classAtom = RegisterClass(wc)
#       # Create the Window.
#       style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
#       self.hwnd = CreateWindow(classAtom, "Taskbar", style, \
#                                0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
#                                0, 0, hinst, None)
#       UpdateWindow(self.hwnd)
#       iconPathName = os.path.abspath(os.path.join(sys.path[0], "balloontip.ico"))
#       icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
#       try:
#           hicon = LoadImage(hinst, iconPathName, \
#                             win32con.IMAGE_ICON, 0, 0, icon_flags)
#       except:
#           hicon = LoadIcon(0, win32con.IDI_APPLICATION)
#       flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
#       nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "tooltip")
#       Shell_NotifyIcon(NIM_ADD, nid)
#       Shell_NotifyIcon(NIM_MODIFY, \
#                        (self.hwnd, 0, NIF_INFO, win32con.WM_USER + 20, \
#                         hicon, "Balloon  tooltip", title, 200, msg))
#       # self.show_balloon(title, msg)
#       time.sleep(10)
#       DestroyWindow(self.hwnd)
#
#   def OnDestroy(self, hwnd, msg, wparam, lparam):
#       nid = (self.hwnd, 0)
#       Shell_NotifyIcon(NIM_DELETE, nid)
#       PostQuitMessage(0)  # Terminate the app.
#
#
#ef balloon_tip(title, msg):
#   w = WindowsBalloonTip(msg, title)
#   print(w)
#
#itle = 'lmao kill me'
#rint(balloon_tip(title,title))




#import notify2
#
#
#
#
#def notify():
#    icon_path = './icons8_sonic_the_hedgehog_filled_32W_icon.ico'
#    notify2.init('Service-Now Notification')
#    n = notify2.Notification('Service-Now Notification',icon=icon_path)
#    n.set_urgency(notify2.URGENCY_CRITICAL)
#    n.set_timeout(10)
#    text = 'lmao i hope this works'
#    n.update('Alert',text)
#    n.show()
#notify



