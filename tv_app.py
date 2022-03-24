import webview
import time

def toggle_fullscreen(window):
    time.sleep(1.0)

    window.toggle_fullscreen()


if __name__ == '__main__':
    window = webview.create_window('Tradium TV', 'http://127.0.01:5000')
    webview.start(toggle_fullscreen, window)
