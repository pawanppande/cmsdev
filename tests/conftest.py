import sys
from pathlib import Path

# Make the function code in ../src importable for tests
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))