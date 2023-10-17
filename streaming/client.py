import tkinter

import cv2
import numpy as np
import socket
import threading
from ui import VideoChatUI
import tkinter as tk
import queue


class VideoChatClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 2323))
        print("Connected to server.")

        self.ui = VideoChatUI(tk.Tk(), "화상 채팅 클라이언트")
        self.ui.on_send_message = self.send_message_to_server

        # 메시지 수신 스레드 시작
        self.receive_thread = threading.Thread(target=self.receive_message)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.show_frame()

        # GUI 시작
        tk.mainloop()

    def show_frame(self):
        received_frame_data = self.client_socket.recv(65536)
        received_frame_array = np.frombuffer(received_frame_data, dtype=np.uint8)
        received_frame = cv2.imdecode(received_frame_array, cv2.IMREAD_COLOR)
        if received_frame is not None:
            self.ui.show_frame(received_frame)
        self.ui.window.after(100, self.show_frame)

    def send_message_to_server(self, message):
        print("Sending message to server:", message)
        self.client_socket.send(message.encode())

    def send_message_to_clients(self, message):
        self.ui.receive_message(message)

    def receive_message(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break
                self.send_message_to_clients(message)
            except:
                pass


if __name__ == "__main__":
    client = VideoChatClient()

'''
test
'''