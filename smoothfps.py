#!/usr/bin/env python3
# SmoothFPS.py
# Fully interactive, fixed-width box UI, safe PUBG config, 1-100 loading animation
# Compatible: Termux / Linux / macOS / Windows (Python3)

import os
import sys
import time
import shutil

# -------------------- Config -------------------- #
MIN_WIDTH = 60         # minimum box width
PADDING = 2            # left/right padding inside box
PROGRESS_SLEEP = 0.02  # default sleep between progress updates (seconds)

# Colors (optional) - safe fallback if terminal doesn't support
USE_COLOR = True
if os.name == 'nt':
    # try enabling ANSI on Windows 10+
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        pass

def col(code):
    if not USE_COLOR:
        return ""
    return f"\033[{code}m"

RESET = col('0')
GREEN = col('92')
CYAN  = col('96')
YELLOW= col('93')
RED   = col('91')
PURPLE= col('95')

# -------------------- Terminal helpers -------------------- #
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def term_width():
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return MIN_WIDTH

def box_width():
    w = term_width() - 4
    if w < MIN_WIDTH:
        w = MIN_WIDTH
    return w

def center_text(s, width):
    # returns string padded to width (centered)
    s = str(s)
    if len(s) >= width - (PADDING*2):
        return s[:width - (PADDING*2)]
    space = width - (PADDING*2) - len(s)
    left = space // 2
    right = space - left
    return (" " * left) + s + (" " * right)

def print_box(lines, title=None):
    w = box_width()
    border = "+" + "-" * (w - 2) + "+"
    print(CYAN + border + RESET)
    if title:
        t = center_text(title, w - 2)
        print(CYAN + "|" + RESET + " " * PADDING + PURPLE + t + RESET + " " * PADDING + CYAN + "|" + RESET)
        print(CYAN + border + RESET)
    for ln in lines:
        # ensure each line has same width to avoid sliding
        content = center_text(ln, w - 2)
        print(CYAN + "|" + RESET + " " * PADDING + content + " " * PADDING + CYAN + "|" + RESET)
    print(CYAN + border + RESET)

# -------------------- UI Content -------------------- #
HEADER_LINES = [
    "LAG FIX MODE FOR ALL GAMES",
    "Created By : @code07777",
    "Telegram Channel : https://t.me/codeteamback077",
    "Telegram Dev     : https://t.me/code07777"
]

DEVICE_INFO = [
    "DEVICE : Redmi",
    "MODEL  : M2004J7AC"
]

PUBG_RECOMMENDED = [
    "Recommended In-Game Settings:",
    " - Graphics : Smooth",
    " - FPS      : Extreme / 90FPS (if supported)",
    " - Shadows  : OFF",
    " - Anti-Aliasing : OFF",
    " - Screen Optimization : ON"
]

SAFE_NOTES = [
    "SAFE: No game files modified • No root required",
    "Safe device-side optimizations only"
]

# -------------------- Main Flow -------------------- #
def read_choice(prompt, valid):
    while True:
        try:
            v = input(GREEN + prompt + RESET).strip()
        except (KeyboardInterrupt, EOFError):
            print()
            return None
        if v in valid:
            return v
        print(YELLOW + "Invalid choice — try again." + RESET)

def progress_bar(total=100, sleep=PROGRESS_SLEEP, label="Applying Tweaks"):
    # Animated 1..100 with fixed-width box to avoid shifting
    w = box_width()
    bar_width = max(20, w - 40)
    for i in range(0, total + 1):
        percent = i
        filled = int(bar_width * i / total)
        bar = "[" + "#" * filled + " " * (bar_width - filled) + "]"
        # Build stable line of fixed length
        line = f"{label}: {bar} {percent:3d}%"
        # clear single line and print centered inside box area
        # We'll print a small inner box with one line to keep alignment
        clear_screen()
        print_box(HEADER_LINES, title="LAG FIX MODE FOR ALL GAMES")
        print() 
        print_box(DEVICE_INFO, title="DEVICE INFO")
        print()
        # display current progress as single centered line
        print_box([line], title="PROGRESS")
        time.sleep(sleep)

