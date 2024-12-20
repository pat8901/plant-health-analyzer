from pathlib import Path
import os
from load import *

def main():
    DATASET_DIR = os.path.join(Path(__file__).resolve().parent.parent.parent,"documentation/dataset/fruit_and_plant_dataset")
    my_list = []
    
    load_into_database(my_list, DATASET_DIR)
    print_list(my_list)

if __name__ == "__main__":
    main()