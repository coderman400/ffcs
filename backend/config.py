# config.py
from pathlib import Path

# Define the root directory of your project
ROOT_DIR = Path(__file__).resolve().parent
UPLOADS = ROOT_DIR / "uploads"
HERE = lambda name,function :print(f"Called {function} from: {name}")