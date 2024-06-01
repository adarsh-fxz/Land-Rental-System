"""
This file contains a class that reads data from a text file and stores it in a dictionary.
"""

import os

def read_land_data(file_name):
    """
    Reads data from the main text file and stores it in a dictionary.

    Parameters:
    file_name (str): The name of the file to read.

    Returns:
    dict: A dictionary containing land data, with keys as 'kitta'
    and values as dictionaries containing 'city', 'direction', 'area', 'price', and 'status'.
    """
    lands_data = {}
    try:
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as file:
                for line in file:
                    kitta, city, direction, area, price, status = line.strip().split(", ")
                    lands_data[kitta] = {
                        "city": city,
                        "direction": direction,
                        "area": int(area),
                        "price": int(price),
                        "status": status.strip()
                    }

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

    return lands_data
