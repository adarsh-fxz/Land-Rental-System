"""
This module contains the Operations class which contains functions to display available and
rented lands, rent lands, and return lands.
"""

import os

from read import read_land_data
from write import Write

FILE_NAME = "lands.txt"

class Operations:
    """
    This class contains functions to display available and
    rented lands, rent lands, and return lands.
    """
    lands_data = read_land_data(FILE_NAME)
    kitta_duration = {}
    total_amount = 0
    kitta_string = ""
    lands = {}

    @staticmethod
    def display_available_lands():
        """
        Function to display available lands to the user.
        """

        print("\nAvailable Lands:")
        for kitta, land_info in Operations.lands_data.items():
            if land_info["status"] == "Available":
                print(f"Kitta: {kitta}, City: {land_info['city']}, Direction: {land_info['direction']}, Area: {land_info['area']} anna, Price: Rs. {land_info['price']}")

    @staticmethod
    def display_rented_lands():
        """
        Function to display rented lands to the user.
        """
        print("\nRented Lands:")
        for kitta, land_info in Operations.lands_data.items():
            if land_info["status"] == "Not Available":
                print(f"Kitta: {kitta}, City: {land_info['city']}, Direction: {land_info['direction']}, Area: {land_info['area']} anna, Price: Rs. {land_info['price']}")

    @staticmethod
    def rent_lands():
        """
        Function to rent single or multiple lands for the customer, update the status and generate invoice.
        """
        customer_name = input("Enter customer name: ").replace(" ", "")
        kitta_list = input("Enter kitta numbers to rent (comma-separated): ").split(",")
        Operations.kitta_string = ""

        for kitta in kitta_list:
            kitta = kitta.strip()
            Operations.lands[kitta] = customer_name
            if kitta in Operations.lands_data:
                if Operations.lands_data[kitta]["status"] == "Available":
                    Operations.lands_data[kitta]["status"] = "Not Available"
                    duration = int(input(f"Enter rent duration (in months) for kitta {kitta}: "))
                    Operations.total_amount += Operations.lands_data[kitta]["price"] * duration
                    Operations.kitta_string += f"{kitta}, "
                    Operations.kitta_duration[kitta] = duration
                    Write.generate_rent_invoice(Operations.lands_data, kitta, customer_name, duration, Operations.total_amount, Operations.kitta_string)
                    print(f"Land {kitta} rented to {customer_name} for {duration} months.")
                    Write.update_file(FILE_NAME, kitta, "Available", "Not Available")

                else:
                    print(f"Land {kitta} is not available for rent.")
            else:
                print(f"Land {kitta} not found.")

    @staticmethod
    def return_lands():
        """
        Function to return single or multiple lands rented by the customer by checking
        if the customer has rented land before returing or not from the rent file,
        update the status and generate invoice, bill, fine if applicable, and update the total amount.
        """

        customer_name = input("Enter customer name: ").replace(" ", "")
        if os.path.exists(f"{customer_name}_invoice.txt"):
            kitta_list = input("Enter kitta numbers to return (comma-separated): ").split(",")

            for kitta in kitta_list:
                kitta = kitta.strip()
                if kitta in Operations.lands_data:
                    if Operations.lands_data[kitta]["status"] == "Not Available" and Operations.lands[kitta] == customer_name:
                        Operations.lands_data[kitta]["status"] = "Available"
                        if not kitta in Operations.kitta_duration:
                            print(f"Land {kitta} not rented by {customer_name}.")
                            continue
                        return_duration = int(input(f"Enter the duration (in months) after which kitta {kitta} is returned: "))
                        Operations.kitta_string = Operations.kitta_string.replace(f"{kitta}, ", "")
                        rent_duration = Operations.kitta_duration[kitta]
                        Operations.total_amount -= Operations.lands_data[kitta]["price"] * rent_duration
                        amount = Write.generate_return_invoice(Operations.lands_data, kitta, customer_name, rent_duration, return_duration, Operations.total_amount, Operations.kitta_string)
                        Operations.total_amount = amount
                        print(f"Land {kitta} returned by {customer_name} after {return_duration} months.")
                        Write.update_file(FILE_NAME, kitta, "Not Available", "Available")
                    else:
                        print(f"Land {kitta} not rented by {customer_name}.")
                else:
                    print(f"Land {kitta} not found.")

        else:
            print(f"No rented land found for {customer_name}.")
