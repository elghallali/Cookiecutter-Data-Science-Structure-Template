import os
from pathlib import Path


list_of_files = [
   ".github/workflows/ci.yaml",
   "src/__init__.py",
   "src/data/__init__.py",
   "src/data/make_dataset.py",
   "src/features/__init__.py",
   "src/features/build_features.py",
   "src/models/__init__.py",
   "src/models/predict_model.py",
   "src/models/train_model.py",
   "src/visualization/__init__.py",
   "src/visualization/visualize.py",
   "data/external/",
   "data/interim/",
   "data/processed/",
   "data/raw/",
   "docs/",
   "models/",
   "notebooks/",
   "referances/",
   "reports/figures/",
   "requirements.txt",
   "setup.py",
   "Makefile",
   "tox.ini"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w", encoding="utf-8") as f:
            pass # create an empty file

#its updated