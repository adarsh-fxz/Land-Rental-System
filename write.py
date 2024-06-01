"""
This file contains a class that writes data to a text file.
"""

import os
import datetime

class Write:
    """
    This file contains a class that writes data to a text file.
    """

    @staticmethod
    def generate_rent_invoice(lands_data, kitta, customer_name,
                              duration, total_amount, kitta_string):
        """
        Function to generate rent bill for the customer.
        If the same customer rents more than one land, the details are added to the same file
        and the total amount is updated.
        """
        bill_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bill_amount = lands_data[kitta]['price'] * int(duration)
        file_name = f"{customer_name}_invoice.txt"

        if os.path.exists(file_name):
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(f"\nRent Bill for {customer_name}\n")
                file.write(f"\nBill Date: {bill_date}\n")
                file.write(f"Kitta: {kitta}\n")
                file.write(f"City: {lands_data[kitta]['city']}\n")
                file.write(f"Direction: {lands_data[kitta]['direction']}\n")
                file.write(f"Area: {lands_data[kitta]['area']} anna\n")
                file.write(f"Rent: Rs. {lands_data[kitta]['price']} per month\n")
                file.write(f"Rent Duration: {duration} months\n")
                file.write(f"Total Amount for Kitta {kitta}: Rs. {bill_amount}\n")
                file.write(
                    f"Total Amount to be paid for kitta {kitta_string}: Rs. {total_amount}\n")
        else:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(f"Rent Bill for {customer_name}\n")
                file.write(f"\nBill Date: {bill_date}\n")
                file.write(f"Kitta: {kitta}\n")
                file.write(f"City: {lands_data[kitta]['city']}\n")
                file.write(f"Direction: {lands_data[kitta]['direction']}\n")
                file.write(f"Area: {lands_data[kitta]['area']} anna\n")
                file.write(f"Rent: Rs. {lands_data[kitta]['price']} per month\n")
                file.write(f"Rent Duration: {duration} months\n")
                file.write(f"Total Amount for Kitta {kitta}: Rs. {bill_amount}\n")
                file.write(
                    f"Total Amount to be paid for kitta {kitta_string}: Rs. {total_amount}\n")

        return bill_amount

    @staticmethod
    def generate_return_invoice(lands_data, kitta, customer_name, rent_duration,
                                return_duration, total_amount, kitta_string):
        """
        Function to generate return bill for the customer. If the same customer
        returns more than one land, the details are added to the same file and
        the total amount is updated.
        """
        bill_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if rent_duration > return_duration:
            bill_amount = lands_data[kitta]['price'] * rent_duration
        else:
            bill_amount = lands_data[kitta]['price'] * return_duration
        file_name = f"{customer_name}_invoice.txt"
        fine_amount = 0

        with open(file_name, "a", encoding="utf-8") as file:
            fine_amount = 0
            file.write(f"\nReturn Bill for {customer_name}\n")
            file.write(f"\nBill Date: {bill_date}\n")
            file.write(f"Kitta: {kitta}\n")
            file.write(f"City: {lands_data[kitta]['city']}\n")
            file.write(f"Direction: {lands_data[kitta]['direction']}\n")
            file.write(f"Area: {lands_data[kitta]['area']} anna\n")
            file.write(f"Rent: Rs. {lands_data[kitta]['price']} per month\n")
            file.write(f"Return Duration: {return_duration} months\n")
            if return_duration > rent_duration:
                fine_amount = (
                    return_duration - rent_duration) *lands_data[kitta]['price'] * 0.1
                file.write(f"Fine Amount: Rs. {fine_amount}\n")

            file.write(
                f"Total Amount returned for Kitta {kitta}: Rs. {bill_amount + fine_amount}\n")
            file.write(f"Total Amount left to be paid for kitta {kitta_string}without fine: Rs. {total_amount}\n")

            return total_amount
