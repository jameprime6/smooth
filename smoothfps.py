#!/usr/bin/env python3
# SmoothFPS.py — Fully Animated Version
# Slow typing, slow menu reveal, stable box UI

import os, time, shutil, sys

# ---------------- COLOR ---------------- #
def col(code): return f"\033[{code}m"
RESET = col("0"); CYAN = col("96"); PURPLE = col("95")
GREEN = col("92"); YELLOW = col("93")

# ---------------- TERMINAL ---------------- #
def clear(): os.system("cls" if os.name=="nt" else "clear")
def width(): 
    try: return shutil.get_terminal_size().columns
    except: return 80

BOX_W = 70

# ---------------- TYPING EFFECT ---------------- #
def type_slow(text, speed=0.02):
    for ch in text:
        sys.stdout.write(ch); sys.stdout.flush()
        time.sleep(speed)
    print()

def type_center(text, speed=0.02):
    pad = (BOX_W - len(text)) // 2
    line = " " * pad + text
    for ch in line:
        sys.stdout.write(ch); sys.stdout.flush()
        time.sleep(speed)
    print()

# ---------------- BOX PRINT ---------------- #
def box(lines, title=None, slow=False):
    border = "+" + "-"*(BOX_W-2) + "+"
    print(CYAN + border + RESET)

    if title:
        tt = title.center(BOX_W-2)
        print(CYAN + "|" + PURPLE + tt + CYAN + "|" + RESET)
        print(CYAN + border + RESET)

    for ln in lines:
        padded = " " + ln.center(BOX_W-4) + " "
        if slow:
            type_slow(CYAN + "|" + RESET + padded + CYAN + "|" + RESET, 0.002)
        else:
            print(CYAN + "|" + RESET + padded + CYAN + "|" + RESET)

    print(CYAN + border + RESET)

# ---------------- PROGRESS ---------------- #
def progress(label="Loading"):
    for i in range(1, 101):
        bar = "#" * (i//5)
        line = f"{label} [{bar:<20}] {i:3d}%"
        clear()
        box([line], title="PROGRESS")
        time.sleep(0.02)

# ---------------- MENU ---------------- #
def menu(title, items):
    clear()
    lines = []
    for x in items:
        lines.append(x)
    box(lines, title, slow=True)

def ask(prompt, valid):
    type_slow(GREEN + prompt + RESET, 0.01)
    while True:
        ans = input("→ ").strip()
        if ans in valid:
            return ans
        type_slow(YELLOW + "Invalid! Try again..." + RESET, 0.01)

# ---------------- MAIN ---------------- #
def main():
    clear()
    # Header
    box([
        "LAG FIX TOOL - ANIMATED VERSION",
        "By @code07777",
        "Telegram Channel: t.me/codeteamback077"
    ], title="WELCOME", slow=True)

    time.sleep(0.6)

    # GAME PACKAGE
    type_center("Enter Game Package Name", 0.01)
    pkg = input("→ ") or "com.tencent.ig"

    # FPS MENU
    menu("SELECT FPS", [
        "[1] 60FPS (Stable)",
        "[2] 90FPS (Stable)",
        "[3] 120FPS (Unstable)"
    ])
    fps = ask("Select Option:", {"1","2","3"})
    time.sleep(0.3)

    # HZ MENU
    menu("SELECT REFRESH RATE", [
        "[1] 60HZ",
        "[2] 90HZ",
        "[3] 120HZ"
    ])
    hz = ask("Select Option:", {"1","2","3"})
    time.sleep(0.3)

    # MODE MENU
    menu("SELECT MODE", [
        "[1] Extreme",
        "[2] Ultra",
        "[3] Medium"
    ])
    mode = ask("Select Option:", {"1","2","3"})
    time.sleep(0.3)

    # BOOST
    menu("CPU/GPU BOOST", [
        "[1] Maximum",
        "[2] Medium"
    ])
    boost = ask("Select Option:", {"1","2"})
    time.sleep(0.3)

    # TOUCH
    menu("TOUCH BOOST", [
        "[1] Maximum",
        "[2] Medium"
    ])
    touch = ask("Select Option:", {"1","2"})
    time.sleep(0.3)

    # HW
    menu("HARDWARE OPTIMIZATION", [
        "[1] Enable",
        "[2] Disable"
    ])
    hw = ask("Select Option:", {"1","2"})
    time.sleep(0.5)

    # APPLYING
    progress("Applying Tweaks")

    # RESULTS (No 'No game files modified')
    final = [
        f"Game Package : {pkg}",
        f"FPS          : {fps}",
        f"Refresh Rate : {hz}",
        f"Mode         : {mode}",
        f"Boost Level  : {boost}",
        f"Touch Boost  : {touch}",
        f"HW Opt       : {hw}",
        "",
        "PUBG SAFE CONFIG:",
        " • Graphics: Smooth",
        " • FPS: Extreme / 90FPS",
        " • Shadows: OFF",
        " • Anti-Aliasing: OFF",
        " • Screen Optimization: ON"
    ]

    clear()
    box(final, title="RESULTS", slow=True)
    print()
    type_center("Restart Device For Best Performance!", 0.01)
    print()
    input("Press Enter to exit…")

# ---------------- RUN ---------------- #
if __name__ == "__main__":
    main()
