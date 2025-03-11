import tkinter as tk
import threading
from queue import Queue, Empty
from PIL import Image, ImageTk
import server1  # Import server module

# Queue for receiving predictions from the server
prediction_queue = server1.prediction_queue

# GUI application
def create_gui():
    my_w = tk.Tk()
    my_w.geometry("1000x800")
    my_w.title("CSI Explorer GUI")
    Normal_font = ("Ubuntu", 14)

    # Load and resize the background image
    bg = Image.open("./bg.jpg")
    bg = bg.resize((1000, 800), Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(bg)

    background_label = tk.Label(my_w, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    l1 = tk.Label(my_w, text="Connect to Server", font=Normal_font, bg="lightblue")
    l1.grid(row=0, column=0, columnspan=2, pady=30)

    prediction_label = tk.Label(my_w, text="Waiting for prediction...", font=Normal_font, bg="lightblue")
    prediction_label.grid(row=1, column=0, columnspan=2, pady=30)

    def update_prediction_label():
        try:
            pred = prediction_queue.get_nowait()
            prediction_label.config(text=f"Prediction: {pred}", font='white')
        except Empty:
            pass
        finally:
            my_w.after(100, update_prediction_label)

    def start_server_thread():
        server_thread = threading.Thread(target=server1.start_server, daemon=True)
        server_thread.start()

    b1 = tk.Button(my_w, text="Connect", width=20, command=start_server_thread)
    b1.grid(row=2, column=0, columnspan=2, pady=30)

    my_w.grid_columnconfigure(0, weight=1)
    my_w.grid_columnconfigure(1, weight=1)
    my_w.grid_rowconfigure(0, weight=1)
    my_w.grid_rowconfigure(1, weight=1)
    my_w.grid_rowconfigure(2, weight=1)

    my_w.resizable(0, 0)

    update_prediction_label()  # Start updating the prediction label
    my_w.mainloop()

if __name__ == "__main__":
    create_gui()