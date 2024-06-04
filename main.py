"""
This is the main file to run the land rental system.
"""

from operations import Operations

def main():
    '''
    Main function to run the land rental system.
    '''

    print("\n***** Land Rental System *****")

    while True:
        print("\n1. Display Available Lands")
        print("2. Display Rented Lands")
        print("3. Rent Land")
        print("4. Return Land")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            Operations.display_available_lands()

        elif choice == "2":
            Operations.display_rented_lands()

        elif choice == "3":
            Operations.rent_lands()

        elif choice == "4":
            Operations.return_lands()

        elif choice == "5":
            print("Exiting...")
            print("Thank you for using the Land Rental System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
