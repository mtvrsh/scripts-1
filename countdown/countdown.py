#!/usr/bin/python3

import os
import sys
import time

def countdown(seconds: int, filename=None):
    total = seconds

    while total > 0:
        timer = f"{total}s" if total < 60 else f"{int(total / 60)}m"

        try:
            with open(filename, "w") as file:
                file.write(timer)
        except (TypeError, FileNotFoundError):
            print(timer)

        time.sleep(1)

        total -= 1

def parse_seconds(t: str):
    multiplier = 1

    try:
        seconds = int(t)
    except ValueError:
        try:
            match t[-1]:
                case "m":
                    multiplier = 60
                case "h":
                    multiplier = 3600
        except IndexError:
            return 0

        try:
            seconds = int(t[:-1])
        except (IndexError, ValueError):
            return 0

    return seconds * multiplier

def playsound():
    os.system("mpv /usr/share/sounds/budgie/default/alerts/bark.ogg")

def main():
    try:
        time = parse_seconds(sys.argv[1])
    except IndexError:
        sys.exit("No time given")

    try:
        filename = sys.argv[2]
    except IndexError:
        filename = None

    try:
        while time:
            countdown(time, filename)
            playsound()
    except KeyboardInterrupt:
        print()

        try:
            os.remove(filename)
        except (TypeError, OSError) as e:
            pass

if __name__ == "__main__":
    main()