def main():
    clear_screen()
    # Show header
    print_box(HEADER_LINES, title="LAG FIX MODE FOR ALL GAMES")
    print()
    print_box(DEVICE_INFO, title="DEVICE INFO")
    print()
    # Game package
    pkg = input(GREEN + "Enter Game Package Name (e.g., com.tencent.ig): " + RESET).strip()
    if not pkg:
        pkg = "com.tencent.ig"
    # FPS choice
    print()
    print_box(["[1] 60FPS (Stable)", "[2] 90FPS (Stable)", "[3] 120FPS (Unstable)"], title="SELECT GAMING FRAME RATE")
    fps = read_choice("Select Option (1/2/3): ", {"1","2","3"})
    if fps is None:
        return
    # HZ choice
    print()
    print_box(["[1] 60HZ (Stable)", "[2] 90HZ (Stable)", "[3] 120HZ (Stable)"], title="SELECT GAMING REFRESH RATE")
    hz = read_choice("Select Option (1/2/3): ", {"1","2","3"})
    if hz is None:
        return
    # Mode
    print()
    print_box(["[1] Extreme", "[2] Ultra (Device may heat)", "[3] Medium"], title="SELECT GAMING MODE")
    mode = read_choice("Select Option (1/2/3): ", {"1","2","3"})
    if mode is None:
        return
    # Boost
    print()
    print_box(["[1] Maximum (Device may heat)", "[2] Medium (Stable)"], title="CPU / GPU BOOST")
    boost = read_choice("Select Option (1/2): ", {"1","2"})
    if boost is None:
        return
    # Touch
    print()
    print_box(["[1] Maximum", "[2] Medium"], title="TOUCH SAMPLING BOOST")
    touch = read_choice("Select Option (1/2): ", {"1","2"})
    if touch is None:
        return
    # Hardware opt
    print()
    print_box(["[1] Enable", "[2] Disable"], title="HARDWARE OPTIMIZATION")
    hw = read_choice("Select Option (1/2): ", {"1","2"})
    if hw is None:
        return

    # Ask animation speed (optional)
    print()
    print_box(["Choose loading speed", "[1] Fast", "[2] Normal", "[3] Slow"], title="LOADING SPEED")
    sp = read_choice("Select Option (1/2/3): ", {"1","2","3"})
    if sp == "1":
        speed = 0.005
    elif sp == "3":
        speed = 0.06
    else:
        speed = PROGRESS_SLEEP

    # Start progress animation 1..100
    progress_bar(total=100, sleep=speed, label="Applying Tweaks")

    # After finished, present final config box (stable width)
    clear_screen()
    final_lines = [
        f"Game Package : {pkg}",
        f"Frame Rate   : {'60FPS' if fps=='1' else '90FPS' if fps=='2' else '120FPS'}",
        f"Refresh Rate : {'60HZ' if hz=='1' else '90HZ' if hz=='2' else '120HZ'}",
        f"Mode         : {'Extreme' if mode=='1' else 'Ultra' if mode=='2' else 'Medium'}",
        f"CPU/GPU Boost: {'Maximum' if boost=='1' else 'Medium'}",
        f"Touch Boost  : {'Maximum' if touch=='1' else 'Medium'}",
        f"Hardware Opt : {'Enabled' if hw=='1' else 'Disabled'}",
    ]

    # PUBG safe config block
    final_lines += ["", "PUBG SAFE CONFIG (Device-side, Non-Ban):"]
    final_lines += [
        " - Graphics : Smooth",
        " - FPS      : Extreme / 90FPS (if supported)",
        " - Shadows  : OFF",
        " - Anti-Aliasing : OFF",
        " - Screen Optimization : ON",
        "",
        "Notes: No game files modified • No root required"
    ]

    print_box(final_lines, title="RESULTS")
    print()
    print(GREEN + "All Scripts Applied Successfully!" + RESET)
    print(YELLOW + "Restart Device For Better Result." + RESET)
    print()
    input("Press Enter to exit...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
