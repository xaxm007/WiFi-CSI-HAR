# Frontend

This GUI is developed using the Tkinter library. You can integrate it with PyTorch models by modifying specific files to fit your use case.

## Setup

### Modifying the Model
To use your own PyTorch models, make the necessary changes in the following files:

- [`models/inference.py`](./Frontend/model/inference.py): Adjust inference logic as needed.
- [`models/models.py`](./Frontend/model/models.py): Define or modify the model architecture.

### Preprocessing
If you need to tweak it, modify: [`preprocess/preprocess.py`](./Frontend/preprocess/process.py)

---

# Backend
The [`ClientPi.py`](./Backend/ClientPi.py) script should be executed on a Raspberry Pi or any client device running the Nexmon firmware.

---
## Usage
- Ensure all dependencies are installed.
- Run `ClientPi.py` on the Raspberry Pi.
- Run `gui.py` on the receiving laptop.

## Dependencies
Ensure you have the following installed:
- Python 3.x
- Tkinter
- PyTorch
- [Nexmon firmware](../Setup/) (for Raspberry Pi)

    ```bash
        pip install -r requirements.txt
    ```
    or
    ```bash
        conda env create -f environment.yml
    ```

## License
This project is open-source. Feel free to modify and use it as needed.

---

