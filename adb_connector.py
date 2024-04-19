import os

'''This program connects the android over adb automatically
    you need turn on USB Debugging on android and connect android to laptop
    then run this code.
    It will find ip address of android automatically and connects the android over adb'''

def connect_android():
        
    ip = os.popen('adb shell ifconfig')
    output = ip.read()
    ip_adds = []
    a=output.split()
    for i in a:
        if 'addr:' in i:
            i= i.split(':')
            if i[1]=='':
                pass
            else:
                ip_adds.append(i[1])

    os.system('adb tcpip 4444')
    connected = 0
    print(ip_adds)
    for ip in ip_adds:
        print('cnnected ',connected)
        if connected ==0:
            connection = os.popen('adb connect '+str(ip)+':4444').read()
            print(connection)
            if 'connected to ' in connection:
            # if 'connected to' in (os.popen('adb connect '+str(ip)+':4444')):
                
                connected = 1
                print(' heeyyyy  connected')
                break

            else:
                print('continuning ',ip)
                continue
        else:
            print('wokking')
            break

connect_android()
