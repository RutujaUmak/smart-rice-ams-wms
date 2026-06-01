# First run: pip install roboflow
from roboflow import Roboflow
import os

# Initialize Roboflow API
rf = Roboflow(api_key="YOUR_ROBOFLOW_API_KEY")

# Create target directory
os.makedirs("datasets", exist_ok=True)
os.chdir("datasets")

# Example 1: Download Gunny Bag Counting Dataset (YOLOv8/v11 format)
project_bags = rf.workspace("your-workspace").project("gunny-bag-counting")
dataset_bags = project_bags.version(1).download("yolov8")

# Example 2: Download Damage Detection Dataset
project_damage = rf.workspace("your-workspace").project("gunny-bag-damage")
dataset_damage = project_damage.version(1).download("yolov8")

print("✅ Roboflow datasets successfully downloaded into the datasets/ folder!")