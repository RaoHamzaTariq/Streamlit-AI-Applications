import time

def countdown_timer(seconds):
    """A countdown timer that prints the remaining time."""

    try:
        seconds = int(seconds)  
        if seconds < 0:
            print("Please enter a positive number of seconds.")
            return

        while seconds > 0:
            minutes, secs = divmod(seconds, 60)
            timer = '{:02d}:{:02d}'.format(minutes, secs)
            print(timer, end="\r")  
            time.sleep(1)
            seconds -= 1

        print("Time's up!      ") 

    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Gets user input and starts the countdown timer."""
    try:
        seconds = input("Enter the countdown time in seconds: ")
        countdown_timer(seconds)
    except KeyboardInterrupt: 
        print("\nTimer interrupted.")

if __name__ == "__main__":
    main()