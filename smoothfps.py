#!/usr/bin/env python3
# SmoothFPS.py — Fully Animated Pro Version
# Rainbow typing • Glow effect • Smooth fade menu • Animated box UI

import os, time, sys, shutil

# ---------------- COLOR ---------------- #
def col(code): return f"\033[{code}m"
RESET = col("0")
CYAN  = col("96")
PURPLE= col("95")
GREEN = col("92")
YELLOW= col("93")

RAINBOW = ["91", "93", "92", "96", "94", "95"]

# ---------------- TERMINAL ---------------- #
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def width():
    try: return shutil.get_terminal_size().columns
    except: return 80

BOX_W = 70

# ---------------- ANIMATION ---------------- #
def rainbow_slow(text, speed=0.02):
    c = 0
    for ch in text:
        sys.stdout.write(f"\033[{RAINBOW[c]}m{ch}\033[0m")
        sys.stdout.flush()
        time.sleep(speed)
        c = (c + 1) % len(RAINBOW)
    print()

def glow_slow(text, speed=0.02):
    for ch in text:
        for i in [2,1,0]:  # bold → normal
            sys.stdout.write(f"\033[9{i}m{ch}\033[0m")
            sys.stdout.flush()
            time.sleep(speed/3)
    print()

def type_slow(text, speed=0.02):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def type_center_ani(text, speed=0.01):
    line = text.center(BOX_W)
    for i in range(len(line)):
        sys.stdout.write(line[:i+1])
        sys.stdout.flush()
        time.sleep(speed)
    print()

# ---------------- BOX PRINT ---------------- #
def box_fade(lines, title=None):
    border = "+" + "-"*(BOX_W-2) + "+"
    frames = 8

    for f in range(frames):
        fade = 90 + f
        clear()
        print(f"\033[{fade}m{border}\033[0m")

        if title:
            t = title.center(BOX_W-2)
            print(f"\033[{fade}m|{t}|\033[0m")
            print(f"\033[{fade}m{border}\033[0m")

        for ln in lines:
            print(f"\033[{fade}m| {ln.center(BOX_W-4)} |\033[0m")

        print(f"\033[{fade}m{border}\033[0m")
        time.sleep(0.03)

# ---------------- MENU ---------------- #
def menu_smooth(title, items):
    clear()
    print()
    type_center_ani(title)
    print()
    time.sleep(0.2)

    for it in items:
        rainbow_slow("  " + it, 0.01)
        time.sleep(0.05)

def ask(prompt, valid):
    glow_slow(GREEN + prompt + RESET, 0.01)
    while True:
        ans = input("→ ").strip()
        if ans in valid:
            return ans
        rainbow_slow(YELLOW + "Invalid! Try again..." + RESET, 0.01)

# ---------------- PROGRESS ---------------- #
def progress(label="Applying"):
    for i in range(1, 101):
        wave = "#" * ((i // 5) % 20)
        line = f"{label} [{wave:<20}] {i:3d}%"
        clear()
        box_fade([line], title="PROGRESS")
        time.sleep(0.02)

# ---------------- MAIN ---------------- #
def main():
    clear()

    # INTRO UI
    box_fade([
        "LAG FIX TOOL - ANIMATED VERSION",
        "By @code07777",
        "Telegram: t.me/codeteamback077"
    ], title="WELCOME")

    time.sleep(0.8)

    # GAME PACKAGE
    type_center_ani("Enter Game Package Name")
    pkg = input("→ ") or "com.tencent.ig"

    # FPS MENU
    menu_smooth("SELECT FPS", [
        "[1] 60FPS (Stable)",
        "[2] 90FPS (Stable)",
        "[3] 120FPS (Unstable)"
    ])
    fps = ask("Select Option:", {"1","2","3"})

    # HZ MENU
    menu_smooth("SELECT REFRESH RATE", [
        "[1] 60HZ", "[2] 90HZ", "[3] 120HZ"
    ])
    hz = ask("Select Option:", {"1","2","3"})

    # MODE MENU
    menu_smooth("SELECT MODE", [
        "[1] Extreme", "[2] Ultra", "[3] Medium"
    ])
    mode = ask("Select Option:", {"1","2","3"})

    # BOOST
    menu_smooth("CPU/GPU BOOST", [
        "[1] Maximum", "[2] Medium"
    ])
    boost = ask("Select Option:", {"1","2"})

    # TOUCH
    menu_smooth("TOUCH BOOST", [
        "[1] Maximum", "[2] Medium"
    ])
    touch = ask("Select Option:", {"1","2"})

    # HW
    menu_smooth("HARDWARE OPTIMIZATION", [
        "[1] Enable", "[2] Disable"
    ])
    hw = ask("Select Option:", {"1","2"})

    # APPLYING
    progress("Applying Tweaks")

    # RESULT SCREEN
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
        "  • Graphics: Smooth",
        "  • FPS: Extreme / 90FPS",
        "  • Shadows: OFF",
        "  • Anti-Aliasing: OFF",
        "  • Screen Optimization: ON"
    ]

    clear()
    box_fade(final, title="RESULTS")
    print()
    type_center_ani("Restart Device For Best Performance!")
    print()
    input("Press Enter to exit…")

# ---------------- RUN ---------------- #
if __name__ == "__main__":
    main()
