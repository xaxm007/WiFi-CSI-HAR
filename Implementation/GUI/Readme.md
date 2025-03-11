# GUI for PyTorch Models with Tkinter

This GUI is developed using the Tkinter library. You can integrate it with PyTorch models by modifying specific files to fit your use case.

## Setup

### Modifying the Model
To use your own PyTorch models, make the necessary changes in the following files:

- [`models/inference.py`](models/inference.py) – Adjust inference logic as needed.
- [`models/models.py`](models/models.py) – Define or modify the model architecture.

### Running the Client
The [`client.py`](client.py) script should be executed on a Raspberry Pi or any client device running the Nexmon firmware.

### Preprocessing
Real-time preprocessing is enabled. If you need to tweak it, modify:

- [`preprocess/preprocess.py`](preprocess/preprocess.py)

## Usage
1. Ensure all dependencies are installed.
2. Run `client.py` on the Raspberry Pi.
3. Start the GUI application.

## Dependencies
Ensure you have the following installed:
- Python 3.x
- Tkinter
- PyTorch
- Nexmon firmware (for Raspberry Pi)

## License
This project is open-source. Feel free to modify and use it as needed.

---

