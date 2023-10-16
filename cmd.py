import os

def info_command():
    print("dev by XikSam")
    

if __name__ == "__main__":
    while True:
        user_input = input("Enter command: ")
        if user_input.lower() == "info":
            info_command()
