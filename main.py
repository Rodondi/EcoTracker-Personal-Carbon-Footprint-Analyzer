from tracker import log_activities
from report import generate_report
from utils import get_random_tip
from database import setup_database

def menu():
    setup_database()
    while True:
        print("""
        === EcoTracker Menu ===
        1. Log Today's Activities
        2. View Report
        3. Get Eco Tip
        4. Exit
        """)
        choice = input("Enter your choice: ")

        if choice == '1':
            log_activities()
        elif choice == '2':
            generate_report()
        elif choice == '3':
            print("Eco Tip:", get_random_tip())
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()