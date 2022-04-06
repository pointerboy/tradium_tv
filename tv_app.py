import webview
import time

web_address = 'http://127.0.01:5000'

def refresh_webview():
    while True:
        time.sleep(180)
        window.load_url(web_address)        


def toggle_fullscreen(window):
    time.sleep(1.0)

    window.toggle_fullscreen()


if __name__ == '__main__':
    window = webview.create_window('Tradium TV', web_address)
    webview.start(toggle_fullscreen, window)
