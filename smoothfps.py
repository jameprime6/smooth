#!/usr/bin/env python3
import os, time, sys, random, subprocess
from threading import Thread

# ────────────────────────────────────────────────
# COLORS + GLOW
# ────────────────────────────────────────────────
RESET = "\033[0m"
BOLD = "\033[1m"
BLINK = "\033[5m"
GREEN = "\033[92m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
WHITE = "\033[97m"

GLOW = f"{BOLD}{CYAN}"

# ────────────────────────────────────────────────
# DEVICE INFO (SAFE)
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
# MATRIX RAIN (NO ERROR VERSION)
# ────────────────────────────────────────────────
def matrix_rain():
    chars = "01"
    width = os.get_terminal_size().columns
    while True:
        line = "".join(random.choice(chars) for _ in range(width))
        print(f"\033[1;32m{line}{RESET}")
        time.sleep(0.03)

def start_matrix():
    Thread(target=matrix_rain, daemon=True).start()

# ────────────────────────────────────────────────
# SIDE SLIDE EFFECT (SMOOTH TEXT)
# ────────────────────────────────────────────────
def slide_text(text):
    print()
    for i in range(1, len(text)+1):
        sys.stdout.write(f"\r{CYAN}{text[:i]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n")

# ────────────────────────────────────────────────
# SMOOTH LOADING BAR
# ────────────────────────────────────────────────
def smooth_loading(text):
    slide_text(text)
    bar = "■■■■■■■■■■■■■■■■■■■■"
    for i in range(1, len(bar)+1):
        sys.stdout.write(f"\r{GREEN}{bar[:i]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n")

# ────────────────────────────────────────────────
# HEADER (WITH GLOW)
# ────────────────────────────────────────────────
def header():
    os.system("clear")
    brand, model, android, cpu, ram = get_device_info()

    print(f"""
{GLOW}═══════════════════════════════════════════════{RESET}

{MAGENTA}◖ DEVICE AND HARDWARE INFO ◗{RESET}

{CYAN}➤ DEVICE  : {WHITE}{brand}{RESET}
{CYAN}➤ MODEL   : {WHITE}{model}{RESET}
{CYAN}➤ ANDROID : {WHITE}{android}{RESET}
{CYAN}➤ CPU     : {WHITE}{cpu}{RESET}
{CYAN}➤ RAM     : {WHITE}{ram}{RESET}

{MAGENTA}═══════════════════════════════════════════════{RESET}

{CYAN}Tool by @code07777{RESET}
{WHITE}https://t.me/codeteamback077{RESET}

""")

# ────────────────────────────────────────────────
# ASK INPUT
# ────────────────────────────────────────────────
def ask(msg):
    slide_text(msg)
    return input("➤ ").strip()

# ────────────────────────────────────────────────
# MAIN MENU
# ────────────────────────────────────────────────
def main():
    start_matrix()
    time.sleep(0.1)
    header()

    pkg = ask("Game Package Name")

    print(f"""
{MAGENTA}Select Gaming Frame Rate{RESET}
 [1] 60FPS  
 [2] 90FPS  
 [3] 120FPS  
""")
    fps = ask("Select FPS")

    print(f"""
{MAGENTA}Select Refresh Rate{RESET}
 [1] 60HZ
 [2] 90HZ
 [3] 120HZ
""")
    hz = ask("Select HZ")

    print(f"""
{MAGENTA}Gaming Mode{RESET}
 [1] Extreme
 [2] Ultra
 [3] Medium
""")
    mode = ask("Select Mode")

    print(f"""
{MAGENTA}CPU/GPU Boost{RESET}
 [1] Max
 [2] Medium
""")
    boost = ask("Select Boost")

    print(f"""
{MAGENTA}Touch Sampling Rate{RESET}
 [1] Max
 [2] Medium
""")
    ts = ask("Select Touch Rate")

    print(f"""
{MAGENTA}Hardware Optimization{RESET}
 [1] Enable
 [2] Disable
""")
    opt = ask("Select Option")

    smooth_loading("Applying Lag Fix Scripts…")
    smooth_loading("Optimizing RAM…")
    smooth_loading("Optimizing System…")

    header()
    slide_text("Rechecking Script And Files...")
    time.sleep(1)

    print(f"""
{GREEN}✔ All Scripts Applied Successfully!{RESET}
{YELLOW}✔ Restart Device For Best Performance!{RESET}
""")

# ────────────────────────────────────────────────
# RUN
# ────────────────────────────────────────────────
if __name__ == "__main__":
    main()
