# # # # # # # import os
# # # # # # # import subprocess
# # # # # # # import ctypes
# # # # # # # import sys

# # # # # # # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# # # # # # # file_path = os.path.join(os.path.dirname(__file__), "Home.py")
# # # # # # # subprocess.Popen(["streamlit", "run", file_path], shell=True)

# # # # # import os
# # # # # import subprocess
# # # # # import ctypes
# # # # # import sys

# # # # # # Hide the console window
# # # # # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# # # # # # Handle path correctly in both script and PyInstaller .exe mode
# # # # # if getattr(sys, 'frozen', False):
# # # # #     base_path = sys._MEIPASS  # Extracted temp folder used by PyInstaller
# # # # # else:
# # # # #     base_path = os.path.dirname(__file__)

# # # # # file_path = os.path.join(base_path, "Home.py")

# # # # # # Use python -m streamlit for better reliability
# # # # # subprocess.Popen(f"python -m streamlit run \"{file_path}\"", shell=True)


# # # # # # import os
# # # # # # import subprocess
# # # # # # import ctypes
# # # # # # import sys
# # # # # # import logging

# # # # # # # Setup logging
# # # # # # logging.basicConfig(filename="app_log.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")
# # # # # # logging.debug("Launcher started")

# # # # # # # Hide console window
# # # # # # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# # # # # # try:
# # # # # #     # Determine correct file path in .exe or .py mode
# # # # # #     if getattr(sys, 'frozen', False):
# # # # # #         base_path = sys._MEIPASS
# # # # # #     else:
# # # # # #         base_path = os.path.dirname(__file__)

# # # # # #     file_path = os.path.join(base_path, "Home.py")
# # # # # #     logging.debug(f"Resolved Home.py path: {file_path}")

# # # # # #     # Run the streamlit app
# # # # # #     result = subprocess.Popen(f'python -m streamlit run "{file_path}"', shell=True)
# # # # # #     logging.debug("Streamlit command executed")

# # # # # # except Exception as e:
# # # # # #     logging.error(f"Error occurred: {e}")


# # # # import os
# # # # import subprocess
# # # # import ctypes
# # # # import sys
# # # # import logging

# # # # # Setup logging
# # # # logging.basicConfig(filename="app_log.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")
# # # # logging.debug("Launcher started")

# # # # # Hide console window
# # # # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# # # # try:
# # # #     # Determine correct file path in .exe or .py mode
# # # #     if getattr(sys, 'frozen', False):
# # # #         base_path = sys._MEIPASS
# # # #     else:
# # # #         base_path = os.path.dirname(__file__)

# # # #     file_path = os.path.join(base_path, "Home.py")
# # # #     logging.debug(f"Resolved Home.py path: {file_path}")

# # # #     # Use the same Python interpreter as the executable
# # # #     python_executable = sys.executable
# # # #     cmd = f'"{python_executable}" -m streamlit run "{file_path}"'
# # # #     logging.debug(f"Command: {cmd}")
# # # #     subprocess.Popen(cmd, shell=True)

# # # # except Exception as e:
# # # #     logging.error(f"Error occurred: {e}")


# # # import subprocess
# # # import os
# # # import ctypes

# # # # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
# # # streamlit_path = os.path.join(os.path.dirname(__file__), 'Home.py')
# # # subprocess.Popen(['streamlit', 'run', streamlit_path])

# # import os
# # import subprocess
# # import sys

# # # Get correct path inside PyInstaller bundle
# # if hasattr(sys, '_MEIPASS'):
# #     base_path = sys._MEIPASS
# # else:
# #     base_path = os.path.dirname(os.path.abspath(__file__))

# # file_path = os.path.join(base_path, "Home.py")

# # subprocess.Popen(["streamlit", "run", file_path])


# import os
# import subprocess
# import ctypes
# import sys

# # Hide the console window
# ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# # Path to bundled Home.py in temp folder (when packaged with PyInstaller)
# base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
# home_path = os.path.join(base_path, "Home.py")

# # Launch Streamlit
# subprocess.Popen(["streamlit", "run", home_path])


# run_app.py
# import os
# os.system("streamlit run Home.py")

import os
from pathlib import Path

script_path = Path(__file__).resolve().parent / "home.py"
os.system(f"streamlit run {script_path}")


# import os
# import sys
# from pathlib import Path

# script_path = Path(__file__).resolve().parent / "home.py"

# log_file = Path(__file__).resolve().parent / "error.log"

# try:
#     os.system(f"streamlit run {script_path} --server.headless true --server.port 8501")
# except Exception as e:
#     with open(log_file, "a") as f:
#         f.write(str(e) + "\n")

