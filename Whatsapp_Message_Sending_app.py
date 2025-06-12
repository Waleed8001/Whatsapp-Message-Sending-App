import os
from pathlib import Path

script_path = Path(__file__).resolve().parent / "home.py"
os.system(f"streamlit run {script_path}")


