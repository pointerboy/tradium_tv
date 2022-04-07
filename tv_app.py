import webview
import os 
import time

web_address = 'http://192.168.0.13:5000'


def refresh_webview(window):
    window.toggle_fullscreen()
    while True:
        time.sleep(120)
        window.load_url(web_address)        

if __name__ == '__main__':
    time.sleep(5)

    os.system("python3 ~/production/tradium_tv/webapp/app.py &")
    
    time.sleep(10) # wait for server to fully start
    
    window = webview.create_window('Tradium TV', web_address)
    webview.start(refresh_webview, window)
