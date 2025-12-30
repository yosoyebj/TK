# How to Build the Token Calculator .exe

Since you are on Windows, you can easily turn the Python script into a standalone `.exe` file using `pyinstaller`.

## Prerequisites
1.  **Python Installed**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
2.  **Install PyInstaller**: Open your command prompt (cmd) or PowerShell and run:
    ```bash
    pip install pyinstaller
    ```

## Build Steps
1.  Download the `calculator.py` file to a folder on your computer.
2.  Open your command prompt/terminal in that folder.
3.  Run the following command:
    ```bash
    pyinstaller --onefile --noconsole --name "TokenSplitter" calculator.py
    ```
    *   `--onefile`: Bundles everything into a single .exe file.
    *   `--noconsole`: Hides the black command window when running the app (so only the GUI shows).
    *   `--name "TokenSplitter"`: Names your output file "TokenSplitter.exe".

4.  Once finished, look for a `dist` folder in the same directory.
5.  Inside `dist`, you will find `TokenSplitter.exe`. You can run this file or share it with others.
