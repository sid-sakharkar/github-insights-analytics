def display_menu():
    print("\n--- GitHub Insights Analytics ---")
    print("1. View Analytics")
    print("2. Generate Report")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print("Viewing Analytics...")  # Logic to view analytics goes here
        elif choice == '2':
            print("Generating Report...")  # Logic to generate report goes here
        elif choice == '3':
            print("Exiting the application. Bye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == '__main__':
    main()