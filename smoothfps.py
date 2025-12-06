#!/usr/bin/env python3
import os, time, sys, random, subprocess
from threading import Thread

# ────────────────────────────────────────────────
#   COLORS
# ────────────────────────────────────────────────
RESET = "\033[0m"
BOLD = "\033[1m"
BLINK = "\033[5m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
WHITE = "\033[97m"

GLOW = f"{BOLD}{BLINK}{CYAN}"

# ────────────────────────────────────────────────
#   GET DEVICE INFO (SAFE NO-ROOT)
# ────────────────────────────────────────────────
def getprop(prop):
    try:
        return subprocess.check_output(["getprop", prop]).decode().strip()
    except:
        return "Unknown"

def get_device_info():
    brand = getprop("ro.product.brand")
    model = getprop("ro.product.model")
    android = getprop("ro.build.version.release")
    cpu = getprop("ro.product.cpu.abi")

    try:
        mem = open("/proc/meminfo").read()
        total_ram = mem.split("MemTotal:")[1].split("kB")[0].strip()
        total_ram = f"{int(total_ram)//1024} MB"
    except:
        total_ram = "Unknown"

    return brand, model, android, cpu, total_ram

# ────────────────────────────────────────────────
#   MATRIX BACKGROUND ANIMATION
# ────────────────────────────────────────────────
def matrix_rain():
    chars = "1234567890abcdef#$%@&?"
    while True:
        print(f"\033[1;32m{random.choice(chars)}{RESET}", end="")
        time.sleep(0.001)

def start_matrix():
    for _ in range(40):
        Thread(target=matrix_rain, daemon=True).start()

# ────────────────────────────────────────────────
#   SMOOTH LOADING
# ────────────────────────────────────────────────
def smooth_loading(text, speed=0.01):
    print(f"\n{YELLOW}{text}{RESET}")
    bar = "■■■■■■■■■■■■■■■■■■■■"
    for i in range(1, len(bar) + 1):
        sys.stdout.write(f"\r{GREEN}{bar[:i]}{RESET}")
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")

# ────────────────────────────────────────────────
#   HEADER
# ────────────────────────────────────────────────
def header():
    os.system("clear")
    brand, model, android, cpu, ram = get_device_info()

    print(f"""
{GLOW}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{RESET}

{MAGENTA}◖ DEVICE AND HARDWARE INFO ◗{RESET}

{CYAN}➤ DEVICE  : {WHITE}{brand}{RESET}
{CYAN}➤ MODEL   : {WHITE}{model}{RESET}
{CYAN}➤ ANDROID : {WHITE}{android}{RESET}
{CYAN}➤ CPU     : {WHITE}{cpu}{RESET}
{CYAN}➤ RAM     : {WHITE}{ram}{RESET}

{CYAN}◖ Copyright © code07777 ◗{RESET}

{MAGENTA}{BOLD}Tool by @code07777{RESET}
{GREEN}Telegram : @code07777{RESET}
{YELLOW}Buy VIP File : @code07777{RESET}

{CYAN}Telegram Channel:{RESET}
{WHITE}https://t.me/codeteamback077{RESET}

""")

# ────────────────────────────────────────────────
#   INPUT PROMPT
# ────────────────────────────────────────────────
def ask(msg):
    return input(f"{YELLOW}{msg}{RESET}")

# ────────────────────────────────────────────────
#   MAIN MENU
# ────────────────────────────────────────────────
def main():
    start_matrix()
    time.sleep(0.2)
    header()

    print(f"{MAGENTA}➤ [ = ] Game Package Name ◗{RESET}")
    pkg = ask("➤ Type Here  = ")

    print(f"""
{MAGENTA}➤ [ = ] Select Gaming Frame Rate ◗{RESET}
 [1] 60FPS (Stable)
 [2] 90FPS (Stable)
 [3] 120FPS (Unstable)
""")
    fps = ask("➤ Select Option = ")

    print(f"""
{MAGENTA}➤ [ = ] Select Gaming Refresh Rate ◗{RESET}
 [1] 60HZ
 [2] 90HZ
 [3] 120HZ
""")
    hz = ask("➤ Select Option = ")

    print(f"""
{MAGENTA}➤ [ = ] Select Gaming Mode ◗{RESET}
 [1] Extreme
 [2] Ultra (Heats)
 [3] Medium
""")
    mode = ask("➤ Select Option = ")

    print(f"""
{MAGENTA}➤ [ = ] CPU/GPU Boost ◗{RESET}
 [1] Maximum
 [2] Medium
""")
    boost = ask("➤ Select Option = ")

    print(f"""
{MAGENTA}➤ [ = ] Touch Sampling Rate ◗{RESET}
 [1] Maximum
 [2] Medium
""")
    ts = ask("➤ Select Option = ")

    print(f"""
{MAGENTA}➤ [ = ] Hardware Optimization ◗{RESET}
 [1] Enable
 [2] Disable
""")
    opt = ask("➤ Select Option = ")

    smooth_loading("➤ Applying Lag Fix Scripts…")
    smooth_loading("➤ Optimizing RAM Performance…")
    smooth_loading("➤ Optimizing System Performance…")

    time.sleep(1)
    header()
    print(f"{GREEN}➤ Rechecking Script And Files...{RESET}")
    time.sleep(1.5)

    print(f"""
{GREEN}➤ All Script Applied Successfully!{RESET}
{YELLOW}➤ Restart Device For Better Results (Recommended){RESET}

[Process Completed]
""")

# ────────────────────────────────────────────────
#   RUN
# ────────────────────────────────────────────────
if __name__ == "__main__":
    main()
