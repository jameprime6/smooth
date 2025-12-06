#!/usr/bin/env python3

import os, time, sys, shutil

# ---------------- COLOR ---------------- #
def col(code): return f"\033[{code}m"
RESET = col("0")
CYAN   = col("96")
GREEN  = col("92")
YELLOW = col("93")
MAGENTA= col("95")
BLUE   = col("94")

# ---------------- TERMINAL ---------------- #
def clear():
    os.system("clear")

def box(text_lines, title=None):
    w = 70
    border = "+" + "-"*(w-2) + "+"
    print(border)
    if title:
        print("|" + title.center(w-2) + "|")
        print(border)
    for line in text_lines:
        print("| " + line.center(w-4) + " |")
    print(border)

def print_center(text):
    width = shutil.get_terminal_size().columns
    print(text.center(width))

# ----------------- SAFE LOADING ---------------- #
def loading(label="Loading"):
    for i in range(101):
        bar = "#"*(i//4)
        percent = f"{i}%".rjust(4)
        clear()
        box([f"{label}: [{bar:<25}] {percent}"], "PROGRESS")
        time.sleep(0.02)

# ---------------- MENU ---------------- #
def menu(title, items):
    clear()
    print()
    print_center(MAGENTA + title + RESET)
    print()
    for item in items:
        print("  " + CYAN + item + RESET)
    print()
    return input(GREEN + "Select Option → " + RESET)

# ---------------- MAIN ---------------- #
def main():
    clear()

    # Intro Box
    box([
        "LAG FIX TOOL - TERMUX SAFE EDITION",
        "By @code07777",
        "Telegram: t.me/codeteamback077",
        "BUY VIP FILE: @code07777"
    ], "WELCOME")

    time.sleep(1)

    # Game Package
    print()
    print_center("Enter Game Package Name")
    pkg = input("→ ") or "com.tencent.ig"

    # FPS
    fps = menu("SELECT FPS", [
        "[1] 60FPS (Stable)",
        "[2] 90FPS (Stable)",
        "[3] 120FPS (Unstable)"
    ])

    # REFRESH RATE
    hz = menu("SELECT REFRESH RATE", [
        "[1] 60Hz",
        "[2] 90Hz",
        "[3] 120Hz"
    ])

    # MODE
    mode = menu("SELECT MODE", [
        "[1] Extreme",
        "[2] Ultra",
        "[3] Medium"
    ])

    # BOOST
    boost = menu("CPU / GPU BOOST", [
        "[1] Maximum",
        "[2] Medium"
    ])

    # TOUCH BOOST
    touch = menu("TOUCH BOOST", [
        "[1] Maximum",
        "[2] Medium"
    ])

    # HW OPT
    hw = menu("HARDWARE OPTIMIZATION", [
        "[1] Enable",
        "[2] Disable"
    ])

    # Loading Progress
    loading("Applying Tweaks")

    # Final Result
    clear()
    box([
        f"Game Package  : {pkg}",
        f"FPS           : {fps}",
        f"Refresh Rate  : {hz}",
        f"Mode          : {mode}",
        f"Boost Level   : {boost}",
        f"Touch Boost   : {touch}",
        f"HW Optimize   : {hw}",
        "",
        "PUBG SAFE SETTINGS:",
        " • Graphics: Smooth",
        " • FPS: Extreme / 90FPS",
        " • Shadows: OFF",
        " • Anti-Aliasing: OFF",
        " • Screen Optimization: ON"
    ], "RESULTS")

    print()
    print_center("Restart Device For Best Performance!")
    print()
    input("Press Enter to Exit… ")

# ---------------- RUN ---------------- #
if __name__ == "__main__":
    main()
